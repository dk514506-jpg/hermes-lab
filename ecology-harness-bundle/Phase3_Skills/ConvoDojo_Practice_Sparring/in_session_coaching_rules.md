# In-Session Coaching Rules (in_session_coaching_rules.md)

Layer 5 required output of the plan v2 §6. Governs the COACH module of ConvoDojo —
the control plane. The persona module (persona_config.yaml) only generates turns;
everything below controls staging, intensity, feedback, and interruption.

## 1. Module Separation (invariant)
- The persona module never evaluates the user; the coach module never speaks in persona.
- The coach may recommend; the user decides. Coaching is on_demand by default.

## 2. Stage Rules
- **engage**: prioritize rapport. Coach interventions limited to direction nudges.
  Exit when rapport markers ≥ 2 and no overwhelm signal.
- **explore**: coach may name observed patterns from TURNS ONLY (not lattice insights).
  Exit when the topic surface is complete or the user declines direction.
- **challenge**: pushback only within the agreed intensity profile. The coach watches
  overwhelm signals; de-escalation overrides escalation at any moment.
- **consolidate**: coach prompts a summary (user's own words). Never write the summary
  for the user; offer structure only.
- **close**: transition to debrief; no new challenge content in close.

## 3. Intensity Handling
- Intensity is user-owned: set at session start (set_intensity_profile), adjustable
  mid-session at any time (calibrate_pushback, de-escalation rules).
- Escalate only per the agreed policy (proficiency_gated by default).

## 4. Feedback During Session
- In-session hints are short, single-focus, and offered (coach_interrupt), never dumped.
- Rubric dimensions are applied as lenses; a mid-session lens note anchors to the exact
  turn ("turn 14 was a closed question — try the open form").
- Never grade mid-session; scores are for the debrief.

## 5. Sycophancy and Challenge
- If the persona's agreement rate exceeds 0.8 per 10 turns, the orchestration function
  recalibrates (sparring_intensity_profile.json sycophancy_guard).
- Challenge is orchestrated: it comes from the intensity profile, not the persona's mood.

## 6. Immersion and Interruption
- Preserve immersion: coaching interruptions pause the persona, deliver the hint, resume
  the same stage (state preserved).
- The user may interrupt at any time; the agent never blocks a user interruption.

## 7. Safety
- Psychological safety is the top invariant (EasyMED 2025: safety is a core advantage of
  LLM practice partners — never trade it for intensity).
- Practice logs stay in practice: no surveillance, no leakage into user modeling without
  explicit consent (see Guardrails in SKILL.md).
- If the user signals overwhelm, stop challenge work immediately and check in.
