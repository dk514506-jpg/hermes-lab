# Evaluation Rubric — Motivational Ecology Agent Architecture

Project: Motivational Ecology Agent Architecture
Phase: 8 of 8 — Evaluation and Calibration
Date: 2026-08-06
Status: MASTER RUBRIC — operationalizes the 10 plan criteria (Phase8_Plan.md §Requirements)
against the actual artifacts. Valens-style: every criterion is answered from a named
artifact, scored on a 0/1/2 ladder, and guarded by the verifier that enforces it (where one
exists). Findings from any evaluation run feed Calibration_Log.md.

Sibling instruments (applied forms of this rubric, built by the Phase 8 Council):
- Skill_Package_QA_Checklist.md — per-package application of criteria 1-5 (+ state-schema coherence)
- Motivational_Lattice_QA_Checklist.md — lattice-layer application of criteria 6, 7, 10
- Practice_Dojo_QA_Checklist.md — dojo-layer application of criteria 8, 9 (+ executor)

---

## 1. Evaluation Protocol

### 1.1 Council build
Phase 8 runs as a 3-member Council with disjoint outputs (Phase8_Plan.md §Council Split):
- **A:** this rubric (master) + Calibration_Log.md
- **B:** Skill_Package_QA_Checklist.md + Motivational_Lattice_QA_Checklist.md
- **C:** Practice_Dojo_QA_Checklist.md + harness-integration notes

Each member APPLIES its checklist against the real files (Phase3_Skills/, Phase5_Safeguards/,
Phase6_Dojo/, Hermes_Agent_Harness/) — never generic templates.

### 1.2 Outside-judge round (post-build, standing instruction)
After the Council builds, a cross-provider outside-judge round reviews the evaluation
artifacts themselves: do the criteria discriminate quality? Are the checklists answerable
from the artifacts? Independent voice on the evaluation design, per Phase8_Plan.md
§Revision Plan. Invocation (keys verified in Phase 2):
- Claude: `hermes chat -q "<critique brief>" -m claude-sonnet-4-5 --provider anthropic`
- Second API: the campaign build model `deepseek/deepseek-v4-flash-0731` (nous provider),
  or another provider API — run as a second independent voice.
Judge critiques are saved to `council_notes/judge_<model>_phase8.txt`, integrated per the
sublative method (preserve kernel, negate weak, raise), then the tree is re-verified.

### 1.3 Score aggregation
- Each criterion below is scored **per artifact** (the artifact(s) named in "Where the
  evidence lives") on the 0/1/2 ladder by: (a) the owning Council member, (b) each outside
  judge. Scores are independent, then compared.
- **Per-criterion score** = median of all scores for that criterion (Council + judges),
  rounded to the nearest integer (0/1/2). Disagreement of ≥1 point between Council and a
  judge forces a written reconciliation note into Calibration_Log.md (finding → fix → guard).
- **Overall score** = mean across the 10 criteria. Bands:
  - **PASS (≥ 1.8):** deployable/uploadable as-is; findings recorded, no blocker.
  - **WARN (1.2 – 1.79):** usable but carries open items; remediation tracked in
    Calibration_Log.md standing items; not claimed "complete" until closed.
  - **FAIL (< 1.2):** not uploadable/claimable; must remediate before the next round.
- A criterion scored 0 on any artifact it governs blocks that artifact's PASS (per-artifact
  floor, matching verify_phase7.py's exit-0 gate philosophy).

### 1.4 Findings feed Calibration_Log
Every evaluation run appends rows to Calibration_Log.md: phase=8, finding (artifact-referenced),
fix, verifier guard (or "no automated guard — review-round enforced"). Standing items Q6-Q11
carry forward there. The loop closes with `verify_all.py` green + continuity updated in
handoff_notes.md.

### 1.5 Artifact map (evidence index)
| Layer | Evidence lives in |
|---|---|
| Phase 1 theory | Foundation_Matrix.md, Construct_Map.md, Theory_to_Routine_Interface.md (Foundation/) |
| Phase 2 evidence | Foundation/Recent_Evidence_Digest.md, Annotated_Bibliography.md, Contrary_Findings_and_Limits.md; council_notes/phase2_api_seed.md (packaged copies at harness evidence/) |
| Phase 3 skills | Phase3_Skills/ (8 packages × 9 core files) + harness skills/ |
| Phase 4 graph/lattice | Phase3_Skills/skill_graph_index.json, lattice_index.json, skill_lattice_interface.md, insight_trigger_policy.md, T2R_traceability.json + harness lattices/ |
| Phase 5 safeguards | Phase5_Safeguards/ (5 docs) + harness governance/ |
| Phase 6 dojos | Phase6_Dojo/ (5 dojos × 7 artifacts) + harness routines/ |
| Phase 7 harness | Hermes_Agent_Harness/ (README, governance/, verify/verify_harness.py, DEFERRED_PACKAGES.md) |
| Verifiers | council_notes/verify_phase3..8.py, verify_critique_revisions.py, verify_packages.py, _verify_skills.py, verify_all.py (FULL GATE — chains all 9) |
| Runtime contract | harness logs/log_schema.md (ships empty) |

### 1.6 GAP Sampling Protocol (post-judge revision, Claude 5.2)

The three checklists mark 47+ GAP/PARTIAL checks with no automated guard. When a
review round must exercise them, sample by tier:
- **Tier 1 — mandatory (all):** GAPs guarding safety invariants — sycophancy
  guard content, no-surveillance prose, spirit-gate / de-escalation prose,
  hypothesis-status wording, user-rejection-absolute. (~10-12 checks.)
- **Tier 2 — random 20%:** evidence-citation presence (≥1 VERIFIED source per
  package), state-schema↔SKILL.md name parity, completion-conditions presence.
  (~2 packages + 1 dojo.)
- **Tier 3 — conditional:** trigger T1-T6 policy↔index parity, lattice-skill-
  edges↔MLG-edge-map parity — only if a judge/Council member raises a lattice
  coherence concern (one-time checks already recorded in Calibration_Log rows
  10/14).

### 1.7 Disagreement Budget (post-judge revision, Claude 5.3 + DeepSeek)

- **Expected:** 2-4 of 10 criteria showing ≥1-point Council↔judge disagreement
  is normal for a rigorous round. 0-1 suggests judges aren't independent; ≥6
  means the rubric is ambiguous or the artifacts inconsistent — pause and
  revise the rubric before continuing.
- **Reconciliation:** one written note per disagreeing criterion (Council +
  all dissenting judges' findings combined), not one per judge pair, into
  Calibration_Log.md.
- **1.5 rounding:** median exactly 1.5 resolves toward the Council owner's
  score, else the lower score (DeepSeek rec 2).
- **Judge-vs-judge full-point splits** also force a reconciliation note (they
  indicate rater disagreement the median may hide).
- **Score citations:** every 0/1/2 score must carry a one-line artifact
  citation (mirroring review_rubric.md's per-dimension format), and the rater
  × criterion matrix is published (in Calibration_Log or a Phase8_Scorecard)
  so the median is auditable, not asserted (DeepSeek rec 2).

### 1.8 Runtime-Deferral Scope (post-judge revision, DeepSeek rec 5)

Static-file evaluation cannot verify: log conformance in live sessions,
skill_load_snapshot recording, verdict→quarantine execution, boundary-gate
runtime blocking, actual T1-T6 firing. Criteria touching these (C3 runtime
claim, C5, C7 chain) are capped at 1 by design. Re-evaluation trigger: after
the first N=5 logged dojo sessions or the first real deployment cycle, run
this rubric again on the live logs. Wired to Q8/Q11 in Calibration_Log.

### 1.9 Deployment and Iteration Protocol (post-judge revision, Claude 5.5)

- **PASS (≥1.8, no 0-scoring artifact):** harness uploadable to the
  OneDrive/SharePoint path (Q8) and installable by a fresh Hermes instance per
  the README; open items (Q6, Q7, Q10, Q11) tracked as standing calibrations,
  not blockers; campaign closes at Phase 8.
- **WARN (1.2-1.79):** usable but not claimable as complete; remediation plan
  required (fix 0-scoring artifacts, raise ≥2 partial criteria to full);
  Phase 9 = remediation round re-evaluated per this rubric.
- **FAIL (<1.2 or 0-scoring artifact persists after one revision):** pause;
  root-cause (rubric ambiguity, artifact incompleteness, scope creep); revise
  or document lessons learned.
- **Acceptance test (usability):** Dallas installs the harness in a fresh
  Hermes profile and runs one dojo session; confirms (a) the session runs per
  the artifacts, (b) logs conform to log_schema.md, (c) governance rules
  (boundary gate, fade policy) are observable in the session flow.

---

## 2. The Ten Criteria

Scoring ladder (applies to every criterion unless the criterion's ladder refines it):
- **0 — ABSENT or CONTRADICTED:** no artifact answers the criterion, or artifacts contradict it.
- **1 — PARTIAL:** present as declaration/prose or in a single artifact; not structural,
  not cross-artifact consistent, and/or not verifier-guarded.
- **2 — FULL:** structural (encoded in data/ops/schema, not prose), cross-artifact
  consistent, and enforced by a named verifier (where one exists).

### C1. AtomicOp decomposition
**What to look for:** every package's `atomic_ops.json` lists named, single-responsibility
AtomicOps with inputs/outputs/guardrails; ops trace to register ops in
`lattices/T2R_traceability.json` (48 entries: 39 instantiated, 9 UNINSTANTIATED marked);
decomposition edges are direction-consistent (index `decomposes_to COMB→TDF` VERIFIED Cane
2012, mirrored in COMB's edge_map, no reverse `supports TDF→COMB`). Reference counts: COMB 14,
TDF 10, PPS 9, MI 14, MLG 12, ConvoDojo 13, HEB 11.
**Where the evidence lives:** Phase3_Skills/<pkg>/atomic_ops.json + skill_node.json +
edge_map.json; Hermes_Agent_Harness/skills/; lattices/T2R_traceability.json.
**Verifier guard:** verify_phase3.py (file presence, JSON validity, "Atomic Operations"
section in every SKILL.md, edge-type whitelist); verify_critique_revisions.py (ConvoDojo: 13
ops, every op inputs/outputs/guardrails, check_psychological_safety reads sycophancy_risk;
MI: agree_direction/prioritize with guardrails); verify_phase7.py (atomic_ops.json among the
9 core files of all 8 packages). Union op-schema coverage (critique_1 finding: HEB/MLG/
ConvoDojo ops originally carried no guardrails) is asserted only for the fixed packages —
audit the rest per the QA checklist.
**Ladder:** 0 = no atomic_ops.json, or ops non-executable. 1 = ops exist but some lack
inputs/outputs/guardrails, or T2R traceability incomplete, or decomposition edges
inconsistent between index and package maps. 2 = all ops fully specified and guardrailed,
T2R-traced, decomposition direction-consistent, verifier-guarded.

### C2. Trigger and completion conditions
**What to look for:** a "Trigger Conditions" section in every SKILL.md naming when the skill
fires (HEB: 14 triggers incl. high-meaning tasks, skill-atrophy risk; lattice: insight
triggers T1-T6 with confirmation gates in insight_trigger_policy.md); every dojo stage
carries entry_conditions / exit_conditions / coach_rules_ref; completion = explicit exit
criteria, not exhaustion (PPS readiness_gate, MI plan_when_ready, ConvoDojo debrief_session →
run_transfer_scenario only after sustained proficiency).
**Where the evidence lives:** Phase3_Skills/<pkg>/SKILL.md; harness
routines/*/dialogue_state_machine.json; lattices/insight_trigger_policy.md.
**Verifier guard:** verify_phase3.py (all 16 SKILL.md sections incl. "Trigger Conditions"
required in all 8 packages); verify_phase6.py (every stage in every dojo carries
entry/exit conditions + coach_rules_ref). Presence is asserted; the QUALITY of the
conditions (are they executable?) is the checklist's job — content is not machine-checked.
**Ladder:** 0 = no trigger or completion conditions anywhere. 1 = triggers named in prose but
no executable exit criteria, or conditions missing for some ops/stages. 2 = every op/stage
has named trigger + completion conditions coherent with its state schema, presence
verifier-guarded.

### C3. User empowerment preservation
**What to look for:** an Empowerment Boundary section in every SKILL.md declaring what the
agent may do automatically vs. what it must preserve for the user (COMB: "agent must not
answer questions the user can answer", final endorsement/correction/rejection reserved; HEB:
five modes ACT/SCAFFOLD/ASK/DEFER/STOP with preserved_user_decision output and recovery ops
Undo_Interpretive_Closure / Reopen_User_Choice); `governance.boundary_gate: required` on all
8 skill_node.json; debrief templates carry a "Preserved User Decision" section; persona
boundary_rules encode no-coercion/no-shaming/no-lattice-reference.
**Where the evidence lives:** Phase3_Skills/<pkg>/SKILL.md + skill_node.json; harness
governance/empowerment_boundary.md + agent_deference_rules.md (Phase5_Safeguards/ originals);
routines/*/debrief_template.md + persona_config.yaml; skill_graph_index.json governance block.
**Verifier guard:** verify_phase4.py (boundary_gate == required on all 8 nodes; index
governance block); verify_phase6.py (debrief "Preserved User Decision" section; persona
boundary keywords coerc/sham/lattice); verify_phase7.py (index governance.boundary_gate_rule
present). Q11 carries the open tail: runtime EXECUTION of the gate is declaration + policy
only (no wrapper) — that caps this criterion at 1 for runtime claims until wired.
**Ladder:** 0 = no empowerment boundary anywhere. 1 = boundary in prose only — nodes lack
boundary_gate, no preserved-user-decision output, no debrief section, or gate not enforced
at runtime. 2 = boundary structural (gate required on all nodes, preservation outputs +
debrief recording + log boundary_gate_outcome event), verifier-guarded.

### C4. Skill-atrophy reduction
**What to look for:** measurable atrophy machinery, not slogans: PPS ops compute_skill_load
(0..1), detect_atrophy_risk (baseline-vs-recent arrays), separate_performance_capability,
fade_scaffolds ("fade is mandatory"), readiness_gate; HEB skill_load_trend derived from
skill_load_score; learnability_state_schema.json (ecology-learnability/0.1) with
skill_load_score/trend, baseline/recent performance tracks, assistance_fraction,
atrophy_risk, empowerment_ratio; skill_atrophy_risk_check.md pipeline (Budzyń ADR 28.4→22.4
anchor, no-single-point-action rule); scaffolding_fade_rules.md 5→0 rung ladder.
**Where the evidence lives:** Phase3_Skills/Proximal_Practice_Selector + Human_Empowerment_Boundary
(state_schema, atomic_ops); Phase5_Safeguards/ + harness governance/ (learnability schema,
atrophy check, fade rules); logs/log_schema.md skill_load_snapshot event.
**Verifier guard:** verify_phase5.py (schema is valid draft-07 via meta-schema check; a
realistic estate instance conforms; negative tests reject invalid enums/ranges and enforce
required telemetry_policy.rationale; no dangling $refs; skill_atrophy_risk_check.md carries
the required operational sections); verify_phase3.py ("Learnability / Skill-Atrophy Check"
section in every SKILL.md).
**Ladder:** 0 = no atrophy machinery (no schema, no ops). 1 = atrophy discussed but
unmeasured (no validated schema, no skill-load state, fade rules absent or unreferenced).
2 = measurable state + validated schema + fade policy wired to dojo layer
(scaffolding_fade_rules.md §3.5), verifier-guarded.

### C5. Future unassisted capability
**What to look for:** first-class tracking of what the user does without the agent:
unassisted_competence_track, unassisted_completion_rate, assistance_fraction,
empowerment_ratio in the learnability schema; PPS record_unassisted_competence op;
separate_performance_capability (performance ≠ capability); HEB capability_preservation_plan
output; fade conditions tied to unassisted evidence; the campaign's own self-application
record (Q10 — per-phase unassisted user task; this Phase 8 review is itself an instance).
**Where the evidence lives:** Phase5_Safeguards/learnability_state_schema.json;
Phase3_Skills/Proximal_Practice_Selector/atomic_ops.json; HEB SKILL.md outputs;
handoff_notes.md (Q10); 03_Open_Questions_Register.txt.
**Verifier guard:** NO dedicated guard. Nearest: verify_phase5.py (its instance test
exercises unassisted_competence_track / unassisted_completion_rate /
empowerment_ratio fields); verify_critique_revisions.py (HEB skill_load_trend documented as
derived from skill_load_score — the producer→consumer wiring). Whether the runtime log
(skill_load_snapshot) actually records unassisted completions is unchecked — checklist +
judge question. Cap at 1 until a runtime record exists.
**Ladder:** 0 = no capability track; over-assistance risk unaddressed. 1 = capability
concepts present but unmeasured/unrecorded at runtime (no schema field, no log event, no
fade-to-unassisted rule). 2 = unassisted competence tracked as first-class state + logged
(skill_load_snapshot) + fade policy consumes it.

### C6. Evidence citation for motivational insights
**What to look for:** every motivational claim carries a VERIFIED / RECONSTRUCTED /
UNVERIFIED flag; lattice insights cite supporting observations via evidence_edges
(evidence_edge_schema.json); bibliography entry schema has Status as first field; digest↔bib
numeric fidelity (critique_0 traced ~60 cross-references — all matched); opinion/preprint
caveats enforced (Jose 2025 opinion; CALM-IT Nguyen 2026 preprint; Beacock preprint n=51);
integrity register (Wang & Fan 2025 RETRACTED, SRSUPM 2026 WITHDRAWN — register-only, never
cited as evidence); thresholds labeled calibration anchors, not doctrine.
**Where the evidence lives:** lattices/evidence_edge_schema.json + lattice_index.json
(insight_triggers carry flags); evidence/Annotated_Bibliography.md (78 entries) +
Recent_Evidence_Digest.md; dojo rubric.json grounding blocks; skills SKILL.md grounding
lines; Phase5_Safeguards/ + harness governance/ evidence registers.
**Verifier guard:** verify_phase5.py truthfulness guards (Jose 2025 cited with
opinion+commentary caveat and never bare-VERIFIED; every CALM-IT/Nguyen 2026 line in
scaffolding_fade_rules.md carries "preprint"); verify_phase6.py (every dojo artifact carries
VERIFIED AND RECONSTRUCTED flags at DATA level — comments don't count); verify_phase4.py
(lattice index triggers ≥ 5 with evidence anchors); verify_phase7.py (evidence/ 4 files
present). Flag PRESENCE is machine-checked; per-citation correctness is a human/judge
sampling task (as critique_0 did).
**Ladder:** 0 = insights uncited or flags absent. 1 = flags present but drift (opinion cited
as VERIFIED, preprint unflagged, register-only source cited as evidence) or flags live only
in prose/comments. 2 = structural flags + caveat discipline + integrity register +
verifier-guarded for the known caveat classes.

### C7. User correction of insights
**What to look for:** a user-verdict path in data, not prose: MLG record_user_verdict op
with user_verdict state (pending/confirmed/rejected/revised) in lattice_index.json;
quarantine_insight op — an insight the user rejects is removed from active use regardless of
evidence strength (Valens quarantine law transposed); COMB record_diagnosis(user_corrections)
array; MI change_talk_log user-correction field; present_lattice_for_review before any use;
logs/log_schema.md append-only with correction-by-new-entry + outcome_arbitration field;
debrief records preserved decisions.
**Where the evidence lives:** Phase3_Skills/Motivational_Lattice_Generator/ (atomic_ops,
state_schema, insight_validation_protocol.md); lattice_index.json state variables; COMB +
MI atomic_ops; logs/log_schema.md; routines/*/debrief_template.md.
**Verifier guard:** NO dedicated guard asserts the verdict path. Nearest: verify_phase4.py
(quarantine tiers incl. Q2_IDENTITY_LEVEL present; triggers ≥ 5); verify_phase6.py (debrief
"Preserved User Decision" section). Op presence is verifier-visible (atomic_ops.json parses)
but the verdict→quarantine→log chain is not asserted — checklist + judge question. Cap at 1
until asserted.
**Ladder:** 0 = no user-verdict mechanism (insights treated as facts). 1 = correction
possible in prose but not structural (no verdict state, no quarantine op, corrections not
logged). 2 = verdict recorded as state + quarantine enforced + corrections appended to logs
+ debrief carries preserved decisions.

### C8. Calibrated practice
**What to look for:** practice intensity is a designed, agreed parameter: sparring intensity
profiles with levels 1-5, escalation + de-escalation policies, and user_agreement REQUIRED
(intensity never assumed); rubrics are lens-type scoring with every score anchored to ≥1
utterance quote (rubric.json scoring.anchoring); hint-not-answer scaffolding invariant in
every in_session_coaching_rules.md (Bastani 2025); transfer sets per dojo (≥ 3 base + ≥ 2
transfer scenarios); run_transfer_scenario gated on sustained proficiency; stage families
with entry/exit conditions per dojo (Ambivalence 6 stages, Conflict 6, Workplace 9).
**Where the evidence lives:** Phase6_Dojo/<Dojo>/ (7 artifacts each) + harness routines/;
ConvoDojo executor ops (set_intensity_profile, apply_rubric_lens, calibrate_pushback,
debrief_session, run_transfer_scenario).
**Verifier guard:** verify_phase6.py (all dojos: intensity levels exactly [1..5] with
escalation/deescalation/sycophancy_guard; rubric count ≥ 2, all lens-type, use-rules present;
hint-not-answer + persona/coach module separation; debrief section; transfer counts; owned
dojos additionally: exact stage families, hard gates, intensity user_agreement required,
mirror_monitor for Workplace); verify_phase7.py (5 dojos × exactly 7 artifacts).
**Ladder:** 0 = no calibration machinery (no intensity profile, no rubric, no transfer). 1 =
some calibration but not per-dojo structural (intensity without user agreement, rubric
unanchored, no transfer sets, gates missing). 2 = full calibrated-practice stack per dojo,
verifier-guarded.

### C9. Sycophancy avoidance in sparring
**What to look for:** anti-sycophancy as an orchestration invariant, not a style choice:
sycophancy_guard field in every sparring_intensity_profile.json; persona/coach separation
(the persona generates turns and NEVER evaluates; the coach controls staging/intensity/
feedback and never answers for the user); check_psychological_safety op reading
sycophancy_risk state; calibrate_pushback as a designed parameter (1-5), not free-form
personality; persona never scripted from lattice insights (persona_config.yaml boundary_rules);
mirror_monitor in the Workplace dojo's guard; run_adversarial_stress_test before deployment.
**Where the evidence lives:** Phase6_Dojo/*/sparring_intensity_profile.json +
persona_config.yaml + in_session_coaching_rules.md; ConvoDojo SKILL.md + atomic_ops
(configure_persona, coach_interrupt, calibrate_pushback, check_psychological_safety,
run_adversarial_stress_test); harness routines/ copies.
**Verifier guard:** verify_phase6.py (sycophancy_guard present in every intensity profile;
mirror_monitor for Workplace; persona boundary keywords coerc/sham/lattice; module
separation declared); verify_critique_revisions.py (check_psychological_safety present and
reads sycophancy_risk as input).
**Ladder:** 0 = no sycophancy guard (persona may flatter, coach may praise). 1 = guard
mentioned in prose but not structural (no sycophancy_guard field, no safety op, separation
not declared). 2 = structural: guard field + safety op reading risk state + persona/coach
separation + verifier-guarded.

### C10. Evidence / interpretation / implication / selection distinction
**What to look for:** the four epistemic layers are separated in DATA and OPS, not just
named: lattice layers are exactly observation → interpretation → evidence_edge
(lattice_index.json lattice_layers); MLG ops separate_inference_layers,
form_interpretation_hypothesis (hypothesis, never fact), derive_implication_and_action
(implication/action derived only from evidence-backed insights), present_lattice_for_review
(selection requires user review); TDF separate_evidence_interpretation op; COMB profile is
"hypothesis — user-correctable, never a verdict"; descriptive-vs-predictive distinction
named (Foundation_Matrix Obs 3, Construct_Map Tension 5, Contrary D1); log envelope carries
evidence_flag (VERIFIED machine record vs RECONSTRUCTED interpretation); insight_trigger_policy
T1-T6 confirmation gates separate detection (evidence) from action (selection).
**Where the evidence lives:** lattice_index.json (lattice_layers, quarantine tiers);
MLG atomic_ops + schemas (observation/insight/evidence_edge); TDF atomic_ops;
COMB SKILL.md; logs/log_schema.md common envelope; lattices/insight_trigger_policy.md;
evidence/Contrary_Findings_and_Limits.md D1/D5.
**Verifier guard:** verify_phase4.py (lattice layers set exactly
{observation, interpretation, evidence_edge}; Q2 quarantine tier; triggers ≥ 5);
verify_phase6.py (data-level VERIFIED/RECONSTRUCTED flags). The implication/selection
separation (derive_implication_and_action gated on review) is structural-presence only —
not asserted; checklist + judge question.
**Ladder:** 0 = layers conflated (interpretation presented as evidence; action derived
without review). 1 = layers named but not separated in ops (no separate_inference_layers,
implications derived without present-for-review, flags only in prose). 2 = structural
separation in ops + schemas + log envelope + verifier-guarded layers.

---

## 3. Verdict assembly

Score each criterion per artifact per §1.3. Record every finding — including WARN-level
partials — in Calibration_Log.md with a proposed fix and the verifier guard that will hold
it. A FAIL overall (or any 0-scoring artifact) blocks upload/claim of the harness until the
next revision round. The evaluation artifacts themselves then go through the outside-judge
round (§1.2) before the campaign is declared complete.

Verifier chain (run at every gate): `council_notes/verify_all.py` → verify_phase3.py,
verify_phase4.py, verify_phase5.py, verify_phase6.py, verify_phase7.py,
verify_critique_revisions.py, verify_packages.py, _verify_skills.py + shipped
`Hermes_Agent_Harness/verify/verify_harness.py`. All must exit 0.
