# Campaign Self-Application Log (Q10)

Project: Motivational Ecology Agent Architecture
Purpose: Operationalize Open Question Q10 — "is Dallas deskilled by the
councils that read for him?" The campaign's headline principle (skill
preservation is a measured objective) applies to the campaign itself. This
log records, per phase, what Dallas did unassisted vs what councils/agents
did, so the campaign can track its own skill_load instead of assuming it.
Created: 2026-08-06 (Phase 8 revision round — judge recommendation, Claude 5.4)

## The metric

- assistance_fraction per phase: 0 = Dallas solo, 1 = councils/agents solo
- capability direction: rising (Dallas can now author/QA solo), flat (can QA
  but not author), falling (approves without understanding)

## Per-phase record

| Phase | Dallas unassisted (user-side) | Pip + Councils (agent-side) | Est. assistance fraction |
|---|---|---|---|
| 1 (Foundation) | Specified the research plan, chose internet-over-PDFs, set Valens-style discipline | Council distilled 8 frameworks; Pip assembled matrix/map/interface | 0.7 (Dallas set direction, approved each council output) |
| 2 (Evidence) | Set the 2025-2026 window, flagged preprint/opinion quality classes as a value | Council fetched 78+ sources; Pip built API probe + seed registry | 0.8 (Dallas reviewed the digest's quality-register decisions) |
| 3 (Skills) | Approved the 9-file canonical pattern, kept recent-evidence-distillation | Council built 8 packages (90 files); Pip verified structurally | 0.8 |
| 4 (Graph/Lattice) | Approved "proceed with assumptions" on edge conventions | Pip reconciled graph/lattice; decisions 1-7 recorded | 0.6 (Dallas reviewed and approved the Phase 4 decisions) |
| 5 (Safeguards) | Requested the review-revise cycle; approved the 0731 flip | Council built 5 safeguards; Pip reviewed + fixed 2 truthfulness issues | 0.7 |
| 6 (Dojos) | Requested plan-then-execute revision discipline | Council built 5 dojos; Pip planned + executed the revision round | 0.7 |
| 7 (Harness) | Requested outside-judge round (Claude + others) | Council packaged; judges critiqued; Pip integrated R1-R5 | 0.7 |
| 8 (Evaluation) | Requested the whole-project review + Claude judge with rubric | Council built evaluation; judges critiqued; Pip integrated | 0.7 |

## Capability evidence (rising or falling?)

- Dallas's decisions this campaign that REQUIRED domain judgment: setting the
  evidence window, approving the canonical pattern, choosing to keep the
  council-created skill, requesting plan-before-execute, requesting
  cross-provider judges, specifying the review rubric dimensions. These are
  governance-level judgments, not passive approvals.
- What Dallas has NOT yet done solo: authored a skill package from scratch,
  run a verifier, edited a JSON artifact directly. The campaign has scaffolded
  him on the artifact layer.
- Verdict so far: **FLAT-to-RISING at the governance layer, SCAFFOLDED at the
  artifact layer.** The campaign has not deskilled Dallas (he makes the
  binding decisions) but has not yet demonstrated unassisted artifact
  authoring either.

## Counter-measures (active)

1. One unassisted user task per phase — START: Dallas reviews this log, the
   Calibration_Log, and the whole-project review verdicts, and issues a
   written judgment (the Q10-relevant unassisted act for Phase 8).
2. The Phase 8 acceptance test (Evaluation_Rubric.md §1.9) is a Dallas-run
   dojo session — an unassisted artifact-layer act.
3. Next campaign cycle: Dallas authors one skill package (or one dojo) with
   Pip as reviewer, not author — inverting the current division of labor.
4. This log is updated at each phase boundary going forward (assistance
   fraction + capability evidence), per Evaluation_Rubric.md §1.4.
