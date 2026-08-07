# Skill Package QA Checklist — Phase 8 (Applied)

Project: Motivational Ecology Agent Architecture — Phase 8: Evaluation and Calibration
Date: 2026-08-06
Status: APPLIED against the real Phase3_Skills/ artifacts (all 8 packages), the lattice layer, and the build verifiers.
Method: For each plan criterion (Phase8_Plan.md §Requirements 1–10) and each of the 8 skill packages, this checklist names (a) the exact file(s) that answer the check, (b) the pass condition, and (c) enforcement status — "verified by <verifier> check N" where a verifier already enforces it, or **GAP** where nothing enforces it and review is the only gate.

## Verifier Coverage Map (used throughout)

| Verifier | File | Checks |
|---|---|---|
| verify_packages.py | Phase3_Skills/verify_packages.py | 1 JSON parse · 2 YAML parse · 3 canonical 9-file structure · 4 SKILL.md 16-section standard · 5 AtomicOps SKILL.md ↔ atomic_ops.json ↔ edge_map.json · 6 edge endpoint resolution · 7 seed-index agreement |
| verify_phase4.py | council_notes/verify_phase4.py | 1 Phase-4 outputs exist · 2 all JSON valid · 3 source/target keys (no from/to) · 4 recovers_with cross-skill kind + direction · 5 node id PascalCase + boundary_gate required · 6 TDF binding_constraint_comb rename · 7 skill_load canonical in T2R · 8 quarantined edges + deferred nodes · 9 index governance section · 10 lattice index coherence (layers, Q2 tier, ≥5 triggers, MLG schema refs) · then re-runs verify_packages + verify_phase3 |
| verify_critique_revisions.py | council_notes/verify_critique_revisions.py | 1 ConvoDojo 13 ops + per-op guardrails + check_psychological_safety · 2 HEB skill_load_trend derived + notes skill_load_score · 3 T2R 48 entries, 39 instantiated + 9 uninstantiated + 0 partial · 4 index COMB→TDF decomposes_to RECONCILED + recovers_with convention resolved · 5 COMB/TDF edge-map direction reconciliation · 6 MI focusing ops (agree_direction, prioritize) |

Cross-cutting result: all three verifiers pass (verified 2026-08-06). The gaps below are therefore **content-level gaps** — sections and files exist and pass structural checks, but no verifier checks the *substance* the Phase-8 criteria ask about.

---

## 1. Human_Empowerment_Boundary (governance)

| Criterion (Phase-8 #) | Evidence file(s) | Pass condition | Enforcement |
|---|---|---|---|
| AtomicOp decomposition (#1) | `Human_Empowerment_Boundary/atomic_ops.json`, `SKILL.md` "## Atomic Operations", `edge_map.json` decomposes_to | 11 ops listed in SKILL.md, present in atomic_ops.json, all decomposes_to targets match ops in order 1..11 | verified by verify_packages.py check 5 (decomp-matches-ops, decomp-ordered) |
| Trigger conditions (#2) | `SKILL.md` "## Trigger Conditions" | ≥1 concrete trigger present (here 9: high-meaning tasks, option-space constraint, lattice-insight steering, atrophy risk, recovery handoff, friction removal, theater check…) | header verified by verify_packages.py check 4 (section presence only) — trigger *content* is **GAP** |
| Completion conditions (#2) | `SKILL.md` "## Outputs" + `select_empowerment_mode` / `record_boundary_outcome` ops; state var `recommended_mode` | Completion determinable: mode selected (ACT/SCAFFOLD/ASK/DEFER/STOP) + outcome recorded; `record_boundary_outcome` is the terminal op | **GAP** — the 16-section standard has no "Completion Conditions" section; completion is carried implicitly by terminal `record_*` ops; no verifier checks terminal-op existence per package |
| Empowerment section (#3) | `SKILL.md` "## Empowerment Boundary" | Section lists agent-auto vs preserve-for-user; here preserves decisions, interpretation, identity claims, verdicts, readiness | header verified by verify_packages.py check 4; content **GAP** |
| Learnability / atrophy (#4, #5) | `SKILL.md` "## Learnability / Skill-Atrophy Check" | Section present; here asks 6 atrophy questions, falling-trend-overrides-performance rule, SCAFFOLD-over-ACT default | header verified by check 4; content **GAP** |
| Evidence citations (#6, #10) | `SKILL.md` Purpose + ops (Beacock 2026, Bastani 2025, Brynjolfsson 2025, Xu 2026, ProACT 2026, Liu 2026, Budzyń 2025, Heudel 2026) | Core claims name sources; anti-empowerment-theater and friction-as-design carry named citations | **GAP** — no verifier scans for citations or VERIFIED/RECONSTRUCTED flags (review-enforced; see Calibration_Log catches) |
| User-correction paths (#7) | `SKILL.md` "## Recovery Operations", `recovery_ops.md` (8 recovery ops), `edge_map.json` recovers_with endpoints | Recovery ops exist (Reopen_User_Choice, Ask_Targeted_Clarification, Downgrade_To_Scaffold, Mark_As_Provisional, Return_To_User_Authority, Reduce_Automation_Level, Undo_Interpretive_Closure, Debrief_Overreach) and resolve as edge endpoints; lattice-interface section grants user reject/revise rights | recovery-op endpoints verified by verify_packages.py check 6; right-to-reject substance **GAP** |
| State schema coherence (#8, #10) | `state_schema.json` vs `SKILL.md` "## State Variables"; `T2R_traceability.json` canonical_state_variables | State vars consistent; canonical names used; `skill_load_trend` documented as DERIVED from PPS `skill_load_score` | JSON parse verified by check 1; T2R canonicality verified by verify_phase4.py check 7 + verify_critique_revisions.py check 2 — but SKILL.md↔state_schema cross-check is **GAP** (see Reconciliation Notes R2) |

---

## 2. COMB_Behavioral_Diagnosis

| Criterion | Evidence file(s) | Pass condition | Enforcement |
|---|---|---|---|
| AtomicOp decomposition (#1) | `COMB_Behavioral_Diagnosis/atomic_ops.json`, `SKILL.md`, `edge_map.json` | 14 ops consistent across all three; decomposes_to ordered 1..14 | verified by verify_packages.py check 5 |
| Trigger conditions (#2) | `SKILL.md` "## Trigger Conditions" | ≥1 concrete trigger (6 listed: stuck-goal language, why-won't-change, no-diagnosis plan, TDF/MI/SDT anchor, BCW/BCT input, diagnostic mirroring) | header by check 4; content **GAP** |
| Completion conditions (#2) | `SKILL.md` "## Outputs" + `emit_component_profile` / `record_diagnosis` | Completion: profile emitted with hypothesis label + recorded; `record_diagnosis` terminal | **GAP** (no completion-section standard; no terminal-op check) |
| Empowerment section (#3) | `SKILL.md` "## Empowerment Boundary" | Preserves user's own words, knowledge-probe answers, time-allocation, commitments, profile endorsement/correction/rejection | header by check 4; content **GAP** |
| Learnability / atrophy (#4, #5) | `SKILL.md` "## Learnability / Skill-Atrophy Check" | Teaches six-component vocabulary; profile marked teachable artifact; agent role faded | header by check 4; content **GAP** |
| Evidence citations (#6, #10) | `SKILL.md` Purpose (Michie 2011 88%/79% IRR; Willmott 2021 31%/23%); M-Au habit/emotion collapse flagged RECONSTRUCTED | Descriptive-not-predictive framing cited; critique flags carry RECONSTRUCTED label | **GAP** (review-enforced) |
| User-correction paths (#7) | `SKILL.md` recovery ops + `recovery_ops.md` (7 ops incl. Reopen_Component_Assignment, Downgrade_To_Hypothesis, Separate_Evidence_Interpretation_Implication); state var `user_corrections`; `label_hypothesis_status` op | Every profile emitted with hypothesis label; user_corrections recorded per rejected slot; recovery ops resolve as endpoints | endpoints by check 6; `user_corrections` state presence and hypothesis-label-always rule **GAP** |
| State schema coherence (#8, #10) | `state_schema.json` vs SKILL.md State Variables | `binding_constraint` enum C-Ph..M-Au|none identical in both; `lattice_insights_used` bool present; hypothesis_status always true | JSON by check 1; T2R canonical binding_constraint by verify_critique_revisions.py check 3 + verify_phase4.py check 6 (COMB keeps the name, TDF renamed) — SKILL.md↔state_schema **GAP** |

---

## 3. TDF_Barrier_Facilitator_Grid

| Criterion | Evidence file(s) | Pass condition | Enforcement |
|---|---|---|---|
| AtomicOp decomposition (#1) | `TDF_Barrier_Facilitator_Grid/atomic_ops.json`, `SKILL.md`, `edge_map.json` | 10 ops consistent; ordered decomposes_to 1..10 | verified by verify_packages.py check 5 |
| Trigger conditions (#2) | `SKILL.md` "## Trigger Conditions" | ≥1 concrete trigger (5: COM-B refinement need, barrier/facilitator language, implementation question, PPS/BCW-BCT input, "what is really in the way") | header by check 4; content **GAP** |
| Completion conditions (#2) | `SKILL.md` "## Outputs" + `emit_barrier_grid` / `record_grid` | Completion: salience-ordered grid + version metadata + confirmation queue recorded; `record_grid` terminal | **GAP** |
| Empowerment section (#3) | `SKILL.md` "## Empowerment Boundary" | Preserves final interpretation, construct-code acceptance/correction, every identity-level claim, barrier reality, facilitator worth | header by check 4; content **GAP** |
| Learnability / atrophy (#4, #5) | `SKILL.md` "## Learnability / Skill-Atrophy Check" | Grid teaches domain vocabulary; fade to self-coding; attribution clarity (user quotes vs agent codes) | header by check 4; content **GAP** |
| Evidence citations (#6, #10) | `SKILL.md` Purpose (Cane 2012 silhouette 0.29 fragility encoded; Michie 2005; Zhou 2024; Wu 2024); all domain codes labeled RECONSTRUCTED | Fragile validation encoded as low confidence; coder-level inference labeled | **GAP** (review-enforced) |
| User-correction paths (#7) | `SKILL.md` recovery ops + `recovery_ops.md` (Reopen_Construct_Assignment, Downgrade_Confidence, Mark_Identity_Claim_Provisional, Reencode_Version_Metadata); `confirmation_queue` state; `ask_identity_domain_confirmation` op; `user_corrections` state | Domain-3/identity claims held in confirmation_queue until explicit user confirmation; rejected constructs re-coded; correction recorded | endpoints by check 6; confirmation-queue semantic (identity gate) **GAP** |
| State schema coherence (#8, #10) | `state_schema.json` vs SKILL.md State Variables; verify_phase4.py check 6 | state_schema renamed `binding_constraint_comb` (C/O/M/none) to kill COMB collision — verified. SKILL.md "## State Variables" UPDATED to `binding_constraint_comb` (Calibration_Log row 18, 2026-08-06 whole-project round) — drift CLOSED in both source and harness copies | rename + SKILL.md sync verified by verify_phase4.py check 6; no remaining drift (was **GAP**, resolved row 18) |

---

## 4. SDT_Need_Support_Check

| Criterion | Evidence file(s) | Pass condition | Enforcement |
|---|---|---|---|
| AtomicOp decomposition (#1) | `SDT_Need_Support_Check/atomic_ops.json`, `SKILL.md`, `edge_map.json` | 10 ops consistent; ordered decomposes_to 1..10 | verified by verify_packages.py check 5 |
| Trigger conditions (#2) | `SKILL.md` "## Trigger Conditions" | ≥1 concrete trigger (8: phrasing a recommendation, designing user-facing flow, pressure language, reward consideration, discord flag, internalization goal, lattice insight use, dependency risk) | header by check 4; content **GAP** |
| Completion conditions (#2) | `SKILL.md` "## Outputs" + `record_need_support_outcome` | Completion: need-support audit + regulatory-style classification + guardrail flags recorded; terminal op | **GAP** |
| Empowerment section (#3) | `SKILL.md` "## Empowerment Boundary" | Preserves user's own reasons, classification acceptance, final choice, meaning, values/identity, need-frustration interpretation acceptance | header by check 4; content **GAP** |
| Learnability / atrophy (#4, #5) | `SKILL.md` "## Learnability / Skill-Atrophy Check" | Trains volition not compliance; scaffolds fade; classification provisional; introjection treated as alarm not lever | header by check 4; content **GAP** |
| Evidence citations (#6, #10) | `SKILL.md` Purpose/ops (Deci 1999 undermining; Beacock 2026; Li et al. 2025 introjection centrality; OIT internalization) | SDT red lines carry named citations; anti-introjection + no-tangible-reward guardrails | **GAP** (review-enforced) |
| User-correction paths (#7) | `SKILL.md` recovery ops + `recovery_ops.md` (Remove_Reward_Contingency, Reopen_User_Choice, Downgrade_To_Scaffold, Undo_Introjection_Label, Return_To_User_Authority, Debrief_Need_Support_Overreach); `regulatory_style_confidence` labeled inference | Classification offered as labeled, user-correctable hypothesis; reward contingency removable | endpoints by check 6; labeled-inference rule **GAP** |
| State schema coherence (#8, #10) | `state_schema.json` vs SKILL.md State Variables | need_support audit levels, regulatory_style enum, guardrail flags consistent; T2R name variant `autonomy_support_phrasing`→`suggest_autonomy_support_phrasing` reconciled | JSON by check 1; T2R variant reconciled in verify_critique_revisions.py check 3 (counts); SKILL.md↔state_schema **GAP** |

---

## 5. MI_Ambivalence_Conversation

| Criterion | Evidence file(s) | Pass condition | Enforcement |
|---|---|---|---|
| AtomicOp decomposition (#1) | `MI_Ambivalence_Conversation/atomic_ops.json`, `SKILL.md`, `edge_map.json` | 14 ops consistent incl. Phase-4 focusing ops `agree_direction` + `prioritize`; ordered decomposes_to | verified by verify_packages.py check 5 + verify_critique_revisions.py check 6 |
| Trigger conditions (#2) | `SKILL.md` "## Trigger Conditions" | ≥1 concrete trigger (7: ambivalence, sustain talk, behavior-change exploration, diagnosis-handoff, readiness need, stuck between reasons, sparring mode) | header by check 4; content **GAP** |
| Completion conditions (#2) | `SKILL.md` "## Outputs" + `record_mi_session` | Completion: process_state + change-talk log + fidelity report + readiness verdict recorded; terminal op `record_mi_session` | **GAP** |
| Empowerment section (#3) | `SKILL.md` "## Empowerment Boundary" | Preserves user's own reasons (evocation — agent never supplies the case), direction, readiness judgment, commitments, change decision, ambivalence interpretation | header by check 4; content **GAP** |
| Learnability / atrophy (#4, #5) | `SKILL.md` "## Learnability / Skill-Atrophy Check" | Evocation vs substitution; explore vs argue; practice scaffolds reflection skill; calibrated challenge over demo | header by check 4; content **GAP** |
| Evidence citations (#6, #10) | `SKILL.md` Purpose/ops (Kuchipudi 1990 + Miller & Rose 2009 spirit gate; Bischof 2021 OR 1.55; Amrhein 2003 commitment slope; Aimi/MISC-2 ~0.84 ratio + ≥50% complex; Miller & Mount 2001 self-report; Eiroa-Solans 2025; Karve 2025) | Fidelity targets and causal chain carry named citations | **GAP** (review-enforced) |
| User-correction paths (#7) | `SKILL.md` recovery ops + `recovery_ops.md` (Return_To_Spirit, Explore_Resistance_Openly, Downgrade_To_Reflection, Defer_Planning, Reopen_Ambivalence, Debrief_Fidelity_Failure); reflections-as-hypotheses ("is that close?"); recovers_with SDT on discord | Reflections offered as correctable hypotheses; sustain talk explored never fought; discord → SDT autonomy-support repair | endpoints by check 6 + verify_phase4.py check 4 (cross-skill recovers_with); hypothesis-form rule **GAP** |
| State schema coherence (#8, #10) | `state_schema.json` vs SKILL.md State Variables | spirit_state, process enums, fidelity targets, change_talk_log/sustain_talk_log, commitment_slope, readiness_verdict consistent; `change_talk_log` canonical per T2R | JSON by check 1; change_talk_log canonical kept (T2R) — SKILL.md↔state_schema **GAP** |

---

## 6. Proximal_Practice_Selector

| Criterion | Evidence file(s) | Pass condition | Enforcement |
|---|---|---|---|
| AtomicOp decomposition (#1) | `Proximal_Practice_Selector/atomic_ops.json`, `SKILL.md`, `edge_map.json` | 9 ops consistent; ordered decomposes_to 1..9 | verified by verify_packages.py check 5 |
| Trigger conditions (#2) | `SKILL.md` "## Trigger Conditions" | ≥1 concrete trigger (7: learning/practice task, about-to-help, fade due, proactive-timing decision, post-assisted atrophy check, dose design, other-skill flag) | header by check 4; content **GAP** |
| Completion conditions (#2) | `SKILL.md` "## Outputs" + `record_unassisted_competence` | Completion: assistance_mode + skill_load_score + readiness verdict + atrophy alert; terminal op records unassisted track | **GAP** |
| Empowerment section (#3) | `SKILL.md` "## Empowerment Boundary" | Preserves task performance itself, unassisted-attempt timing, goal setting, scaffold acceptance, practice meaning, acting on alerts | header by check 4; content **GAP** |
| Learnability / atrophy (#4, #5) | `SKILL.md` "## Learnability / Skill-Atrophy Check" (this skill IS the check) | Hints-before-answers; fade tied to unassisted evidence; assisted/unassisted logged separately; falling skill_load triggers alert | header by check 4; content **GAP** |
| Evidence citations (#6, #10) | `SKILL.md` Purpose/ops (Bastani 2025 +48%/−17%; Budzyń 2025 28.4→22.4%; Brynjolfsson 2025; Liu 2026 +21%; Eiroa-Solans 2025; Natali 2025; Heudel 2026; Lee 2025; CALM-IT) | Red-line divergence finding and fade/dose/timing rules carry named citations | **GAP** (review-enforced) |
| User-correction paths (#7) | `SKILL.md` recovery ops + `recovery_ops.md` (Restore_Scaffold, Reschedule_Practice, Reopen_User_Choice, Downgrade_To_Hint, Surface_Unassisted_Track, Debrief_Atrophy_Event); lattice interface: inferred readiness never overrides user's stated readiness | Scaffold restorable after failed fade; readiness inference user-overridable; unassisted track surfaced to user | endpoints by check 6; readiness-override rule **GAP** |
| State schema coherence (#8, #10) | `state_schema.json` vs SKILL.md State Variables | `skill_load_score` number 0..1 canonical (PPS writes); assisted/unassisted tracks separate; scaffold_level 0..5 consistent | JSON by check 1; skill_load canonical by verify_phase4.py check 7 (T2R) — SKILL.md↔state_schema **GAP**; see R2 for score→trend conversion |

---

## 7. Motivational_Lattice_Generator (lattice producer)

| Criterion | Evidence file(s) | Pass condition | Enforcement |
|---|---|---|---|
| AtomicOp decomposition (#1) | `Motivational_Lattice_Generator/atomic_ops.json`, `SKILL.md`, `edge_map.json` | 12 ops consistent incl. `label_hypothesis_status`-equivalent (`form_interpretation_hypothesis`), `quarantine_insight`, `record_user_verdict`; ordered decomposes_to | verified by verify_packages.py check 5; quarantine/verdict ops registered in T2R (instantiated) |
| Trigger conditions (#2) | `SKILL.md` "## Trigger Conditions" | ≥1 concrete trigger (6: accumulated observations, user shares material, any-skill inference, reusing inferred preferences, recurring pattern, Phase-4 policy input) | header by check 4; content **GAP** |
| Completion conditions (#2) | `SKILL.md` "## Outputs" + `present_lattice_for_review` / `record_user_verdict` | Completion: lattice rendered for review + verdict recorded + quarantine list maintained; terminal ops | **GAP** |
| Empowerment section (#3) | `SKILL.md` "## Empowerment Boundary" | Preserves insight accept/reject/revise, identity confirmation, "what motives really are" closure, interpretive closure, un-made decisions; rejection absolute regardless of evidence | header by check 4; content **GAP**; rejection-absolute rule cross-checked in Motivational_Lattice_QA_Checklist.md |
| Learnability / atrophy (#4, #5) | `SKILL.md` "## Learnability / Skill-Atrophy Check" | Prefers reflection prompt over delivered insight; lattice scaffolding fades; user's reflective capacity never replaced; evidence rendered for user verification | header by check 4; content **GAP** |
| Evidence citations (#6, #10) | `SKILL.md` Purpose (Lim 2025 0.80 LOOCV; SERUM 2026 schematic equilibrium; AnnoMI; Shaikh 2026 ~17%); `insight_node_schema.json` `source_influences` field; guardrail: uncited insights discarded | Every insight cites observations; evidence anchors recorded per node | **GAP** (review-enforced; runtime rule in schemas + validation protocol, not machine-checked) |
| User-correction paths (#7) | `SKILL.md` recovery ops + `recovery_ops.md` (User_Verdict_Override, Rebuild_Lattice_From_Raw_Observations, Undo_Interpretive_Closure, Quarantine_Insight, Reopen_User_Choice, Downgrade_Confidence, Debrief_Overinterpretation); `record_user_verdict` op; `user_verdict_record` state | Verdict recorded per insight (pending/confirmed/rejected/revised); rejection propagates through dependents (User_Verdict_Override) | endpoints by check 6; verdict-propagation substance **GAP** (see Lattice QA: user verdict paths) |
| State schema coherence (#8, #10) | `state_schema.json` + 3 schemas (`observation_schema.json`, `insight_node_schema.json`, `evidence_edge_schema.json`) vs `SKILL.md` State Variables vs `lattice_index.json` layers/state_variables | MLG state vars mirror lattice_index state_variables block; schema required fields match lattice_index layer `required` lists; `user_verdict` enum consistent (pending/confirmed/rejected/revised) | JSON parse by check 1; lattice_index schema refs + layers by verify_phase4.py check 10; field-level schema↔index cross-check **GAP** |

---

## 8. ConvoDojo_Practice_Sparring

| Criterion | Evidence file(s) | Pass condition | Enforcement |
|---|---|---|---|
| AtomicOp decomposition (#1) | `ConvoDojo_Practice_Sparring/atomic_ops.json`, `SKILL.md`, `edge_map.json` | 13 ops consistent incl. anti-sycophancy `check_psychological_safety` (Phase-4 critique op); every op carries inputs/outputs/guardrails; ordered decomposes_to | verified by verify_packages.py check 5 + verify_critique_revisions.py check 1 (13 ops, guardrails on all, safety op reads sycophancy_risk) |
| Trigger conditions (#2) | `SKILL.md` "## Trigger Conditions" | ≥1 concrete trigger (6: pre-real-use practice, pre-deployment stress test, evidence-grounded feedback, calibrated resistance, role-play separation, skill-package practice track) | header by check 4; content **GAP** |
| Completion conditions (#2) | `SKILL.md` "## Outputs" + `debrief_session`; state `session_complete` | Completion: staged transcript + rubric feedback + debrief report + transfer/stress results; `session_complete` true | **GAP** |
| Empowerment section (#3) | `SKILL.md` "## Empowerment Boundary" | Preserves whether/how much to practice, intensity acceptance, performance interpretation, next-step choice, real-conversation decisions, user-controlled coaching interrupts | header by check 4; content **GAP** |
| Learnability / atrophy (#4, #5) | `SKILL.md` "## Learnability / Skill-Atrophy Check" | Practice builds unassisted conversational capability; intensity in proximal zone; scaffold fades across sessions; transfer scenarios verify generalization | header by check 4; content **GAP** |
| Evidence citations (#6, #10) | `SKILL.md` Purpose (EasyMED 2025; AgentForge 2026 / Voigt 2025; 2026 adversarial testing r=0.82; Aimi/Shenoi 2026; Han 2026 52.6%; Rudolph 2025; Ma 2025) | Practice architecture + rubric-as-lens + persona-sanitization claims carry named citations | **GAP** (review-enforced) |
| User-correction paths (#7) | `SKILL.md` recovery ops + `recovery_ops.md` (Reduce_Intensity, Reframe_Rubric_As_Lens, Switch_Persona, Downgrade_To_Scaffold, Return_To_User_Authority); `set_intensity_profile` requires user agreement; `coach_interrupt` user-controlled; rubric as lens not verdict | Intensity agreed with user, adjustable mid-session; coaching interruptions user-controlled; feedback never a verdict | endpoints by check 6; intensity-user-agreement rule **GAP** |
| State schema coherence (#8, #10) | `state_schema.json` vs SKILL.md State Variables | stage machine, intensity 1–5, coaching_mode, sycophancy_risk, psychological_safety, stress_test_status, transfer_flag consistent | JSON by check 1; SKILL.md↔state_schema **GAP**; anti-sycophancy substance (orchestration invariant) cross-checked in Lattice QA no-manipulation section |

---

## Reconciliation Notes (known, tracked)

**R1 — T2R traceability: 9 uninstantiated register ops.** `T2R_traceability.json` registers 48 AtomicOp candidates from Theory_to_Routine_Interface.md; 39 instantiated, **9 UNINSTANTIATED** (status field): `canvass_full_range`, `select_bct`, `retrocode_delivered_plan` (BCW/BCT layer deferred — no package), `assess_coherence`, `form_cmo_hypothesis` (NPT / realist evaluation — Feedback_Ecology_Map not built), `scan_materials`, `scan_meanings`, `detect_shared_elements`, `design_novelty_into_routine` (practice theory — Material_Arrangement_Scan not built). All 9 map to deferred packages already quarantined in `skill_graph_index.json` (verify_phase4.py check 8). Pass condition: 48/39/9/0 counts hold and every uninstantiated op names its blocking package — verified by verify_critique_revisions.py check 3. Standing scope decision needed on the BCW/BCT layer (the only one not tied to a deferred-but-planned package).

**R2 — skill_load_score → skill_load_trend conversion PENDING.** Canonical variable `skill_load` (= `skill_load_score`, number 0..1) is written by Proximal_Practice_Selector (`compute_skill_load`); Human_Empowerment_Boundary consumes a *derived* `skill_load_trend` (rising/flat/falling) for its atrophy override. T2R `canonical_state_variables.skill_load.action` = "UNIFY in Phase 4 — HEB reads skill_load_trend, PPS writes skill_load_score; add conversion or single variable"; HEB `state_schema.json` note: "Unification pending Phase 4." Phase 4 fixed the direction (PPS writes score, HEB derives trend) but **no conversion op is instantiated** — this is the T4 trigger's dependency (falling-trend triggers atrophy response; single-point dips must not). verify_critique_revisions.py check 2 verifies only that the note exists, not the conversion. Status: documented decision, uninstantiated conversion — GAP for criterion #8 (state coherence) until the conversion op exists.

**R3 — TDF naming drift (CLOSED).** `TDF_Barrier_Facilitator_Grid/state_schema.json` renamed `binding_constraint` → `binding_constraint_comb` (C/O/M/none, Phase-4 decision 4, verified by verify_phase4.py check 6). The SKILL.md "## State Variables" prose that still wrote the old name was corrected to `binding_constraint_comb` in the Phase 8 whole-project round (Calibration_Log row 18) — both source Phase3_Skills/ and harness skills/ copies now agree. No remaining drift. Recommended (still open): add a SKILL.md↔state_schema name cross-check to verify_packages.py so the class is machine-guarded, not review-guarded.

**R4 — Cross-cutting verifier gaps (all 8 packages).** (a) No verifier checks *completion conditions*: the 16-section standard (SECTIONS16) has no "## Completion Conditions" header and no check that each package has a terminal `record_*` op. (b) No verifier checks *evidence citations*: nothing scans for named sources, VERIFIED/RECONSTRUCTED flags, or the "every insight cites observations" rule — evidence discipline is enforced only by review rounds (see Calibration_Log: Jose 2025 opinion flag, CALM-IT preprint, missing VERIFIED anchors). (c) No verifier cross-checks SKILL.md "## State Variables" against `state_schema.json` contents (only JSON validity). (d) Empowerment/learnability sections are header-checked (check 4) but never content-checked. Proposed closure: extend verify_packages.py with checks 8 (completion: terminal op exists), 9 (state-var name parity SKILL.md ↔ state_schema.json), 10 (citation presence: ≥1 named source per package), and a lattice QA check that insight nodes require `evidence_edges` non-empty.
