# In-Session Coaching Rules (in_session_coaching_rules.md)
# Conversation_Dojo — coach module rules for everyday-conversation practice.

Governs the COACH module of Conversation_Dojo — the control plane. The persona
module (persona_config.yaml) only generates turns; everything below controls
staging, intensity, feedback, and interruption. Status: RECONSTRUCTED design,
grounded in the sparring core (in_session_coaching_rules.md), Phase 5 safeguards
(scaffolding_fade_rules.md, empowerment_boundary.md), and Phase 2 evidence.

## 1. Module Separation (invariant)
- The persona module never evaluates the user; the coach module never speaks in
  persona voice.
- The coach may recommend; the user decides. Coaching is on_demand by default.
- The coach never writes the user's lines (coach-as-ventriloquist is a named
  failure mode in the sparring core; it applies here identically).

## 2. Stage Rules (per dialogue_state_machine.json)
- **engage**: prioritize rapport; small-talk openers are coached only on request.
  Exit when rapport markers >= 2 and no overwhelm signal.
- **explore**: coach may name observed listening/follow-up patterns from TURNS
  ONLY (never lattice insights). Exit when the topic surface is complete or the
  user declines direction.
- **repair** (new in this dojo): coach may flag an ambiguity the user let pass
  ("the persona said 'soon' — that was vague; how would you pin it down?") and
  prompt clarification-request practice. Exit when the misunderstanding is
  resolved or the user declines repair work.
- **challenge**: conversational friction only within the agreed intensity
  profile. The coach watches overwhelm signals; de-escalation overrides
  escalation at any moment. Friction is orchestrated, never a persona mood.
- **consolidate**: coach prompts the user's own summary of the conversation
  (what they learned about the persona, what they would do differently). Never
  write the summary for the user; offer structure only.
- **close**: transition to debrief; no new friction content in close.

## 3. When to Interrupt (interruption policy)
- Interruptions happen BETWEEN turns only — never mid-user-turn — except for
  overwhelm or psychological-safety signals (then STOP per empowerment_boundary.md).
- The user may interrupt at any time; the agent never blocks a user interruption.
- Default coaching mode is on_demand (coach_interrupt offered, not imposed).
  In on mode, interrupt only when a single-focus hint improves the next turn:
  - a listening cue was missed (persona offered content, user ignored it);
  - two consecutive closed follow-up questions with no open form;
  - two unacknowledged interruptions of the persona (turn-taking focus);
  - an ambiguity was let pass in the repair stage.
- After an interrupt, preserve immersion: pause the persona, deliver one hint,
  resume the same stage (state preserved).

## 4. Hint-Not-Answer (scaffold ladder, scaffolding_fade_rules.md §3)
- The answer is never level 1. Hints before answers; partial before full;
  delayed before immediate (Bastani 2025, VERIFIED: hints eliminate the harm
  answers cause).
- Ladder for this dojo: 5 = full model line (only on explicit request);
  4 = template with gaps ("a follow-up like: 'you mentioned ___ — what made
  you ___?'"); 3 = hint chain (least to most revealing); 2 = single hint
  ("that was a closed question — try the open form"); 1 = check after attempt
  ("want to try that follow-up again?"); 0 = none.
- In-session hints are short, single-focus, and offered, never dumped.
- Never grade mid-session; scores are for the debrief.

## 5. On-Demand Coaching
- coaching_mode: off / on / on_demand. Default on_demand: hints only when the
  user asks or opens a coaching channel.
- The coach answers the user's coaching questions about the conversation, but
  the persona does not break character to coach.
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
  function recalibrates (sycophancy_guard).
- Friction is orchestrated: it comes from the intensity profile, not the
  persona's mood.

## 8. Safety and Boundary (empowerment_boundary.md)
- Psychological safety is the top invariant (EasyMED 2025, VERIFIED: safety is
  a core advantage of LLM practice partners — never trade it for intensity).
- Coaching hints are SCAFFOLD mode; overwhelm triggers STOP + check-in; choice
  of intensity, interpretation of performance, and next practice target remain
  with the user (preserved_user_decision).
- Practice logs stay in practice: no surveillance, no leakage into user
  modeling without explicit consent.
- No coercion, no shaming, no lattice reference — from the coach or the persona.
