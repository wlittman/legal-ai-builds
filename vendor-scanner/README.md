# AI Vendor Scanner

This tool scans a folder of Python source code and reports every place it finds evidence that the code calls a third-party AI vendor's API — services like OpenAI, Anthropic, Google Gemini, Cohere, and others. It looks for the kinds of code-level fingerprints a real integration leaves behind: `import` statements for a vendor's SDK, code that creates that vendor's client object, calls to that vendor's web address (endpoint), and environment variable names that vendor commonly uses for API keys. The output is a flat list of findings — file, line number, which vendor, what kind of evidence, and how confident the tool is — meant to give a reviewer a fast, repeatable starting point for figuring out which third-party AI services a codebase actually talks to, before that question gets answered definitively by contract review or engineering interviews.

## What This Tool Does NOT Do

Is not a comprehensive security audit. It detects code-level patterns (imports, client instantiation, endpoint strings, environment variable names) indicating third-party AI API usage. It does not assess whether that usage is secure, whether other categories of vulnerabilities exist, or whether data is handled safely once it reaches the vendor.

Is not a contract or licensing review. Identifying that a codebase calls a given vendor's API says nothing about whether an adequate vendor agreement exists, what that agreement permits, or whether its data-use, training, or liability terms are acceptable. That determination requires separate review of the actual contract.

Is not exhaustive. Detection relies on a seeded list of known vendor signatures (currently: OpenAI, Azure OpenAI, Anthropic, Google Gemini, Cohere, Mistral, Together AI, Groq, Replicate, Perplexity, xAI, Hugging Face Inference API, AWS Bedrock). A vendor not in that list, or an integration disguised through an unusual pattern (e.g., a generic HTTP client rather than an official SDK, or a proxied/renamed endpoint), may not be detected. Absence of a finding is not proof of absence of AI usage.

Is not immune to false negatives from obfuscation. Because detection is pattern-based rather than a full runtime analysis, a sufficiently unusual or deliberately obscured integration could evade detection.

Is Python-only at this time. Codebases in other languages are not scanned, even if they contain third-party AI API calls.

Does not evaluate data sensitivity. The tool flags that an AI API is being called; it does not assess what data is being sent to it, or whether that data includes personal information, trade secrets, or other sensitive content.

Is not legal advice, and does not replace attorney judgment. This is a first-pass triage aid intended to surface candidates for review. Every finding — and every file that did not generate a finding — should be independently verified by counsel before being relied upon in any client-facing determination.

## How to Run It

The tool is a single command-line script (`scanner.py`) that takes a folder path and scans every `.py` file inside it (skipping virtual environments, `.git`, `node_modules`, and similar noise directories).

```
python3 scanner.py /path/to/codebase
```

That prints a plain-text report to the screen: a summary count of matches per vendor, followed by a table of every individual finding (file, line, vendor, finding type, confidence, and the offending line of code).

Two optional flags save the same findings to a file, for attaching to an engagement record or handing to someone else on the review team:

- `--json report.json` — writes the full results as structured JSON, including both the flagged matches and anything the tool recognized but deliberately excluded (see "Local vs. Third-Party" below).
- `--csv report.csv` — writes just the flagged matches as a spreadsheet-friendly CSV (one row per finding), suitable for opening in Excel.

Example:

```
python3 scanner.py ./client-repo --json results.json --csv results.csv
```

A third flag, `--vendors`, lets you point the tool at a different vendor-signature file instead of the built-in `vendors.json` — useful if you maintain a customized or expanded vendor list for a particular engagement.

## What It Flags, and How Confidence Tiers Work

Every finding is one of several "match types," each of which is a different kind of evidence found in the code. Not all evidence is equally conclusive, so each finding also carries a confidence tier: **high**, **medium**, or **low**. Think of confidence as "how likely is it that this line of code represents the codebase actually sending data to that vendor," not "how likely is it that this vendor's name appears somewhere nearby."

**High confidence** — the code is actively constructing a vendor's client object or calling a method on one. This is the strongest signal: the code isn't just referencing the vendor, it's using it. Example, from a real scan of a small test project:

```
src/01_first_call.py:7   Anthropic   client_init   high
  client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

src/01_first_call.py:12  Anthropic   api_call      high
  response = client.messages.create(
```

**Medium confidence** — the code imports a vendor's SDK, references a vendor's known API endpoint as a string, or reads an environment variable with a name that vendor conventionally uses for its API key. Each of these is suggestive but not, on its own, proof the vendor is actually being called (a library might be imported and never used; an env var might be read and discarded). Examples, from a scan of a Django test project:

```
openapp/views.py:7    OpenAI   import    medium
  from openai import OpenAI

openapp/views.py:25   OpenAI   env_key   medium
  api_key=os.getenv("OPENAI_API_KEY"),
```

**Low confidence** — the tool found a string literal in the code that is *shaped* like one of that vendor's API keys (matches a known key prefix, such as `sk-` for OpenAI or `sk-ant-` for Anthropic) but the context doesn't otherwise confirm it. This mainly exists to catch hardcoded credentials left directly in source — a finding worth a human's attention precisely because it's unusual, but one the tool can't fully verify from context alone.

In every case, the "note" field (when present) gives the specific evidence — e.g. the exact import statement, or why a match was suppressed — so a reviewer isn't just trusting a label.

## Local vs. Third-Party: `local_allowlist` and `local_host_markers`

Not every AI-related import is a call to an outside vendor. A codebase might run its own machine learning model locally — on its own hardware, with no data ever leaving the organization's control — using libraries like Hugging Face's `transformers`, `sentence-transformers`, `llama.cpp`, `vLLM`, or `Ollama`, or general frameworks like PyTorch/TensorFlow. That's a fundamentally different risk picture than calling a hosted third-party API, so the tool distinguishes the two rather than lumping them together:

- **`local_allowlist`** is a list of import patterns known to represent locally-run or self-hosted models. When the tool sees one of these imports, it still records the fact (so the report shows what it saw and why it wasn't flagged), but it's placed in a separate "suppressed" / "recognized as local" bucket rather than counted as a third-party vendor finding.
- **`local_host_markers`** catches a different case: code that *does* instantiate an official vendor SDK client (e.g. the OpenAI Python client), but points it at a local address — `localhost`, `127.0.0.1`, `0.0.0.0`, or `::1` — via a `base_url` or similar override. That pattern typically means someone is running an OpenAI-API-compatible server on their own machine, not actually sending data to OpenAI, so the tool suppresses that finding too rather than misreporting a local setup as a live third-party call.

This distinction matters for a data-flow review specifically: the question a lawyer or privacy reviewer usually cares about is "does data leave our infrastructure," and a locally-run model, by design, does not send data anywhere.

## Why `vendors.json` Is Structured as Data, Not Code

All vendor-specific knowledge — which imports to look for, which class names count as "creating a client," which network endpoints belong to a vendor, which environment variable names it uses, and what its API keys look like — lives in the `vendors.json` file, not hardcoded into the Python scanning logic. `scanner.py`'s only Python-specific job is parsing Python source code and checking it against whatever signatures `vendors.json` contains.

This separation is deliberate for two reasons. First, it means adding a new vendor, or correcting/expanding an existing one, is a matter of editing a data file — no code changes, no risk of introducing a bug in the parsing logic. Second, and more importantly, the signature format (dotted import paths, class names, endpoint strings, environment variable names, key prefixes) isn't Python-specific — the same file can be read by a parser for a different language. If this tool is ever extended to scan JavaScript/TypeScript, Go, or another language, that new parser can reuse `vendors.json` as-is rather than re-encoding the same vendor knowledge a second time.

## Redaction: Hardcoded Keys Are Masked, Not Reproduced

When the tool's report includes the actual line of code where a finding occurred (the "snippet"), it never reproduces what looks like a real, complete API key. Before a snippet is written into the on-screen report, the JSON file, or the CSV, the tool checks it against every vendor's known key-prefix patterns (e.g. `sk-`, `sk-ant-`, `AIzaSy`, `hf_`) and, if it finds something key-shaped, replaces the sensitive part with the prefix plus `<REDACTED>` — so a finding like `sk-ant-a1b2c3...` becomes `sk-ant-<REDACTED>` in the output.

This matters because these reports — JSON files, CSV exports, or just pasted terminal output — routinely get committed to case files, emailed, or handed to clients and co-counsel. Without this masking, a security/compliance report could itself become a second place a live credential is stored and circulated. The redaction preserves enough of the key (which vendor it belongs to) for the finding to remain useful, while ensuring the report itself is never a leak vector.
