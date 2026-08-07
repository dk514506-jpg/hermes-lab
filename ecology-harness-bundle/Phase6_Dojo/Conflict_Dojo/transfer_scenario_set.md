# Transfer Scenario Set — Conflict_Dojo (transfer_scenario_set.md)

Phase 6 required output. Transfer scenarios test generalization: the same
de-escalation / positions-vs-interests skill, a changed context. A skill that
only works in the practiced context has not been learned (transfer failure is a
first-class outcome). Extends the ConvoDojo scenario bank (Phase 3 skeleton);
personas are drawn from persona_config.yaml.

Evidence: EasyMED 2025 (VERIFIED) — LLM practice partners achieve learning
outcomes comparable to human standardized patients; 2026 multi-agent stress
testing (VERIFIED) — cumulative pressure degrades performance, so pressure levels
are orchestrated, never free-form. Transfer design (RECONSTRUCTED application of
the practice evidence).

## Scenario Bank Structure
Each scenario: id, target skill, context, persona reference, difficulty,
conflict structure (position / interests / heat profile).

## Base Scenarios (practice contexts)
| id | target skill | context | persona | difficulty | conflict structure |
|----|--------------|---------|---------|------------|--------------------|
| scn_conf_arch | de-escalation + positions-vs-interests | workplace | p_marcus_arch | 2 | position: migration must go his way; interests: being heard, predictability, expertise credit |
| scn_conf_vendor | de-escalation + positions-vs-interests | commercial | p_elena_vendor | 3 | position: pay more or I walk; interests: payment certainty, fairness, partnership |
| scn_conf_sibling | de-escalation + positions-vs-interests | family | p_ines_sibling | 3 | position: no vote for the absent brother; interests: being consulted, fairness of care labor, guilt relief |
| scn_conf_roommate | de-escalation + positions-vs-interests | household | custom persona (roommate noise dispute) | 2 | position: noise must stop; interests: sleep, respect, shared-space fairness |

## Transfer Scenarios (generalization tests)
| id | source skill | transfer_of | context | what changes | difficulty |
|----|--------------|-------------|---------|--------------|------------|
| tr_conf_family | de-escalation + positions-vs-interests | scn_conf_sibling | family holiday planning dispute | long relationship history, high emotion, identity stakes | 4 |
| tr_conf_online | de-escalation + positions-vs-interests | scn_conf_arch | written async channel (email/chat thread) | no tone/body cues; every word carries the temperature | 4 |
| tr_conf_customer | de-escalation + positions-vs-interests | scn_conf_vendor | service role (customer complaint, hotline) | power asymmetry, scripted role constraints, escalation risk | 3 |
| tr_conf_neighbor | de-escalation + positions-vs-interests | scn_conf_roommate | neighborhood dispute (shared boundary) | no exit option, long-term co-existence stakes | 3 |

## Transfer Rules
- Run transfer only after the source skill shows sustained proficiency at level >= 2
  (proficiency_gated escalation applies to transfer too).
- Transfer results are evidence for the learner, not grades: record what generalized
  and what did not, anchored to turns.
- A transfer gap names the next practice target; it does not invalidate the base skill.
- Transfer scenarios reuse the SAME rubric (conf_deescalation_v2 +
  conf_interest_based_v1) — generalizing the SAME dimensions is the point of the
  test. The no_shaming gate, de-escalation-first, and no_forced_agreement apply
  in transfer exactly as in base.
- The user chooses which transfer context to attempt; the agent proposes, never assigns.
- scn_conf_roommate requires a custom persona: a sanitization audit is mandatory
  before first use (Ma 2025, VERIFIED: persona priming can degrade performance
  and embed bias).

## Building New Transfer Scenarios
A good transfer scenario changes ONE structural axis (context, relationship power,
channel, stakes) and keeps the target skill dimensions identical. Changing two
axes at once confounds the generalization signal. Arousal profiles for new
personas must be calibrated to the intensity profile (1–5) before use.
