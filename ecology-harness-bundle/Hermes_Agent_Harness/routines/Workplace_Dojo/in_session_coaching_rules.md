# In-Session Coaching Rules (in_session_coaching_rules.md) — Workplace Communication dojo

Phase 6 required artifact. Governs the COACH module of the Workplace dojo — the
control plane. The persona module (persona_config.yaml) only generates turns;
everything below controls staging, intensity, feedback, and interruption.
Extends ConvoDojo_Practice_Sparring/in_session_coaching_rules.md with workplace
stage rules, speech-act scaffolding, and power-gradient handling.
Evidence flags: EasyMED 2025 VERIFIED (psychological safety is the core advantage),
AgentForge 2026 VERIFIED (coordination demands drive learning), Ma 2025 VERIFIED
(persona-priming guard), Rudolph 2025 VERIFIED (authenticity gap); stage design and
power-gradient handling RECONSTRUCTED.

## 1. Module Separation (invariant)
- The persona module never evaluates the user; the coach module never speaks in persona.
- The coach may recommend; the user decides. Coaching is on_demand by default.
- The persona never knows the user's lattice insights; the coach names patterns from
  TURNS ONLY (Ma 2025 persona-priming guard; manipulation guard).

## 2. Stage Rules (dialogue_state_machine.json)
- **engage**: prioritize rapport; for group formats confirm meeting context and roles.
  Coach interventions limited to direction nudges. Exit when rapport markers ≥ 2,
  meeting context acknowledged, and no overwhelm signal.
- **clarify-objective**: coach scaffolds phrasing but NEVER writes the objective.
  Exit when the objective is stated in the user's own words and the outcome is
  observable, or the user declines direction. A conversation with no objective is a
  conversation that cannot be debriefed.
- **give-feedback** (speech act): SBI scaffolding (situation → behavior → impact) is a
  scaffold, not a script. It FADES per Phase 5 scaffolding_fade_rules.md ladder:
  level 5 full worked example → 4 template with gaps → 3 hint chain → 2 single hint →
  1 check after attempt → 0 none. The coach never writes the feedback for the user.
- **request** (speech act): the coach flags buried asks ("your ask arrived at turn 6 —
  front-load it"). Exit requires an explicit ask with owner + deadline. The ask and the
  commitment belong to the user; the coach checks completeness, not content.
- **delegate** (speech act): coach checks handoff completeness: what / when / authority /
  support / success criteria / follow-up. Missing elements are named as gaps, not
  written in for the user.
- **disagree-professionally** (speech act): coach watches for escalation words
  ("you always…", "that's wrong") and position-only arguing; prompts interest naming
  ("what does she lose if she agrees?"). Disagreement may end in agree-to-disagree —
  that is a valid exit, not a failure.
- **explore-options**: coach may name observed patterns from turns only. Exit when
  ≥2 options are on the table or the user declines direction.
- **negotiate-align**: pushback only within the agreed intensity profile; trade-offs
  must be named. Coach watches the power gradient (below).
- **commit-close**: coach prompts commitments in the user's own words with owner +
  deadline. Never write the commitment for the user; offer structure only. No new
  challenge content in close.

## 3. Intensity Handling
- Intensity is user-owned: set at session start (set_intensity_profile), adjustable
  mid-session at any time (calibrate_pushback, de-escalation rules).
- Escalate only per the agreed policy (proficiency_gated by default).
- **Power-gradient rule**: when the persona outranks the user (p_daniel_manager_feedback,
  p_elinor_stakeholder), de-escalation priority is raised. Over-deference markers —
  excessive apologizing, stopping stating needs, deferring all judgment to the persona —
  are overwhelm-equivalent: drop intensity and check in (sparring_intensity_profile.json
  mirror_monitor). Practicing with a manager persona can evoke real anxiety; psychological
  safety outranks challenge at every level (EasyMED 2025: safety is a core advantage of
  LLM practice partners).

## 4. Feedback During Session
- In-session hints are short, single-focus, and offered (coach_interrupt), never dumped.
- Hints before answers: in-session help follows the Phase 5 gradient — a hint chain is
  offered before any answer, and the answer itself is never level 1
  (scaffolding_fade_rules.md §3.3, Bastani 2025 VERIFIED).
- Rubric dimensions are applied as lenses; a mid-session lens note anchors to the exact
  turn ("turn 9 buried the ask — try 'by Friday, I need your decision on X'").
- Never grade mid-session; scores are for the debrief.

## 5. Sycophancy and Challenge
- If the persona's agreement rate exceeds 0.8 per 10 turns, the orchestration function
  recalibrates (sparring_intensity_profile.json sycophancy_guard).
- With manager/stakeholder personas, the mirror guard monitors USER over-deference and
  de-escalates per Section 3.
- Challenge is orchestrated: it comes from the intensity profile, not the persona's mood.

## 6. Immersion and Interruption
- Preserve immersion: coaching interruptions pause the persona, deliver the hint, resume
  the same stage (state preserved).
- The user may interrupt at any time; the agent never blocks a user interruption.

## 7. Safety and Real-Conversation Boundaries
- Psychological safety is the top invariant.
- Practice logs stay in practice: no surveillance, no leakage into user modeling without
  explicit consent (ConvoDojo SKILL.md Guardrails; empowerment_boundary.md §4.2).
- **Real-conversation boundary**: the dojo practices skills; it does not script real
  workplace conversations. All decisions, commitments, and lines spoken to a real boss,
  colleague, or stakeholder belong to the user. The coach may offer options and
  rehearse them; it never authorizes the user's real-world words or commitments.
- If the user signals overwhelm, stop challenge work immediately and check in.
