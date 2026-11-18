# NDA Review Eval Rubric

Oct 16, 2026 · @WL

## Purpose

This eval measures whether an AI workflow can redline an inbound NDA against an in-house playbook the way a competent senior associate would. It borrows the structure of the open-sourced [Legora BAR tax case](https://github.com/legora-oss/legora-bar-tax-case): one fixed case, binary expert-written criteria, weighted by risk, and grouped into affirmative requirements, negative space and hedging guards.

Playbook positions below reflect the Fernway NDA playbook (a fictional company).

## Test case

The case is a synthetic mutual NDA for "Project Falcon" with nine planted issues and four acceptable clauses that must be left alone. Every criterion below traces to one row of this table, so a grader can verify it against the draft.

**Prompt given to the system**

> We received the counterparty's draft NDA for Project Falcon (in the matter folder). Redline it against our NDA playbook, with particular attention to the term, the definition of Confidential Information, and the non-solicit. Mark anything that has to stay out of policy, and give me a short cover note on the points that need a decision from us.

**Matter file room:** counterparty draft NDA (.docx), the NDA playbook, and the company's standard mutual NDA as precedent.

**Planted issues and playbook positions**

| Draft section | What the counterparty draft says | Playbook position | Severity | Criteria |
| --- | --- | --- | --- | --- |
| 2. Definition of CI | All information "whether or not marked"; oral disclosures covered with no written follow-up | Marked, or what a reasonable person would understand to be confidential; no written confirmation required | High | A-03, A-04 |
| 2. Exclusions | Omits the independent-development exception | All four standard exclusions required | High | A-05 |
| 4. Term | Obligations last 7 years from disclosure for all CI | 3 years from disclosure; trade secrets protected while they remain trade secrets | High | A-01, A-02 |
| 6. Non-solicit | 24 months, all employees, no general-solicitation carve-out | Strike; fallback 12 months, only employees met through the deal, carve-out for general ads | High | A-06, A-07, A-08 |
| 7. Residuals | Broad residuals clause for anything retained in unaided memory | Reject for sales or deal NDAs (Falcon is one); accept with guardrails for technical NDAs | High | A-09 |
| 9.4 Misc. (buried) | 18-month bar on dealing with the discloser's portfolio companies | Reject; out of policy, needs a business decision | High | A-10, A-11 |
| 8. Return/destroy | Destroy all copies in 10 days with certification; no backup carve-out | 30 days; carve-out for automatic backups and legal-hold copies | Medium | A-12 |
| 10. Assignment | Counterparty may assign freely; company may not | Mutual, with consent not unreasonably withheld | Medium | A-13 |
| 11. Notices | Email notice deemed received on sending | Received on confirmation or next business day | Low | A-14 |
| 5. Compelled disclosure | Prompt notice and cooperation | Acceptable as drafted | None | B-01 |
| 12. Governing law | Delaware, Delaware courts | Delaware or New York acceptable | None | B-02 |
| 13. Injunctive relief | Standard equitable relief clause | Acceptable as drafted | None | B-03 |
| Throughout | Obligations run both ways | Mutuality required | None | C-01 |

Open item: the synthetic NDA text itself still needs drafting so each planted issue sits in realistic surrounding language.

## Scoring method

Each criterion is pass or fail, weighted High = 3, Medium = 2, Low = 1, and the score is weighted points earned over points available. Weighting follows Legora's reasoning: a missed residuals clause and a missed notice provision are both errors, but no partner treats them alike. The exact point values are this rubric's choice; Legora does not publish its own.

1. Run each configuration (model, effort setting, prompt version) three times on the same case.
2. Grade each output with an LLM judge that sees one criterion at a time and must quote the passage of the output that supports its verdict.
3. Have a lawyer spot-check at least 20% of judgments, and every judgment where the three runs disagree.
4. Report the weighted score, the unweighted pass count, and every failed High criterion by ID.

Any failed High criterion is reported on its own line, whatever the overall score. A 90% score with a missed buried non-compete is not a passing review.

## Part A: Affirmative requirements

These 20 criteria test whether the review finds and fixes every planted issue and delivers what the prompt asked for. Each is worded so a grader can check it against the output without judgment calls.

| ID | The output must... | Weight |
| --- | --- | --- |
| A-01 | Redline the Section 4 term from 7 years to 3 years from disclosure | High |
| A-02 | Add a carve-out keeping trade secrets protected for as long as they remain trade secrets | Medium |
| A-03 | Narrow "whether or not marked" to information that is marked, or that a reasonable person would understand to be confidential given its nature and the circumstances of disclosure | High |
| A-04 | Cover oral disclosures through the reasonable-person standard, without demanding marking or written confirmation | Medium |
| A-05 | Add the independent-development exclusion to Section 2 | High |
| A-06 | Strike the Section 6 non-solicit as the primary position | High |
| A-07 | Offer the fallback non-solicit: 12 months, limited to employees met through the deal | Medium |
| A-08 | Include a carve-out for general solicitations not targeted at the discloser's employees | Medium |
| A-09 | Strike the Section 7 residuals clause in full, because Falcon is a sales or deal discussion, not a technical one | High |
| A-10 | Identify the 18-month portfolio-company restriction in Section 9.4 | High |
| A-11 | Strike Section 9.4 and mark it out of policy, needing a business decision | High |
| A-12 | Extend return/destroy to 30 days, with a carve-out for backups and legal-hold copies | Medium |
| A-13 | Make assignment mutual, with consent not unreasonably withheld | Medium |
| A-14 | Change email notice to effective on confirmation or the next business day | Low |
| A-15 | Deliver the changes as tracked changes against the counterparty draft, not a clean rewrite | High |
| A-16 | Give a cover note that lists the out-of-policy points needing a decision, including Section 9.4 and the non-solicit fallback | High |
| A-17 | Keep the cover note to points that need a decision, leaving routine fixes out of it | Medium |
| A-18 | Tie each proposed change to the relevant playbook position | Medium |
| A-19 | Address all three priority points named in the prompt: term, CI definition, non-solicit | High |
| A-20 | Leave the counterparty's defined terms and section numbering intact | Low |

## Part B: Negative space

These 9 criteria test what the review must not do: invent problems, over-lawyer acceptable clauses, or misstate the draft. In the Legora tax case, models scored well here, so a failure on this list is a strong signal of regression.

| ID | The output must not... | Weight |
| --- | --- | --- |
| B-01 | Redline the Section 5 compelled-disclosure clause, which is acceptable as drafted | Medium |
| B-02 | Flag Delaware governing law or venue as an issue | Medium |
| B-03 | Redline or weaken the Section 13 injunctive-relief clause | Low |
| B-04 | State or imply that the NDA is one-way | High |
| B-05 | Cite a playbook position that is not in the playbook | High |
| B-06 | Attribute to the counterparty draft language it does not contain | High |
| B-07 | Silently change any clause without tracking the change | High |
| B-08 | Recommend accepting the residuals clause or Section 9.4 in any form | High |
| B-09 | Add new obligations on the counterparty that the playbook does not call for | Medium |

## Part C: Hedging guards

These 5 criteria test whether the review states plain facts plainly. Over-hedging was the weakest category in the Legora tax case, and in contract work it pushes verification back onto the lawyer the tool was meant to save time for.

| ID | The output must state, without a "please confirm" or "may" qualifier... | Weight |
| --- | --- | --- |
| C-01 | That the NDA is mutual | Medium |
| C-02 | That the Section 4 term is 7 years, outside the 3-year playbook position | Medium |
| C-03 | That Section 2 omits the independent-development exclusion | Medium |
| C-04 | That the residuals clause is out of policy | Medium |
| C-05 | That Delaware governing law is acceptable under the playbook | Low |

A guard fails if the fact is wrong, missing, or wrapped in a request to confirm something the matter file already settles.

## Using it for model switch-outs

The rubric has 34 criteria worth 79 weighted points, and its main job is to catch what a model change breaks. Run it before any change to the model, effort setting, prompt or playbook, and compare criterion by criterion, not just the totals.

1. Record a baseline: per-criterion results for the current configuration across three runs.
2. Rerun the identical case and rubric on the new configuration. Never edit criteria between the two runs.
3. Treat any criterion that passed in most baseline runs and fails in most new runs as a regression.
4. Ship the change only with zero High regressions and a weighted score no more than 3 points below baseline.
5. When a live review misses something, write a new criterion for it and add it to the next baseline.

This rubric and its synthetic test case are published as a portfolio sample. Because public test cases can end up in future AI training data, scores on this exact case should be treated as illustrative. A real evaluation should use private, unpublished cases.

## Sources

- [Introducing the Legora BAR](https://legora.com/bar), Legora
- [Legora BAR tax case](https://github.com/legora-oss/legora-bar-tax-case), GitHub
- [Legora BAR Tax Case independent evaluation](https://overfittingdicta.com/), Overfitting Dicta
