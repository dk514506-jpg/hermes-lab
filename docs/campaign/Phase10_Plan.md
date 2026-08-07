# Phase 10 Plan — FAOS × Ecology Integration

Project: Motivational Ecology Agent Architecture
Plan date: 2026-08-07
Status: PLAN — written before execution. Dallas directive: "proceed with
assumptions and complete phase 10 with the help of Locus and the Council."
Assumptions = the FAOS_Ecology_Integration_Memo.md D1-D5 recommendations,
locked as decisions below.

## Decisions (from the memo, now binding — Dallas "proceed with assumptions")

- **D1 — Quarantine reconciliation: ACCEPTED (memo §4).** Two scales, typed,
  independent axes: FAOS Q0-Q10 (claim trust, epistemic) + Ecology Q0-Q5
  (use permissibility, agency). Never added or averaged. Load-bearing rule:
  FAOS clearing a claim never licenses Ecology's use of it; Ecology's
  user-rejected class is final regardless of FAOS tier.
- **D2 — Gate mechanics: ACCEPTED (memo §6 D2).** Ecology's
  select_empowerment_mode is the FAOS gate. Mode → FAOS result states:
  ACT→TRUE, SCAFFOLD→PARTIAL, ASK→INCONCLUSIVE, DEFER→PARTIAL, STOP→BLOCKED.
- **D3 — Close discipline: ACCEPTED (memo §5 Phase B).** Dojo sessions close
  through the FAOS 6-pass instrumented close.
- **D4 — Scope: FULL engine import + gate adapter (memo §5 Phase A).**
  faos_engine_extension.py imported; gate adapter wired; S0-S9 + absence
  gating become enforced at the engine level per the FAOS engine's contract
  (explicit prohibited_edges blocklist S6→S5/S8→S3/S0→S5 + halt-state
  membership — the engine's honest enforcement surface; full stepwise +
  pre-declared-selector promotion is recorded as a Phase 11 item).
- **D5 — Memo stays at docs/Ecology/Foundation/FAOS_Ecology_Integration_Memo.md.**

## What Phase 10 delivers

1. A merged integration module: `integration/faos_ecology_engine.py` that
   imports the FAOS engine machinery and adds the Ecology gate (5-mode
   selector → FAOS result states) + quarantine two-typing + S0-S9 item
   lifecycle + absence gating.
2. A merged config: `integration/faos_ecology_config.yaml` — FAOS blocks
   (evidence ladder, state lineage, quarantine two-typed, absence register,
   non-op registry, typed metrics, close) + Ecology wiring (gate → modes,
   roles incl. locus, dojo close binding).
3. Dojo close wrapper: the DojoClose class (6-pass instrumented close
   applied to any dojo session record) — shipped INSIDE
   faos_ecology_engine.py (integration memo Phase B; plan-vs-file naming
   reconciled in the Phase 10 revision round, R8).
4. Verifier: `integration/verify_integration.py` — asserts the merged
   config loads under FaosConfig, gate maps all 5 modes, quarantine is
   two-typed, absence register fails closed, S0-S9 lifecycle enforced,
   dojo close has 6 passes, both legacy suites still pass.
5. Witness run: one dojo session walked through the MERGED pipeline
   (gate → mode selection → close) — criterion B for the integrated estate.

## Architecture (from memo §1)

FAOS engine = gateway infrastructure (intake → triage → research → route →
GATE → fulfill → close). Ecology = Guardian intellect: at the GATE stage,
select_empowerment_mode decides ACT/SCAFFOLD/ASK/DEFER/STOP; the outcome
feeds FAOS result states. Locus arbitrates (route validity, evidence
ladder, shadow promotion, close completeness, mode-selection validity).

## Verification plan

- verify_integration.py (new, ~15 checks) exit 0
- FAOS canonical suite (scripts/run_tests.sh) still exit 0
- Ecology full gate (verify_all.py incl. phase9) still exit 0
- Witness run through merged pipeline exit 0

## Judge + revise (Dallas directive)

- Locus validation (7-check discipline) — subagent, retry-then-direct on 503
- Council critique (DeepSeek outside judge, adversarial) — subagent
- Self-review revision round: read my own output critically, apply sublative
  method, re-verify
- Record in Calibration_Log + journal

## Out of scope

- BCW/BCT COMB stage (Phase 11 — plan only, per Dallas's ordering)
- Material_Arrangement_Scan / Feedback_Ecology_Map (activation criteria unmet)
- Autopoietic_Boundary_Check (indefinite hold)
- Astral persona compatibility (deferred by choice, Q3.2)
- Gateway runtime execution (still architectural until a platform is wired)
