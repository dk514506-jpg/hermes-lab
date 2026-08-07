# Insight Trigger Policy v1.0

Project: Motivational Ecology Agent Architecture — Phase 4: Graph and Lattice Integration
Date: 2026-08-06
Status: RECONCILED — companion to skill_graph_index.json v1.0, lattice_index.json, skill_lattice_interface.md
Evidence discipline: thresholds carry VERIFIED / RECONSTRUCTED flags; prediction ceilings constrain autonomous action (Contrary_Findings_and_Limits D5).

## Purpose

The policy governing when a lattice insight may trigger a skill, what
confirmation is required, and what must never happen. This is the operational
heart of Phase 4: it turns the lattice from an interpretive layer into a
steering mechanism that respects the empowerment boundary.

## 1. Trigger Prerequisites (universal)

No insight triggers any skill unless ALL hold:

1. `user_verdict != pending` — the user has confirmed, revised, or explicitly
   left the insight active. `rejected` blocks forever (absolute quarantine).
2. `quarantine_status == active` or `cleared` — Q2 identity-level claims
   require `cleared` via explicit user confirmation.
3. `evidence_sufficiency >= partial` — insufficient insights may inform
   conversation but never select a skill.
4. The skill's `boundary_gate` check has passed for the task's meaning level
   (HEB gate, Phase 4 decision 7).
5. `manipulation_risk` and `surveillance_risk` are both `low` — else the
   insight is quarantined for governance review.

## 2. Per-Trigger Thresholds

### T1: TDF_Barrier_Facilitator_Grid / COMB_Behavioral_Diagnosis

- **Signal:** C-Ps knowledge/skill gap pattern across >= 2 observations
  (RECONSTRUCTED threshold; grounded in COM-B classifier design).
- **Confidence:** insight `confidence >= medium` AND `evidence_sufficiency >= partial`.
- **Gate:** user_verdict = confirmed.
- **Action:** refine component profile into 14-domain grid; output is
  hypothesis-status, user-correctable.

### T2: SDT_Need_Support_Check

- **Signal:** regulatory-style pattern (introjected vs identified vs
  intrinsic) in user language (Li 2025 VERIFIED; Lim 2025 VERIFIED).
- **Confidence:** `confidence >= low` (style classification is coder-level
  inference; RECONSTRUCTED labeling mandatory).
- **Gate:** labeled inference, user-correctable; no guilt/shame levers.
- **Action:** need-support audit of agent utterances; anti-introjection
  guardrails active.

### T3: MI_Ambivalence_Conversation

- **Signal:** change-talk / sustain-talk / ambivalence pattern (DARN-CAT
  signals; Lim 2025 HMM transition dynamics VERIFIED).
- **Confidence:** `confidence >= low` for engagement; `>= medium` for
  evocation targeting.
- **Gate:** observations enter conversation ONLY via evocation — never as
  accusation ("you said X last week" is prohibited; "what changed since
  then?" is allowed).
- **Action:** ambivalence conversation; commitment-slope tracking.

### T4: Proximal_Practice_Selector

- **Signal:** atrophy/dependency risk — rising assistance fraction, falling
  unassisted performance (Bastani 2025 VERIFIED; Budzyń 2025 VERIFIED).
- **Confidence:** objective telemetry over self-report (self-report is
  unreliable per Lee 2025 VERIFIED; Bastani perception data VERIFIED).
- **Gate:** skill_load_score trend (PPS computes; HEB derives trend) —
  falling trend triggers; single-point dips do not.
- **Action:** minimal-sufficiency redesign (hints > answers), scaffolding
  fade, readiness-gated timing.

### T5: Human_Empowerment_Boundary

- **Signal:** identity-level claim (identity_level_flag = true), values,
  commitments, interpretive closure, high-branching decisions.
- **Confidence:** n/a — trigger is structural, not confidence-based.
- **Gate:** Q2 quarantine; explicit user confirmation MANDATORY before any use.
- **Action:** ACT/SCAFFOLD/ASK/DEFER/STOP mode selection; preserved_user_decision output.

### T6 (deferred): Material_Arrangement_Scan / Feedback_Ecology_Map

- **Signal:** practice-element (materials/competences/meanings) or
  embedding-work patterns.
- **Status:** edges quarantined in skill_graph_index.json until packages are built.

## 3. Prediction-Ceiling Constraints (Contrary_Findings D5, now wired)

The Phase-2 evidence critic demanded that prediction ceilings constrain
autonomous action. This policy does it:

| Signal | Ceiling (VERIFIED) | Constraint |
|---|---|---|
| Next-action prediction | 17.1-26% alignment (Shaikh 2026) | May inform TIMING only; never license autonomous action |
| Automatic MI coding | 52.6% accuracy (Han 2026) | Fidelity claims require human review at medium+ stakes |
| Proactive agent success | 26-40% (ProEvent, PROBE) | Agent must default to silence/restraint; over-action is a failure mode |
| Motivation-state inference | 0.80 LOOCV session quality (Lim 2025) | Strong for session-level pattern; weak for single-utterance claims |

## 4. Prohibitions (absolute)

1. **No manipulation.** Insights never steer the user toward agent-chosen
   outcomes.
2. **No surveillance.** Lattice observations never become monitoring;
   surveillance_risk = high blocks the observation.
3. **No identity closure without consent.** Identity-level insights are
   quarantined (Q2) until explicit user confirmation.
4. **No reward mechanics on intrinsic motivation.** Performance-contingent
   tangible rewards prohibited (Deci 1999 VERIFIED undermining effect).
5. **No MI without spirit.** Technical evocation without partnership is
   prohibited (Kuchipudi 1990 VERIFIED).
6. **No argument against resistance.** Sustain talk is explored, never fought.
7. **No autonomous action on low-confidence signals.** Prediction ceilings
   gate autonomy (section 3).
8. **No premature closure.** Ambivalence, open questions, and unresolved
   selectors are designed halt states, not defects (Valens corpus law).

## 5. Escalation and Recovery

- If a triggered skill stalls, loops, overreaches, or misreads:
  - MI discord → recovers_with SDT_Need_Support_Check (autonomy-support repair).
  - Sparring overreach → recovers_with Human_Empowerment_Boundary (boundary reset).
  - Diagnosis overreach/premature closure → recovers_with Human_Empowerment_Boundary.
  - Identity overreach/paternalism → recovers_with Human_Empowerment_Boundary.
- Recovery ops per package (kind=internal recovers_with edges) handle
  in-skill failures: Downgrade_To_Scaffold, Return_To_User_Authority,
  Reopen_User_Choice, Mark_As_Provisional, etc.

## 6. Governance and Review

- Policy owner: Human_Empowerment_Boundary (governance skill).
- Review cadence: with the Open Questions Register (Q6-Q11) monthly review.
- Threshold revisions: only with new evidence (VERIFIED) — thresholds are
  calibration anchors, not study-validated norms (Phase-2 critique, evidence
  critic items 4/7).
- The campaign's own self-application: the same policy governs how the
  campaign uses insights about Dallas (Q10 — skill_load self-tracking).
