# Phase 5 — Empowerment and Learnability Safeguards

Project: Motivational Ecology Agent Architecture
Phase: 5 of 8 — the two anti-domestication controls
Date: 2026-08-06
Status: COMPLETE — five deliverables, Council-built, reviewed, revised, verified

## The Two Controls

Per the research plan v2 (Phase 5): "Add the two key anti-domestication
controls: Do not steal human agency. Do not create skill atrophy."

## Deliverables

| File | Control | What it is |
|---|---|---|
| empowerment_boundary.md | agency | Estate-wide rulebook for NOT stealing human agency: five modes (ACT/SCAFFOLD/ASK/DEFER/STOP), the preserved_user_decision set (6 categories), 10 absolute prohibitions, escalation ladder L1-L5, quarantine-law interaction. |
| agent_deference_rules.md | agency | WHEN the agent defers: defer triggers, DEFER/STOP mechanics (what it says + records), silence-as-action, propose/dispose asymmetry, pressure-free re-opening. Includes the estate-wide dispatch table for runtime. |
| learnability_state_schema.json | atrophy | Estate-wide JSON Schema (ecology-learnability/0.1) tracking skill_load_score (0..1, canonical), trend (derived), baseline/recent tracks, assistance_fraction, dependency_ratio, and the inverse empowerment_ratio. |
| skill_atrophy_risk_check.md | atrophy | The operational check: when it runs, the 5-step pipeline, risk classification (none/low/medium/high) with precise criteria, what each level means for scaffolding. Canonical warning: Budzyn 2025 (VERIFIED, ADR 28.4%→22.4%). |
| scaffolding_fade_rules.md | atrophy | Estate-wide fade rules: fade is mandatory, triggers vs holds (hold beats fade), hints>answers gradient, scaffold ladder 5→0, stepwise bidirectional pacing, readiness-gate timing (Liu 2026), unassisted-metrics signal, what never fades. |

## Governance

- Owner: Human_Empowerment_Boundary (all five documents)
- Every threshold is a RECONSTRUCTED calibration anchor, not study-validated
  doctrine; revisions require new VERIFIED evidence
- Estate scope wins over package-local statements; conflicts recorded, not
  harmonized (Valens discipline)

## Verification

council_notes/verify_phase5.py — 21 checks, exit 0:
schema validity (draft-07 meta-check), realistic-instance conformance,
negative tests (invalid enum/range rejected, required fields enforced),
$ref integrity, markdown section presence, and the post-review truthfulness
guards (Jose 2025 opinion-caveat, CALM-IT preprint flag).

## Review Round (2026-08-06)

Post-build critical review found and fixed two truthfulness issues:
1. Jose 2025 cited as plain VERIFIED in skill_atrophy_risk_check.md — it is
   an OPINION article per the digest quality register; now carries the caveat.
2. CALM-IT (Nguyen 2026) cited without its preprint status in
   scaffolding_fade_rules.md — now flagged in text and the evidence register.
Both locked in as durable verifier guards. All other citations verified
against the Phase 1-2 artifacts (Kuchipudi, Beacock, Heudel, Budzyn, Bastani,
Brynjolfsson, Liu, Shaikh, ProEvent/PROBE, Lee, Eiroa-Solans, Natali, Chen).

## Handoff to Phase 6

Phase 6 (Practice Dojo Routines) builds the ConvoDojo layer: dialogue state
machine, persona bank, rubric, sparring intensity, in-session coaching,
debrief template, transfer scenarios. The safeguards here govern that layer
(ConvoDojo pairs with PPS for sparring-scaffold fading).
