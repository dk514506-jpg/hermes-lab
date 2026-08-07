# Transfer Scenario Set (transfer_scenario_set.md)

Layer 5 required output of the plan v2 §6. Transfer scenarios test generalization:
the same conversational skill, a changed context. A skill that only works in the
practiced context has not been learned (transfer failure is a first-class outcome).

## Scenario Bank Structure
Each scenario: id, target skill, context, persona references, difficulty, transfer_of.

## Base Scenarios (practice contexts)
| id | target skill | context | persona | difficulty |
|----|--------------|---------|---------|------------|
| scn_mi_career | MI evoking | workplace | p_sam_ambivalent_career | 2 |
| scn_mi_health | MI evoking | health behavior | p_jordan_smoking | 2 |
| scn_coach_team | coaching inquiry | workplace | p_priya_team_lead | 2 |
| scn_conflict_meeting | conflict de-escalation | workplace | p_marcus_dismissive | 3 |
| scn_negotiation_vendor | negotiation framing | commercial | p_elena_vendor | 3 |

## Transfer Scenarios (generalization tests)
| id | source skill | transfer_of | context | what changes | difficulty |
|----|--------------|-------------|---------|--------------|------------|
| tr_mi_family | MI evoking | scn_mi_career | family (parent-adult child) | authority gradient, emotional stakes | 3 |
| tr_mi_peer | MI evoking | scn_mi_health | peer fitness partner | symmetry, no formal helper role | 2 |
| tr_coach_student | coaching inquiry | scn_coach_team | mentoring a student | developmental context, power distance | 3 |
| tr_conflict_family | conflict de-escalation | scn_conflict_meeting | family dispute | long relationship history, high emotion | 4 |
| tr_conflict_online | conflict de-escalation | scn_conflict_meeting | written async channel | no tone/body cues | 4 |
| tr_negotiation_personal | negotiation framing | scn_negotiation_vendor | household decision | shared resources, identity stakes | 3 |

## Transfer Rules
- Run transfer only after the source skill shows sustained proficiency at level ≥ 2
  (proficiency_gated escalation applies to transfer too).
- Transfer results are evidence for the learner, not grades: record what generalized
  and what did not, anchored to turns.
- A transfer gap names the next practice target; it does not invalidate the base skill.
- Transfer scenarios may reuse the same rubric (generalization of the SAME dimensions)
  — that is the point of the test.
- The user chooses which transfer context to attempt; the agent proposes, never assigns.

## Building New Transfer Scenarios
A good transfer scenario changes ONE structural axis (context, relationship power,
channel, stakes) and keeps the target skill dimensions identical. Changing two axes
at once confounds the generalization signal.
