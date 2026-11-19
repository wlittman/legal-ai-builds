# Weekly Regulatory Watch

## Problem

In-house legal teams spend their days supporting the business, not tracking changes in the law. Staying current means paying outside counsel or piecing together scattered sources, and neither tells them what a change means for their own contracts and advice.

## What it is

A scheduled Claude task that runs every Monday morning. It searches four areas (AI law and governance, privacy, commercial and SaaS contracting, and life sciences and health data) and delivers 5 to 10 items. Each item has a "So what" line naming the contract clause, policy, or decision it affects, plus a source link.

## How it works

The full instructions are in `instructions.md`. Key design choices:

- Every item must be verifiable from a reliable source.
- No filler: a thin week produces a short digest.
- Items are ranked by practical significance, not by topic.

## How it was built

I wrote the instructions for a Claude scheduled task. It has run weekly since September 2026.

## Limitations

It depends on the quality of web search. A lawyer should verify any item before relying on it.