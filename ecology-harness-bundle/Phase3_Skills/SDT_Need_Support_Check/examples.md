## SDT Need Support Check Examples

### Example 1: Auditing a reminder utterance
Task: User is building a writing habit; agent drafts a reminder.
Candidate utterance: "You should write 500 words tonight — don't let the streak break."
Audit:
- Autonomy support: undermining (obligation framing, no rationale, no choice).
- Competence support: neutral (no challenge calibration, no feedback).
- Relatedness support: neutral.
- Pressure language: detected ("should", streak-shaming).
- Recommended mode: rephrase.
Agent response pattern: "Writing tonight would keep the draft warm for tomorrow's edit — and if tonight doesn't work, we can protect the streak by banking the outline now. Your call."

### Example 2: Classifying regulatory style (introjected)
Task: User says "I have to do this or I'll feel guilty — everyone expects it."
Classification:
- Regulatory style: introjected (provisional, medium confidence).
- Introjection lever detected in user's own language: true.
- Recommended mode: SCAFFOLD — explore, never leverage.
Agent response pattern: "It sounds like this has become about what you 'should' do rather than what you want — that distinction often matters for whether it sticks. What would make it feel like yours?" (No guilt reinforcement; evocation of user's own reasons.)

### Example 3: Undermining risk in a gamification proposal
Task: Agent proposes a points-and-badge reward for tasks the user already enjoys.
Candidate action: "Earn 50 points per completed practice session, redeemable for a coffee."
Audit:
- Undermining risk: high (performance-contingent tangible reward on intrinsically
  motivated behavior — Deci 1999 undermining effect).
- Recommended mode: rephrase to informational feedback.
Agent response pattern: "Since you already enjoy the practice, points could actually drain the enjoyment — instead I can track your progress against your own goals and surface the patterns you care about."

### Example 4: Need-support audit of a scaffolded onboarding flow
Task: Designing onboarding for a new routine.
Candidate design: Single mandatory path, no choice, completion bar with red warning.
Audit:
- Autonomy support: undermining (no choice, warning pressure).
- Competence support: supportive (progressive steps), but scaffold has no fade plan.
- Recommended mode: SCAFFOLD with fade.
Agent response pattern: Offer three entry paths (quick, standard, deep), explain the trade-off of each, keep the progress display informational ("where you are" not "you're behind"), and schedule scaffold fade via Proximal_Practice_Selector.

### Example 5: Practice mode — user practices autonomy-supportive phrasing
Task: User is learning to give feedback that preserves autonomy.
Candidate action: Agent supplies a full model phrasing immediately.
Boundary analysis:
- Skill atrophy risk: high if user is building this skill.
- Recommended mode: SCAFFOLD.
Agent response pattern: Provide the structure ("acknowledge perspective → state your need → offer choice"), invite the user's draft, give hints on their draft, and offer a full model only if explicitly requested.
