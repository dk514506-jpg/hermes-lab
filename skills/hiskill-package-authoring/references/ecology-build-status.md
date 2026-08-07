# Ecology Build Status — Phase3_Skills (as of 2026-08-06)

## Packages in the tree
| Package | Layer | Role | Files | Ops | Edges | Status |
|---|---|---|---|---|---|---|
| Human_Empowerment_Boundary | 3 | governance | 14 | 11 | 34 | built 2026-08-06 (v2.0, evidence-grounded: Beacock 2026, Bastani 2025, Xu 2026) |
| Motivational_Lattice_Generator | 1 | understanding | 15 | 12 | 29 | built 2026-08-06 (Lim 2025, SERUM 2026, LongNAP) |
| ConvoDojo_Practice_Sparring | 5 | practice | 16 | 12 | 27 | built 2026-08-06 (EasyMED, AgentForge, Ma 2025) |
| COMB_Behavioral_Diagnosis | 1 | diagnosis | ? | 14 | 28 | referenced in skill examples (prior session) — NOT present in Phase3_Skills at 2026-08-06 build; LOCATE before extending |
| TDF_Barrier_Facilitator_Grid | 1 | diagnosis | ? | 10 | 24 | same as COMB — locate |
| SDT_Need_Support_Check | 3 | motivation | — | — | — | pending first build |
| MI_Ambivalence_Conversation | 5 | conversation | — | — | — | pending first build |
| Proximal_Practice_Selector | 4 | learnability | — | — | — | pending first build |
| Material_Arrangement_Scan | — | — | — | — | — | deferred (practice theory) |
| Feedback_Ecology_Map | — | — | — | — | — | deferred (NPT) |
| Autopoietic_Boundary_Check | — | — | — | — | — | deferred (cybernetics; philosophy kept as philosophy) |

Seed `skill_graph_index.json` still marks all 8 first-build skills "in_build" —
it lags the tree (ground-truth-first rule: list the directory, don't trust status).

## Layer extras added per plan §6 (in addition to the 9 core files)
- Layer 1 (lattice): observation_schema.json, insight_node_schema.json,
  evidence_edge_schema.json, motivation_lattice.md, insight_validation_protocol.md,
  paternalism_and_overinterpretation_guardrails.md
- Layer 3 (empowerment): empowerment_boundary.md, human_decision_point_detector.json,
  agent_deference_rules.md, obviousness_threshold_protocol.md,
  option_space_preservation_check.md
- Layer 5 (dojo): dialogue_state_machine.json, persona_config.yaml, rubric.json,
  sparring_intensity_profile.json, in_session_coaching_rules.md,
  debrief_template.md, transfer_scenario_set.md

## Seed edges vs built edge_maps (agreement status)
| Seed edge | Status |
|---|---|
| supports Human_Empowerment_Boundary → * | AGREES (HEB edge_map) |
| compatible_with COMB → Motivational_Lattice_Generator | AGREES (MLG edge_map, self-sourced) |
| recovers_with ConvoDojo_Practice_Sparring → Human_Empowerment_Boundary | AGREES (Dojo edge_map, seed direction) |
| decomposes_to COMB → TDF; supports SDT → MI; can_follow MI → COMB; can_follow TDF → Proximal; recovers_with MI → SDT | pending those packages (both endpoints unbuilt) |

Direction note: seed writes recovers_with from=recovered-skill to=provider; the
canonical example writes source=op target=skill. Cross-skill edges mirror the
seed; in-package recovery edges use the canonical op→skill form.

## Open items for Phase 4
- Locate the prior session's COMB/TDF packages (or rebuild per this pattern).
- Reconcile SKILL.md heading level across packages (`##` per plan §8 vs `###`
  per canonical bundle) — verifiers accept both.
- Update seed index statuses from "in_build" and fold in built edge counts.
- Verify `verify_packages.py` (project tree) vs `scripts/verify_package.py`
  (this skill) stay in agreement; the project one adds YAML/endpoint/seed checks.
