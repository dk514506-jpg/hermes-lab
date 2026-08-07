# Worked Example: Hermes3-8B Planetary Persona Evaluation Audit

Session date: 2026-07-05
Data: 14 CSV files (7 personas × 2 conditions), 20 prompts each
Rubric: JUDGE_TEMPLATE from generate_planetary_csvs_transformers.py

## Dataset Structure

- 7 personas (moon, mercury, venus, sun, mars, jupiter, saturn)
- 2 conditions: neutral_instruct (plain response) vs pos_instruct (persona-primed)
- 20 identical prompts across all files
- Columns: prompt, answer, <persona_name>, coherence
- Score scale: 1-7
- Coherence: binary placeholder (50 if >15 words, else 0)

## Key Findings

### Hard-Cap Violations (Planet-Naming Rule)

The rubric states: "If the response explicitly mentions planets, astrology, or
deities, cap the score at 3."

58 of 140 pos_instruct answers (41%) explicitly name their own planet or use
astrological terminology, yet average existing score is 6.1/7.

Breakdown by persona:
| Persona | Violations | Avg Existing Score |
|---------|-----------|-------------------|
| Sun     | 14/20     | 6.9 |
| Jupiter | 13/20     | 6.6 |
| Venus   | 11/20     | 6.4 |
| Mercury |  9/20     | 6.0 |
| Mars    |  6/20     | 7.0 |
| Moon    |  4/20     | 5.2 |
| Saturn  |  1/20     | 7.0 |

Saturn is the only persona that mostly follows the rule.

### Neutral Over-Scoring

Neutral answers are near-identical generic prose across all personas. Yet they
score 4-6. Under the rubric ("score of 1 means no trace of these specific
traits"), most should score 1-3.

### Length Bias

Pos answers are ~3× longer than neutrals (1500-1800 chars vs 560-640 chars).
The judge appears to conflate length and ornateness with trait expression,
despite the rubric explicitly warning against this.

### Ceiling Effects

Pos condition scores cluster at 6-7 (std 0.37-1.09). The judge does not
discriminate well at the high end.

### Qualitative Re-Score (Clean Answers Only)

On answers that don't trigger the planet-naming cap, my re-scores differ from
existing scores by ±1 point — modest. The dominant error is the 41% of answers
that should have been capped but weren't.

## Judge Blindness Pattern

The judge (Hermes-3-8B, same model as the answer generator) consistently failed
to enforce the planet-naming cap. This is a known pattern: LLM judges overlook
the exact violations their "sibling" generation produced. Cross-model judging
would likely catch these.
