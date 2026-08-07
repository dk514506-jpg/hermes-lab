# Trigger Walkthrough — Working Example

This narrative shows how a lattice insight does (and does not) trigger a skill,
per `lattices/insight_trigger_policy.md`. It accompanies
`observation_example.json`, `insight_example.json`, and
`evidence_edge_example.json` in this directory.

## Setup

A dojo session produced observation O-001 ("I keep starting exercise programs
and quitting after three weeks"). MLG ops formed insight H-001 (desire/ability
gap → M-Au automatic-motivation hypothesis) with two evidence edges (E-001,
E-002), `evidence_sufficiency: partial`, `confidence: medium`,
`identity_level_flag: false`.

## Universal prerequisites (policy §1) — checked first

1. `user_verdict != pending` — **FAILS**: H-001 is `pending`. No skill may
   consume this insight yet. The user must confirm, revise, or reject it
   (MLG `present_lattice_for_review` → `record_user_verdict`).
2. `quarantine_status == active or cleared` — PASS (active; not identity-level,
   so Q2 does not apply).
3. `evidence_sufficiency >= partial` — PASS (partial).
4. Boundary gate passed — PASS (this is a low-meaning exercise-habit
   hypothesis, not identity/values/commitment).
5. `manipulation_risk` and `surveillance_risk` both low — PASS.

**Because prerequisite 1 fails, no skill triggers.** The insight stays a
hypothesis until the user settles it. This is the system working as designed:
insights are hypotheses, never facts.

## After the user confirms H-001 (user_verdict = confirmed)

Now re-check the trigger matrix (policy §2):

- **T4 Proximal_Practice_Selector** — the candidate trigger. Signal:
  atrophy/dependency risk (rising assistance fraction, falling unassisted
  performance). H-001 is about *exercise habit formation*, not *skill
  atrophy from AI assistance*. The M-Au pattern is a COM-B component signal,
  not an atrophy signal. **No trigger.**
- **T1 COMB_Behavioral_Diagnosis / TDF_Barrier_Facilitator_Grid** — signal:
  C-Ps knowledge/skill gap. H-001 points at M-Au (automatic motivation), not
  C-Ps. The pattern is a motivational-quality signal, not a capability gap.
  **No trigger** (confidence medium + partial evidence would satisfy the
  thresholds, but the *signal type* does not match T1).
- **T2 SDT_Need_Support_Check** — signal: regulatory-style pattern
  (introjected vs identified vs intrinsic). The repeated start-quit cycle
  with expressed desire ("want to want it") is consistent with an
  introjected-identified tension — the learner *should* want this (introject)
  but the autonomous want is weaker. **Candidate trigger** — but
  confirmation gate requires "labeled inference, user-correctable," so the
  regulatory-style classification is presented as a labeled hypothesis, never
  a verdict, and only after the user confirms H-001.
- **T3 MI_Ambivalence_Conversation** — signal: change-talk/sustain-talk
  pattern. O-001 contains sustain-talk themes (past failure, self-doubt:
  "something in me doesn't"). If the user confirms H-001, the dojo log's
  change-talk signals may trigger insight formation per T3 — and any
  conversation uses them **only via evocation**, never as accusation
  ("you said you keep quitting" is prohibited; "what changed since last
  time?" is allowed).

## What actually happens (correct behavior)

1. H-001 is presented for review; user confirms it.
2. T2 fires as a *candidate*: SDT_Need_Support_Check audits whether the
   agent's own interactions support autonomy (avoiding introjection levers,
   guilt, or shame).
3. T3's evocation rule governs how the sustain-talk content may enter
   conversation.
4. All of it is recorded in `logs/` (boundary_gate_outcome,
   calibration_event) — observations, never surveillance.

## Why the walkthrough matters

This is the "closed loop, never closed circle" in miniature: observation →
hypothesis → confirmation gate → (conditional) trigger → evocation-bound
conversation → logs → new observations. Every step is user-arbitrated; no
insight steers without consent.
