# Hermes-3-8B Persona Scoring Audit (2026-07-05)

## Dataset

140 answers total: 7 planets × 2 conditions (neutral_instruct, pos_instruct) × 20 prompts.
Model: NousResearch/Hermes-3-Llama-3.1-8B.

## Key Findings

### 1. Planet-Naming Violations (Rubric Cap Breach)

58 of 140 pos_instruct answers (41%) explicitly name planets or astrological
terms, yet average existing score is 6.1 — should be ≤3 per rubric.

| Persona | Violations | Avg Score (should be ≤3) |
|---------|-----------|--------------------------|
| Sun     | 14/20     | 6.9 |
| Jupiter | 13/20     | 6.6 |
| Venus   | 11/20     | 6.4 |
| Mercury |  9/20     | 6.0 |
| Mars    |  6/20     | 7.0 |
| Moon    |  4/20     | 5.2 |
| Saturn  |  1/20     | 7.0 |

Saturn is the only compliant persona. Sun violates on 70% of answers.

### 2. Neutral Answers Systematically Over-Scored

Generic "peaceful sanctuary" prose scores 4-6 across all personas.
Most should be 1-3 — they show zero persona-specific traits.

### 3. Uniform Theatricality in Pos Answers

All pos answers share the same Renaissance-astral-prose register.
Differentiation is cosmetic (adjective swaps) not structural (pacing,
withholding, rhythm). The model learned one trick and applied it uniformly.

### 4. Judge/Generator Information Asymmetry

The generator received 7 fields (core_qualities, named_virtue, humoral_basis,
embodiment, motion_texture, sensory_register, operative_tendency). The judge
received only core_qualities. The judge could not distinguish legitimate
sensory choices (e.g., Jupiter's peach/cinnamon/sapphire palette) from
generic ornateness.

## Root Causes

1. **POSITIVE_TEMPLATE** dumped full Renaissance theory → uniform ornate register
2. **JUDGE_TEMPLATE** lacked sensory/behavioral reference data → conflated
   ornateness with trait alignment
3. **No pre-check** for planet-naming → 41% of scores invalid
4. **Hardcoded PLANETS dict** in script → data drift from canonical YAML profiles

## Remediations Applied

- Replaced POSITIVE_TEMPLATE with behavioral-rules template from
  `planetary_prompt_template.md`
- Enriched judge context with named_virtue, sensory_register, intended_behaviors
- Built bridge_profile_loader.py to load from YAML profiles
- Enriched all 7 YAMLs with sensory_register, named_virtue, ficino_spiritus fields
- Removed hardcoded PLANETS dict from CSV script
