# Debrief Template (debrief_template.md)
# Conversation_Dojo — evidence-grounded debrief for everyday-conversation practice.

Debriefs are evidence-grounded and provisional: every claim anchors to turns;
the user corrects the record. Rubric output is consumed as LENSES, never
verdicts (rubric_use_rules). Evidence flags: VERIFIED / RECONSTRUCTED per
ecology discipline.

## Session Header
- Session id / date / practice_target (turn-taking | listening | follow-up |
  small talk | clarity) / scenario_id / persona_id
- Intensity profile used (start -> end) and any de-escalation events
- Coaching mode (off / on / on_demand) and interruption count

## 1. What Happened (evidence layer)
- Stage transitions (dialogue_state_machine record)
- 2-5 anchor turns: user utterance + persona response + what the turn shows
- Friction events (if level >= 3): how pressure was handled, turn by turn

## 2. Rubric Lenses (lens layer — not verdicts)
For each rubric dimension scored (listening_and_followup_v1 /
small_talk_flow_v1 / clarity_and_repair_v1):
- Dimension, lens level (developing / practicing / proficient)
- Evidence quotes (>=1 per score)
- Practice direction: ONE next-step focus the user chooses

## 3. Patterns Noticed (hypothesis layer)
- Patterns from turns only, marked HYPOTHESIS, with turn citations
- Explicit note: "These are hypotheses about this session, not verdicts about you."

## 4. Intensity and Friction Calibration
- What friction landed well (evidence)
- What friction missed / overshot (evidence)
- Recommended intensity for next session (user decides)

## 5. Transfer Notes
- If transfer_flag: what generalized, what did not (evidence-anchored)
- Suggested next transfer context (user decides)

## 6. Preserved User Decisions (preserved_user_decision)
What remains with the user — the agent records, never decides:
- Intensity for the next session
- Which practice target to focus next
- Which transfer scenario (if any) to attempt
- The user's interpretation of their own performance
- Any real conversation this practice prepares them for, and its decisions
The agent may propose; the user disposes.

## 7. User Corrections / Verdict
- What the user wants to keep, drop, or change from this debrief
- Any corrections to the record (recorded verbatim)
- The debrief is provisional until the user reviews it.

## 8. Calibration Log Entry
- For the agent: sycophancy events, intensity mis-calibrations, rubric misreads
  (overreach signals for recovery ops — feeds the monthly review with the Open
  Questions Register; empowerment_boundary.md §5 L5)

---
Template end. The debrief is provisional until the user reviews it.
