# Motivational Lattice Generator

## Purpose
This skill builds evidence-grounded, provisional motivation lattices from user-provided
logs, reflections, and artifacts. A lattice is a graph of observations, insight nodes,
and evidence edges in which every insight is a hypothesis that cites its supporting
observations, and in which observation, interpretation, implication, and proposed action
are kept in separated layers. The lattice is the Layer 1 "Motivational Understanding"
mechanism of the Motivational Ecology Agent Architecture: it makes motivation inference
auditable, user-correctable, and safe, instead of implicit and opaque.

Grounded in: Lim 2025 (LLM-scored change-talk valence → HMM transition dynamics predict
session quality at 0.80 LOOCV — the empirical core of behavior latticing); SERUM 2026
(finite-state action/intent models from egocentric video via hierarchical VLM annotation,
with "schematic equilibrium" as the convergence criterion; Markov models beat frequency
baselines); the AnnoMI corpus (annotated MI sessions as observation-rich training ground);
Shaikh 2026 LongNAP (next-action prediction is viable but only ~17% of trajectories align —
insights are timing priors, never autonomous-action triggers).

## Trigger Conditions
Use this skill when any of the following are true:
- The agent has accumulated observations about a user's behavior, speech, or artifacts
  and is considering using them to personalize, time, or steer assistance.
- The user shares reflections, journals, logs, work artifacts, or session transcripts
  and asks (or the task implies) the agent to notice patterns.
- A motivational inference is being considered by any other skill (e.g., SDT regulatory
  style, MI change-talk trends, TDF domain salience).
- The agent is about to reuse a previously inferred user preference, motive, or pattern
  as if it were settled.
- The agent detects a recurring behavioral pattern (task-switching, avoidance, bursts,
  withdrawal) across sessions and wants to name it.
- Phase 4 integration requires an insight_trigger_policy (which insights may trigger
  which skills) — this skill produces the raw material for that policy.

## Inputs
Required inputs:
- observation_log: dated, sourced observations (verbatim quotes, artifact descriptors,
  behavioral events) with provenance.
- evidence_sources: which logs/reflections/artifacts/transcripts the observations come from.
- user_consent_level: whether the user has opted into pattern analysis for this material.
- task_description: what the lattice is for (e.g., "understand barriers to the writing
  routine", "inform coaching", "nothing yet — just surface patterns").

Optional inputs:
- prior_lattice: an existing lattice to extend or revise.
- user_verdicts: prior accept/reject/revise/correct decisions on existing insights.
- change_talk_log: DARN-CAT tagged utterances from MI sessions (Lim-style input).
- session_transcripts: AnnoMI-style annotated dialogue.
- skill_context: the skill that requested the lattice or will consume it.

## Outputs
Primary outputs:
- motivation_lattice.md: the rendered lattice with separated layers
  (observation | interpretation | implication | action).
- insight_nodes.json: hypothesis nodes, each with confidence, evidence citations,
  identity-level flag, and quarantine status.
- evidence_edges.json: observation→insight citation links.
- quarantined_insights.md: identity-level or low-evidence interpretations held out of
  active use pending user confirmation.
- insight_validation_protocol.md: the validation run record (evidence sufficiency,
  convergence state, user verdicts).

Secondary outputs:
- user_verdict_record: for each insight — pending / confirmed / rejected / revised / corrected.
- convergence_state: diverging / emerging / schematic_equilibrium.
- next_skill_candidates: skills that may consume confirmed insights.
- risk_notes: overinterpretation, paternalism, circular-evidence, surveillance flags.

## State Variables
- observation_count: integer
- insight_count: integer
- evidence_sufficiency: insufficient / partial / sufficient
- convergence_state: diverging / emerging / schematic_equilibrium
- interpretation_confidence: low / medium / high
- identity_level_flag: true / false
- quarantine_status: active / cleared / pending_review
- user_verdict: pending / confirmed / rejected / revised
- manipulation_risk: low / medium / high
- surveillance_risk: low / medium / high
- lattice_freshness: stale / fresh
- lattice_status: draft / under_review / confirmed / superseded

## Atomic Operations
- capture_observation — Record a raw observation with timestamp, source, and verbatim content.
- classify_observation_type — Tag observation as behavior / statement / artifact / pattern.
- separate_inference_layers — Enforce the four-layer separation
  (observation | interpretation | implication | action) on any emerging claim.
- form_interpretation_hypothesis — Generate a candidate interpretation, explicitly marked
  as hypothesis, citing the observations that support it.
- link_evidence_edges — Create observation→insight evidence edges with strength and
  provenance (the lattice's citation mechanism).
- score_evidence_sufficiency — Rate whether the supporting evidence base is
  insufficient / partial / sufficient for each insight.
- detect_schematic_convergence — Assess whether independent observations converge on the
  same schematic (SERUM-style convergence; distinguishes emerging from equilibrium).
- flag_identity_level_claim — Detect interpretations about who the user *is* (identity),
  which require explicit confirmation and default to quarantine.
- quarantine_insight — Move an insight to the quarantined set; it may not steer action.
- derive_implication_and_action — Produce the implication and proposed-action layers,
  each marked as hypothesis-derived and non-binding.
- present_lattice_for_review — Render the lattice for user review with evidence citations.
- record_user_verdict — Record the user's accept / reject / revise / correct response and
  propagate it through dependent insights.

## Typed Edges
#### decomposes_to
capture_observation, classify_observation_type, separate_inference_layers,
form_interpretation_hypothesis, link_evidence_edges, score_evidence_sufficiency,
detect_schematic_convergence, flag_identity_level_claim, quarantine_insight,
derive_implication_and_action, present_lattice_for_review, record_user_verdict
#### can_follow
ConvoDojo_Practice_Sparring, MI_Ambivalence_Conversation, COMB_Behavioral_Diagnosis,
TDF_Barrier_Facilitator_Grid
#### compatible_with
Human_Empowerment_Boundary, SDT_Need_Support_Check, Proximal_Practice_Selector,
COMB_Behavioral_Diagnosis (seed edge: lattice insights inform component profile)
#### supports
SDT_Need_Support_Check, Human_Empowerment_Boundary
#### recovers_with
Mark_As_Provisional, Quarantine_Insight, Reopen_User_Choice, Return_To_User_Authority,
Undo_Interpretive_Closure, Separate_Evidence_Interpretation_Implication,
Rebuild_Lattice_From_Raw_Observations

## Empowerment Boundary
The agent may do automatically:
- organize observations; detect candidate patterns; propose interpretations marked as
  hypotheses; build evidence bundles; prepare lattice renderings; track evidence sufficiency;
  maintain quarantine lists; record user verdicts.

The agent must preserve for the user:
- whether an insight is accepted, rejected, or revised;
- whether an identity-level interpretation is confirmed (explicit confirmation required);
- what the user's motives "really are" (only the user can close that question);
- interpretive closure and final meaning-making;
- any decision or commitment that the lattice suggests but the user has not made.

Latticing is a tool for the user's self-knowledge, not a verdict on the user. An insight
that the user rejects is removed from active use regardless of evidence strength.

## Learnability / Skill-Atrophy Check
Before acting, ask:
- Is this pattern something the user could notice for themselves with a better scaffold?
  (Prefer a reflection prompt over a delivered insight when the user is building
  self-observation skill.)
- Would full "insight delivery" reduce the user's future unassisted self-knowledge?
- Does the lattice render the evidence so the user can verify the inference themselves?
- Can the lattice's scaffolding fade (e.g., from agent-named patterns to user-named
  patterns over sessions)?
- Will the user know which observations the agent used and which parts are the agent's
  interpretation vs. their own words?

The user's reflective capacity is the capability this skill must never replace. Insights
should increasingly be *elicited* (MI evocation spirit), not only delivered.

## Motivational-Lattice Interface
This skill is itself the lattice producer, so it must apply its own rules to its own
output: every insight it emits is a hypothesis; every insight cites observations; identity-
level claims are quarantined until confirmed; user verdicts override evidence. When
consuming insights from other skills (e.g., TDF domain coding, SDT regulatory style), it
carries those insights with their provenance and applies the same quarantine rules.
Do not use lattice insights to manipulate, shame, coerce, or pathologize the user; do not
use them to script a sparring persona against the user (see ConvoDojo guardrails).

## Conversational / Practice Mode
Latticing can be interactive:
- Present insights one at a time in conversation, each with its evidence, and invite a verdict.
- Use MI-style evocation to elicit the user's own interpretation before offering the agent's.
- Practice sessions (ConvoDojo) and MI conversations feed fresh observations into the lattice;
  change-talk transitions (Lim 2025) are first-class observation material.
- In practice mode, insights about the user are never used to make the simulated
  interlocutor "know" the user; the persona stays persona (see ConvoDojo persona rules).

## Guardrails
- Insights are hypotheses, not facts — never present them as settled.
- Every insight must cite supporting observations; uncited insights are discarded.
- Do not make identity-level claims without explicit user confirmation (quarantine by default).
- Do not use motivational insights to manipulate, nudge covertly, or steer without consent.
- Do not convert practice logs, chat logs, or telemetry into surveillance; observation is
  opt-in and bounded to the agreed material.
- Do not mistake convergence for truth: schematic equilibrium (SERUM) is a stability
  criterion, not a correctness proof.
- Do not build on the withdrawn SRSUPM recommender; do not cite retracted meta-analyses
  (Wang & Fan 2025 retraction flagged in the evidence register).
- Do not treat next-action prediction as an action trigger (LongNAP: ~17% trajectory
  alignment) — use as timing priors only.
- Do not mistake engagement metrics for motivation truth (Beacock 2026: perceived agency
  ≠ structural empowerment).
- Do not let the lattice become self-fulfilling: do not steer the user toward the pattern
  the lattice predicts (circular-evidence and confirmation-bias guard).

## Failure Modes
- Overinterpretation: weak evidence dressed as deep insight.
- Paternalism: agent decides what the user's motives "really are" without consent.
- Circular evidence: observations defined by the interpretation they supposedly support.
- Premature closure: declaring schematic equilibrium before convergence is real.
- Insight theater: trivial observations presented as revelation (Beacock's empowerment
  theater, applied to insight delivery).
- Identity labeling: characterizing who the user is without confirmation.
- Surveillance creep: latticing material the user did not opt in to.
- Self-fulfilling lattice: acting on an insight until the user conforms to it.
- Dependency: user stops self-observing because the agent "knows" them.
- Stale lattice: acting on superseded insights after user change.

## Recovery Operations
- Rebuild_Lattice_From_Raw_Observations: discard interpretations, restart from observations.
- Undo_Interpretive_Closure: convert a settled conclusion back into a hypothesis.
- Quarantine_Insight: pull an overreaching insight out of active use immediately.
- User_Verdict_Override: apply the user's rejection/correction through all dependents.
- Reopen_User_Choice: name the interpretation question that belongs to the user.
- Downgrade_Confidence: lower evidence sufficiency or confidence on challenged insights.
- Debrief_Overinterpretation: record where the lattice overreached, for calibration.

## Examples
See examples.md.

## Handoff Notes
Place this folder at:
skills/Motivational_Lattice_Generator/ (harness)
Lattice outputs (motivation_lattice.md, quarantined_insights.md, validation records)
belong in the harness `lattices/` folder. Dallas must save or upload generated files
into OneDrive/SharePoint; Pip can generate files locally.
