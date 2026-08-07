# FAOS Integration Audit — worked example (2026-07-30)

Audit of `triage_faos_integration.yaml` (the FAOS-extended pipeline config at
`~/.hermes/hermes-agent/docs/triage_faos_integration.yaml`) against the stock
hermes-multi-agent-workflow engine. Use this as a template for future audits.

## Method

Loaded the YAML with `yaml.safe_load`, then checked cross-references
programmatically. Findings below are what the check surfaced — the checks
themselves are the audit discipline in the SKILL.md body.

## Findings (severity-ranked)

### Severity 1 — actual defects

1. **route.map is NOT stock-engine compatible.** Stock `Route` dataclass is
   `dict[str, str]`; extended entries are dicts with
   primary/shadow/shadow_conditions/promotion_rule. Consequences:
   - `validate()` → `TypeError: unhashable type: 'dict'`
   - routing → dict returned as path name → `ConfigError`
   Fix: engine patch (`route_with_shadow()`) or flag as spec-only.
2. **Typo in source id:** `knowlege-scout` → `knowledge-scout`.
3. **Orphan role:** `hardware-operator` defined in `roles:` but used nowhere.
4. **Undeclared source profile:** sources use `profile: persona-research`
   which appears in no `roles:` mapping.

### Severity 2 — incomplete

5. **`astra:` block is metadata only** — header comment says "not consumed by
   the engine." Persona governance depends on the orchestrator skill reading
   it; nothing enforces this.
6. **No Locus/Validator-Steward role** (FAOS §11.5) — the epistemic
   gatekeeper for corrected beginnings, route validity, shadow promotion,
   dissent, proof obligations is absent.
7. **No proof obligations** (FAOS §8) — route-selection/action/generalization/
   promotion proofs not encoded anywhere.
8. **No triage depth / cached routes** (FAOS §6.3, failure-mode 10) — every
   item runs the full ladder; governance-saturation risk for low-stakes items.
9. **No `schema_version`** — config has no version stamp; drift undetectable.
10. **perception contract mismatch** — `perception.required_outputs` lists 10
    fields; stock `intake_parser.py` parses only title/claim/sources/why.
11. **Scout skills referenced but not created** — triage-scout-bridge,
    triage-scout-generation, triage-scout-hardware, triage-scout-seer are
    declared in sources: but don't exist (template ships one generic scout).

### Severity 3 — continuity

12. **Four planetary-mapping tables with no single source of truth** —
    stakes.governed_by/monitored_by, rubric.planetary_governor,
    astra.circuit_map, skill §7.1 role table. Change one, others drift.
13. **Always-on persona has no load mechanism** — the harness skill must be
    loaded per session; nothing (AGENTS.md, cron, config) primes it.
14. **Layer connections are aspirational** — four-layer diagram shows See-R →
    pipeline and HOMES → pipeline links, but no mechanism (Zenoh topics?
    GreptimeDB queries? vocabulary constraints?) is specified.

## What passed

- All route targets resolve to defined paths (primary + shadow).
- All roles used in stages/lanes are defined.
- Evidence ladder: 5 canonical levels in order, non_skip: true.
- Every path's close block has all 6 required passes.
- Learning_loop pattern thresholds all present.
- astra block complete (persona, harness_skill, circuit_map, reference_doc).

## Reusable verification pattern (python)

```python
import yaml, sys
data = yaml.safe_load(open(cfg_path))
# check: route targets in paths; roles used ⊆ roles defined;
# evidence ladder order; close passes complete; no orphans
```

A fuller version of these checks is what produced the pass/fail table above;
the discipline is: run the structural check BEFORE claiming compatibility,
and always verify dataclass types against the engine source when extending
the schema.
