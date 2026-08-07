---
name: astro-persona-profiles
description: Manage planetary persona profiles, YAML enrichment, and CSV eval generation.
version: 1.0
author: greenknight
tags: [persona, astrology, yaml, evaluation, csv, prompt-engineering]
platforms: [linux]
---

# Astro Persona Profiles Skill

Work with the `astro_activation_engineering` project — planetary persona YAML
profiles, the correspondence lexicon, prompt templates, and the CSV generation
pipeline for evaluating persona expression in LLM outputs.

## When to Use

- Editing, auditing, or enriching planet YAML profiles under `03_profiles/planets/`
- Modifying the generation prompt template in `04_prompts/persona_prompts/`
- Cross-referencing profiles against the `Medieval_Astrology_Correspondence_Lexicon.xlsx`
- Running or modifying `generate_planetary_csvs_transformers.py`
- Diagnosing persona scoring failures (uniform theatricality, rubric violations,
  judge/generator information asymmetry)

## Project Structure

```
astro_activation_engineering/
├── 03_profiles/
│   ├── planets/{saturn,jupiter,mars,sun,venus,mercury,moon}.yaml
│   └── Medieval_Astrology_Correspondence_Lexicon.xlsx  # source-of-truth reference
├── 04_prompts/persona_prompts/planetary_prompt_template.md
├── 09_scripts/
│   ├── bridge_profile_loader.py   # loads YAMLs + template, formats prompts
│   └── validate_profiles.py       # checks YAMLs for required fields
└── LLM_Persona-main/
    ├── generate_planetary_csvs_transformers.py  # main eval pipeline
    └── eval_persona_extract/hermes3_8b/         # output CSVs
```

## YAML Profile Structure

Each planet YAML has three groups of fields:

**Behavioral** (for generation prompt):
- `prompt_profile.identity_instruction` — feeds `{{historical_core}}`
- `prompt_profile.behavioral_rules` — feeds `{{intended_model_behaviors}}`
- `prompt_profile.anti_profile_guardrails` — feeds `{{anti_profile_guardrails}}`

**Source-grounded** (from the lexicon, for enrichment):
- `named_virtue` — Picatrix operative power (e.g. "Retentive virtue")
- `sensory_register` — taste, odor, color, sound, stones, metals, animals, plants, organs
- `ficino_spiritus` — relationship to the subtle medium, gift, cost, remediation

**Governance** (for validation):
- `symbolic_construct.core_terms` — feeds judge's `core_qualities`
- `behavioral_translation.intended_model_behaviors` — feeds judge's `intended_behaviors`
- `behavioral_translation.forbidden_caricatures`
- `failure_conditions` — what happens when the profile goes wrong

## The Bridge Architecture

`bridge_profile_loader.py` connects the separated directories:

```
YAML profiles + .md template  ──bridge──>  CSV generation script
(astro_activation_engineering)           (LLM_Persona-main)
```

Key functions:
- `load_all_planets()` → `dict[name, profile]`
- `build_generation_prompt(name)` → full persona system prompt
- `build_judge_context(name)` → `dict` with `core_qualities`, `named_virtue`,
  `sensory_register`, `intended_behaviors` — all four feed the JUDGE_TEMPLATE

The CSV script imports via `sys.path` manipulation from its location:

```python
_SCRIPT_DIR = Path(__file__).resolve().parent
_ASTRO_ROOT = _SCRIPT_DIR.parent
sys.path.insert(0, str(_ASTRO_ROOT / "09_scripts"))
import bridge_profile_loader as _bridge
```

## Related: Composite Persona Approach

A second persona methodology exists alongside the single-planet YAML profiles.
The `astral-research-harness` skill implements the **composite chart persona**
approach — planetary functions arranged by aspect relations (conjunctions,
oppositions, trines, sextiles) into a unified operating system rather than
discrete single-planet profiles.

Key differences from single-planet YAML profiles:
- **Source:** A composite-chart operating guide (407-line constitution) plus
  an operational harness with dynamic mode selection, self-correction probes,
  and an automatic learning loop.
- **Target:** An always-on research assistant persona that dynamically selects
  planetary circuits per task archetype — not a fixed single-planet persona.
- **Evolution:** Patches itself via structured reflection thresholds, rather
  than requiring manual YAML enrichment.

To view: `skill_view(name='astral-research-harness')`
Reference doc: `.hermes/hermes-agent/docs/Ideal_Research_Assistant_Operating_Guide.txt`

## Pitfalls

### Judge/Generator Information Asymmetry
The judge must see the same reference data the generator used. If the
generator received a sensory register (colors, tastes, sounds) but the
judge only sees `core_qualities`, the judge cannot distinguish legitimate
sensory choices from generic ornateness. **Always give the judge the full
context: core_qualities, named_virtue, sensory_register, AND intended_behaviors.**

### Rubric Violations (Planet Naming)
The judge rubric caps scores at 3 when the response explicitly mentions
planets, astrology, or deities. The generation prompt says "do not name
the planet." Yet models reliably break this rule — in one audit, 41% of
pos_instruct answers named a planet and scored 6-7 instead of ≤3.
**Add a regex pre-check before the LLM judge to catch planet names
deterministically.**

### Uniform Theatricality
Dumping Renaissance theory (Ficino, Picatrix, humoral bases, named
virtues) on the model produces uniform ornate prose across all personas.
**Use behavioral rules ("Identify constraints before conclusions") instead
of sensory catalogues.** The sensory register is reference material, not
stage direction.

### Hardcoded Data Rot
The original script had a 65-line hardcoded `PLANETS` dict. When the
canonical data lives in YAML profiles, the script drifts. **Always load
from YAML via the bridge — never duplicate persona data inline.**

## Verification

Run `09_scripts/validate_profiles.py` to check YAML structural integrity.
Run `bridge_profile_loader.py <planet>` to preview a generated prompt.
