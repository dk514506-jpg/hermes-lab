# Transfer Scenario Set (transfer_scenario_set.md) — Workplace Communication dojo

Phase 6 required artifact. Transfer scenarios test generalization: the same
conversational skill, a changed context. A skill that only works in the practiced
context has not been learned (transfer failure is a first-class outcome). The base
set covers 1:1 and group meetings; the transfer set covers the email-equivalent
(written async) channel and group/meeting variations, plus a new speech act
(delegation) on an existing relationship.
Evidence flags: EasyMED 2025 VERIFIED, AgentForge 2026 VERIFIED, Voigt 2025 VERIFIED
(role-play mechanism, digest Area 6); scenario design and transfer axes RECONSTRUCTED.

## Scenario Bank Structure
Each scenario: id, target skill, context, persona references, format, difficulty, transfer_of.

## Base Scenarios (practice contexts)
| id | target skill | context | persona | format | difficulty |
|----|--------------|---------|---------|--------|------------|
| scn_wk_feedback_give | feedback_effectiveness_v1 (giving) | peer whose behavior affects your work | p_maya_crossfunctional | 1:1 | 2 |
| scn_wk_feedback_receive | feedback_effectiveness_v1 (receiving) | manager delivers constructive feedback | p_daniel_manager_feedback | 1:1 | 2 |
| scn_wk_request_stakeholder | professional_clarity_v1 | requesting a decision/resource from a sponsor | p_elinor_stakeholder | 1:1 | 2 |
| scn_wk_align_crossfunctional | workplace_negotiation_align_v1 | aligning priorities with a peer whose KPI conflicts | p_maya_crossfunctional | 1:1 | 2 |
| scn_wk_disagree_group | workplace_negotiation_align_v1 + professional_clarity_v1 | disagreeing professionally in a project review | p_maya + p_elinor (rotation) | group meeting | 3 |

## Transfer Scenarios (generalization tests)
| id | source skill | transfer_of | context | what changes | format | difficulty |
|----|--------------|-------------|---------|--------------|--------|------------|
| tr_wk_email_request | professional_clarity_v1 | scn_wk_request_stakeholder | written async request to sponsor | channel: no tone/body cues, formal register, async pacing | email-equivalent | 3 |
| tr_wk_group_request | professional_clarity_v1 | scn_wk_request_stakeholder | steering committee, multiple stakeholders | audience: group, persona rotation, public stakes | group meeting | 4 |
| tr_wk_feedback_email | feedback_effectiveness_v1 | scn_wk_feedback_receive | manager sends feedback in writing; user must respond in writing | channel + response mode: written reply, no immediacy cues | email-equivalent | 3 |
| tr_wk_delegate_1on1 | workplace_negotiation_align_v1 | scn_wk_align_crossfunctional | delegating a task to the peer with competing priorities | speech act: new (delegate) on the same relationship | 1:1 | 2 |

## Format Coverage
- 1:1: scn_wk_feedback_give, scn_wk_feedback_receive, scn_wk_request_stakeholder,
  scn_wk_align_crossfunctional, tr_wk_delegate_1on1
- group: scn_wk_disagree_group, tr_wk_group_request
- email-equivalent (written async): tr_wk_email_request, tr_wk_feedback_email

## Transfer Rules
- Run transfer only after the source skill shows sustained proficiency at level ≥ 2
  (proficiency_gated escalation applies to transfer too).
- Transfer results are evidence for the learner, not grades: record what generalized
  and what did not, anchored to turns.
- A transfer gap names the next practice target; it does not invalidate the base skill.
- Transfer scenarios may reuse the same rubric (generalization of the SAME dimensions)
  — that is the point of the test. Written-channel transfers additionally exercise the
  professional_clarity_v1 channel_register dimension.
- The user chooses which transfer context to attempt; the agent proposes, never assigns.
- Group-format transfers use the multi-party turn policy from the dialogue state
  machine (persona rotation, one persona active per turn).
- Intensity for transfers follows sparring_intensity_profile.json levels 1–5: group and
  public-stakes transfers (e.g., tr_wk_group_request) default to level 3; levels 4–5
  (stress, gauntlet) run only with explicit user consent.

## Building New Transfer Scenarios
A good transfer scenario changes ONE structural axis (context, relationship power,
channel, format, stakes, or speech act) and keeps the target skill dimensions
identical. Changing two axes at once confounds the generalization signal. For the
workplace dojo, the highest-value untested axes are: public vs private stakes,
cross-cultural register, and async group channels (shared docs, chat threads).
