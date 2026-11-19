# NDA Review Evaluation Rubric

## Problem

An AI-generated NDA review can sound confident and still miss issues. Without a fixed rubric, judging its quality is laregly subjective and a matter of opinion.

## What it is

A rubric of 34 pass-or-fail criteria worth 79 weighted points (High = 3, Medium = 2, Low = 1), organized in three parts:

- Affirmative requirements: did the review catch what it should catch?
- Negative space: did the review avoid accepting what it should not accept?
- Hedging guards: checks on how the review qualifies its conclusions.

Scoring is binary, with no partial credit. The criteria are tied to the Fernway NDA positions, and the format follows the weighted-criteria style used by published legal AI benchmarks.

## First result

I used the rubric to score an AI review of the synthetic Project Falcon NDA. It scored 70 of 79 points (88.6%), passing 30 of 34 criteria. Its one High-weight failure: it suggested that a narrowed version of a restriction could be accepted. See `falcon-scorecard-run1.md`.

## What is in this folder

- `rubric.md`: the rubric.
- `falcon-scorecard-run1.md`: the first scorecard, criterion by criterion.

## How it was built

I designed the rubric with Claude. The scoring run was performed by Claude against the rubric, and I spot-checked the closest calls.

## Limitations

One test document so far. Scoring by an AI model needs human spot checks. The next step is measured testing across many NDAs.