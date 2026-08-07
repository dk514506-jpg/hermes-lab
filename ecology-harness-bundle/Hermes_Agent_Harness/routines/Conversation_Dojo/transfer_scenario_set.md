# Transfer Scenario Set (transfer_scenario_set.md)
# Conversation_Dojo — everyday-conversation practice.

Transfer scenarios test generalization: the same conversational skill, a changed
context. A skill that only works in the practiced context has not been learned
(transfer failure is a first-class outcome). Transfer rules below are inherited
from the sparring core (ConvoDojo_Practice_Sparring/transfer_scenario_set.md),
flagged RECONSTRUCTED as package authority.

Evidence: EasyMED 2025 (VERIFIED) — LLM practice partners achieve learning
outcomes comparable to human standardized patients; AgentForge 2026 (VERIFIED) —
role-play is most effective when the trainee's role carries visible coordination
demands, which transfer tests exercise by changing context axes. Transfer
scenario design is a RECONSTRUCTED application of the practice evidence to
generalization testing.

## Scenario Bank Structure
Each scenario: id, target skill, context, persona references, difficulty, transfer_of.

## Base Scenarios (practice contexts)
| id | target skill | context | persona | difficulty |
|----|--------------|---------|---------|------------|
| scn_convo_intro | small talk + follow-up | work social event | p_maya_chatty_colleague | 1 |
| scn_convo_flatmate | listening + follow-up | household, terse speaker | p_dev_terse_flatmate | 2 |
| scn_convo_topic_shift | listening + follow-up under drift | friendly chat | p_liam_topic_hopper | 2 |
| scn_convo_clarity | clarity + repair | neighbor planning a shared task | p_dev_terse_flatmate | 2 |

## Transfer Scenarios (generalization tests)
| id | source skill | transfer_of | context | what changes | difficulty |
|----|--------------|-------------|---------|--------------|------------|
| tr_convo_family_dinner | small talk + follow-up + repair | scn_convo_intro | family dinner | long relationship history, higher emotion, multiple speakers | 3 |
| tr_convo_remote_async | clarity + follow-up | scn_convo_clarity | written async channel (chat/DM) | no tone or body cues; reply delay | 3 |
| tr_convo_networking | small talk + follow-up + turn-taking | scn_convo_intro | professional conference networking | higher stakes, first impression, time-boxed | 3 |

## Transfer Rules (inherited from sparring core; RECONSTRUCTED)
- Run transfer only after the source skill shows sustained proficiency at
  level >= 2 (proficiency_gated escalation applies to transfer too).
- Transfer results are evidence for the learner, not grades: record what
  generalized and what did not, anchored to turns.
- A transfer gap names the next practice target; it does not invalidate the
  base skill.
- Transfer scenarios may reuse the same rubric (generalization of the SAME
  dimensions) — that is the point of the test.
- The user chooses which transfer context to attempt; the agent proposes,
  never assigns.

## Building New Transfer Scenarios
A good transfer scenario changes ONE structural axis (context, relationship
power, channel, stakes) and keeps the target skill dimensions identical.
Changing two axes at once confounds the generalization signal.
