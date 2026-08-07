## COMB Behavioral Diagnosis

### Purpose
This skill turns user statements about a stuck goal or habit into a six-component
COM-B profile (C-Ph, C-Ps, O-Ph, O-So, M-Re, M-Au), identifies the binding
constraint (the component whose deficit most plausibly holds the behavior in
place), and emits a hypothesis-status profile the user can correct. It is the
diagnostic spine of the ecology: TDF refines each component, BCW/BCT convert the
diagnosis into intervention functions and techniques, and SDT/MI govern the
motivational quality of whatever follows.
Grounded in Michie, van Stralen & West 2011 (six typed components; behavioural
target specification + component profiling; 88%/79% inter-rater reliability) and
Willmott 2021 (31%/23% variance explained). The framework is descriptive, not
predictive — the profile is a hypothesis, never a verdict.

### Trigger Conditions
Use this skill when any of the following are true:
- The user describes a stuck goal or habit ("I keep...", "I can't seem to...",
  "It always falls apart after...", "I have no time for...").
- The user asks why a behavior will not change, or what is in the way.
- The user asks for a behavior-change plan and no diagnosis exists yet.
- A TDF barrier grid, MI conversation, or SDT check needs a component-level anchor.
- An intervention-selection skill (BCW function/BCT layer) needs a COM-B input.
- The user asks the agent to explain their behavior back to them (diagnostic
  mirroring) — apply the hypothesis label before responding.

### Inputs
Required inputs:
- target_behavior: The behavior named by the user, specified as verb + context
  (e.g., "walk 30 minutes after dinner", not "be healthier").
- user_statements: Utterances, reflections, or logs about the stuck behavior.
- user_goal_or_stated_intent: The user's own account of what they want.
Optional inputs:
- schedule_or_resource_data: Time/energy signals for O-Ph coding.
- social_context: Opt-in information about norms, others, or pressures (O-So).
- habit_or_telemetry_log: Repeated-pattern or emotion signals for M-Au.
- motivational_lattice_insights: Provisional insights (must be marked provisional
  and evidence-cited before use).
- prior_tdf_grid: A finished TDF grid that can be compressed into components.
- known_constraints: Health, policy, or scope limits.

### Outputs
Primary output: component_profile — a six-slot record (C-Ph, C-Ps, O-Ph, O-So,
M-Re, M-Au), each slot carrying a salience level (none / weak / moderate / strong),
evidence quotes, and a confidence flag.
Secondary outputs:
- binding_constraint: The single component whose deficit is most load-bearing,
  or "none identified" when evidence is insufficient.
- hypothesis_status: "hypothesis — user-correctable" label attached to the whole
  profile and to each slot.
- component_notes: Per-component explanation in user language.
- next_skill_candidates: TDF_Barrier_Facilitator_Grid (refine), SDT_Need_Support_Check
  (motivational quality), MI_Ambivalence_Conversation (M-Re/M-Au ambiguity),
  Proximal_Practice_Selector (design from binding constraint).
- open_probes: Questions the agent still needs answered (if evidence insufficient).

### State Variables
- target_behavior: string
- component_profile: array of 6 slots {component, salience, evidence_quotes, confidence}
- binding_constraint: enum C-Ph | C-Ps | O-Ph | O-So | M-Re | M-Au | none
- evidence_sufficiency: enum insufficient | partial | sufficient
- hypothesis_status: true (always; the profile is never emitted as fact)
- user_corrections: array of {component, user_statement, accepted}
- open_probes: array of strings
- next_skill_candidates: array of skill ids
- lattice_insights_used: boolean

### Atomic Operations
- specify_target_behavior — Pin the behavior as verb + context from user language;
  refuse to diagnose an underspecified target.
- classify_component — Six-label typed-node classifier: map a user utterance to
  one of C-Ph, C-Ps, O-Ph, O-So, M-Re, M-Au (e.g., "I don't know how" → C-Ps;
  "no time" → O-Ph; "I keep forgetting" → M-Au). Labeled inference, user-correctable.
- ask_knowledge_probe — For C-Ps: ask what the user already knows/tried before
  proposing learning paths (guided discovery, not answering for them).
- surface_resource_scan — For O-Ph: scan time/resources/schedule and surface
  arrangements; agent reorganizes logistics, never makes commitments.
- surface_social_context — For O-So: surface norms and pressures from opt-in
  social data only; social changes are user-chosen.
- evocation_prompt — For M-Re: MI-style open prompt (e.g., "What would be
  different for you if it worked?") to elicit intentions/evaluations without
  arguing against resistance.
- habit_scan — For M-Au: look for cue→routine→reward patterns and emotion
  signals in logs; note that habit and emotion collapse is a known COM-B limit
  (RECONSTRUCTED critique) — do not silently conflate them.
- suggest_education_or_training — For C-Ps deficits: propose learning paths;
  the user does the learning.
- suggest_environmental_or_training_opts — For C-Ph deficits: propose
  environmental or training options; health limits are user-authoritative and
  medical advice is hard-blocked.
- cue_restructure_suggestion — For M-Au: propose cue restructuring; environment
  change supplements, never replaces, user practice.
- identify_binding_constraint — Rank the six slots; select the most load-bearing
  deficient component, or "none" if evidence is insufficient (abstain over guess).
- label_hypothesis_status — Attach the hypothesis label to profile and slots.
- emit_component_profile — Render the profile with evidence quotes, salience,
  confidence, and binding constraint in user language.
- record_diagnosis — Write profile, corrections, and open probes to task state.

### Typed Edges
#### decomposes_to
- specify_target_behavior, classify_component, ask_knowledge_probe,
  surface_resource_scan, surface_social_context, evocation_prompt, habit_scan,
  suggest_education_or_training, suggest_environmental_or_training_opts,
  cue_restructure_suggestion, identify_binding_constraint, label_hypothesis_status,
  emit_component_profile, record_diagnosis
#### can_follow
- TDF_Barrier_Facilitator_Grid (14-domain grid refines the six-component profile —
  VERIFIED, Cane 2012 mapping)
- SDT_Need_Support_Check (motivational quality under the M components —
  RECONSTRUCTED)
- MI_Ambivalence_Conversation (M-Re/M-Au ambiguity opens evocation — RECONSTRUCTED;
  reverse direction also valid per register)
- Proximal_Practice_Selector (binding constraint → proximal practice design —
  RECONSTRUCTED)
#### compatible_with
- Material_Arrangement_Scan (O-Ph evidence from practice theory scan — RECONSTRUCTED)
- Feedback_Ecology_Map (O-So/O-Ph feedback-loop evidence — RECONSTRUCTED)
- Motivational_Lattice_Generator (provisional lattice insights inform the profile —
  RECONSTRUCTED, Lim 2025 grounding)
#### supports
- TDF_Barrier_Facilitator_Grid (component profile is the grid's input layer)
- Proximal_Practice_Selector (binding constraint is a proximal-state input)
- BCW function / BCT selection layer (diagnosis → function via Table-2 matrix)
#### recovers_with
- Human_Empowerment_Boundary (overreach, premature closure, or user correction)
- Reopen_Component_Assignment, Downgrade_To_Hypothesis, Ask_Targeted_Clarification,
  Return_To_User_Authority (see recovery_ops.md)

### Empowerment Boundary
The agent may do automatically:
- classify utterances into the six components; organize evidence quotes; propose
  learning paths, environmental options, and cue-restructure options; reorganize
  logistics and schedules into options; draft the profile and its labels.
The agent must preserve for the user:
- stating the gap in their own words; answering knowledge probes (agent must not
  answer questions the user can answer); time-allocation judgment; commitments;
  any social change; final endorsement, correction, or rejection of the profile;
  whether an inferred motive (M-Re/M-Au) is accepted.

### Learnability / Skill-Atrophy Check
Before completing a profile, ask:
- Would answering this knowledge probe myself reduce the user's future unassisted
  capacity to self-diagnose? Prefer guided discovery (C-Ps).
- Am I respecting the user's time-allocation judgment rather than deciding their
  schedule for them? (O-Ph)
- Is the environment change supplementing, not replacing, user practice? (M-Au)
- Am I arguing against resistance instead of evoking? (M-Re — MI spirit)
- Does the emitted profile teach the six-component vocabulary so the user can run
  a lighter version of this diagnosis unassisted next time? If yes, label the
  profile as a teachable artifact and fade the agent's role.

### Motivational-Lattice Interface
This skill may use motivational-lattice insights only if: the insight is marked
provisional; it cites supporting observations; it is relevant to the current
target behavior; it does not manipulate, shame, coerce, or pathologize; and the
user retains revision/rejection/quarantine rights.
Do not use lattice insights to make identity-level or normative claims about the
user without explicit confirmation (e.g., "you avoid hard work" is NOT an
acceptable M-Re slot without the user saying it or confirming it).

### Conversational / Practice Mode
In practice or sparring mode, this skill teaches the six-component vocabulary:
- Give the user sample statements and ask them to classify; give rubric feedback
  (right component, wrong component, evidence missing), not verdicts.
- Sparring move: challenge single-component myopia ("You've coded everything as
  motivation — where does opportunity live in this picture?").
- If the user is overwhelmed by six slots, present two at a time and aggregate.
- Full demonstration is allowed when requested, but label which parts can be
  practiced later.

### Guardrails
- Never emit a profile without the hypothesis label; the user corrects it.
- Never give medical advice under C-Ph; refer to professional care.
- Never use social data without opt-in (O-So privacy).
- Never treat habits and emotions as the same thing silently under M-Au
  (RECONSTRUCTED critique) — flag the conflation when it would matter.
- Never argue against resistance while probing M-Re (MI spirit).
- Never answer a knowledge probe the user can answer themselves.
- Never use inferred motivation to steer, shame, or nudge covertly.
- Never present the profile as predictive — COM-B is descriptive (Willmott 2021).
- Never diagnose an underspecified target behavior.

### Failure Modes
- Single-component myopia: everything coded to one component (usually M-Re).
- Descriptive-as-predictive: profile treated as a forecast or verdict.
- Over-asking: endless probes instead of a provisional profile (false deference).
- Medical overreach: C-Ph handled as diagnosis instead of referral.
- Paternalism: agent decides what the user "really" lacks without consent.
- Covert steering: M-Re/M-Au inferences used to nudge without labeling.
- Habit/emotion conflation: M-Au slot hides a distinction that matters.
- Premature closure: binding constraint named on insufficient evidence.

### Recovery Operations
- Reopen_Component_Assignment: Offer to re-code any slot the user rejects.
- Downgrade_To_Hypothesis: Reframe any profile language that drifted into verdict.
- Ask_Targeted_Clarification: One precise probe when evidence is insufficient.
- Return_To_User_Authority: Explicitly state the user decides what the profile
  means for them.
- Separate_Evidence_Interpretation_Implication: Rebuild the profile in disciplined
  layers (quote → component → implication → next step).
- Reframe_As_Options: Convert a single binding-constraint claim into alternative
  component readings.
- Escalate_To_Empowerment_Boundary: Invoke Human_Empowerment_Boundary when
  overreach, dependency, or interpretive closure is detected.
(De-ossification path: Downgrade_To_Hypothesis + Reopen_Component_Assignment —
unfreezing a component assignment the agent closed too hard.)

### Examples
See examples.md.

### Handoff Notes
Place this folder at:
~/.hermes/skills/COMB_Behavioral_Diagnosis/
Pip can generate the files locally; Dallas must save or upload them into the
OneDrive/SharePoint harness location. Keep skill_node.json, edge_map.json, and
skill_graph_index.json in agreement after any edge change.
