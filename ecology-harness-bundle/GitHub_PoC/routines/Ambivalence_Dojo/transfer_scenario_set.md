# Transfer Scenario Set — Ambivalence_Dojo (transfer_scenario_set.md)

Phase 6 required output. Transfer scenarios test generalization: the same MI
ambivalence skill, a changed context. A skill that only works in the practiced
context has not been learned (transfer failure is a first-class outcome).
Extends the ConvoDojo scenario bank (Phase 3 skeleton) with domain-specific
ambivalence scenarios; personas are drawn from persona_config.yaml.

Evidence: EasyMED 2025 (VERIFIED) — LLM practice partners achieve learning
outcomes comparable to human standardized patients; transfer tests verify the
skill generalizes beyond the practiced scenario (RECONSTRUCTED application of the
practice evidence to transfer design).

## Scenario Bank Structure
Each scenario: id, target skill, context, persona reference, difficulty,
ambivalence structure (change-talk buckets / sustain-talk themes).

## Base Scenarios (practice contexts)
| id | target skill | context | persona | difficulty | ambivalence structure |
|----|--------------|---------|---------|------------|-----------------------|
| scn_amb_career | MI ambivalence (interviewer role) | workplace | p_maia_career | 2 | CT: Desire/Ability/Reasons vs ST: security, identity, fear of regret |
| scn_amb_exercise | MI ambivalence (interviewer role) | health | p_devon_exercise | 2 | CT: Reasons/Need vs ST: time, past failure, self-doubt |
| scn_amb_smoking | MI ambivalence (interviewer role) | health | p_devon_exercise (topic variant) | 3 | CT: Reasons/Need vs ST: coping function, social identity |
| scn_amb_caregiving | MI ambivalence (interviewer role) | family | p_robin_caregiving | 3 | CT: Desire/Need/Ability vs ST: guilt, resentment, duty |

## Transfer Scenarios (generalization tests)
| id | source skill | transfer_of | context | what changes | difficulty |
|----|--------------|-------------|---------|--------------|------------|
| tr_amb_family_move | MI ambivalence | scn_amb_career | family (adult child ambivalent about relocating near vs away from parents) | authority gradient + emotional stakes; relationship history replaces the workplace frame | 3 |
| tr_amb_peer | MI ambivalence | scn_amb_exercise | peer (friend ambivalent about a health change) | symmetry: no formal helper role, equal footing | 2 |
| tr_amb_async | MI ambivalence | scn_amb_smoking | written async channel (text-based check-in) | no tone/body cues; reflections must carry all the meaning | 4 |
| tr_amb_clinical | MI ambivalence | scn_amb_caregiving | clinical-adjacent (patient ambivalent about a treatment change) | power distance, medical vocabulary, high stakes | 4 |

## Transfer Rules
- Run transfer only after the source skill shows sustained proficiency at level >= 2
  (proficiency_gated escalation applies to transfer too).
- Transfer results are evidence for the learner, not grades: record what generalized
  and what did not, anchored to turns.
- A transfer gap names the next practice target; it does not invalidate the base skill.
- Transfer scenarios reuse the SAME rubric (amb_mi_fidelity_v1) — generalizing the
  SAME dimensions is the point of the test. The spirit gate and the
  no-premature-closure guard apply in transfer exactly as in base.
- The user chooses which transfer context to attempt; the agent proposes, never assigns.
- tr_amb_clinical is optional-flagged: only run when the learner's real practice
  context includes clinical conversations, and never as a substitute for
  supervised clinical training (RECONSTRUCTED boundary note).

## Building New Transfer Scenarios
A good transfer scenario changes ONE structural axis (context, relationship power,
channel, stakes) and keeps the target skill dimensions identical. Changing two
axes at once confounds the generalization signal. Persona sanitization audit is
required before any new persona is used (Ma 2025, VERIFIED: persona priming can
degrade performance and embed bias).
