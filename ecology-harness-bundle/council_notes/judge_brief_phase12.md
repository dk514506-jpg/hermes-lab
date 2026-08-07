# Phase 12 Judge Brief — Conditional Package Activation

Judge: DeepSeek (nous portal deepseek-v4-flash-0731) — adversarial outside judge
Locus: independent validator (separate pass)

## What to review

Read these artifacts (in order):
1. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase12_Plan.md
   (the plan + binding decisions; governance trigger)
2. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/GitHub_PoC/skills/Material_Arrangement_Scan/
   (9-file package: SKILL.md, skill_node.json, atomic_ops.json, edge_map.json,
   state_schema.json, examples.md, support_ops.md, recovery_ops.md, evaluation_notes.md)
3. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/GitHub_PoC/skills/Feedback_Ecology_Map/
   (same 9-file set)
4. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase12_Activation/phase12_conditional_packages.py
   (executable ops — the 6 atomic ops as deterministic code)
5. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase12_Activation/verify_phase12.py
   (the verifier)
6. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/GitHub_PoC/skill_graph_index.json
   + /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/GitHub_PoC/lattices/T2R_traceability.json
   (activation wiring: edges un-quarantined, 6 ops flipped to instantiated)

Context: The two conditional packages from DEFERRED_PACKAGES.md were
activated by Dallas's user-request trigger (the documented activation
branch). Material_Arrangement_Scan = practice-theory lens (Shove et al.
2012: materials/competences/meanings; bundles); Feedback_Ecology_Map = NPT
embedding-work (May & Finch 2009: coherence + CMO realist-eval). Discipline
carried: "cues supplement, never replace, practice"; meanings user-owned
(agent surfaces, never imposes); identity-level reframes require explicit
confirmation (Phase 11 confirmed-Q2 path); user defines meaning (agent asks,
never supplies); CMO hypotheses are claim-level hypotheses, never verdicts.

## Success criteria

Judge against:
A. Do the packages faithfully implement their theory (practice-theory
   materials/competences/meanings + bundles; NPT coherence + CMO)?
B. Is the discipline actually carried in BOTH the schema (atomic_ops
   guardrails) AND the executable code (phase12_conditional_packages.py)?
C. Is the activation honest? (edges un-quarantined, T2R flips, no
   overclaiming — e.g. assess_participation/collective_action/monitoring
   are REGISTERED-NOT-BUILT, not claimed built)

## What to return (structured)

1. VERDICT: DEPLOY / REVISE / BLOCK (one line)
2. Score 0-5 with one-line justification
3. KERNEL — what is strong and should be preserved exactly as-is (max 5)
4. WEAKNESSES — numbered, each with severity HIGH/MED/LOW and a concrete fix
5. HONESTY CHECK — anything that overclaims: does the executable implement
   what the schema declares? do the guardrails exist in code or only in
   JSON? is the activation wiring honest (nothing claimed built that isn't)?
6. DISCIPLINE CHECK — Valens: premature coherence (does the package claim
   more than it delivers?), user-owned meaning (no imposed reframes),
   claim-level hypotheses (no verdicts), identity confirmation gating.
7. RECOMMENDED REVISIONS — the minimal list that would move you to DEPLOY.

Be adversarial. The campaign's history: judges caught dead fail-open flags,
mis-aimed guards, wholesale pass-throughs, evidence strings asserting facts
absent from input, stand-in disclosures missing from registries. Assume
this phase has an analogous hidden flaw and find it. READ THE ACTUAL CODE —
do not trust docstrings. Note the deterministic stand-in parsing
(environment split on ";") — is that disclosed honestly as a stand-in for
real text parsing?
