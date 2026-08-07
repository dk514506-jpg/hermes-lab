---
name: faos-pipeline-architecture
description: Design/audit FAOS-governed multi-agent pipelines on Hermes.
---

# FAOS Pipeline Architecture

Design pattern for config-driven multi-agent pipelines governed by FAOS
(Field-to-Action Operating System) semantics, built on the
hermes-multi-agent-workflow skeleton (tonbistudio, MIT).

## When to use

- Extending a triage.yaml-style pipeline with epistemic governance
  (evidence ladders, shadow routing, instrumented close, learning loop)
- Wiring a behavioral/persona layer into multi-agent pipeline roles
- Auditing whether a pipeline config is actually engine-compatible
- Working across the user's four-layer stack: See-R / FAOS / persona / HOMES

## The four-layer stack

1. **See-R Knowledge Base** — source inventory, authority maps, quarantine
   registers, controlled vocabularies, evidence provenance levels.
2. **FAOS / Multi-Agent Pipeline** — the operating cycle: field perception →
   task abstraction → triage → research → route (with shadow) → human gate →
   execute → instrumented close → digest → calibrate.
3. **Astral Research Persona** — behavioral governance for every pipeline
   role; defines HOW each role executes (see astral-research-harness skill).
4. **HOMES Core** — hardware substrate: RTX 3060 host, Pi cluster, ESP32
   sensors, Wi-Fi CSI, Zenoh mesh, Neo4j hypergraph, GreptimeDB.

## Reference artifacts

- Integrated config: `~/.hermes/hermes-agent/docs/triage_faos_integration.yaml`
  (schema `faos-integration/2.0` — the schema_version key lives under
  PIPELINE IDENTITY, a real YAML key, not a comment)
- **Engine extension: `~/.hermes/hermes-agent/docs/faos_engine_extension.py`**
  — makes the extended schema RUNNABLE without patching the stock engine.
  `FaosConfig.load()` accepts BOTH v1 string route values and v2 dict
  values (primary/shadow). `FaosEngine` implements route_with_shadow,
  should_promote_shadow, assert_evidence_promotion, assert_state_transition,
  assert_quarantine_claim, validate_metric, assert_not_absent (Book X
  absence gate), assert_operational (Book VII non-operational registry),
  close_spec, locus_review_spec.
  Self-test: `python3 faos_engine_extension.py`
- **Verification harness: `~/.hermes/hermes-agent/docs/verify_faos_pipeline.py`**
  — 20 deterministic checks against the real config (routes resolve,
  weights 5..1, ladder stepwise-only, S0→S5 blocked, Q0-Q2 only operational,
  metric bundle required, absence register blocks registered key, barred
  resonance blocked, close ≥6 passes, locus 7 checks, roles defined).
  Exit 0 = pass. This is the standing test entry point — re-run after any
  config edit: `python3 verify_faos_pipeline.py`
- **Canonical test runner: `~/.hermes/hermes-agent/docs/scripts/run_tests.sh`**
  — the standard entrypoint: 1/4 py_compile, 2/4 behavioral harness,
  3/4 engine self-test, 4/4 YAML structural checks. Exit 0 = ALL LAYERS
  PASSED. Run this instead of the individual commands.
- FAOS design memo: `~/.hermes/hermes-agent/docs/Real_World_Relational_Procedural_Operating_System_Design_Memo.txt`
- Upstream skeleton: github.com/tonbistudio/hermes-multi-agent-workflow

## Extension blocks for triage.yaml

| Block | Purpose | FAOS § |
|---|---|---|
| `perception:` | Field-perception window; required outputs before task reduction | §6.1 |
| `field_model:` | Entity types, relation types, stakes with planetary governors | §5.1 |
| `evidence_ladder:` | 5-level epistemic provenance (impression→lead→fact→claim→judgment), non_skip | §10.1 |
| `route.map` entries as dicts | Primary path + monitored shadow + promotion conditions | §6.4, §7 |
| `task_frame:` per path | Success condition, non-goals, boundaries, required evidence | §6.2 |
| `close:` | 6 required passes: victory, defect, dissent, proxy, boundary, transfer | §6.8 |
| `learning_loop:` | Digest-before-calibration, pattern thresholds | §6.9-6.10 |
| `state_lineage:` | Valens-derived S0-S9 item lifecycle; prohibited edges, halt states (S6/S7/S8), fail_closed | Book IX |
| `quarantine_tiers:` | Valens-derived Q0-Q10 claim-level register; deny_by_default, only Q0-Q2 operational | Book VIII/IX |
| `typed_metrics:` | Valens-derived VALUE+UNIT+SCALE+SOURCE on every metric; ordinal ≠ completed; row-closure | Book VII |
| `route.authority_weights:` | Victor-method weights (5/4/3/2/1) on classifications; primary by weight, shadow preserved as non-winning witness | §I.18 |
| `absence_register:` | Book X — 'absence is a state, not an invitation.' Known-missing data GATES work (ABSENCE-BLOCKED halt), never invented. Classes: never-recorded / confirmed-absent / pending-verification; fail_closed | Book X 2P-5P |
| `non_operational_registry:` | Book VII — barred analogies ('temporal echo'): context-only, never evidence. Enforces the persona's premature-symbolic-coherence guardrail | Book VII |
| `astra:` | Persona circuit map (metadata for orchestrator skill) | — |

Valens blocks are OPTIONAL: the engine extension enforces them only when
present, so a minimal config still loads. When present, quarantine_tiers
must nest tiers under a `tiers:` subkey (`quarantine_tiers.tiers.Q0`), not
flat at the block root — the loader reads the nested shape.

## Engine compatibility rule (CRITICAL)

The stock hermes-multi-agent-workflow `Route` dataclass is `dict[str, str]`.
The shadow-route extension makes map values dicts — **this breaks the stock
engine**:

- `validate()` iterates route targets → `TypeError: unhashable type: 'dict'`
- `route_from_classification()` returns the dict as a path name → ConfigError

Rule: any schema extension must ship with its engine patch (e.g.
`route_with_shadow()`, `close_specs()`, `evidence_promotion_check()`), or be
explicitly flagged as spec-without-implementation. A config that validates
structurally may still be unrunnable on the stock engine — always check the
dataclass types before claiming compatibility.

## Audit discipline (verification pattern)

Before claiming an integration works, verify structurally:

1. Route targets resolve to defined paths (primary AND shadow).
2. Every role used in any stage/lane is defined in `roles:`.
3. No orphan roles (defined but never used) and no undeclared source profiles.
4. Evidence ladder has the 5 canonical levels in order, `non_skip: true`.
5. Every path's close block has all 6 passes.
6. The `astra:`/`field_model:` blocks are complete and internally consistent.
7. Check for `schema_version` — add one if missing.

Run via `scripts/verify_faos_config.py [path]` (exit 0 = pass) or a quick
python yaml.safe_load script (see references/faos-integration-audit.md for
the worked example from 2026-07-30).

## Council-brainstorm pattern (hunting hidden gaps)

When asked to find applications/use cases NOT already covered (or brainstorm
novel angles on a corpus), don't brainstorm alone in-context — convene a
council:

1. **Pick 3 disciplinary lenses** that slice the material orthogonally
   (e.g. systems/control engineer, epistemologist/archivist, behavioral
   architect). Each lens sees different gaps.
2. **Brief each subagent with the ALREADY-COVERED list** — explicit,
   itemized ("do NOT re-suggest these"). This is what forces them into the
   crevices instead of re-deriving what the parent already built.
3. **Ground them in the distilled wiki first** — point each at the
   synthesis/concept pages, not the raw corpus. Cheap grounding, high
   fidelity.
4. **Demand an output format** with mandatory fields: Valens source anchor,
   concrete application, implementation sketch, **explicit novelty
   justification vs the covered list**, difficulty. The novelty field is
   what prevents overlap.
5. **Synthesize yourself afterward** — dedupe across lenses, rank, and
   check against YOUR OWN pre-council candidates (independent thought
   catches what all three lenses missed; in 2026-07-30 the council missed
   the non-operational-registry crevice that independent reading found).
6. **Watch for cross-lens convergence** — when 2+ lenses independently
   derive the same law from different sources, that law is load-bearing,
   not coincidence.

Result: 24 novel use cases from a 3-lens council, 6 true crevices
identified, 0 re-suggestions of covered items. See
`references/valens-council-crevices.md` for the worked example (the six
crevices + how they were implemented).

## Pitfalls

- **Four separate planetary-mapping tables** (stakes.governed_by,
  rubric.planetary_governor, astra.circuit_map, skill role table) with no
  single source of truth — they drift silently; note which one is canonical.
- **`astra:` is metadata only** — "not consumed by the engine." Persona
  governance is decorative unless the orchestrator skill is wired to read it.
- **perception contract mismatch** — `perception.required_outputs` lists 10
  fields but stock `intake_parser.py` parses only title/claim/sources/why.
  Both sides must be extended together.
- **Scout skills must exist** — sources: reference skill names (e.g.
  triage-scout-bridge) that must be installed on the scout profile; the
  template ships only one generic scout.
- **Locus/validator role (RESOLVED in schema 2.0)** — FAOS §11.5's epistemic
  gatekeeper was absent from stock pipelines; validation fell on the
  orchestrator, violating fat-engine/thin-skill. Fixed by: `roles: locus`,
  a `locus_review` final stage in every path's fulfill chain, and
  `engine.locus_review_spec()` (7 checks → ADMISSIBLE/REVISE/BLOCKED).
  Locus the agent applies judgment where the engine has no rule.
- **PDF references** — HOMES plan is a PDF; read_file won't extract it, use
  `pdftotext -layout` via terminal.
