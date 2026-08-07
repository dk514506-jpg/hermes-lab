## Proximal Practice Selector Examples

### Example 1: Hint instead of answer
Task: User is learning to write a function and asks the agent to "just do it."
Candidate action: Deliver the full solution.
Analysis:
- Learnability: high (skill-building task).
- Assistance mode: full_execution would over-scaffold.
- Recommended mode: hint.
Agent response pattern: "You've got the inputs and the loop already — the missing
piece is the edge case when the list is empty. What does the function need to return
then? Try it, and I'll check your version." (Logs the attempt as assisted; records the
hint level.)

### Example 2: Scaffold fade decision
Task: User has completed the last six practice tasks with hints only; unassisted
competence is stable and rising.
Analysis:
- skill_load_score: 0.83 (five of six tasks completed unassisted).
- fade_schedule: level 3 → level 2 this week, tied to the unassisted evidence.
- Recommended mode: fade one level; keep the next fade conditional on the next two
  unassisted attempts.
Agent response pattern: "You've done the last five on your own — I'm dropping my hint
level one step. If the next two go well unassisted, the scaffold comes off entirely.
If you stall, we re-add one level and slow down; that's the plan, not a judgment."

### Example 3: Atrophy alert (Budzyń pattern)
Task: After a month of agent-assisted work, the user's unassisted attempts decline:
last three unassisted tasks failed where they previously passed.
Analysis:
- unassisted_competence_track: declining vs baseline.
- atrophy_risk: high.
- Recovery: Restore_Scaffold (one level), slow the fade schedule, surface the track.
Agent response pattern: "Your assisted results look great, but your unassisted results
have dipped — that's the exact pattern where assistance quietly replaces skill. I'm
re-adding one scaffold level for two weeks, then we fade again on evidence. Here's your
own track so you can see it with me."

### Example 4: Readiness gate
Task: Agent planned to send a proactive practice prompt at 9am daily.
Analysis:
- readiness_signals: user has been initiating practice at midday; morning prompts are
  ignored; stated preference for self-initiation (Liu 2026: timing matters as much as
  content).
- Recommended mode: hold proactive help; wait for user initiation.
Agent response pattern: "You tend to start around midday, and you've said you like to
initiate — so I'll hold the prompts unless you ask. If you want a nudge anyway, say
the word and I'll time it to your usual start."

### Example 5: Practice dose after decay
Task: User practiced once, felt good, but a week later shows no retention.
Analysis:
- Eiroa-Solans 2025 pattern: single-session gains decayed by 24h.
- Recommended mode: select_practice_dose — three short spaced sessions per week with
  retrieval prompts, not one long session.
Agent response pattern: "One long session felt good but didn't stick — the evidence
says gains fade within a day. Let's try three short sessions a week with a quick
recall prompt at the start of each. We'll check the unassisted track in two weeks."
