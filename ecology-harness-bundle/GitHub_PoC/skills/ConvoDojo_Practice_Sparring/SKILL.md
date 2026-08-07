# ConvoDojo Practice Sparring

## Purpose
This skill builds structured practice environments for conversational skills (MI,
coaching, conflict, workplace communication, ambivalence work) in which a simulated
interlocutor (persona module) is strictly separated from the feedback/coach module.
Conversations are staged explicitly, feedback is rubric-grounded as a lens rather than a
verdict, pushback is calibrated through an intensity profile (productive challenge is an
orchestration function, not a free-form personality trait), and sessions debrief with
evidence-grounded feedback. Before a trained pattern is deployed into real use, it is
adversarially stress-tested (multi-agent judging, r=0.82 human-aligned). Transfer
scenarios test generalization beyond the practiced context.

Grounded in: EasyMED 2025 (persona/case module separated from response generation;
learning outcomes comparable to human standardized patients, stronger early gains for
novices, better psychological safety); AgentForge 2026 / Voigt 2025 (trainee roles
separated from feedback/tutor roles; visible coordination demands = most effective
learning); 2026 multi-agent adversarial stress testing (cumulative degradation under
pressure; judge aligns with humans r=0.82); Aimi/Shenoi 2026 (structured-workflow coach,
reflection-to-question ratio and complex-reflection fidelity targets); Han 2026
(automatic MI coding ~52.6% accuracy — automated rubric scoring is a lens, not gospel);
Rudolph 2025 (LLM clients elicit measurably different counseling patterns than humans —
authenticity gap acknowledged); Ma 2025 (persona priming can degrade performance below
chance and embed demographic bias — persona bank sanitization required).

## Trigger Conditions
Use this skill when any of the following are true:
- The user wants to practice a conversation skill before using it in a real setting
  (job talk, difficult conversation, MI session, coaching session, negotiation).
- A conversational pattern is being prepared for deployment and needs rehearsal and
  stress testing first.
- The user asks for feedback on their conversational performance and wants it grounded
  in evidence (utterance-level), not vibes.
- The user needs calibrated resistance — a sparring partner that pushes back — rather
  than agreement.
- The agent is about to role-play and needs to separate the persona from the coach.
- A skill package (e.g., MI_Ambivalence_Conversation) needs a practice track.

## Inputs
Required inputs:
- practice_target: the conversational skill to rehearse (e.g., MI evoking, coaching
  inquiry, conflict de-escalation, negotiation framing).
- scenario_id: selected scenario from the scenario bank (or custom).
- persona_config: persona profile from the sanitized persona bank (or custom).
- intensity_profile: agreed pushback level (1–5) and escalation policy.
- rubric_id: the rubric to use as the feedback lens (rubric.json).

Optional inputs:
- session_history: prior practice sessions for continuity.
- transfer_mode: whether this session is a transfer scenario (generalization test).
- stress_test_flag: whether this is a pre-deployment adversarial stress test.
- user_state_flags: overwhelm/readiness signals that should reduce intensity
  (from in-session coaching rules or the empowerment boundary).
- skill_context: the parent skill whose practice this is (e.g., MI_Ambivalence_Conversation).

## Outputs
Primary outputs:
- session_log: staged dialogue transcript with turn-level annotations.
- stage_transitions: record of dialogue state machine transitions.
- rubric_feedback: rubric-grounded feedback (lens-form, with evidence quotes).
- coaching_interventions: coach module interruptions and their triggers.
- debrief_report: evidence-grounded debrief (debrief_template.md).
- transfer_results: generalization results for transfer scenarios.
- deployment_readiness: stress-test outcome (pending / passed / failed) for real use.

Secondary outputs:
- sycophancy_risk_notes: where the sparring partner agreed too easily.
- intensity_calibration_notes: how pushback was adjusted mid-session.
- practice_log: learner-side observations (never surveillance — see Guardrails).
- next_scenario_candidates: suggested next practice or transfer scenario.

## State Variables
- stage: current dialogue state machine stage (e.g., engage / explore / challenge / consolidate / close)
- stage_history: list of visited stages
- immersion_level: low / medium / high
- intensity_level: 1 / 2 / 3 / 4 / 5
- coaching_mode: off / on / on_demand
- persona_active: persona id
- sycophancy_risk: low / medium / high
- rubric_scores: map of rubric dimension → evidence-anchored score
- session_complete: true / false
- stress_test_status: pending / passed / failed
- transfer_flag: true / false
- psychological_safety: low / medium / high

## Atomic Operations
- select_scenario — Choose a scenario from the bank matched to practice_target.
- configure_persona — Configure the simulated interlocutor from the sanitized persona bank
  (persona module; never the coach).
- set_intensity_profile — Set pushback level (1–5) and escalation policy with user agreement.
- open_stage — Open a dialogue state machine stage.
- advance_stage — Transition the dialogue state machine on completion conditions.
- generate_interlocutor_turn — Produce the persona's next utterance, grounded in
  persona_config and stage (generation module, separated from control).
- coach_interrupt — User-controlled coaching interruption; preserves immersion, allows
  in-session hints (on-demand coaching).
- apply_rubric_lens — Score the user's turns against the rubric dimensions, anchored to
  utterance-level evidence (lens, not verdict).
- calibrate_pushback — Escalate or de-escalate challenge according to the intensity
  profile and user state.
- run_adversarial_stress_test — Multi-agent adversarial testing (cumulative pressure,
  edge-case personas) with r=0.82-aligned judging before deployment.
- debrief_session — Produce the evidence-grounded debrief from rubric scores and turn
  evidence (debrief_template.md).
- run_transfer_scenario — Run a scenario that changes context to test generalization.
- check_psychological_safety — Monitor sycophancy_risk and psychological_safety state;
  intervene if the practice environment becomes unsafe or sycophantic.

## Typed Edges
#### decomposes_to
select_scenario, configure_persona, set_intensity_profile, open_stage, advance_stage,
generate_interlocutor_turn, coach_interrupt, apply_rubric_lens, calibrate_pushback,
run_adversarial_stress_test, debrief_session, run_transfer_scenario, check_psychological_safety
#### can_follow
MI_Ambivalence_Conversation, SDT_Need_Support_Check, Human_Empowerment_Boundary,
Motivational_Lattice_Generator
#### compatible_with
Motivational_Lattice_Generator, Proximal_Practice_Selector, Human_Empowerment_Boundary
#### supports
MI_Ambivalence_Conversation, Proximal_Practice_Selector
#### recovers_with
Human_Empowerment_Boundary, Downgrade_To_Scaffold, Reduce_Intensity,
Return_To_User_Authority, Reframe_Rubric_As_Lens, Switch_Persona

## Empowerment Boundary
The agent may do automatically:
- run the persona; stage the dialogue; propose rubric lenses; produce evidence-grounded
  debriefs; calibrate pushback within the agreed intensity profile; run stress tests;
  suggest next scenarios.

The agent must preserve for the user:
- whether and how much to practice; the intensity they are willing to take;
- interpretation of their own performance (rubric feedback is offered, not imposed);
- what to practice next; when to stop;
- all decisions and commitments in the real conversation this practice prepares them for;
- whether coaching interruptions happen (user-controlled).

Practice logs are the user's learning material, not the agent's surveillance data.
The persona never embodies lattice insights about the user (the sparring partner does
not "know" the user's weak points).

## Learnability / Skill-Atrophy Check
Before acting, ask:
- Does this practice improve the user's future unassisted conversational capability
  (EasyMED: comparable to human standardized patients — practice is a capability builder)?
- Is the coach doing the talking for the user, or coaching the user's own turns?
- Does the intensity profile match the user's proximal development zone (challenge
  without overwhelm)?
- Will the user know which parts of the feedback are evidence-anchored vs. general advice?
- Can scaffolding fade — does the coach hint less and require more over sessions?
- Do transfer scenarios verify that the skill generalizes beyond the practiced scenario?

## Motivational-Lattice Interface
Lattice insights may inform scenario selection and intensity calibration ONLY with user
consent and provisional marking. The simulated persona must never be scripted from
lattice insights about the user (Ma 2025 persona-priming degradation; also a
manipulation guard — the sparring partner is not a covert diagnostic instrument).
Feedback uses observable turn evidence, not inferred motives; where a lattice insight
could explain a pattern, it is offered as a hypothesis the user may confirm or reject.

## Conversational / Practice Mode
This skill IS the practice mode. Operating rules:
- Separate generation from control: the persona module generates turns; the coach
  module (in-session coaching rules) controls staging, intensity, and feedback.
- Productive challenge is an orchestration function (intensity profile + calibration
  rules), never a free-form personality trait of the persona.
- Stage conversations explicitly; each stage has entry/exit conditions
  (dialogue_state_machine.json).
- Use rubrics as lenses, not verdicts; rubric scores always anchor to quotes.
- Preserve immersion but allow user-controlled coaching interruptions.
- Debrief with evidence-grounded feedback; include transfer scenarios to test generalization.

## Guardrails
- Do not let the sparring partner sycophantically agree (anti-sycophancy is an
  orchestration invariant, not a style choice).
- Do not exceed the agreed intensity profile; watch overwhelm signals and de-escalate.
- Do not use rubric scores as verdicts about the user as a person.
- Do not convert practice logs into surveillance; practice data stays in practice.
- Do not embed demographic bias or degrading priming in personas (Ma 2025) — persona
  bank is sanitized and audited.
- Do not claim persona authenticity beyond the evidence (Rudolph 2025: LLM clients
  differ measurably from humans) — the persona is a practice tool, not a human.
- Do not treat automated rubric scores (Han 2026: ~52.6% auto-coding accuracy) as final;
  they are lenses requiring evidence anchoring.
- Do not deploy a trained pattern without an adversarial stress test when the real
  conversation is high-stakes.
- Do not let stress tests become judgments on the user; they gate patterns, not people.
- Do not script the persona from lattice insights about the user.

## Failure Modes
- Sycophantic sparring: the partner agrees, so the user never faces calibrated resistance.
- Over-aggressive sparring: intensity exceeds tolerance; psychological safety collapses
  (EasyMED's safety advantage lost).
- Persona bias: primed personas degrade performance or embed demographic stereotypes.
- Rubric-as-verdict: scores become judgments instead of lenses.
- Immersion collapse: coaching interrupts so often the practice is not immersive.
- Surveillance creep: practice logs leak into user modeling without consent.
- Transfer failure: practiced skill does not generalize (rubric looks good, transfer fails).
- Intensity mis-calibration: challenge set from the agent's guess, not the user's state.
- Deployment without stress test: high-stakes patterns go live unrehearsed.
- Coach as ventriloquist: the coach writes the user's lines instead of coaching them.

## Recovery Operations
- Reduce_Intensity: drop pushback level and restore autonomy (overwhelm recovery).
- Switch_Persona: replace a persona that is biasing or degrading the session.
- Reframe_Rubric_As_Lens: convert a verdict-flavored report into evidence-anchored lenses.
- Reopen_Debrief: revisit the debrief with the user when feedback was misread or missed.
- Restage_Scenario: restart a stage with different conditions when the session loops.
- Return_To_User_Authority (via Human_Empowerment_Boundary): sparring overreach resets
  through the boundary — name the choice that should remain with the user.
- Pause_And_Check_In: stop the session and check the user's state when immersion or
  intensity is wrong.
- Debrief_Overreach: record where the sparring overstepped, for calibration.

## Examples
See examples.md.

## Handoff Notes
Place this folder at:
skills/ConvoDojo_Practice_Sparring/ (harness)
Session logs and debriefs belong in the harness `logs/` folder (per logs/log_schema.md — dojo_session events). Persona bank and
scenario bank live beside this package (persona_config.yaml, transfer_scenario_set.md).
Dallas must save or upload generated files into OneDrive/SharePoint; Pip can generate
files locally.
