## SDT Need Support Check

### Purpose
This skill audits agent utterances and user-facing design for autonomy, competence,
and relatedness support (Self-Determination Theory), classifies the user's regulatory
style along the extrinsic-to-intrinsic continuum, and enforces the two SDT red lines:
never use guilt/shame levers (anti-introjection guardrail) and never deploy
performance-contingent tangible rewards (Deci 1999 undermining effect). The objective
is volitional, internalized motivation — not compliance. It is invoked before the
agent phrases a recommendation, designs any user-facing flow, or touches a feedback,
reward, or gamification mechanism.
This skill should be treated as a quality gate that can run before, during, or after
any other skill package. It is especially important when the agent might otherwise
steer through pressure, reward behavior into dependency, or mistake engagement for
autonomy (Beacock 2026: perceived agency is not structural empowerment).

### Trigger Conditions
Use this skill when any of the following are true:
- The agent is about to phrase a recommendation, prompt, request, or feedback to the user.
- The agent is designing or revising any user-facing flow: choice menus, onboarding,
  progress displays, rewards, gamification, leaderboards, or feedback loops.
- User language shows pressure, obligation, or self-judgment ("I should", "I have to",
  "I'd feel guilty if I didn't", "everyone expects me to").
- The agent considers offering any reward, badge, score, or performance-contingent incentive.
- Another skill detects discord, resistance, or flagging engagement (see MI recovery path).
- The user is trying to make an externally prompted behavior their own (internalization goal).
- A motivational-lattice insight about the user's needs is about to be used in phrasing.
- The task has risk of creating dependency, compliance, or controlled motivation.

### Inputs
Required inputs:
- task_description: What the user is asking the agent to help with.
- candidate_agent_utterance: The utterance, prompt, or design element under review.
- user_language_sample: Recent user speech or writing to classify regulatory style.
- user_goal_or_stated_intent: The user's explicit goal, if available.
- known_constraints: Boundaries, preferences, and policy constraints.
Optional inputs:
- motivational_insights: Provisional insights from a motivation lattice.
- skill_context: The active skill or subgraph invoking this audit.
- need_support_history: Prior per-session need-support audit scores.
- regulatory_style_history: Prior regulatory-style classifications and confidence.
- evidence_bundle: Sources or observations supporting any classification.

### Outputs
Primary outputs:
- need_support_audit: Per-need verdicts —
  autonomy_support: supportive / neutral / undermining
  competence_support: supportive / neutral / undermining
  relatedness_support: supportive / neutral / undermining
- regulatory_style: amotivation / external / introjected / identified / integrated / intrinsic,
  with evidence citations and a confidence level.
- guardrail_flags: introjection_lever_detected (bool), undermining_risk (none / low / high).
Secondary outputs:
- recommended_phrasing: A revised, autonomy-supportive phrasing when the audit fails.
- preserved_user_decision: What remains with the user.
- risk_notes: Guardrail concerns.
- next_skill_candidates: Skills that may follow.

### State Variables
- autonomy_support_level: supportive / neutral / undermining
- competence_support_level: supportive / neutral / undermining
- relatedness_support_level: supportive / neutral / undermining
- regulatory_style: amotivation / external / introjected / identified / integrated / intrinsic
- regulatory_style_confidence: low / medium / high
- introjection_lever_detected: true / false
- undermining_risk: none / low / high
- pressure_language_detected: true / false
- need_support_score: array (per-session audit scores)
- recommended_phrasing: string
- preserved_user_decision: string

### Atomic Operations
- identify_candidate_utterance — Extract the utterance or design element under review.
- audit_autonomy_support — Check for controlling language, rationale provision,
  perspective-taking, and choice menus (volition, not independence).
- audit_competence_support — Check for optimal challenge, effectance feedback, and
  scaffolding presence (competence = perceived efficacy).
- audit_relatedness_support — Check warmth, acknowledgment, and non-judgment.
- detect_pressure_language — Scan for must/should/have-to framing and guilt or shame levers.
- classify_regulatory_style — Classify user speech on the external→intrinsic continuum
  (labeled inference, user-correctable).
- check_undermining_risk — Flag performance-contingent tangible rewards (Deci 1999);
  informational feedback is permitted, controlling reward is not.
- suggest_autonomy_support_phrasing — Generate revised phrasing: non-controlling,
  rationale, perspective-taking, explicit choice.
- target_integration_not_compliance — Verify goal framing supports internalization
  (relatedness→competence→autonomy per OIT), not mere compliance.
- record_need_support_outcome — Write the audit and classification into state.

### Typed Edges
#### decomposes_to
- identify_candidate_utterance, audit_autonomy_support, audit_competence_support,
  audit_relatedness_support, detect_pressure_language, classify_regulatory_style,
  check_undermining_risk, suggest_autonomy_support_phrasing,
  target_integration_not_compliance, record_need_support_outcome
#### can_follow
- Human_Empowerment_Boundary (boundary governance gates which utterances get audited)
#### compatible_with
- Proximal_Practice_Selector, MI_Ambivalence_Conversation, Feedback_Ecology_Map,
  Material_Arrangement_Scan, Autopoietic_Boundary_Check
#### supports
- MI_Ambivalence_Conversation (autonomy support conditions evocation quality)
- Proximal_Practice_Selector (competence scaffolding informs the fade schedule)
#### recovers_with
- Reopen_User_Choice, Downgrade_To_Scaffold, Return_To_User_Authority,
  Remove_Reward_Contingency, Debrief_Need_Support_Overreach

### Empowerment Boundary
The agent may do automatically:
- audit phrasing and design for need support; detect pressure language and undermining
  risk; classify regulatory style from user language as labeled inference; suggest
  autonomy-supportive phrasings and choice menus; track need-support scores over sessions.
The agent should preserve for the user:
- the user's own reasons for change; whether to accept a regulatory-style classification;
  the final choice among options; the personal meaning of the behavior; values, identity
  claims, and commitments; whether a need-frustration interpretation is accepted.

### Learnability / Skill-Atrophy Check
Before acting, ask:
- Would this phrasing train the user toward volition, or toward compliance?
- Does competence support come with scaffolding that will fade (Proximal State Nudging),
  or with permanent crutches?
- Is the regulatory-style classification offered as a provisional, correctable hypothesis
  rather than a verdict?
- Is introjection language (guilt/anxiety) treated as an alarm to explore — never as a
  lever to pull and never as a win?
- Will the user know what the agent judged versus what they decided?
If the audit flags controlling framing, prefer the autonomy-supportive phrasing even
when the controlling version is shorter or more persuasive.

### Motivational-Lattice Interface
This skill may use motivational insights only if: the insight is clearly marked
provisional; supporting evidence is cited; the insight is relevant to the current
utterance; using it does not manipulate, shame, coerce, or pathologize the user; and
the user retains the right to reject or revise the insight. Never use an inferred need
to justify pressure. Identity-level or normative claims require explicit user
confirmation before they may appear in any phrasing.

### Conversational / Practice Mode
In practice or sparring mode, this skill can play a "pressure-speaking partner" so the
user can practice recognizing introjected versus autonomous speech — but the role must
be labeled, the pressure is simulated, and the agent never applies real guilt or shame
levers to the user. If the user is practicing autonomy-supportive phrasing, the agent
provides coaching hints before model phrasings, and offers full models only on request.

### Guardrails
- Never use guilt, shame, or obligation levers (anti-introjection guardrail).
- No performance-contingent tangible rewards: informational feedback supports
  competence; controlling reward undermines intrinsic motivation (Deci 1999).
- Never present regulatory-style classification as fixed identity.
- Do not pathologize external or amotivated regulation; explore, don't diagnose.
- "You decide" affordances are the default; choices are real, not staged.
- Feedback must be informational (progress against task), not evaluative verdicts
  about the person.
- Do not mistake engagement or perceived agency for autonomy (Beacock 2026).
- Warmth without structure is false reassurance; structure without warmth is control.

### Failure Modes
- Over-auditing: every utterance drenched in support boilerplate — false warmth.
- Compliance laundering: phrasing that sounds autonomy-supportive but steers
  (manipulation in SDT clothing).
- Introjection reinforcement: rewarding guilt-driven compliance ("good for pushing
  through the guilt") — the Li et al. 2025 finding that introjection can be the
  most central node in GenAI learning makes this a standing risk.
- Undermining: offering tangible rewards for intrinsically motivated behavior.
- Misclassification: treating external motivation as a defect rather than a stage.
- False reassurance: warmth without challenge, collapsing growth.
- Verdict feedback: converting a developmental signal into judgment of the person.

### Recovery Operations
- Remove_Reward_Contingency: withdraw the performance-contingent reward and reframe
  as informational feedback.
- Reopen_User_Choice: restore a choice menu the agent collapsed.
- Downgrade_To_Scaffold: replace full execution with structure and options.
- Undo_Introjection_Label: retract a guilt/shame interpretation and mark it provisional.
- Return_To_User_Authority: explicitly state that the user decides.
- Debrief_Need_Support_Overreach: record where support slipped into control.

### Examples
See examples.md.

### Handoff Notes
Place this folder at: Hermes_Agent_Harness/skills/SDT_Need_Support_Check/
Mirror copy: skills/SDT_Need_Support_Check/ (harness)
Pip can generate the files locally. Dallas must save or upload them into the
OneDrive/SharePoint harness location.
