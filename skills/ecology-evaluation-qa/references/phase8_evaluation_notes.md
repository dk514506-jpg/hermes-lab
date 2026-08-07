# Phase 8 Evaluation Notes (session detail, 2026-08-06)

Condensed from the Phase-8 evaluation run. All check numbers below were read from
verifier SOURCES on 2026-08-06 — re-read before citing in later phases.

## Deliverables produced
- `docs/Ecology/Foundation/Phase8_Evaluation/Skill_Package_QA_Checklist.md`
- `docs/Ecology/Foundation/Phase8_Evaluation/Motivational_Lattice_QA_Checklist.md`
- Sibling-owned: `Evaluation_Rubric.md`, `Practice_Dojo_QA_Checklist.md`,
  `Calibration_Log.md` (council split A/B/C per Phase8_Plan.md).

## Verifier coverage map (exact check numbers)
**verify_packages.py** (`Phase3_Skills/`, all 8 packages):
1 JSON parse · 2 YAML parse (persona_config) · 3 canonical 9-file structure (core9) ·
4 SKILL.md 16-section standard (SECTIONS16 list) · 5 AtomicOps SKILL.md ↔
atomic_ops.json ↔ edge_map.json decomposes_to (ordered 1..N) · 6 edge endpoint
resolution (recovery/support op names, KNOWN_SKILLS, "*") · 7 seed-index agreement
(direction-sensitive for recovers_with/can_follow/decomposes_to/supports; set-equality
for compatible_with).

**verify_phase4.py** (`council_notes/`):
1 Phase-4 outputs exist · 2 all JSON valid · 3 index source/target keys, no from/to ·
4 recovers_with cross-skill kind + exact direction set · 5 node id PascalCase ==
dirname + governance.boundary_gate required · 6 TDF state_schema has
binding_constraint_comb, no bare binding_constraint · 7 skill_load canonical in T2R
canonical_state_variables · 8 quarantined_edges >= 3 + deferred nodes declared ·
9 index governance.boundary_gate_rule · 10 lattice index coherence (layers
observation/interpretation/evidence_edge, Q2_IDENTITY_LEVEL tier, >= 5
insight_triggers, MLG schema refs). Re-runs verify_packages + verify_phase3.

**verify_critique_revisions.py** (`council_notes/`):
1 ConvoDojo 13 ops, every op has inputs/outputs/guardrails,
check_psychological_safety reads sycophancy_risk · 2 HEB skill_load_trend exists and
note references skill_load_score · 3 T2R 48 entries, 39 instantiated + 9
uninstantiated + 0 partial · 4 index COMB→TDF decomposes_to with RECONCILED note,
recovers_with convention resolved (no "DIRECTION CONVENTION PENDING"), kind=cross-skill
· 5 COMB/TDF edge-map direction reconciliation · 6 MI agree_direction + prioritize.

## Per-package op counts (16-section standard; verify_packages check 5 + critique 1/6)
HEB 11 · COMB 14 · TDF 10 · SDT 10 · MI 14 (incl. Phase-4 focusing agree_direction,
prioritize) · PPS 9 · MLG 12 · ConvoDojo 13 (incl. check_psychological_safety).

## Reconciliation notes (tracked in the package checklist)
- **R1 T2R**: 48 register ops → 39 instantiated, 9 UNINSTANTIATED: BCW/BCT
  (canvass_full_range, select_bct, retrocode_delivered_plan), NPT/realist eval
  (assess_coherence, form_cmo_hypothesis), practice theory (scan_materials,
  scan_meanings, detect_shared_elements, design_novelty_into_routine). All map to
  deferred packages (Material_Arrangement_Scan, Feedback_Ecology_Map) quarantined in
  skill_graph_index; BCW/BCT has NO package — open scope decision.
- **R2 skill_load**: canonical skill_load_score (0..1) written by PPS
  `compute_skill_load`; HEB derives skill_load_trend (rising/flat/falling) — the
  conversion op is NOT instantiated (T2R action "UNIFY in Phase 4 — add conversion or
  single variable"; HEB state_schema note "Unification pending Phase 4"). T4 trigger
  depends on it: falling trend triggers, single-point dips don't. Critique check 2
  verifies only the note's existence.
- **R3 TDF drift**: state_schema.json renamed binding_constraint →
  binding_constraint_comb (C/O/M/none); TDF SKILL.md "## State Variables" still says
  binding_constraint. No verifier cross-checks SKILL.md ↔ state_schema (cosmetic now,
  would bite if it were semantic).

## Lattice QA facts
- Tiers: Q0_STRUCTURAL · Q1_PROVISIONAL · Q2_IDENTITY_LEVEL (default quarantine;
  explicit user confirmation before ANY use) · Q3_REJECTED (absolute, removed from
  active use regardless of evidence strength) · Q4_MANIPULATION_RISK ·
  Q5_SURVEILLANCE_RISK.
- Universal trigger prerequisites (insight_trigger_policy.md §1): user_verdict !=
  pending (rejected blocks forever) · quarantine_status active or cleared (Q2 needs
  cleared) · evidence_sufficiency >= partial · HEB boundary_gate passed ·
  manipulation_risk AND surveillance_risk both low.
- Triggers: T1 TDF/COMB (conf >= medium, verdict confirmed, >= 2 observations) ·
  T2 SDT (conf >= low, labeled user-correctable inference) · T3 MI (conf >= low
  engagement / >= medium targeting; evocation-only gate — "you said X last week"
  prohibited) · T4 PPS (objective telemetry over self-report; skill_load trend) ·
  T5 HEB (structural, not confidence-based; Q2 mandatory) · T6 deferred
  (Material_Arrangement_Scan, Feedback_Ecology_Map).
- Schemas (required fields): observation [id ^O[0-9]+$, timestamp, source, content,
  observation_type, consent_scope — opt_in_pending cannot be latticed]; insight_node
  [id ^H[0-9]+$, hypothesis, layer=interpretation const, evidence_sufficiency,
  confidence, identity_level_flag, quarantine_status, user_verdict, evidence_edges];
  evidence_edge [id ^E[0-9]+$, from_insight, to_observation, strength
  direct_quote|consistent|weak|contradictory, provenance, direction
  supports|tensions|contradicts].
- Validation gates (insight_validation_protocol.md): Gate A admission (layers
  separated, citations present, not identity-level unless flagged+quarantined, no
  circularity, worded as hypothesis); Gate B action influence (verdict confirmed/
  revised, sufficiency partial+, convergence emerging/equilibrium, no manipulation
  risk, fresh, boundary respected); Gate C re-validation (goal change, >= 3 new
  contradicting observations, cluster revision, 90-day default, recovery ops).
  Calibration: rejection rate > 30% over rolling 8 insights ⇒ halt generation;
  user-confirmed insight replaces conflicting agent hypothesis; user wording becomes
  primary citation.
- Prediction ceilings (trigger policy §3): Shaikh 2026 17.1–26% next-action (timing
  only, never autonomous action) · Han 2026 52.6% MI auto-coding (human review at
  medium+ stakes) · ProEvent/PROBE 26–40% proactive success (restraint default) ·
  Lim 2025 0.80 LOOCV session quality (strong session-level, weak single-utterance).

## Cross-cutting verifier gaps + proposed closures (R4)
(a) No completion-condition check — 16-section standard lacks "## Completion
Conditions"; completion lives in terminal record_* ops → add verify_packages check 8
(terminal op exists). (b) No evidence-citation check (named sources,
VERIFIED/RECONSTRUCTED flags) → check 10. (c) No SKILL.md State Variables ↔
state_schema.json parity check → check 9. (d) Empowerment/learnability content
unchecked (header-only via check 4). (e) Lattice: lattice_skill_edges ↔ MLG edge_map
set parity, insight_trigger_policy §2 ↔ lattice_index insight_triggers field parity,
insight admission (evidence_edges non-empty), verdict lifecycle simulation (pending
blocks trigger, rejected blocks forever) — all unverified (manual comparison
2026-08-06: consistent).

## House conventions worth reusing
- atomic_ops.json may be a list OR {"ops": [...]} (Phase-4 schema 0.2) — handle both.
- Directed vs undirected edge checking: direction-sensitive for
  recovers_with/can_follow/decomposes_to/supports; set-equality for compatible_with.
- T2R canonical_state_variables + edge_conventions is the anti-drift register —
  consult before asserting state-variable names.
- Lattice status is SEED (index schema + policy); insight instances populate at
  runtime via MLG ops — QA validates schemas/policy, not live data.
