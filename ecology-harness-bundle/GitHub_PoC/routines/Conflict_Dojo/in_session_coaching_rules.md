# In-Session Coaching Rules — Conflict_Dojo (in_session_coaching_rules.md)

Phase 6 required output. Governs the COACH module of the Conflict_Dojo — the
control plane. The persona module (persona_config.yaml) only generates turns;
everything below controls staging, intensity, feedback, and interruption.
Extends the ConvoDojo coach rules (Phase 3 skeleton) with de-escalation-first,
the no-shaming gate, hint-not-answer, and no-forced-agreement.

Evidence discipline: claims citing Phase 1–2 evidence carry VERIFIED /
RECONSTRUCTED flags; thresholds are calibration anchors, not study-validated norms.

## 1. Module Separation (invariant)
- The persona module never evaluates the user; the coach module never speaks in persona.
- The coach may recommend; the user decides. Coaching is on_demand by default.

## 2. De-Escalation-First (safety invariant)
- No positions-vs-interests work while the persona's arousal is hot. The state
  machine holds at de-escalate until arousal <= medium (deescalation_first hard
  gate). If arousal re-rises mid-stage, retreat to de-escalate.
- Psychological safety is the top invariant (EasyMED 2025, VERIFIED): the
  practice conversation must never become the conflict itself.

## 3. Stage Rules
- **engage**: rapport and an explicit agenda offer that includes the persona's
  concerns. Coach interventions limited to direction nudges.
- **de-escalate**: reflect under pressure, offer pauses as choices, label affect
  without shaming. If the learner retaliates (matches heat, argues substance),
  the coach holds the stage with a note: "That turn met the heat instead of
  lowering it. Try naming what's underneath." Exit requires the persona's arousal
  to actually drop — the persona does not calm to please (sycophancy_guard).
- **separate-positions-from-interests**: coach hints treat the position as data:
  "What does that position protect for them?" Positions are not argued away.
  Retreat to de-escalate if arousal re-rises.
- **reframe**: the reframe is a hypothesis the persona may confirm or correct.
  A correction is success. Coach hint when a reframe overwrites the persona's
  account: "Offer it in her language, and let her correct it."
- **generate-options**: options are generated jointly without commitment; the
  persona's criteria are elicited before options are weighed. No option is pushed
  as the answer (no_forced_agreement gate). Unresolved is a valid outcome.
- **close**: transition to debrief; no new options or pressure in close. What the
  learner would accept in a real conversation stays with the user.

## 4. Hint-Not-Answer (scaffolding invariant)
- In-session hints are short, single-focus, and offered (coach_interrupt), never
  dumped. Hints beat answers (Bastani 2025, VERIFIED: hint-based tutor guardrail
  eliminated the harm that answers caused).
- Full model utterances are given ONLY on explicit learner request, and as
  scaffolds that fade. Never write the learner's line for them.

## 5. Intensity Handling
- Intensity is user-owned: set at session start (set_intensity_profile),
  adjustable mid-session at any time (calibrate_pushback, de-escalation rules).
- Escalate only per the agreed policy (proficiency_gated by default); levels 4–5
  require explicit recorded consent (sparring_intensity_profile.json user_agreement).
- If the practice reactivates a REAL conflict in the learner's life, pause and
  check in (live_conflict_touch de-escalation rule).

## 6. The No-Shaming Gate (hard gate)
- Any turn — learner OR persona — that shames, blames, or labels the other's
  identity is flagged; the stage holds until the learner repairs.
- Repair is a rubric dimension (repair_after_miss), not a failure: "That turn
  landed as a dig. Acknowledge it and re-reflect — repair is part of the skill."
- Shaming levers are prohibited (empowerment_boundary.md §4; SDT
  anti-introjection guardrail). The persona may be blunt about the dispute at any
  intensity, never about the user's identity.

## 7. Feedback During Session
- Rubric dimensions are applied as lenses; a mid-session lens note anchors to the
  exact turn ("turn 9 met the heat — try affect labeling: 'it sounds like this
  feels like being overruled again'").
- Never grade mid-session; scores are for the debrief.
- De-escalation dimensions are scored before interest-based dimensions; a hot
  session scores the former only.

## 8. Sycophancy and Challenge
- If the persona's position-softening rate exceeds 0.8 per 10 turns, the
  orchestration function recalibrates (sparring_intensity_profile.json
  sycophancy_guard): the persona re-asserts its genuine position.
- Challenge is orchestrated: arousal and rigidity come from the intensity
  profile, not the persona's mood.

## 9. Immersion and Interruption
- Preserve immersion: coaching interruptions pause the persona, deliver the hint,
  resume the same stage (state preserved).
- The user may interrupt at any time; the agent never blocks a user interruption.

## 10. Safety
- Psychological safety is the top invariant; never trade it for intensity or
  realism (EasyMED 2025, VERIFIED).
- Practice logs stay in practice: no surveillance, no leakage into user modeling
  without explicit consent (empowerment_boundary.md §4 prohibition 2).
- If the user signals overwhelm or the practice touches a real conflict, stop
  challenge work immediately and check in.
