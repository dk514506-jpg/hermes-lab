# Whole-Project Review Rubric — Phases 1-8 (for outside judges)

Project: Motivational Ecology Agent Architecture — Ecology Foundation Campaign
Rubric date: 2026-08-06
Purpose: A detailed, artifact-referenced rubric by which an outside judge
(Claude Sonnet 4.5, independent of the build process) evaluates the TOTALITY
of the campaign output — Phases 1 through 8. The judge reads artifacts, not
assurances; scores are evidence-based.

## Scoring convention

For each dimension: score 0-5 (0 = absent/broken, 3 = acceptable, 5 =
exemplary), with a one-line justification naming the artifact(s) the score
rests on. A dimension may be N/A with reason. Final verdict: overall score +
the single strongest artifact + the single weakest artifact + 5 concrete
recommendations.

## The artifacts (what the judge reads)

- Phase 1: docs/Ecology/Foundation/Foundation_Matrix.md, Construct_Map.md,
  Theory_to_Routine_Interface.md
- Phase 2: Recent_Evidence_Digest.md, Annotated_Bibliography.md,
  Contrary_Findings_and_Limits.md, council_notes/phase2_api_seed.md
- Phase 3: docs/Ecology/Foundation/Phase3_Skills/ (8 skill packages, 90 files)
- Phase 4: skill_graph_index.json, lattice_index.json,
  skill_lattice_interface.md, insight_trigger_policy.md, T2R_traceability.json
- Phase 5: docs/Ecology/Foundation/Phase5_Safeguards/ (5 documents)
- Phase 6: docs/Ecology/Foundation/Phase6_Dojo/ (5 dojos, 36 files)
- Phase 7: docs/Ecology/Foundation/Hermes_Agent_Harness/ (the packaged tree)
- Phase 8: docs/Ecology/Foundation/Phase8_Evaluation/ (5 evaluation documents)
- Governance: docs/Ecology/03_Open_Questions_Register.txt, 05_Project_Atlas.txt,
  Foundation/handoff_notes.md, council_notes/ (critiques, judge reports,
  verifiers)

## Dimensions

### A. Evidence Discipline (weight: high)
A1. VERIFIED/RECONSTRUCTED/UNVERIFIED flags applied consistently across all
phases, not just Phase 2. Sample: do Phase 3-7 artifacts carry flags that
mean the same thing as Phase 2's?
A2. Witness conflicts preserved, not harmonized (TDF 12-vs-14, reward-
undermining dispute, Bastani-vs-Brynjolfsson tension).
A3. Integrity handling: retracted/withdrawn work register-only; preprints and
opinion articles correctly qualified (Jose 2025, CALM-IT, Beacock).
A4. Anti-fabrication: citations trace to real sources; no invented DOIs.

### B. Coherence and Truthfulness (weight: high)
B1. Cross-phase consistency: do Phase 3 packages instantiate Phase 1 theory?
Do Phase 4 edges match Phase 3 packages? Does Phase 5 governance bind Phases
3/4/6? Does Phase 7 packaging contain what its README claims?
B2. The "single source of truth" problem: does skill_graph_index.json agree
with per-package edge_maps? Is divergence documented, not hidden?
B3. Self-description accuracy: do READMEs and handoff notes tell the truth
about status (no "all VERIFIED" style overclaims)?
B4. Correction history: are past errors recorded and guarded (Calibration_Log,
verifier guards)?

### C. Architectural Quality (weight: medium)
C1. Does the 5-layer architecture (lattice, skill graph, safeguards, dojos,
evidence) actually interconnect, or is it decorative?
C2. Are the AtomicOps/typed-edge/state-schema conventions honored consistently?
C3. Is the empowerment boundary (ACT/SCAFFOLD/ASK/DEFER/STOP) encoded in
artifacts, not just prose?
C4. Is the learnability/atrophy machinery (skill_load_score, fade rules,
readiness gate) operational or aspirational?

### D. Governance and Continuity (weight: medium)
D1. Is the campaign registered in its own ecology (Open Questions Register,
Project Atlas, handoff notes)?
D2. Would a fresh agent resume the campaign from disk (handoff_notes.md,
journal)?
D3. Does the self-application gap (Q10: campaign over-assists the user) get
honest treatment?
D4. Are deferred items (packages, ops) documented with reasons and activation
criteria?

### E. Verification Depth (weight: high)
E1. Do the verify_phaseN.py verifiers exist, run, and enforce real
consistency classes (not just file presence)?
E2. Do the verifiers catch the classes of error the review rounds actually
found (flag drift, missing anchors, edge divergence, stale paths)?
E3. Is verification reproducible (in-tree verifier in the harness)?
E4. Was outside-judge feedback (Claude, DeepSeek) integrated, with the
findings recorded?

### F. Valens Discipline Transposition (weight: medium)
F1. Hypothesis-status over doctrine: are insights/profiles/diagnoses labeled
hypotheses, user-correctable?
F2. Quarantine law: user-rejected insights removed regardless of evidence
strength; identity-level claims default to quarantine.
F3. No premature closure: ambivalence and open questions are designed halt
states.
F4. User interpretive sovereignty: the agent proposes, the user disposes;
no manipulation, no surveillance.

### G. Practical Usability (weight: low-medium)
G1. Could a fresh reader install and use the Phase 7 harness?
G2. Could a practitioner run a dojo session per the artifacts?
G3. Is the deferred/roadmap state clear (minimum viable library vs incomplete)?

## Judge output format

1. Per-dimension scores (A-G) with artifact-cited justifications
2. Three strongest artifacts (named, with why)
3. Three weakest artifacts or gaps (named, with why)
4. Five concrete recommendations, priority-ordered
5. Overall verdict: deploy/revise/rebuild for the stated purpose (a governed
   learning-and-agency-support architecture for a home-lab Hermes harness)
