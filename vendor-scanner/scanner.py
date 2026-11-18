#!/usr/bin/env python3
"""Scan a folder of Python files for calls to third-party AI vendor APIs.

Vendor signatures live in vendors.json (language-agnostic: import patterns,
class names, endpoints, env var key names, key prefixes). This script's
Python-specific piece is only the `ast`-based parser that reads those
signatures and applies them to Python source.
"""
import argparse
import ast
import csv
import json
import re
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

SKIP_DIRS = {".git", "__pycache__", "venv", ".venv", "env", "node_modules", ".mypy_cache", ".pytest_cache"}

CONFIDENCE_RANK = {"high": 3, "medium": 2, "low": 1, "info": 0}


@dataclass
class Vendor:
    name: str
    import_patterns: list
    class_names: list
    endpoints: list
    env_key_patterns: list
    key_prefixes: list
    factory_calls: list = field(default_factory=list)


@dataclass
class Match:
    file: str
    line: int
    vendor: str
    match_type: str
    confidence: str
    snippet: str
    note: str = ""


def load_db(path):
    with open(path) as f:
        raw = json.load(f)
    vendors = [Vendor(**v) for v in raw["vendors"]]
    return vendors, raw["local_allowlist"], raw["local_host_markers"]


def module_matches(module: str, patterns) -> bool:
    if not module:
        return False
    for p in patterns:
        if module == p or module.startswith(p + "."):
            return True
    return False


def resolve_dotted(node):
    """Return root-first name parts for a Name/Attribute chain, else None."""
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
    else:
        return None
    return list(reversed(parts))


def const_str(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


class ImportBinding:
    def __init__(self, kind, vendors, orig=None):
        self.kind = kind        # "module" or "member"
        self.vendors = vendors  # list[Vendor]: every vendor whose import_patterns
                                 # matched this import (usually one, but e.g. OpenAI
                                 # and Azure OpenAI both match "openai")
        self.orig = orig        # original imported name, for "member"

    @property
    def vendor(self):
        """First matching vendor -- used for the "import" evidence line itself,
        where we can't yet tell which of several same-module vendors applies."""
        return self.vendors[0]


def redact_secrets(line, prefixes):
    """Mask anything key-shaped before it is recorded in a match.

    Snippets end up in results.json and the CSV, which get committed, emailed
    and handed to clients. A key-shaped literal is replaced with its vendor
    prefix plus a marker, so the finding stays actionable without the report
    becoming a second copy of a live credential.
    """
    # Longest prefix first: "sk-proj-" must win over "sk-".
    for prefix in sorted((p for p in prefixes if p), key=len, reverse=True):
        line = re.sub(re.escape(prefix) + r"[A-Za-z0-9_\-]{8,}",
                      prefix + "<REDACTED>", line)
    return line


class FileScanner(ast.NodeVisitor):
    def __init__(self, filename, source_lines, vendors, local_allowlist, local_host_markers):
        self.filename = filename
        self.lines = source_lines
        self.vendors = vendors
        self.local_allowlist = local_allowlist
        self.local_host_markers = local_host_markers
        self.import_map = {}       # local alias -> ImportBinding
        self.local_import_map = {} # local alias -> label
        self.tracked_vars = {}     # var name -> (vendor_name, suppressed_bool)
        self.key_prefixes = [p for v in vendors for p in v.key_prefixes]
        self.matches = []
        self.suppressed = []

    def snippet(self, lineno):
        if 1 <= lineno <= len(self.lines):
            return redact_secrets(self.lines[lineno - 1].strip(), self.key_prefixes)
        return ""

    def add(self, lineno, vendor, match_type, confidence, note=""):
        self.matches.append(Match(self.filename, lineno, vendor, match_type,
                                   confidence, self.snippet(lineno), note))

    def add_suppressed(self, lineno, vendor, match_type, note):
        self.suppressed.append(Match(self.filename, lineno, vendor, match_type,
                                      "info", self.snippet(lineno), note))

    def vendors_for_module(self, module):
        """All vendors whose import_patterns match this module (usually one,
        but e.g. OpenAI and Azure OpenAI both import from "openai")."""
        return [v for v in self.vendors if module_matches(module, v.import_patterns)]

    def local_label_for_module(self, module):
        for entry in self.local_allowlist:
            if module_matches(module, entry["import_patterns"]):
                return entry["label"]
        return None

    # -- imports --------------------------------------------------------
    def visit_Import(self, node):
        for alias in node.names:
            module = alias.name
            bound = alias.asname or module.split(".")[0]
            lineno = getattr(alias, "lineno", node.lineno)
            vs = self.vendors_for_module(module)
            if vs:
                self.import_map[bound] = ImportBinding("module", vs)
                self.add(lineno, vs[0].name, "import", "medium", f"import {module}")
                continue
            label = self.local_label_for_module(module)
            if label:
                self.local_import_map[bound] = label
                self.add_suppressed(lineno, label, "import", "local/self-hosted, not a third-party API call")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module = node.module or ""
        vs = self.vendors_for_module(module)
        label = self.local_label_for_module(module)
        for alias in node.names:
            bound = alias.asname or alias.name
            lineno = getattr(alias, "lineno", node.lineno)
            if vs:
                self.import_map[bound] = ImportBinding("member", vs, alias.name)
                self.add(lineno, vs[0].name, "import", "medium", f"from {module} import {alias.name}")
            elif label:
                self.local_import_map[bound] = label
                self.add_suppressed(lineno, label, "import", "local/self-hosted, not a third-party API call")
        self.generic_visit(node)

    # -- assignments (client instantiation) ------------------------------
    def visit_Assign(self, node):
        target_name = None
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            target_name = node.targets[0].id

        if isinstance(node.value, ast.Call):
            info = self._client_init_info(node.value)
            if info:
                vendor, suppressed, override_note = info
                if suppressed:
                    self.add_suppressed(node.value.lineno, vendor.name, "client_init",
                                         override_note)
                else:
                    self.add(node.value.lineno, vendor.name, "client_init", "high")
                if target_name:
                    self.tracked_vars[target_name] = (vendor.name, suppressed)

        self.generic_visit(node)

    def _client_init_info(self, call_node):
        """If call_node constructs a known vendor client class, return
        (vendor, suppressed, note); else None."""
        parts = resolve_dotted(call_node.func)
        if not parts:
            return None

        root = parts[0]
        binding = self.import_map.get(root)
        vendor = None
        if binding and binding.kind == "module" and len(parts) == 2:
            for v in binding.vendors:
                if parts[1] in v.class_names:
                    vendor = v
                    break
        elif binding and binding.kind == "member" and len(parts) == 1:
            for v in binding.vendors:
                if binding.orig in v.class_names:
                    vendor = v
                    break

        if vendor:
            suppressed, note = self._check_local_override(call_node)
            return vendor, suppressed, note

        # boto3-style factory calls, e.g. boto3.client("bedrock-runtime")
        for v in self.vendors:
            for factory in getattr(v, "factory_calls", []):
                func_parts = factory["func"].split(".")
                if parts == func_parts or parts[-1] == func_parts[-1]:
                    service = self._first_str_arg(call_node, "service_name")
                    if service and service in factory["service_names"]:
                        return v, False, ""
        return None

    def _first_str_arg(self, call_node, kw_name):
        if call_node.args:
            s = const_str(call_node.args[0])
            if s:
                return s
        for kw in call_node.keywords:
            if kw.arg == kw_name:
                return const_str(kw.value)
        return None

    def _check_local_override(self, call_node):
        for kw in call_node.keywords:
            if kw.arg in ("base_url", "endpoint", "api_base"):
                val = const_str(kw.value)
                if val and any(marker in val for marker in self.local_host_markers):
                    return True, f"base_url override points to a local host ({val!r}); not treated as a third-party call"
        return False, ""

    # -- method calls on tracked client vars, plus env var access --------
    def visit_Call(self, node):
        parts = resolve_dotted(node.func)
        if parts and len(parts) >= 2 and parts[0] in self.tracked_vars:
            vendor_name, suppressed = self.tracked_vars[parts[0]]
            if not suppressed:
                self.add(node.lineno, vendor_name, "api_call", "high")

        if parts == ["os", "getenv"] or parts == ["os", "environ", "get"]:
            key = self._first_positional_str(node)
            if key:
                self._check_env_key(node.lineno, key)

        self.generic_visit(node)

    def _first_positional_str(self, call_node):
        if call_node.args:
            return const_str(call_node.args[0])
        return None

    def visit_Subscript(self, node):
        parts = resolve_dotted(node.value)
        if parts == ["os", "environ"]:
            key_node = node.slice
            # py<3.9 wraps the index in ast.Index
            if isinstance(key_node, ast.Index):
                key_node = key_node.value
            key = const_str(key_node)
            if key:
                self._check_env_key(node.lineno, key)
        self.generic_visit(node)

    def _check_env_key(self, lineno, key):
        for v in self.vendors:
            if key in v.env_key_patterns:
                self.add(lineno, v.name, "env_key", "medium")
                return

    # -- string literal scan: hardcoded endpoints / key-shaped secrets ---
    def scan_string_literals(self, tree):
        for node in ast.walk(tree):
            s = const_str(node)
            if s is None:
                continue
            for v in self.vendors:
                for ep in v.endpoints:
                    if ep in s:
                        self.add(node.lineno, v.name, "endpoint_literal", "medium")
            self.scan_key_literal(node.lineno, s)

    def scan_key_literal(self, lineno, s):
        """Attribute a key-shaped literal to exactly one vendor.

        Key prefixes overlap across vendors -- "sk-ant-..." also starts with
        OpenAI's "sk-" -- so the longest matching prefix wins. A shorter
        prefix from another vendor is a substring collision, not a second
        finding, and reporting it names the wrong vendor in the output.
        """
        if len(s) < 16 or " " in s:
            return
        best_len = 0
        best_vendor = None
        for v in self.vendors:
            for prefix in v.key_prefixes:
                if prefix and s.startswith(prefix) and len(prefix) > best_len:
                    best_len = len(prefix)
                    best_vendor = v.name
        if best_vendor:
            self.add(lineno, best_vendor, "hardcoded_key", "low",
                     "string literal looks like a hardcoded API key")


def scan_file(path: Path, vendors, local_allowlist, local_host_markers, root: Path):
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
    except (SyntaxError, UnicodeDecodeError) as e:
        rel = str(path.relative_to(root))
        return [], [Match(rel, 0, "-", "parse_error", "info", "", str(e))]

    rel = str(path.relative_to(root))
    scanner = FileScanner(rel, source.splitlines(), vendors, local_allowlist, local_host_markers)
    scanner.visit(tree)
    scanner.scan_string_literals(tree)
    return scanner.matches, scanner.suppressed


def find_python_files(root: Path):
    for p in sorted(root.rglob("*.py")):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def dedupe(matches):
    seen = set()
    out = []
    for m in matches:
        key = (m.file, m.line, m.vendor, m.match_type)
        if key in seen:
            continue
        seen.add(key)
        out.append(m)
    return out


def print_report(matches, suppressed):
    matches = sorted(matches, key=lambda m: (m.file, m.line, -CONFIDENCE_RANK[m.confidence]))
    if not matches:
        print("No third-party AI vendor API usage detected.\n")
    else:
        by_vendor = {}
        for m in matches:
            by_vendor[m.vendor] = by_vendor.get(m.vendor, 0) + 1
        print("Summary:")
        for vendor, count in sorted(by_vendor.items(), key=lambda kv: -kv[1]):
            print(f"  {vendor}: {count} match(es)")
        print()
        print(f"{'FILE':40} {'LINE':>5}  {'VENDOR':22} {'TYPE':18} {'CONF':8} SNIPPET")
        print("-" * 120)
        for m in matches:
            print(f"{m.file:40} {m.line:>5}  {m.vendor:22} {m.match_type:18} {m.confidence:8} {m.snippet[:60]}")
            if m.note:
                print(f"{'':40} {'':>5}  {'':22} note: {m.note}")
        print()

    if suppressed:
        print("Recognized as local/self-hosted (not flagged):")
        for m in sorted(suppressed, key=lambda m: (m.file, m.line)):
            label = m.vendor
            print(f"  {m.file}:{m.line}  {label}  -- {m.snippet[:60]}")
            if m.note:
                print(f"      note: {m.note}")
        print()

    errors = [m for m in suppressed if m.match_type == "parse_error"]
    # parse errors are also surfaced separately by caller


def write_csv(path, matches):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "line", "vendor", "match_type", "confidence", "snippet", "note"])
        w.writeheader()
        for m in matches:
            w.writerow(asdict(m))


def write_json(path, matches, suppressed):
    with open(path, "w") as f:
        json.dump({
            "matches": [asdict(m) for m in matches],
            "suppressed": [asdict(m) for m in suppressed],
        }, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Scan Python files for third-party AI vendor API usage.")
    parser.add_argument("path", help="folder to scan")
    parser.add_argument("--vendors", default=str(Path(__file__).parent / "vendors.json"),
                         help="path to vendor signature JSON (default: vendors.json next to this script)")
    parser.add_argument("--json", help="write full results to this JSON file")
    parser.add_argument("--csv", help="write matches to this CSV file")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        sys.exit(1)

    vendors, local_allowlist, local_host_markers = load_db(args.vendors)

    all_matches = []
    all_suppressed = []
    parse_errors = []
    for py_file in find_python_files(root):
        matches, suppressed = scan_file(py_file, vendors, local_allowlist, local_host_markers, root)
        for m in suppressed:
            if m.match_type == "parse_error":
                parse_errors.append(m)
            else:
                all_suppressed.append(m)
        all_matches.extend(matches)

    all_matches = dedupe(all_matches)

    print_report(all_matches, all_suppressed)

    if parse_errors:
        print("Files skipped due to parse errors:")
        for e in parse_errors:
            print(f"  {e.file}: {e.note}")
        print()

    if args.csv:
        write_csv(args.csv, all_matches)
        print(f"Wrote CSV: {args.csv}")
    if args.json:
        write_json(args.json, all_matches, all_suppressed)
        print(f"Wrote JSON: {args.json}")


if __name__ == "__main__":
    main()
