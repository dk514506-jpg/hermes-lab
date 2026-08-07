# In-Session Coaching Rules (in_session_coaching_rules.md)
# Coaching_Dojo — coach module rules for coaching-conversation practice.

Governs the COACH module of Coaching_Dojo — the control plane. The persona
module (persona_config.yaml, the coachee) only generates turns; everything below
controls staging, intensity, feedback, and interruption. Status: RECONSTRUCTED
design, grounded in the sparring core, Phase 5 safeguards (scaffolding_fade_rules.md,
empowerment_boundary.md), and the MI package (spirit gate, evocation-not-accusation).

## 1. Module Separation (invariant)
- The persona module never evaluates the user; the coach module never speaks in
  persona voice.
- The coach may recommend; the user decides. Coaching is on_demand by default.
- The coach never writes the user's questions for them (coach-as-ventriloquist
  is a named failure mode; here it would be the coach asking the powerful
  questions the user is practicing).

## 2. Stage Rules (per dialogue_state_machine.json, GROW-ish mapping)
- **engage (~ Goal)**: prioritize rapport; help surface the coachee's goal in
  the coachee's own words. Coach interventions limited to direction nudges.
  Exit when rapport markers >= 2, goal surface started, no overwhelm signal.
- **explore (~ Reality)**: coach may name observed listening patterns from TURNS
  ONLY (never lattice insights). Powerful-question practice happens here.
  Exit when the reality surface is complete or the user declines direction.
- **challenge (~ Options, inquiry-tension)**: the coachee presses for advice
  within the agreed intensity profile. The coach enforces advice_suppression:
  monitors the user's turns for advice-verbs (should / ought / you need to) and
  offers one inquiry redirect per occurrence ("Ronan asked what to do — what
  question would hand the answer back to him?"). The persona may ask; the user
  must not supply. De-escalation overrides escalation at any moment.
- **consolidate (~ Will)**: coach prompts the user to elicit the coachee's own
  next step; the will statement belongs to the coachee. Never assign homework
  through the persona.
- **close**: transition to debrief; no new pressure content in close.

## 3. When to Interrupt (interruption policy)
- Interruptions happen BETWEEN turns only — never mid-user-turn — except for
  overwhelm or psychological-safety signals (then STOP per empowerment_boundary.md).
- The user may interrupt at any time; the agent never blocks a user interruption.
- Default coaching mode is on_demand (coach_interrupt offered, not imposed).
  In on mode, interrupt only when a single-focus hint improves the next turn:
  - an advice-verb appeared in the user's last turn (inquiry-over-advice focus);
  - a closed or steering question closed a possibility the coachee had opened;
  - the coachee's agenda was redirected by the user;
  - a thinking pause was filled by the user (silence_tolerance focus).
- After an interrupt, preserve immersion: pause the persona, deliver one hint,
  resume the same stage (state preserved).

## 4. Hint-Not-Answer (scaffold ladder, scaffolding_fade_rules.md §3)
- The answer is never level 1. Hints before answers; partial before full;
  delayed before immediate (Bastani 2025, VERIFIED: hints eliminate the harm
  answers cause).
- Ladder for this dojo: 5 = full model question (only on explicit request);
  4 = template with gaps ("a question like: 'what would ___ make possible?'");
  3 = hint chain (least to most revealing); 2 = single hint ("that was advice —
  what question would replace it?"); 1 = check after attempt ("want to try that
  question again?"); 0 = none.
- The coach models powerful questions ONLY on request; modeled questions are
  marked as models, not as the user's turns.
- In-session hints are short, single-focus, and offered, never dumped.
- Never grade mid-session; scores are for the debrief.

## 5. On-Demand Coaching
- coaching_mode: off / on / on_demand. Default on_demand: hints only when the
  user asks or opens a coaching channel.
- The coach answers the user's questions about coaching craft, but the persona
  does not break character to coach.
- Fade is mandatory (scaffolding_fade_rules.md §1.2): across sessions, the
  coach hints less and requires more, gated on unassisted rubric evidence
  (F1/F2) plus readiness (F3) or the user's stated readiness (F4). A hint
  scaffold with no fade plan is dependency by design.

## 6. Intensity Handling
- Intensity is user-owned: set at session start, adjustable mid-session at any
  time. Escalate only per the agreed policy (proficiency_gated by default) and
  never without user agreement (sparring_intensity_profile.json
  user_agreement_requirement).

## 7. Sycophancy and Challenge
- If the persona's agreement rate exceeds 0.8 per 10 turns, the orchestration
  function recalibrates (sycophancy_guard). The coachee who agrees with every
  question teaches nothing.
- Pressure is orchestrated: it comes from the intensity profile, not the
  persona's mood.

## 8. Safety and Boundary (empowerment_boundary.md)
- Psychological safety is the top invariant (EasyMED 2025, VERIFIED: safety is
  a core advantage of LLM practice partners — never trade it for intensity).
- The MI spirit gate applies to the coaching practice: partnership, acceptance,
  compassion, evocation before technique; no argument against resistance; no
  guilt/shame levers (MI package guardrails, VERIFIED).
- Coaching hints are SCAFFOLD mode; overwhelm triggers STOP + check-in; choice
  of intensity, interpretation of performance, and next practice target remain
  with the user (preserved_user_decision).
- Practice logs stay in practice: no surveillance, no leakage into user
  modeling without explicit consent.
- No coercion, no shaming, no lattice reference — from the coach or the persona.
