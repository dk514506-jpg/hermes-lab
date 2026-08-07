# Phase 9 Plan — Valens × Ecology Meld

Project: Motivational Ecology Agent Architecture
Plan date: 2026-08-07
Status: PLAN — written before execution, per campaign discipline. Executes
after Dallas's 31 meld answers are compiled (done, below) and Phase 8 closure.

## What Phase 9 IS

The formal meld of the Valens Anthologies corpus with the Motivational
Ecology Agent Architecture, packaged as a phase with its own verifier and
judge round (Dallas Q6.3). Primary deliverable order per Dallas Q6.1:
(c) single estate → (b) skill library → (a) governance doc → (d) wiki
synthesis. Success criteria (Q6.4): (b) harness can run a Valens-logic-
influenced session, AND (c) Dallas can articulate the meld, AND (a) the
meld doc exists and reads coherently.

## Decision Record — compiled from Dallas's answers (2026-08-07)

| ID | Answer (verbatim intent) | Consequence |
|---|---|---|
| Q1.1 | (b) Operating logics ONLY — corpus details not day-to-day relevant | Import 10 principles + S0-S9 + Q0-Q10 + non-identity controls as governance doc; NOT the 115 artifacts |
| Q1.2 | YES | Logics become first-class harness doc: governance/valens_operating_logics.md |
| Q1.3 | YES | Ecology README carries pointer to the corpus |
| Q1.4 | YES — archive is fine | Only logics + key syntheses actively used; rest remains archive |
| Q1.5 | FROZEN as-is | Corpus frozen; no new registers added going forward |
| Q2.1 | (c) BOTH — Ecology is the operational interface between Dallas and the machine; embodies the astral persona/digital brain background; demonstrates persona through behavior structured by Ecology + its agentic harness | Ecology = governance AND skill layer for the home lab |
| Q2.2 | YES — FAOS pipeline routes THROUGH Ecology's skill graph | triage/research/route consult skill_graph_index + lattice before routing |
| Q2.3 | Depends on authority nature: FAOS rules for research/truth-finding; Ecology governs human-robot relationship | Keep TWO mechanisms + documented mapping (do not unify) |
| Q2.4 | See-R = intended knowledge base blueprint, created from Anthologies-derived principles | See-R is Ecology's evidence source layer |
| Q2.5 | YES — Locus + always-on continuity governed by Ecology's safeguards | Safeguards govern the Locus role and continuity load |
| Q3.1 | NO — astral personas stay in their own harness | No ConvoDojo conversion now |
| Q3.2 | Not ready near-term; wants eventual technical compatibility, NOT primary concern now | Doc bridge later; no schema coupling now |
| Q3.3 | NO | Astral personas not in practice dojos |
| Q3.4 | YES — inherited nature becomes schema | Add persona/user-profile node kind to lattice/skill schema |
| Q3.5 | Possible yes — separation IS the quarantine | Keep astral personas separate from ConvoDojo (already decided) |
| Q4.1 | EXEMPT — corpus exempt from evidence flags (historical archive) | No VERIFIED/RECONSTRUCTED treatment on the corpus itself |
| Q4.2 | N/A (exempt) | — |
| Q4.3 | YES — merge/cross-link witness-comparison ↔ contrary-findings | Cross-link registers |
| Q4.4 | YES — carry printed-vs-reconstructed distinction | Footnote convention in Ecology artifacts citing Valens |
| Q4.5 | Valens = source about METHOD, not findings | Method citation only |
| Q5.1 | YES one vault — valens_wiki home for ALL continuity; assume going forward; tell Dallas when a new vault would be efficient | One vault, two sections |
| Q5.2 | Wiki pointers only (Dallas unsure of difference — plan explains) | Pointers from wiki to Foundation tree; no mirroring of tree docs into wiki |
| Q5.3 | YES | Meld produces new synthesis page: syntheses/ecology-valens-meld.md (primary deliverable) |
| Q5.4 | YES — decisions journaled in wiki AND tree | Dual journaling |
| Q5.5 | ALL of us with conventions | Shared write conventions |
| Q6.1 | (c) single estate, then (b) skill library, then (a) governance doc, then (d) wiki synthesis | Delivery order enforced |
| Q6.2 | Assume embedded BUT verify | Audit the 8 packages against the 10 principles; gap report |
| Q6.3 | Formal Phase 9 with own verifier + judge round | verify_phase9.py + DeepSeek judge + revise round |
| Q6.4 | (b) AND (c) AND (a) | Success = runnable session + articulable + coherent doc |
| Q6.5 | NOW | Meld is the current project (gate wiring + BCW/BCT follow) |
| Q6.6 | NO — Pip drafts | Pip authors; Dallas reviews/disposes |

Plus current directive (2026-08-07): FAOS = gateway infrastructure; Ecology =
Guardian intellect negotiating the gateway. That is the INTEGRATION MEMO
subject (after Phase 9 completes). Phase 9 itself is the meld, not the
integration wiring.

## Deliverables (in Q6.1 order)

### D1 — Single estate (c)
1. `governance/valens_operating_logics.md` in the harness estate — the 10
   principles, S0-S9 lineage, Q0-Q10 tiers, non-identity controls, as a
   first-class governance doc beside the 5 safeguards (Q1.1, Q1.2).
2. README pointer to the Valens corpus location (Q1.3).
3. Inherited-nature schema node: add `persona` / `user-profile` node kind to
   the lattice schema (observation_schema.json / insight_node_schema.json or
   a schema extension note) (Q3.4).
4. Witness-comparison ↔ contrary-findings cross-link: the wiki registers
   (absence-register, non-operational-registry) plus a pointer from
   Ecology's Contrary_Findings_and_Limits.md to the Valens witness-comparison
   discipline (Q4.3).
5. Printed-vs-reconstructed footnote convention documented in the harness
   (Q4.4).

### D2 — Skill library verification (b)
6. Audit the 8 skill packages against the 10 Valens principles: which
   principle is embedded where, which is thin/missing. Deliverable:
   `meld/valens_principle_coverage.md` — principle × package matrix
   (Q6.2 verification mandate). Where gaps exist, record them; do NOT build
   new skills in this phase unless a gap blocks the success criteria.

### D3 — Governance doc (a)
7. `meld/ecology_valens_meld_charter.md` — the unified statement of the
   meld: what Valens supplies (method), what Ecology supplies (agency
   governance), the interface rule (FAOS=truth-finding, Ecology=relationship;
   Q2.3), the exemption rule (Q4.1), the method-not-findings rule (Q4.5).

### D4 — Wiki synthesis (d)
8. `syntheses/ecology-valens-meld.md` in valens_wiki — the primary
   deliverable: readable statement of the meld, its decisions, its
   consequences (Q5.3).
9. Journal entry in valens_wiki/journal/ (2026-08-07) recording Phase 9
   decisions + this campaign's continuity (Q5.4, Q5.5).
10. Wiki pointers (Q5.2): the synthesis links OUT to Foundation tree docs;
    tree docs link IN to the synthesis.

## Canonical estate decision

GitHub_PoC/ is the canonical meld target: it is the complete, git-ready
estate (skills + lattices + routines + governance + evidence + logs +
verify + LICENSE). Hermes_Agent_Harness/ (OneDrive/SharePoint packaging per
its own README) receives the governance doc + README pointer via mirror,
since Dallas's acceptance tests ran there — both trees stay coherent. The
wiki is the continuity home (Q5.1).

## Verifier — verify_phase9.py

Checks (each answerable from disk):
1. governance/valens_operating_logics.md exists, contains all 10 principles +
   S0-S9 + Q0-Q10 + non-identity controls.
2. README pointer to corpus present.
3. Inherited-nature schema node present (schema or extension note).
4. Cross-link present both directions (Ecology ↔ wiki registers).
5. Printed/reconstructed footnote convention documented.
6. meld/valens_principle_coverage.md exists: 10 principles × 8 packages
   matrix, every cell populated (EMBEDDED / PARTIAL / ABSENT).
7. meld/ecology_valens_meld_charter.md exists, states Q2.3 split + Q4.1
   exemption + Q4.5 method-not-findings.
8. Wiki synthesis exists (syntheses/ecology-valens-meld.md).
9. Journal entry for 2026-08-07 exists in valens_wiki/journal/.
10. Harness verifier still passes after the meld (verify_harness.py exit 0).

## Judge + Revise round (per Q6.3 and campaign convention)

1. DeepSeek outside judge (nous portal deepseek-v4-flash-0731 — Dallas's
   preferred judge; explicit "use deepseek, stop using claude") reviews the
   meld artifacts against the success criteria (Q6.4) + the 10 evaluation
   criteria. Judge brief written BEFORE the judge runs.
2. Locus review: independent validation of the meld's internal consistency
   (evidence discipline, no premature coherence, quarantine respected).
3. Sublative revision: preserve kernel, negate weak, raise level; revision
   list written before edits.
4. Re-verify (verify_phase9.py + verify_harness.py), record in
   Calibration_Log, journal the round.

## Out of scope (this phase)

- FAOS engine integration into Ecology (the DESIGN MEMO, next deliverable —
  Dallas's explicit ordering: Phase 9 first, then the memo).
- HEB boundary-gate runtime enforcement (Q11 lead item — now scoped to the
  FAOS-gateway integration memo).
- BCW/BCT build (formally de-scoped per Memo 3; activation criteria in
  DEFERRED_PACKAGES.md).
- OneDrive/rclone automation (Q8: manual upload + wiki continuity stands).
- Any new astral persona work (stays in own harness, Q3.1).
