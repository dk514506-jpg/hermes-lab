# Whole-Project Review — Decision Memos (for Dallas)

Date: 2026-08-06
Source: judge_deepseek_whole_project.txt (the whole-project verdict, 4.7/5 DEPLOY)
Status: DECISION MEMOS — the judge's recommendations that require user judgment
per the campaign's own sovereignty principles. Each memo: the finding, the
options, the recommended default, and what happens if deferred. These are
Pip's proposals; Dallas disposes.

## Memo 1 — Q11: wire the HEB boundary gate at the execution layer [HIGH]

**The finding (judge):** `boundary_gate: required` is declared on all 8 skill
nodes and the policy is fully specified, but no runtime mechanism BLOCKS an
AtomicOp without a boundary pass. "A declared firewall is not a working
firewall" — the first gap that would bite in real use.

**The options:**
1. Hermes plugin hook — a small plugin that intercepts AtomicOps on
   task_meaning_level ≥ medium or protected-class match and refuses execution
   without a boundary pass. Real enforcement, matches empowerment_boundary.md
   §7's runtime contract.
2. Skill-wrapper — each skill's SKILL.md gains an explicit
   "BOUNDARY GATE: refuse all ops until boundary pass" preamble; enforcement
   is instruction-level (weaker, but zero new code).
3. Defer to Phase 9 — document the design, wire after the acceptance test.

**Recommended:** Option 1 (plugin hook), scoped as a Phase 9 lead item after
the acceptance test — the judge agrees enforcement matters most once the
harness actually runs. Option 3 is acceptable interim if Dallas wants zero
new machinery now.

## Memo 2 — Q7: reward-undermining vs BCT 10.x arbitration [MEDIUM]

**The finding (judge):** Deci 1999 (VERIFIED: external rewards undermine
intrinsic motivation) vs BCT 10.x reward techniques in Proximal_Practice_
Selector — no arbitration rule recorded. This gates the BCW/BCT layer.

**The options:**
1. Default prohibition: BCT 10.x reward techniques are NEVER auto-selected;
   permitted only on explicit user request, with the Deci-undermining risk
   disclosed. (Recommended — matches the evidence: Deci 1999 VERIFIED;
   ProEvent/PROBE ceilings 26-40%; the campaign's own anti-manipulation
   stance.)
2. Conditional allowance: rewards permitted for already-extrinsic behaviors
   (per Eisenberger & Cameron 1996 counter-evidence, preserved in Contrary A3),
   never for intrinsic ones — a domain-tagged rule.
3. Stay open: record both options, defer the decision to the BCW/BCT build.

**Recommended:** Option 1 as the default with Option 2 as a documented
exception path. Either way, the rule must be RECORDED (register + verifier)
so the arbitration isn't silently improvised at build time.

## Memo 3 — BCW/BCT intervention-design layer [MEDIUM]

**The finding (judge):** canvass_full_range, select_bct, and
retrocode_delivered_plan are UNINSTANTIATED — the diagnostic spine
(COMB → TDF) has no built successor that converts diagnosis into an
intervention plan. The "diagnosis → intervention" promise is deferred.

**The options:**
1. Build the 9th package (Behavior_Change_Intervention) — the three ops as a
   package, gated by the Q7 arbitration rule. Real pipeline completion.
2. Formally de-scope — record in DEFERRED_PACKAGES.md with activation
   criteria ("after N dojo sessions demonstrate diagnostic value"), so the
   MVP is honestly declared without the intervention layer.
3. Extend COMB instead — add the three ops to COMB as a successor stage.

**Recommended:** Option 2 now (formal de-scope with activation criteria) —
the MVP is already complete and the judge's own verdict is DEPLOY; building
the intervention layer before ANY runtime evidence would violate the
campaign's anti-premature-coherence discipline (Valens principle 10). Option
1 becomes the Phase 9/10 lead once dojo sessions produce diagnostic value.

## Memo 4 — Q8: OneDrive/SharePoint write path [LOW-MEDIUM]

**The finding (judge):** the upload path is still manual (Pip generates,
Dallas uploads). The judge suggests deciding rclone/onedrive CLI vs manual.

**The options:** 1) rclone (one-way sync, scripted, checksummed), 2) manual
(as now), 3) OneDrive CLI. Recommended: rclone for the harness estate only,
manual for the journal/wiki. Low urgency — nothing blocks deployment.

## What I did NOT decide (per sovereignty)

- Q7's arbitration rule (Memo 2) — a motivational-ethics decision, yours.
- BCW/BCT build-vs-descope (Memo 3) — a scope decision, yours.
- Q8 mechanism (Memo 4) — an environment decision, yours.
- Q11 wiring timing (Memo 1) — a machinery decision, yours.

## What I DID integrate (no judgment needed)

- Stale Skill_Package_QA_Checklist TDF rows → CLOSED (Calibration_Log row 21)
- Flag-semantics grep guard → built and verified (row 22, verify_phase8 check 6)
- Whole-project verdict recorded in the calibration record
- All four memos above written for Dallas's review
