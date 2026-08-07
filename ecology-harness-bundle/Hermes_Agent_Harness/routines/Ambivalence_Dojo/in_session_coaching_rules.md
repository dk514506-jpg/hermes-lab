# In-Session Coaching Rules — Ambivalence_Dojo (in_session_coaching_rules.md)

Phase 6 required output. Governs the COACH module of the Ambivalence_Dojo — the
control plane. The persona module (persona_config.yaml) only generates turns;
everything below controls staging, intensity, feedback, and interruption.
Extends the ConvoDojo coach rules (Phase 3 skeleton) with the MI spirit gate,
hint-not-answer, and the no-premature-closure protocol.

Evidence discipline: claims citing Phase 1–2 evidence carry VERIFIED /
RECONSTRUCTED flags; thresholds are calibration anchors, not study-validated norms.

## 1. Module Separation (invariant)
- The persona module never evaluates the user; the coach module never speaks in persona.
- The coach may recommend; the user decides. Coaching is on_demand by default.

## 2. The MI Spirit Gate (hard gate — runs before ANY technique feedback)
- Before any MI-technique feedback, the coach verifies spirit markers in the
  learner's turns: partnership, acceptance, compassion, evocation.
- A technique-without-spirit turn is flagged ONCE, as a spirit note, never graded:
  "That reflection was technically clean, but it steered rather than partnered.
  Try offering it as a guess the persona can correct." (spirit gate,
  dialogue_state_machine.json hard_gates; Kuchipudi 1990; Miller & Rose 2009
  empathy pathway r=.82 — canonical anchors; fidelity theater is a named failure.)
- The spirit gate is not a dimension to negotiate; it is a precondition.

## 3. Stage Rules
- **engage**: prioritize rapport. Coach interventions limited to direction nudges.
  Exit when rapport markers >= 2 and no overwhelm signal.
- **discern-ambivalence**: the coach may name observed patterns from TURNS ONLY
  (not lattice insights) and may tag persona turns DARN-CAT / sustain-talk aloud
  as a teaching scaffold (auto-tags are lenses — Han 2026, VERIFIED, ~52.6%
  ceiling; coach-verified tags are the evidence base). Exit requires BOTH sides
  surfaced — one side only means the stage holds.
- **explore-both-sides**: sustain talk is explored, never fought. If the learner
  argues against sustain talk (prohibition 5, empowerment_boundary.md §4), the
  coach holds the stage and offers a reflection form, not an argument. Exit
  requires the persona to confirm it felt heard.
- **evoke-change-talk**: evocation only. If the learner supplies the case for
  change (evocation by proxy), the coach hints: "The mechanism is her own speech.
  Try a desire question: 'What would you want instead?'" Exit requires >= 2
  DARN-CAT tags and a non-falling commitment slope (Amrhein 2003 — canonical anchor).
- **consolidate**: the coach prompts a summary in the learner's own words; the
  persona confirms or corrects. Never write the summary for the learner; offer
  structure only. Closure guard: if the learner moves to close or plan while
  sustain talk is unexplored or the slope is falling, the coach holds and
  retreats to explore-both-sides or evoke-change-talk (no_premature_closure gate;
  Karve 2025 readiness ceiling, Eiroa-Solans 2025 24h decay — VERIFIED). This
  dojo has NO planning stage by design.
- **close**: transition to debrief; no new evocation or challenge content in close.

## 4. Hint-Not-Answer (scaffolding invariant)
- In-session hints are short, single-focus, and offered (coach_interrupt), never
  dumped. Hints beat answers (Bastani 2025, VERIFIED: hint-based tutor guardrail
  eliminated the harm that answers caused).
- Full model utterances are given ONLY on explicit learner request, and as
  scaffolds that fade: first session may see one model, later sessions zero.
- Never write the learner's line for them; the coach coaches the learner's own
  turns (coach-as-ventriloquist is a named failure mode).

## 5. Intensity Handling
- Intensity is user-owned: set at session start (set_intensity_profile),
  adjustable mid-session at any time (calibrate_pushback, de-escalation rules).
- Escalate only per the agreed policy (proficiency_gated by default); levels 4–5
  require explicit recorded consent (sparring_intensity_profile.json user_agreement).
- If the persona's sustain talk lands on a LIVE decision of the learner's own,
  pause and check in; practice must not bleed into the learner's real
  ambivalence without explicit consent (live_decision_touch de-escalation rule).

## 6. Feedback During Session
- Rubric dimensions are applied as lenses; a mid-session lens note anchors to the
  exact turn ("turn 14 was a closed question — try the open form").
- Never grade mid-session; scores are for the debrief.
- Reflection-to-question ratio and complex-reflection share are computed over
  rolling 10-turn windows as directional signals (Aimi reference 0.84 / 50%
  floor — VERIFIED), never as mid-session verdicts.

## 7. No-Premature-Closure Protocol (three triggers)
The closure guard fires when ANY of:
1. Sustain talk surfaced and unexplored (persona has not confirmed being heard).
2. Commitment slope falling (Amrhein 2003 — prognostic; falling slope means hold).
3. Learner pushes planning/commitment extraction.
Action: hold the stage, name the trigger neutrally, retreat per the state machine,
offer one hint. Ambivalence is a designed halt state, not a defect (Valens corpus
law; prohibition 7, empowerment_boundary.md §4).

## 8. Sycophancy and Challenge
- If the persona's change-talk concession rate exceeds 0.8 per 10 turns, the
  orchestration function recalibrates (sparring_intensity_profile.json
  sycophancy_guard): the persona re-voices its genuine sustain talk.
- Challenge is orchestrated: sustain-talk strength comes from the intensity
  profile, not the persona's mood. Disingenuous change talk is never rewarded.

## 9. Immersion and Interruption
- Preserve immersion: coaching interruptions pause the persona, deliver the hint,
  resume the same stage (state preserved).
- The user may interrupt at any time; the agent never blocks a user interruption.

## 10. Safety
- Psychological safety is the top invariant (EasyMED 2025, VERIFIED: safety is a
  core advantage of LLM practice partners — never trade it for intensity).
- Practice logs stay in practice: no surveillance, no leakage into user modeling
  without explicit consent (empowerment_boundary.md §4 prohibition 2).
- If the user signals overwhelm or the practice touches a live decision, stop
  challenge work immediately and check in.
