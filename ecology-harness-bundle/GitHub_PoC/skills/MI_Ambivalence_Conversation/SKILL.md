## MI Ambivalence Conversation

### Purpose
This skill runs the Motivational Interviewing layer of conversation: the spirit
(partnership, acceptance, compassion, evocation), the four processes (engaging,
focusing, evoking, planning), the OARS micro-skills (Open questions, Affirmations,
Reflections, Summaries), DARN-CAT change-talk detection with commitment-slope
tracking, and runtime fidelity gates (reflection-to-question ratio toward ~0.84,
complex reflections at or above 50% — the Aimi/MISC-2 evidence targets). Its hard
gate: MI techniques without spirit are not MI (Kuchipudi 1990; Miller & Rose 2009) —
technical manipulation without partnership is prohibited outright.
The causal chain this skill serves: therapist/agent behavior → client change talk
(less sustain talk) → strengthened commitment → behavior change (Bischof 2021 OR
1.55; Amrhein 2003 commitment slope). The agent's job is to evoke the user's own
arguments for change, never to supply them.

### Trigger Conditions
Use this skill when any of the following are true:
- The user expresses ambivalence about a change ("I know I should, but…").
- The user shows sustain talk or resistance to a change under discussion.
- The agent needs to explore a behavior change without prescribing it.
- A diagnosis skill (COMB_Behavioral_Diagnosis, TDF_Barrier_Facilitator_Grid) has
  identified a motivational barrier that needs conversational work.
- A planning or practice skill needs a readiness assessment before proceeding.
- The user is stuck between reasons for and against a change.
- The user is practicing MI skills in sparring mode (ConvoDojo_Practice_Sparring).

### Inputs
Required inputs:
- task_description: What the user is asking the agent to help with.
- user_utterance_stream: Recent user speech for change-talk coding.
- current_process: engaging / focusing / evoking / planning (or "undetermined").
- user_goal_or_stated_intent: The user's explicit goal, if available.
- known_constraints: Boundaries, preferences, and policy constraints.
Optional inputs:
- motivational_insights: Provisional insights from a motivation lattice.
- engagement_state: Rapport/engagement signal from prior turns.
- focus_state: Whether direction has been agreed.
- change_talk_log: Prior DARN-CAT-tagged utterances.
- fidelity_log: Prior runtime fidelity-gate results.
- readiness_signals: Behavioral or stated readiness evidence.

### Outputs
Primary outputs:
- process_state: engaging / focusing / evoking / planning.
- change_talk_log: Utterances tagged DARN-CAT (Desire, Ability, Reasons, Need →
  Commitment, Activation, Taking steps).
- sustain_talk_log: Utterances tagged as sustain talk (to be explored, not fought).
- commitment_slope: rising / flat / falling (Amrhein 2003: slope is prognostic).
- fidelity_report: reflection-to-question ratio, complex-reflection share, gate verdict.
- readiness_verdict: not_ready / ambivalent / ready.
Secondary outputs:
- next_process: What the conversation should move to next.
- preserved_user_decision: What remains with the user.
- risk_notes: Guardrail concerns.
- next_skill_candidates: Skills that may follow.

### State Variables
- spirit_state: present / absent / degraded
- current_process: engaging / focusing / evoking / planning
- reflection_to_question_ratio: number (target ~0.84)
- complex_reflection_share: number (target >= 0.50)
- change_talk_log: array (DARN-CAT tagged)
- sustain_talk_log: array
- commitment_slope: rising / flat / falling
- readiness_verdict: not_ready / ambivalent / ready
- engagement_state: low / medium / high
- focus_state: agreed / unagreed
- fidelity_gate_passed: true / false
- preserved_user_decision: string

### Atomic Operations
- spirit_gate — Verify partnership, acceptance, compassion, evocation are present
  before any MI technique is used (hard gate: refuse technique without spirit).
- open_question — Ask an open question (≥70% of questions should be open).
- affirm — Affirm the user's effort, strengths, and autonomy.
- reflect — Produce a reflection; prefer complex reflections (≥50% target) that add
  meaning or feeling rather than parroting.
- summarize — Link themes and check understanding (periodic, not dominating).
- elicit_change_talk — Evoke the user's own desire, ability, reasons, and need
  (evocation, never argument).
- tag_change_talk — Classify user utterances into DARN-CAT and sustain-talk buckets.
- track_commitment_slope — Track the slope of commitment language over the session
  window (Amrhein 2003).
- run_fidelity_gate — Compute reflection-to-question ratio and complex-reflection
  share; compare against ~0.84 and ≥50% targets (Aimi/MISC-2).
- explore_sustain_talk — Explore resistance openly and without judgment; never argue
  against it.
- plan_when_ready — Gate planning behind readiness; no premature planning.
- record_mi_session — Write fidelity and change-talk state for later calibration.
- agree_direction: focusing-process op — negotiate and agree direction with the user; direction is user-chosen, never imposed.
- prioritize: focusing-process op — help the user order concerns and select the target; requires agreed focus.

### Typed Edges
#### decomposes_to
- spirit_gate, open_question, affirm, reflect, summarize, agree_direction, prioritize,
  elicit_change_talk, tag_change_talk, track_commitment_slope, run_fidelity_gate,
  explore_sustain_talk, plan_when_ready, record_mi_session
#### can_follow
- COMB_Behavioral_Diagnosis (ambivalence resolved -> diagnosis refines),
  SDT_Need_Support_Check (need-support audit after the conversation),
  Proximal_Practice_Selector (readiness verdict -> practice timing),
  Human_Empowerment_Boundary (boundary governance during conversation)
#### compatible_with
- Proximal_Practice_Selector, ConvoDojo_Practice_Sparring, Feedback_Ecology_Map,
  Motivational_Lattice_Generator, Post_Close_Calibration_Debrief
#### supports
- COMB_Behavioral_Diagnosis (M-Re reflective-motivation evidence from change talk)
- Proximal_Practice_Selector (readiness signal for practice timing)
#### recovers_with
- Return_To_Spirit, Explore_Resistance_Openly, Downgrade_To_Reflection,
  Defer_Planning, Reopen_Ambivalence, Debrief_Fidelity_Failure
- (discord during MI recovers via SDT_Need_Support_Check autonomy-support repair)

### Empowerment Boundary
The agent may do automatically:
- ask open questions, affirm, reflect, summarize; detect and tag change talk and
  sustain talk; track commitment slope; run runtime fidelity gates; structure the
  four processes; report readiness evidence.
The agent should preserve for the user:
- the user's own reasons and arguments for change (evocation — the agent never
  supplies the case for change); the direction to focus on; the readiness judgment;
  commitments made; the decision to change or not; the interpretation of the user's
  own ambivalence (reflections are offered as hypotheses, not verdicts).

### Learnability / Skill-Atrophy Check
Before acting, ask:
- Am I evoking the user's change talk, or substituting my own arguments? (The
  mechanism of MI is the client's own speech — supplying arguments robs the user of
  the effect.)
- Am I arguing against resistance, or exploring it? (Arguing trains the user to
  defend the status quo.)
- In practice mode, am I scaffolding the user's reflection skill (hints, models on
  request) rather than performing the conversation for them?
- Will the user leave this conversation more able to articulate their own reasons
  than they entered?
If the user is practicing MI, prefer calibrated challenge and coaching hints over
full demonstrations.

### Motivational-Lattice Interface
This skill may use lattice insights only as hypotheses to inform reflections and
evocation prompts: the reflection must be marked provisional and offered for the
user to confirm or correct ("It sounds like… is that close?"). Never use inferred
motives to make identity-level or normative claims without explicit user
confirmation. Disingenuous change talk — change language the user does not actually
own — must not be manufactured or rewarded.

### Conversational / Practice Mode
In sparring mode (ConvoDojo_Practice_Sparring), the agent plays the ambivalent
speaker while the user practices OARS and DARN-CAT detection, or the agent coaches
the user's reflections turn by turn. Rubric-grounded feedback follows MISC/MITI-style
metrics — never self-report (Miller & Mount 2001: self-reported proficiency does not
equal coded proficiency). Transfer scenarios test generalization to new
ambivalence topics. The agent's own fidelity gates run on its live conversation
utterances, not only in practice.

### Guardrails
- Hard gate: no MI technique without spirit (partnership, acceptance, compassion,
  evocation). MI without spirit is not MI.
- Never argue against resistance; sustain talk is explored, not fought.
- No planning before readiness — premature planning fails (Eiroa-Solans 2025 24h
  decay; Karve 2025 ceiling finding: readiness gates behavior change).
- Self-reported proficiency ≠ coded proficiency: rely on runtime fidelity gates.
- Do not manufacture or reward disingenuous change talk.
- No guilt/shame levers (SDT anti-introjection guardrail applies inside MI too).
- Reflections are hypotheses about the user's meaning, never verdicts.
- Do not collapse ambivalence prematurely; both sides get full airing.

### Failure Modes
- Spiritless technique: manipulation dressed as MI (the hard-gate violation).
- Interrogation: reflection-to-question ratio collapses (question storm).
- Parroting: complex-reflection share below 50% (reflections add nothing).
- Premature planning: pushing to plans while readiness is low.
- Fighting sustain talk: arguing the agent's side, training the user to defend
  the status quo.
- Fabricated change talk / sycophantic affirmation: rewarding agreement rather than
  evoking genuine reasons.
- Over-summarizing: closing the user's meaning-making for them.
- Fidelity theater: hitting numeric targets while spirit is absent — metrics without
  mechanism (relational pathway: empathy r=.82, Miller & Rose 2009).

### Recovery Operations
- Return_To_Spirit: Stop technique and restore partnership, acceptance, compassion,
  evocation.
- Explore_Resistance_Openly: Name the resistance without judgment.
- Downgrade_To_Reflection: When ratio is low, replace a question with a reflection.
- Defer_Planning: Retreat from planning to evoking when readiness is low.
- Reopen_Ambivalence: If closure was premature, reopen both sides of the
  ambivalence.
- Debrief_Fidelity_Failure: Log metric misses and their cause (spirit, ratio,
  complexity), feeding Post_Close_Calibration_Debrief.

### Examples
See examples.md.

### Handoff Notes
Place this folder at: ~/.hermes/skills/MI_Ambivalence_Conversation/
Mirror copy: skills/MI_Ambivalence_Conversation/ (harness)
Pip can generate the files locally. Dallas must save or upload them into the
OneDrive/SharePoint harness location.
