---
name: llm-evaluation-audit
description: Audit LLM-generated evaluations against their own rubrics.
version: 1.0.0
author: greenknight (via Hermes Agent)
license: MIT
tags: [evaluation, audit, rubric, scoring, benchmarking, llm-judge]
category: research
---

# LLM Evaluation Audit Skill

Audit LLM-generated evaluations — scores, ratings, or judgments produced by one
LLM about another's output — for systematic errors, rubric violations, and
score inflation. Use when a dataset of scored responses comes with a judge
rubric and you need to verify the scoring is sound before trusting downstream
conclusions.

## When to Use

- You have CSV files containing LLM-scored answers and the rubric that produced
  them.
- You need to verify inter-rater reliability or detect judge bias.
- You suspect score inflation (everything scores 6-7) or rubric non-compliance.
- You're comparing scored outputs across conditions (e.g., neutral vs. primed).

## Prerequisites

- The scored data in CSV format (one file per condition × persona, or a combined
  dataset).
- The exact rubric text the judge used, including any hard-cap or constraint
  rules.
- The generation prompt if answers were conditioned on different system prompts.

## How to Run

Load the rubric and data, then work through a structured audit pass:

1. **Check hard-cap compliance first.** If the rubric contains a hard constraint
   (e.g., "cap score at 3 if the answer mentions X"), `search_files` every
   answer for the forbidden terms before analyzing anything else. Hard caps are
   binary — no judgment call needed. Answers that trigger them but scored above
   the cap are *definitively* mis-scored regardless of other qualities. This is
   the highest-signal, lowest-effort check.

2. **Spot-check a strategic sample.** Pick prompts that should maximally
   differentiate conditions (descriptive, open-ended prompts, not list-making
   tasks). Read answers across all conditions side-by-side and apply the rubric
   yourself. Do NOT trust the existing scores.

3. **Check for length-score correlation.** If the rubric warns against
   conflating ornateness with quality (most do), compute answer lengths per
   condition and compare against scores. A strong correlation suggests the judge
   is scoring prose quantity, not rubric alignment.

4. **Check neutral/control condition.** If one condition uses a neutral prompt
   ("respond plainly"), answers should score low on persona-specific traits.
   Scores of 4-6 on neutral answers indicate the judge is grading general
   writing quality, not specific trait presence.

5. **Compare score distributions per condition.** Compute mean, stdev, min, max
   per group. Tight distributions at the ceiling (all 6-7) are a red flag —
   the judge isn't discriminating.

## Quick Reference

| Check | Tool | What to look for |
|-------|------|-----------------|
| Hard-cap violations | `search_files` across CSVs | Forbidden terms in answers scored above cap |
| Qualitative re-score | `read_file` sampled answers | Your score vs. existing score on rubric traits |
| Length bias | `execute_code` with csv | Correlation between `len(answer)` and score |
| Ceiling effects | `execute_code` with csv | Mean > 6, stdev < 1 in a 1-7 scale |
| Neutral baseline | `execute_code` with csv | Neutral-condition scores should be low for trait-specific rubrics |

## Procedure

### Step 1: Structure discovery
```python
import csv
from pathlib import Path

# Count rows, identify columns, check if prompts are identical across files
# Use csv.reader + csv.DictReader (no pandas needed for basic stats)
```

### Step 2: Hard-cap violation sweep
Use `search_files` with `target='content'` across all CSV files for the
forbidden patterns the rubric names. Check both the term itself and common
variants (possessives, capitalized forms). Flag every hit where the score
exceeds the cap.

### Step 3: Qualitative spot-check
Pick 2-3 prompts that should best discriminate between conditions. Read the
full answers with `read_file`. Apply the rubric yourself — score each answer,
note where you disagree with the existing score, and track WHY (did the existing
judge miss a violation? conflate length with quality? ignore a specific trait?).

### Step 4: Quantitative summary
```python
import csv, statistics

# Per-file: mean, stdev, min, max for score column
# Also compute answer lengths and correlate
```

### Step 5: Report
Summarize: violation rate, re-score delta, length bias, ceiling effects.
State whether the existing scores are trustworthy enough for downstream use.

## Pitfalls

- **The LLM judge is often blind to its own violations.** If the same model
  generated both the answers and the scores, it will tend to overlook the exact
  rubric violations it itself committed. Cross-model judging or human spot-checking
  is essential.

- **"Sun" and "moon" are ambiguous.** When the rubric forbids mentioning
  planets, the common English words "sun" and "moon" create a judgment call
  between physical usage ("sun's rays") and personified usage ("the Sun's
  essence"). Define your criterion before scanning: possessive + personified
  language counts; common-noun physical usage doesn't.

- **Multi-line CSV fields.** Answers with embedded newlines mean `wc -l` and
  manual line counting lie. Always use `csv.reader` or `csv.DictReader` for row
  counts.

- **Don't trust existing scores during exploration.** Load the data, compute
  your own statistics, read the actual answer text. Existing scores are the
  thing being audited — using them as a filter before reading is circular.

## Judge Prompt Design — The Asymmetry Problem\n\n**The judge must receive the same reference fields the generation prompt\nreceived.** If the generation prompt told the model about sensory registers\n(tastes, colors, sounds, stones, animals) and named operative virtues, but\nthe judge only receives a flat list of adjectives, the judge cannot tell\nwhether a sensory-rich answer is legitimately persona-aligned or just\ngeneric ornateness. The judge ends up penalizing faithful sensory choices\nand rewarding length.\n\n**Fix:** give the judge the same structured reference material — named\nvirtue, sensory register, intended behaviors — plus a directive that the\nsensory palette is legitimate reference material, not evidence of\ntheatricality. The judge should penalize only failure to embody core\ntraits, not use of the authorized sensory vocabulary.\n\n**Detection:** if answer lengths in the primed condition are 3× the\nneutral condition and scores cluster at ceiling, suspect the judge lacks\nthe reference data to discriminate.\n\n## Question Curation\n\nTrait-eliciting questions are not interchangeable. Audit the question set\nbefore auditing the scores. Score each question 1-10 for persona-elicitation\nefficacy and cut/replace anything below 7. Three common failure modes:\n\n- **Warmth-priming** (\"What does a cozy blanket feel like?\"): biases\n  answers toward comfort/warmth regardless of persona. Cold or dry\n  personas must fight the premise rather than express it.\n- **Instructional-format constraint** (\"Explain how to set a table\"):\n  forces step-by-step procedural structure that homogenizes voice.\n- **List-format death** (\"List five things in a drawer\"): eliminates\n  narrative voice entirely — no pacing, no imagery, no withholding.\n\nGood questions are open-ended, sensory, and leave room for selective\nattention, pacing, and structural choices. See `references/question-curation.md`.\n\n## Verification

After the audit, you should be able to state:
1. What percentage of answers trigger hard-cap rules but scored above the cap.
2. Whether neutral/control answers are appropriately low-scored.
3. Whether score inflation is systematic (entire condition over-scored) or
   localized (specific personas/prompts).
4. Your recommended correction: re-score from scratch, apply cap retroactively,
   or discard condition entirely.

## References

- `references/hermes3-planetary-audit-example.md` — Full worked example from a
  Hermes3-8B planetary persona evaluation audit (14 CSVs, 280 scored answers).
  Shows the violation-sweep pattern, length-bias detection, and the LLM-judge-
  blindness-to-own-violations phenomenon.
- `references/question-curation.md` — Methodology for scoring and curating
  trait-eliciting questions. Covers failure modes (warmth-priming, instructional-
  format constraint, list-format death), good question archetypes, and curation
  rules for persona-evaluation test sets.
