# Practice Dojo QA Checklist

Project: Motivational Ecology Agent Architecture — Phase 8: Evaluation and Calibration
Plan: Phase8_Plan.md, output item 4 of 5
Date: 2026-08-06
Status: APPLIED — per-dojo rows against the real Phase 6 artifacts (source
`Phase6_Dojo/<Dojo>_Dojo/`, packaged home `Hermes_Agent_Harness/routines/`) and the
Phase 7 harness tree. Companion to Evaluation_Rubric.md (master rubric, criteria 1–10).

## Purpose

Verify the five practice dojos (Conversation, Coaching, Ambivalence, Conflict,
Workplace) and their executor (`ConvoDojo_Practice_Sparring`) against the plan
criteria that a *practice layer* must meet: calibrated practice, rubric-as-lens,
sycophancy avoidance, no-surveillance, preserved user decision in debriefs,
proficiency-gated transfer, Phase 5 fade policy, and the two dojo-specific safety
gates (Ambivalence spirit gate, Conflict de-escalation-first). Every check names the
exact file(s) that answer it and the pass condition. Where
`council_notes/verify_phase6.py` (257 checks, exit 0 required, chained into
verify_all.py) already machine-enforces the check, this is stated; where it does not,
the row is flagged **GAP** (or **PARTIAL** where the file exists and the semantics are
present but only presence — not content — is machine-checked).

Evidence discipline: Valens-style. The artifacts carry VERIFIED/RECONSTRUCTED flags
at data level (verify_phase6 check 10); this checklist cites files, not claims.
Pass/fail here is against artifact *content as built*; thresholds are calibration
anchors, not study-validated norms.

## Enforcement Legend

- **ENFORCED** — `verify_phase6.py` machine-checks it for the named dojo(s); exit 0 gates the build.
- **PARTIAL** — file exists and content is present, but the verifier checks presence (key/section/substring), not the semantic content (thresholds, gate prose, anchor strings).
- **GAP** — not checked by `verify_phase6.py` (missing entirely, or owned-dojo-only while a sibling dojo carries a divergent form).

---

## 1. Master Grid (5 dojos × criteria)

| Criterion | Conversation | Coaching | Ambivalence | Conflict | Workplace |
|---|---|---|---|---|---|
| Calibrated practice: intensity 1–5 | PASS (PARTIAL) | PASS (PARTIAL) | PASS | PASS | PASS |
| Calibrated practice: user agreement | **GAP** (key drift) | **GAP** (key drift) | PASS | PASS | PASS |
| Rubric-as-lens + evidence anchoring | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) |
| Sycophancy avoidance (anti-sycophancy guard) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL, +mirror) |
| No-surveillance (logs never feed persona) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) |
| preserved_user_decision in debriefs | PASS | PASS | PASS | PASS | PASS |
| Transfer scenarios proficiency-gated | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) |
| Fade policy (Phase 5) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS (PARTIAL) | PASS |
| Spirit gate (Ambivalence) | n/a | n/a | PASS | n/a | n/a |
| De-escalation-first (Conflict) | n/a | n/a | n/a | PASS | n/a |

PASS = artifact content satisfies the pass condition. PARTIAL/GAP detail per dojo row
below; the two **GAP** cells (Conversation/Coaching user agreement) are the only
machine-enforcement holes in the Phase 6 verifier.

---

## 2. Per-Dojo Rows

Common answering files (cited once, apply to all five dojos):

- Executor: `Hermes_Agent_Harness/skills/ConvoDojo_Practice_Sparring/SKILL.md` (AtomicOps
  `set_intensity_profile`, `apply_rubric_lens`, `calibrate_pushback`,
  `check_psychological_safety`, `run_transfer_scenario`, `debrief_session`; Guardrails;
  Learnability/Atrophy check; Handoff Notes → `logs/`).
- Estate governance: `Hermes_Agent_Harness/governance/empowerment_boundary.md` (§3.2
  preserved set, §4 prohibitions 2/5/7/8), `governance/agent_deference_rules.md`
  (§2.1 deferred-decision records), `governance/scaffolding_fade_rules.md` (§3.5
  ConvoDojo pairing, §7 never-fades).
- Cross-dojo conventions: `Hermes_Agent_Harness/routines/README.md` (§2.1–2.4, §5).
- Dojo-specific paths below are `routines/<Dojo>_Dojo/<artifact>`; source of truth
  identical at `Phase6_Dojo/<Dojo>_Dojo/` (Phase 7 copies verified identical inventory
  by verify_phase7.py).

### 2.1 Conversation_Dojo

| Check | Answering file(s) | Pass condition | Enforcement |
|---|---|---|---|
| Calibrated practice: intensity 1–5 | `sparring_intensity_profile.json` (`levels` 1–5, `escalation_policies` incl. `proficiency_gated` default, `deescalation_rules`) | Levels exactly 1–5; escalation/de-escalation policies present; level 4–5 gated on explicit consent | **ENFORCED** (generic: levels list == 1..5; policy keys present) |
| Calibrated practice: user agreement | `sparring_intensity_profile.json` → key `user_agreement_requirement` (rule: "no escalation above the agreed level without explicit user agreement…") | Intensity set with the user, never assumed | **GAP** — sibling dojos are not covered by the owned-only `user_agreement.required` check, and this dojo's key name (`user_agreement_requirement`) diverges from the §2.1 convention (`user_agreement.required`). Semantics present; schema + verifier drift. |
| Rubric-as-lens | `rubric.json` (lens-type scoring, `rubric_use_rules`), `debrief_template.md` §2, `SKILL.md` `apply_rubric_lens` | All rubrics `scoring.type == "lens"`; use rules present; every score anchors to ≥1 utterance quote | **PARTIAL** — lens type + use-rules presence ENFORCED; the `scoring.anchoring` string ("every score carries ≥1 evidence quote") is not machine-checked |
| Sycophancy avoidance | `sparring_intensity_profile.json` `sycophancy_guard` (`agreement_rate_per_10_turns`, threshold 0.8, orchestration recalibration), `in_session_coaching_rules.md` §8 | Guard present with monitor + alert threshold + recalibration response | **PARTIAL** — `sycophancy_guard` key presence ENFORCED for all five; monitor/threshold content not validated |
| No-surveillance | `persona_config.yaml` `boundary_rules` ("persona never references the user's lattice insights"), `in_session_coaching_rules.md` §10, `SKILL.md` Guardrails ("Do not convert practice logs into surveillance"), `governance/empowerment_boundary.md` §4 prohibition 2, `logs/log_schema.md` (governance: "Logs never feed the persona module") | Persona never scripted from user lattice insights; practice data stays in practice | **PARTIAL** — 'lattice' keyword in every persona's `boundary_rules` ENFORCED (generic); no direct machine check of the no-surveillance prohibition itself |
| preserved_user_decision in debriefs | `debrief_template.md` §6 ("Preserved User Decision (required)"), `governance/agent_deference_rules.md` §2.1, `governance/empowerment_boundary.md` §3.2 | Debrief names what remains with the user; the debrief may not close it; user-verdict section present | **ENFORCED** — substring "Preserved User Decision" checked for all five dojos (generic check 8) |
| Transfer proficiency-gated | `transfer_scenario_set.md` Transfer Rules (proficiency ≥ 2 gate), `sparring_intensity_profile.json` `proficiency_gated` escalation | ≥3 base + ≥2 transfer scenarios; transfer runs only after sustained proficiency at level ≥ 2 | **PARTIAL** — counts ENFORCED (≥3/≥2); the proficiency-gate sentence is prose, not machine-checked |
| Fade policy (Phase 5) | `in_session_coaching_rules.md` §4 ("full model utterances … as scaffolds that fade"), `governance/scaffolding_fade_rules.md` §3.5, `routines/README.md` §2.4, `SKILL.md` Learnability check | Scaffolding descends the ladder 5→0 on unassisted-competence evidence; what never fades (§7) holds | **PARTIAL** — estate fade policy governs all dojos; only Workplace carries an explicit `scaffolding_fade_rules` citation that the verifier checks |

### 2.2 Coaching_Dojo

| Check | Answering file(s) | Pass condition | Enforcement |
|---|---|---|---|
| Calibrated practice: intensity 1–5 | `sparring_intensity_profile.json` (advice-seeking/deflection as the orchestrated pressure; levels 1–5) | Levels exactly 1–5; escalation/de-escalation policies present; consent for 4–5 | **ENFORCED** (generic) |
| Calibrated practice: user agreement | `sparring_intensity_profile.json` → key `user_agreement_requirement` (same rule text as Conversation) | Intensity set with the user, never assumed | **GAP** — same key-name drift and same verifier blind spot as Conversation_Dojo |
| Rubric-as-lens | `rubric.json` (`powerful_questions_v1`, `grow_structure_v1`, `listening_ownership_v1`), `debrief_template.md` §2 | Lens-type scoring; anchoring to quotes | **PARTIAL** (as 2.1) |
| Sycophancy avoidance | `sparring_intensity_profile.json` `sycophancy_guard` (agreement rate 0.8; persona re-presses for advice), `in_session_coaching_rules.md` §8 | Guard present with monitor + threshold + response | **PARTIAL** (as 2.1) |
| No-surveillance | `persona_config.yaml` boundary_rules, `in_session_coaching_rules.md` §10, `SKILL.md` Guardrails | Persona never knows lattice insights; logs stay in practice | **PARTIAL** (as 2.1) |
| preserved_user_decision in debriefs | `debrief_template.md` §6 | Required section present | **ENFORCED** (generic) |
| Transfer proficiency-gated | `transfer_scenario_set.md` Transfer Rules; `proficiency_gated` escalation (inquiry-over-advice evidence) | ≥3 base + ≥2 transfer; gate at sustained proficiency ≥ 2 | **PARTIAL** (as 2.1) |
| Fade policy (Phase 5) | `in_session_coaching_rules.md` §4 (scaffolds that fade), `governance/scaffolding_fade_rules.md` §3.5 | Coach hints less and requires more over sessions | **PARTIAL** (as 2.1) |

### 2.3 Ambivalence_Dojo

| Check | Answering file(s) | Pass condition | Enforcement |
|---|---|---|---|
| Calibrated practice: intensity 1–5 | `sparring_intensity_profile.json` (sustain-talk strength IS the pushback; levels 4–5 deepen sustain talk) | Levels exactly 1–5; escalation/de-escalation policies; consent for 4–5 | **ENFORCED** (generic + owned) |
| Calibrated practice: user agreement | `sparring_intensity_profile.json` `user_agreement.required: true` (levels 4–5 explicit recorded consent) | Intensity set with the user, never assumed | **ENFORCED** (owned check: `user_agreement.required is True`) |
| Rubric-as-lens | `rubric.json` (`amb_mi_fidelity_v1` extends `mi_fidelity_v1`; `amb_spirit_gate_v1`; `amb_sustain_talk_navigation_v1`), `debrief_template.md` §2 | Lens-type; anchoring ("every score carries ≥1 evidence quote"); `extends.base` wired to the Phase 3 base rubric | **PARTIAL** — lens type + `extends` ENFORCED (owned); anchoring string not machine-checked |
| Sycophancy avoidance | `sparring_intensity_profile.json` `sycophancy_guard` (persona change-talk concession rate >0.8/10 turns → re-voice genuine sustain talk), `in_session_coaching_rules.md` §8 | Guard present; disingenuous change talk never manufactured or rewarded | **PARTIAL** (as 2.1) |
| No-surveillance | `persona_config.yaml` boundary_rules, `in_session_coaching_rules.md` §10 (incl. `live_decision_touch` — practice must not bleed into real ambivalence), `SKILL.md` Guardrails | Persona never scripted from lattice; live-decision touch pauses and checks in | **PARTIAL** (as 2.1; live_decision_touch present in `deescalation_rules`, not machine-checked) |
| preserved_user_decision in debriefs | `debrief_template.md` §6 (names: interpretation of performance, any real-world decision the practice touched, simulated decision stays simulated, next practice/stop/escalate) | Required section present; real-decision protection explicit | **ENFORCED** (generic) |
| Transfer proficiency-gated | `transfer_scenario_set.md` Transfer Rules; `proficiency_gated` escalation (reflection_to_question_ratio ≥0.7 across 10 turns, zero argument-against-resistance in 3 sessions) | ≥3 base + ≥2 transfer; gate at sustained proficiency ≥ 2 | **PARTIAL** (as 2.1) |
| Fade policy (Phase 5) | `in_session_coaching_rules.md` §4 (model utterances as scaffolds that fade), `governance/scaffolding_fade_rules.md` §3.5 | Hints beat answers; models fade session→zero | **PARTIAL** (as 2.1) |
| **Spirit gate** | `dialogue_state_machine.json` `transition_policy.hard_gates` (`spirit_gate`, `no_premature_closure`, `no_argument_against_resistance`), `in_session_coaching_rules.md` §2 (hard gate runs before ANY technique feedback), `rubric.json` `amb_spirit_gate_v1` (observable verdict per stage block), `governance/empowerment_boundary.md` §4 prohibition 8 | MI spirit (partnership/acceptance/compassion/evocation) verified before technique feedback; technique-without-spirit flagged once as a spirit note, never graded; no planning stage by design | **ENFORCED** — hard-gate ids (owned check), "spirit gate" + "no-premature-closure" in coach rules, spirit-gate rubric present |

### 2.4 Conflict_Dojo

| Check | Answering file(s) | Pass condition | Enforcement |
|---|---|---|---|
| Calibrated practice: intensity 1–5 | `sparring_intensity_profile.json` (arousal + positional rigidity orchestrated; blunt about the dispute, never identity, at any level) | Levels exactly 1–5; policies present; consent for 4–5 | **ENFORCED** (generic + owned) |
| Calibrated practice: user agreement | `sparring_intensity_profile.json` `user_agreement.required: true` | Intensity set with the user, never assumed | **ENFORCED** (owned) |
| Rubric-as-lens | `rubric.json` (`conf_deescalation_v2` extends `conflict_deescalation_v1`; `conf_interest_based_v1`; `conf_emotional_safety_v1`), `debrief_template.md` §2 | Lens-type; anchoring; hot sessions score de-escalation dims only | **PARTIAL** (as 2.3) |
| Sycophancy avoidance | `sparring_intensity_profile.json` `sycophancy_guard` (position-softening rate >0.8/10 turns → persona re-asserts its genuine position), `in_session_coaching_rules.md` §8 ("the persona does not calm to please") | Guard present; positions soften only when interests are heard | **PARTIAL** (as 2.1) |
| No-surveillance | `persona_config.yaml` boundary_rules (incl. `sanitization.bias_checks: lattice_leak: none`), `in_session_coaching_rules.md` §10 (incl. `live_conflict_touch`), `SKILL.md` Guardrails | Persona never knows lattice; practice must not reactivate real conflicts without check-in | **PARTIAL** (as 2.1) |
| preserved_user_decision in debriefs | `debrief_template.md` §6 (what the learner would accept in a real conversation stays with the user) | Required section present | **ENFORCED** (generic) |
| Transfer proficiency-gated | `transfer_scenario_set.md` Transfer Rules ("Run transfer only after the source skill shows sustained proficiency at level >= 2; proficiency_gated escalation applies to transfer too"; same rubric reused; one structural axis changed per transfer) | ≥3 base + ≥2 transfer; gate present; transfer gap names next target, never invalidates base skill | **PARTIAL** (as 2.1) |
| Fade policy (Phase 5) | `in_session_coaching_rules.md` §4 (scaffolds that fade), `governance/scaffolding_fade_rules.md` §3.5 | Coach hints less, requires more, over sessions | **PARTIAL** (as 2.1) |
| **De-escalation-first** | `dialogue_state_machine.json` `transition_policy.hard_gates` (`deescalation_first`, `no_shaming`, `no_forced_agreement`), `in_session_coaching_rules.md` §2 ("No positions-vs-interests work while the persona's arousal is hot… retreat to de-escalate if arousal re-rises"), §6 no-shaming gate, §7 (de-escalation dims scored before interest-based dims) | State machine holds at de-escalate until arousal ≤ medium; unresolved is a valid outcome | **ENFORCED** — hard-gate ids (owned), "de-escalation-first"/"deescalation_first" + "no-shaming gate" in coach rules |

### 2.5 Workplace_Dojo

| Check | Answering file(s) | Pass condition | Enforcement |
|---|---|---|---|
| Calibrated practice: intensity 1–5 | `sparring_intensity_profile.json` (power-gradient sensitivity; over-deference markers treated as overwhelm-equivalent) | Levels exactly 1–5; policies present; consent for 4–5 | **ENFORCED** (generic + owned) |
| Calibrated practice: user agreement | `sparring_intensity_profile.json` `user_agreement.required: true` | Intensity set with the user, never assumed | **ENFORCED** (owned) |
| Rubric-as-lens | `rubric.json` (`professional_clarity_v1`, `feedback_effectiveness_v1`, `workplace_negotiation_align_v1`), `debrief_template.md` §2 | Lens-type; anchoring | **PARTIAL** (as 2.3) |
| Sycophancy avoidance | `sparring_intensity_profile.json` `sycophancy_guard` incl. `mirror_monitor` (`user_over_deference_rate_per_10_turns` — with manager/stakeholder personas the USER's agreement is monitored), `in_session_coaching_rules.md` §8 | Guard present; mirror monitoring for power gradients | **PARTIAL** — `sycophancy_guard` presence generic-ENFORCED; `mirror_monitor` owned-ENFORCED; thresholds not validated |
| No-surveillance | `persona_config.yaml` boundary_rules, `in_session_coaching_rules.md` §10, `SKILL.md` Guardrails | Persona never knows lattice; logs stay in practice | **PARTIAL** (as 2.1) |
| preserved_user_decision in debriefs | `debrief_template.md` §6 | Required section present | **ENFORCED** (generic) |
| Transfer proficiency-gated | `transfer_scenario_set.md` Transfer Rules; `proficiency_gated` escalation (≥2 explicit asks with owner + deadline per 5 turns) | ≥3 base + ≥2 transfer; gate present | **PARTIAL** (as 2.1) |
| Fade policy (Phase 5) | `in_session_coaching_rules.md` (explicit `scaffolding_fade_rules` citation — SBI scaffolding), `governance/scaffolding_fade_rules.md` §3.5 | Explicit reference to the Phase 5 fade doc in coach rules | **ENFORCED** — "scaffolding_fade_rules" substring in coach rules (owned check); the only dojo where the fade linkage is machine-checked |

---

## 3. Harness-Integration QA (Phase 7 tree)

How the dojos integrate with `Hermes_Agent_Harness/`, and what must hold at the
packaged-tree level. Build-time verifier: `council_notes/verify_phase7.py` (chained
into verify_all.py); consumer re-verifier ships inside the tree:
`Hermes_Agent_Harness/verify/verify_harness.py`.

### 3.1 Integration surface

- **routines/ via the ConvoDojo executor.** `routines/<Dojo>_Dojo/` holds the five
  seven-artifact content packages; they are *content*, not new skill nodes — all five
  execute through `skills/ConvoDojo_Practice_Sparring/` (the shared executor whose
  AtomicOps `select_scenario → configure_persona → set_intensity_profile (with the
  user) → open/advance_stage → generate_interlocutor_turn → coach_interrupt →
  apply_rubric_lens → calibrate_pushback → debrief_session → run_transfer_scenario
  (after sustained proficiency)`, with `check_psychological_safety` throughout).
  Wiring documented in `Hermes_Agent_Harness/README.md` (Install/Use → Running
  routines/) and `routines/README.md` §2.1. Graph wiring: ConvoDojo
  `recovers_with: Human_Empowerment_Boundary` (sparring overreach → boundary reset),
  `can_follow` from MLG, pairs with `Proximal_Practice_Selector` for sparring-scaffold
  fade (`skill_graph_index.json`; `routines/README.md` §4.2).
- **logs/ contract.** `logs/log_schema.md` is the runtime contract (ships empty with
  `.gitkeep`). The ConvoDojo executor appends `dojo_session` events; PPS/HEB append
  `skill_load_snapshot` / `boundary_gate_outcome`; calibration runs append
  `calibration_event`. The `dojo_session` event must carry: `dojo`, `persona_id`,
  `intensity_level` (1–5 *as agreed*), `stages_entered`, `coaching_interventions`
  (hints, not answers), `rubric_scores` (each anchored to ≥1 utterance quote),
  `debrief_ref`, `preserved_user_decisions` (per agent_deference_rules.md §2.1),
  `outcome_arbitration` (user verdict) — plus the common envelope (`event_id`,
  `timestamp`, `event_type`, `session_id`, `source`, `schema_version`,
  `user_consent_ref`, `evidence_flag`). Append-only; corrections are new entries.
- **governance/ safeguards.** The five Phase 5 documents are authoritative in
  `governance/` and bind the dojo layer: HEB boundary gate required before any
  AtomicOp on high-meaning tasks (graph `governance.boundary_gate_rule`);
  `scaffolding_fade_rules.md` §3.5 names ConvoDojo + PPS explicitly; log schema
  governance notes logs are consent-scoped observations and **never feed the persona
  module** (Ma 2025).

### 3.2 Concrete integration checks

| # | Check | Answering file(s) | Pass condition | Enforcement |
|---|---|---|---|---|
| I1 | Routine inventory + executor presence | `routines/<Dojo>_Dojo/` × 5, `skills/ConvoDojo_Practice_Sparring/` | Exactly 7 artifacts per dojo dir (no missing, no extra); executor package carries the 9 core files (incl. `evaluation_notes.md`); all JSON/YAML in the tree parse | **ENFORCED** — verify_phase7 checks 2/3/6; verify_harness.py re-checks 2/3/5 for consumers |
| I2 | Log-contract conformance | `logs/log_schema.md` vs. runtime `logs/` entries (e.g. `dojo_session` fields + envelope) | Every log entry conforms to its event type's required fields; append-only; `user_consent_ref` populated (or `none`); scores anchor to quotes | **GAP** — verify_phase7 checks only the scaffold (`log_schema.md` + `.gitkeep` present). No machine check that runtime entries conform. Recommend a log-conformance check (schema-validate sample entries) in verify_phase7 or a runtime validator. |
| I3 | No-surveillance wiring end-to-end | `routines/<Dojo>_Dojo/persona_config.yaml` (`boundary_rules` + `sanitization.bias_checks`), `logs/log_schema.md` governance note, `governance/empowerment_boundary.md` §4 prohibition 2 | Every persona in every dojo carries the no-lattice-reference boundary rule; log schema states logs never feed the persona | **PARTIAL** — 'lattice' keyword per persona ENFORCED by verify_phase6 (generic); the log_schema governance note and prohibition are prose |
| I4 | Governance binding | `governance/` (5 Phase 5 files), `skill_graph_index.json` `governance.boundary_gate_rule`, `routines/README.md` §2.4 (cites `governance/scaffolding_fade_rules.md`, not the stale Phase5 path) | All 5 governance files present; boundary gate declared in graph; packaged routines README points at packaged governance paths; no stale `Phase5_Safeguards`/`Phase6_Dojo` paths outside documented provenance notes | **ENFORCED** — verify_phase7 checks 4 (graph governance), 9 (governance/ presence), 10 (stale-path sweep) |
| I5 | Executor → logs handoff | `skills/ConvoDojo_Practice_Sparring/SKILL.md` (Handoff Notes: "Session logs and debriefs belong in the harness `logs/` folder (per logs/log_schema.md — dojo_session events)"), `evaluation_notes.md` (Layer 5 artifact checks incl. "practice logs bounded to practice (no surveillance)") | Executor explicitly routes session logs/debriefs to `logs/` per the schema; evaluation notes carry the practice-layer QA checks | **PARTIAL** — `evaluation_notes.md` presence ENFORCED (9 core files); the log-routing reference and evaluation checklist are prose |

---

## 4. Gap Register (verifier coverage holes to close)

- **G1 (schema drift):** Conversation_Dojo and Coaching_Dojo declare user agreement as
  `user_agreement_requirement` instead of the §2.1 convention `user_agreement.required:
  true`, and `verify_phase6.py` checks user agreement only for owned dojos
  (Ambivalence, Conflict, Workplace). Semantics are present; key name and verifier
  coverage are not. Fix: rename to `user_agreement.required` in the two sibling
  profiles and extend the generic check to all five.
- **G2 (transfer gate prose):** the "transfer runs only after sustained proficiency ≥ 2"
  gate lives in `transfer_scenario_set.md` Transfer Rules and `routines/README.md`
  §2.4; verify_phase6 checks only scenario counts. Recommend a machine check that the
  Transfer Rules section carries the proficiency-gate sentence.
- **G3 (fade linkage):** only Workplace_Dojo's coach rules are machine-checked for the
  explicit `scaffolding_fade_rules` citation; the other four rely on "scaffolds that
  fade" prose plus the estate doc. Recommend extending the owned-style fade check to
  all five coach-rule files.
- **G4 (sycophancy content):** `sycophancy_guard` key presence is enforced for all
  five, but `monitor` metric, `alert_threshold` (0.8), and recalibration `response`
  are not validated (Workplace adds `mirror_monitor`). Recommend validating the guard
  sub-keys.
- **G5 (rubric anchoring):** lens type and `rubric_use_rules` presence are enforced;
  the `scoring.anchoring` evidence-quote contract is not machine-checked.
- **G6 (log conformance):** harness-level (I2) — no verifier validates runtime
  `logs/` entries against `log_schema.md` event types.
- **G7 (no-surveillance direct check):** no verify_phase6 check names the
  surveillance prohibition itself; only the persona 'lattice' keyword is enforced.
  Recommend a check that `in_session_coaching_rules.md` §10 carries the
  no-surveillance sentence in every dojo (present today in all five).

## 5. Bottom Line

All five dojos **pass** every plan criterion at artifact-content level; the two
dojo-specific safety gates (Ambivalence spirit gate, Conflict de-escalation-first) are
machine-enforced and passing. The verifier's coverage is complete for structure and
the safety gates, partial for semantic content (anchor strings, thresholds, gate
prose), and has one real schema hole (G1: Conversation/Coaching user-agreement key
drift). Recommend closing G1–G7 in the Phase 8 revision round and re-running
verify_phase6.py + verify_phase7.py to exit 0 before the harness is re-uploaded.
