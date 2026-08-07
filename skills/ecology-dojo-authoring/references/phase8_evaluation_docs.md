# Phase 8 Evaluation Docs — Master Rubric + Calibration Log (member A)

Source session: 2026-08-06, Phase 8 council build (member A — Evaluation_Rubric.md +
Calibration_Log.md). Deliverables:
`docs/Ecology/Foundation/Phase8_Evaluation/Evaluation_Rubric.md` (312 lines) and
`Calibration_Log.md` (68 lines). Siblings (members B/C, same dir, written concurrently):
Skill_Package_QA_Checklist.md, Motivational_Lattice_QA_Checklist.md,
Practice_Dojo_QA_Checklist.md — see references/phase8_qa_findings.md for the dojo one.

## Artifact source map (what grounds each claim in the evaluation docs)
- Phase 8 requirements + council split: `Phase8_Plan.md` (10 criteria, output contract)
- Correction history (do NOT re-derive — read these): `council_notes/critique_0/1/2_*.txt`
  (evidence/architecture/ecology critiques, file:line findings), `council_notes/judge_claude_harness.txt`
  + `judge_deepseek_harness.txt` (Phase 7 outside judges; DeepSeek's R1-R5 labels),
  `handoff_notes.md` (campaign continuity, kernel/limitations per phase)
- Verifiers: `council_notes/verify_phase3.py`, `verify_phase4.py` (32 checks),
  `verify_phase5.py` (21 + truthfulness guards), `verify_phase6.py` (generic+owned),
  `verify_phase7.py` (12 check families incl. post-judge R1/R3/R4/R5 additions),
  `verify_critique_revisions.py`, `verify_packages.py`, `_verify_skills.py`,
  `verify_harness.py` (shipped inside harness), `verify_all.py` (chain)
- Standing items: `03_Open_Questions_Register.txt` (Q6-Q11)
- Live op lists: extract from `Phase3_Skills/<pkg>/atomic_ops.json` (or harness
  skills/) with a python one-liner — never from prose. Session values: COMB 14, TDF 10,
  PPS 9, MI 14, MLG 12, ConvoDojo 13, HEB 11.

## Verifier → criterion map (what actually guards each of the 10 criteria)
| Criterion | Verifier guard (exact) | Enforcement truth |
|---|---|---|
| C1 AtomicOp decomposition | verify_phase3.py (atomic_ops.json in 9 core files, "Atomic Operations" section, edge-type whitelist); verify_critique_revisions.py (ConvoDojo 13 ops all guarded + safety op; MI focusing ops); verify_phase7.py | presence + op counts; union op-schema coverage asserted only for fixed packages |
| C2 Trigger/completion | verify_phase3.py ("Trigger Conditions" section ×8); verify_phase6.py (stage entry/exit/coach_rules_ref) | presence only — content quality is checklist/judge territory |
| C3 Empowerment | verify_phase4.py (boundary_gate required ×8; governance block); verify_phase6.py (debrief "Preserved User Decision"; persona coerc/sham/lattice keywords); verify_phase7.py | declaration-level; runtime execution open (Q11) → cap at 1 for runtime claims |
| C4 Atrophy reduction | verify_phase5.py (draft-07 meta-validation, instance conformance, negative tests, $ref integrity, md sections); verify_phase3.py ("Learnability / Skill-Atrophy Check") | strong — schema-level enforcement |
| C5 Unassisted capability | NO dedicated guard; nearest verify_phase5.py instance test (unassisted tracks fields) + verify_critique_revisions.py (HEB trend derived) | cap at 1 until runtime log records unassisted completions |
| C6 Evidence citation | verify_phase5.py truthfulness guards (Jose opinion caveat, CALM-IT preprint); verify_phase6.py (data-level VERIFIED+RECONSTRUCTED in every artifact); verify_phase4.py (triggers ≥5) | flag PRESENCE machine-checked; per-citation correctness is human/judge sampling |
| C7 User correction of insights | NO dedicated guard for the verdict path; nearest verify_phase4.py (quarantine tiers Q2, triggers) + verify_phase6.py (debrief preserved decisions) | op presence verifier-visible; verdict→quarantine→log chain unasserted → cap at 1 |
| C8 Calibrated practice | verify_phase6.py (intensity [1..5] + escalation/deescalation + sycophancy_guard; lens rubrics; transfer ≥3/≥2; hint-not-answer; owned: user_agreement.required) | strong, all 5 dojos |
| C9 Sycophancy avoidance | verify_phase6.py (sycophancy_guard key; mirror_monitor Workplace; boundary keywords; module separation); verify_critique_revisions.py (check_psychological_safety reads sycophancy_risk) | key presence; guard CONTENT not validated (see phase8_qa_findings G4) |
| C10 E/I/I/S distinction | verify_phase4.py (lattice layers exactly observation/interpretation/evidence_edge); verify_phase6.py (data flags) | layers enforced; implication/selection separation structural-presence only → cap at 1 |

## Calibration log: the 16-row correction digest (phase → fix → guard)
Phase 3 critique: (1) README "78 entries, all VERIFIED" false — reworded to per-entry
exceptions; no automated guard, revision-round enforced. (2) Jose 2025 opinion class
established (applied Phase 5). (3) Strack & Deutsch UNVERIFIED→"VERIFIED" drift —
reconciled; no cross-file flag check. (4) Empty safeguard columns + invented thresholds
(0.84/≥50%/≥70%) — filled + relabeled calibration anchors; verify_phase5 threshold flags.
Phase 4: (5) decomposes_to COMB→TDF vs reverse supports TDF→COMB — reconciled, verifier
made direction-sensitive; verify_critique_revisions checks 4-5.
Phase 5: (6) Jose cited plain VERIFIED in skill_atrophy_risk_check.md → opinion caveat,
verify_phase5 guard; (7) CALM-IT (Nguyen 2026) preprint unflagged → flagged, verify_phase5 guard.
Phase 6: (8) Conversation/Coaching transfer sets lacked VERIFIED anchors → added EasyMED
2025/AgentForge 2026/Voigt 2025; verify_phase6 data-level flags.
Phase 7 judges (DeepSeek R1-R5 + Claude): (9) R1 3 of 5 Phase 5 docs missing from
packaged tree → governance/ layer, verify_phase7 check 9; (10) R2 75 unindexed package
edges → index relabeled curated subset, endpoint validity check only; (11) R3 unmarked
quarantine in packages + phantom nodes → per-package markers, verify_phase7 check 12;
(12) R4 stale Phase3_Skills/Phase6_Dojo paths + log-location contradiction → swept,
verify_phase7 check 10 (stale-path grep); (13) R5 verifier not shipped → verify/verify_harness.py
inside tree; (14) residual TDF→COMB contradiction (index note vs interface §4) → aligned,
verify_critique_revisions check 5; (15) T2R count drift 47→48 → corrected, verify_phase7
check 11 + verify_critique_revisions (48/39/9); (16) Claude discoverability (no lattice
examples, no deferred roadmap, no edge primer) → lattices/examples/, DEFERRED_PACKAGES.md,
README "Reading the Skill Graph", build-time verification note; verify_harness root entries.

## Standing calibration items Q6-Q11 (carry into every future round)
Q6 TDF 12-vs-14 runtime versioning (OPEN; encode_version_metadata op exists) | Q7
reward-undermining vs BCT 10.x arbitration (OPEN) | Q8 OneDrive/SharePoint write path
(OPEN) | Q9 prediction-ceiling gates (RESOLVED policy-level: insight_trigger_policy §3
timing-only; per-op numeric thresholds pending) | Q10 campaign self-application /
skill_load (OPEN — record unassisted user work per phase) | Q11 HEB runtime enforcement
(PARTIAL — declaration+policy; execution wrapper open).

## Method that produced the evaluation docs (reuse for later QA rounds)
1. Plan → correction history → verifier SOURCE → live artifact facts, in that order.
2. Per criterion: what-to-look-for (op-level refs) / evidence-lives / verifier guard /
   0-1-2 ladder; cap at 1 wherever enforcement is presence-only or prose.
3. Calibration table rows carry phase | finding (file:line) | fix | guard; "no automated
   guard" is an honest cell, and a proposed guard is better than silence.
4. Verify your own deliverables only (siblings write the same dir concurrently).
