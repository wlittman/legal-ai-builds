# Contract Review Playbook (Fernway)

## Problem

In-house teams review the same kinds of contracts and agreements repeatedly, and the quality of a first-pass review largely depends on the discretion of the individual who picks it up. This leads to increased cycle times and delays deals from getting done in an expedient manner. A written playbook, with clear positions and precise escalation points, makes first-pass review consistent and gives AI something definite to follow instead of guessing.

## What it is

A contract review playbook for Fernway Inc., a fictional company, built on the Claude for Legal commercial-legal plugin. It covers:

- Sales-side positions, for when Fernway sells to customers.
- Purchasing-side positions, for reviewing vendor paper.
- An NDA playbook, for example a reasonable-person standard for confidential information, and residuals clauses rejected for sales NDAs but accepted with guardrails for technical NDAs.
- Escalation points that say when a contract needs a more senior approver.

## How it was tested

- Against HubSpot's public Customer Terms of Service (https://legal.hubspot.com/terms-of-service). The test exposed four gaps, which I closed: a tiered position on AI output indemnity, breach-response costs treated as direct damages, IP indemnity scope tied to how critical the vendor is, and vendor insurance required above $250K in annual contract value when sensitive personal data is involved.
- Against synthetic test documents: a Harborline MSA markup and a Project Falcon NDA with planted issues.

## What is in this folder

- `fernway-profile/`: the playbook itself (practice profile and company profile).
- `fernway-tests/`: the test documents and the reviews they produced. All test documents are synthetic. HubSpot's terms are linked above, not copied.

## How it was built

I set the positions myself through the plugin's guided interview, working with Claude, then tested and refined them.

## Limitations

The positions are for a fictional company and are not legal advice. The playbook has been tested on a handful of documents, not measured at scale. Every output needs a lawyer's review.