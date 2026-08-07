# Transfer Scenario Set (transfer_scenario_set.md)
# Coaching_Dojo — coaching-conversation practice.

Transfer scenarios test generalization: the same coaching skill, a changed
context. A skill that only works in the practiced context has not been learned
(transfer failure is a first-class outcome). Transfer rules below are inherited
from the sparring core (ConvoDojo_Practice_Sparring/transfer_scenario_set.md),
flagged RECONSTRUCTED as package authority.

Evidence: EasyMED 2025 (VERIFIED) — LLM practice partners achieve learning
outcomes comparable to human standardized patients; Voigt 2025 (VERIFIED) —
role separation (trainee vs feedback/tutor) supports skill development, which
transfer tests preserve by changing context axes while keeping the coaching
skill dimensions identical. Transfer scenario design is a RECONSTRUCTED
application of the practice evidence to generalization testing.

## Scenario Bank Structure
Each scenario: id, target skill, context, persona references, difficulty, transfer_of.

## Base Scenarios (practice contexts)
| id | target skill | context | persona | difficulty |
|----|--------------|---------|---------|------------|
| scn_coach_delegation | powerful questions + reality exploration | workplace, stuck team lead | p_aria_stuck_lead | 2 |
| scn_coach_advice_seeker | inquiry over advice | workplace, advice-presser | p_ronan_advice_seeker | 3 |
| scn_coach_vague_goal | GROW goal-setting + listening | workplace, vague goal | p_soham_high_achiever | 2 |
| scn_coach_career_pivot | GROW full pass (goal -> will) | workplace, career change | p_aria_stuck_lead | 3 |

## Transfer Scenarios (generalization tests)
| id | source skill | transfer_of | context | what changes | difficulty |
|----|--------------|-------------|---------|--------------|------------|
| tr_coach_peer | inquiry over advice + listening | scn_coach_advice_seeker | coaching a peer | symmetry: no formal coaching role; the peer can coach back | 3 |
| tr_coach_student | GROW structure + goal clarity | scn_coach_career_pivot | mentoring a student | power distance, developmental context | 3 |
| tr_coach_checkin | powerful questions + will ownership | scn_coach_delegation | 10-minute check-in | time constraint: no full GROW pass; will ownership under time pressure | 2 |

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
