# FAOS × Ecology Integration Design Memo

Project: Motivational Ecology Agent Architecture — post-Phase 9
Date: 2026-08-07
Status: DESIGN MEMO for Dallas's verdict — recommendations, not decisions.
Author: Pip (drafts) · Dallas (disposes) — per meld Q6.6.
Predecessor: Phase9 meld (COMPLETE, verified) — this memo is the NEXT phase
per Dallas's ordering: Phase 9 first, then the integration memo.
Companion: docs/FAOS_Architecture_Isolated/faos_architecture.yaml (the
persona-free FAOS architecture) and FAOS_vs_Ecology_Comparison.md.

---

## 0. Executive summary (one paragraph)

Dallas directed: **FAOS is the gateway infrastructure; Ecology is the
Guardian intellect that negotiates the gateway.** Concretely: the FAOS
engine (faos_engine_extension.py — already runnable, 29 methods) becomes
the execution backbone — intake → triage → research → route → gate →
fulfill → close — and the Ecology estate (8 skill packages, lattice,
dojos, safeguards) becomes the intelligence that decides AT THE GATE how
the work proceeds with respect to the human: ACT / SCAFFOLD / ASK / DEFER /
STOP. The two halves are complementary, not overlapping: FAOS governs the
epistemic cleanliness of work items; Ecology governs the integrity of the
human relationship. The single hardest design decision is quarantine —
the two systems use the word for genuinely different jobs (FAOS: is this
claim trustworthy enough to use? Ecology: may this material touch the
human at all?) — and this memo articulates that difference (Section 3)
and proposes a reconciliation (Section 4) for Dallas's verdict.

---

## 1. The architecture (as directed)

```
                 ┌─────────────────────────────────────────────┐
                 │              FAOS GATEWAY (engine)          │
                 │  intake → triage → research → ROUTE → GATE  │
                 │  → fulfill → instrumented close → digest    │
                 └──────────────────────┬──────────────────────┘
                                        │
                    GATE STAGE — the seam (Q2.3, Q11)
                                        │
                 ┌──────────────────────▼──────────────────────┐
                 │        ECOLOGY — GUARDIAN INTELLECT         │
                 │  select_empowerment_mode (the 5 modes)      │
                 │  ACT ▸ SCAFFOLD ▸ ASK ▸ DEFER ▸ STOP        │
                 │  + lattice, skill graph, dojos, safeguards  │
                 └──────────────────────┬──────────────────────┘
                                        │
                 ┌──────────────────────▼──────────────────────┐
                 │        WORK ITEM (carries its evidence)     │
                 │  S0-S9 lineage · Q-tier · close record      │
                 └─────────────────────────────────────────────┘
```

- **FAOS owns the pipeline.** Field perception, evidence ladder, shadow
  routing, authority weighting, state lineage, instrumented close — the
  engine already enforces these (verified: route_with_shadow,
  assert_evidence_promotion, assert_operational all run against the real
  config).
- **Ecology owns the gate.** Instead of FAOS's binary approve/shelve/
  modify, the gate stage calls `select_empowerment_mode`: the five-mode
  ladder with exact triggers from empowerment_boundary.md. This is the
  Q11 lead item — the HEB boundary gate gets its runtime enforcement by
  BEING the FAOS gate.
- **Locus arbitrates.** The validator-steward role exists on both sides
  (FAOS roles.locus; Ecology council locus_validation) — one role in the
  merged estate: reviews route validity, shadow promotions, evidence
  ladder compliance, close completeness, and empowerment-mode selection.

## 2. What each side supplies (the division of labor, restated)

| | FAOS (gateway) | Ecology (guardian) |
|---|---|---|
| Governs | The WORK — epistemic cleanliness of items | The RELATIONSHIP — integrity of the human |
| Failure it prevents | Contamination: invented data, premature coherence, unverified numbers, seductive analogies as evidence | Erosion: deskilling, coercion, manipulation, meaning-making, option-space shrinkage |
| Core mechanism | Engine assertions (evidence ladder, S0-S9, shadow route, close) | Mode selection (ACT/SCAFFOLD/ASK/DEFER/STOP) with exact triggers |
| Rule when they meet | Evidence discipline outranks rhetorical convenience | Empowerment boundary outranks execution expediency |

Neither is subordinate in its own domain (Q2.3). The interface rule from
the meld charter holds: FAOS determines WHAT is true about the work;
Ecology determines HOW the agent may act toward the user.

## 3. THE QUARANTINE DIFFERENCE (Dallas's question, articulated)

This is the subtle one, and Dallas's instinct is correct: **the two
systems use 'quarantine' for different jobs.** Same word, different axis.

### FAOS quarantine — EPISTEMIC TRUST GRADING (Q0-Q10)

- **Question it answers:** "Is this CLAIM trustworthy enough to be used as
  operational input?"
- **Axis:** reliability of evidence. Ten tiers because the Valens
  reconstruction needed fine gradation: from Q0 (safe, usable) through
  Q6 (numeric shell, values unverified) to Q10 (composted, lessons kept).
- **Default:** deny-by-default — a claim sits at Q0 only if nothing
  questions it; anything reconstructed or fitted-to-outcome is pushed down
  the tiers.
- **Object:** CLAIMS (never whole sources). A source can carry ten claims
  at ten different tiers.
- **Trigger:** what is known about the claim's provenance (witness
  quality, verification state, contamination risk, result-conditioning).
- **Purpose:** keep the pipeline's reasoning epistemically clean. A
  quarantine event means "this claim cannot carry weight right now."

### Ecology quarantine — AGENCY PERMISSIBILITY (Q0-Q5)

- **Question it answers:** "May this MATERIAL touch the human at all, and
  if so, how?"
- **Axis:** permissibility in the human relationship. Five tiers because
  the agency concern has five distinct classes: structural (safe to
  record), provisional (flagged), identity-level (default quarantine —
  characterizes WHO the user is), rejected (user said no — removed
  regardless of evidence strength), manipulation-risk, surveillance-risk.
- **Default:** also deny-by-default for the protected classes
  (identity-level claims default to quarantine; user-rejected insights are
  removed even when the evidence is strong).
- **Object:** INSIGHTS and their use in the relationship — and notably,
  the user's verdict outranks evidence (a user-rejected insight is gone,
  full stop).
- **Trigger:** what the material WOULD DO if used (characterize identity?
  steer a decision? convert practice logs into surveillance?).
- **Purpose:** keep the human the author of their choices. A quarantine
  event means "this material must not be used this way toward this person."

### The crisp contrast

| | FAOS (Q0-Q10) | Ecology (Q0-Q5) |
|---|---|---|
| Kind of question | Epistemic: can we trust it? | Ethical: may we use it? |
| Axis | Reliability of the claim | Permissibility of the use |
| Object | Claims as evidence | Insights as relationship acts |
| What outranks | Provenance discipline | User verdict |
| Failure it prevents | Contaminated reasoning | Eroded agency |
| 10 tiers vs 5 | Fine gradation of trust | Five distinct protected classes |

**The one true overlap:** a claim that is BOTH untrustworthy AND
harmful-to-agency sits at the bottom of both scales. But the systems
quarantine it for different reasons, and that difference matters in the
merged estate: FAOS may clear a claim as trustworthy while Ecology still
bars its use toward the user (e.g. a perfectly verified insight about
someone's identity — FAOS says reliable, Ecology says don't use it on
them without their verdict). **FAOS clearing a claim never licenses
Ecology's use of it.** That is the load-bearing sentence for the merged
estate.

## 4. Reconciliation proposal (for Dallas's verdict)

Dallas prefers the FAOS 10-tier scale ("I tend to like FAOS 10 quarantine
types"). Recommendation — keep BOTH scales, typed, and wire the interface:

1. **Keep Q0-Q10 as the claim-trust scale** (FAOS, epistemic). Every claim
   in a work item carries its Q-tier from the FAOS engine.
2. **Keep Q0-Q5 as the use-permissibility scale** (Ecology, agency). Every
   insight's USE toward the user is gated by Ecology's five classes.
3. **Type the relationship explicitly** — the merge rule: *a claim's
   FAOS Q-tier governs whether the pipeline may build on it; Ecology's
   class governs whether (and how) it may be used toward the user. The
   two scales are never added or averaged; they are independent axes.*
4. **One-way promotion only:** FAOS clearing (Q0) is necessary but never
   sufficient for operational use toward a human — Ecology's class must
   also permit it. Ecology's user-rejected class (Q3_REJECTED) is final
   regardless of FAOS tier (this already exists in lattice_index).
5. **Mapping table as documentation, not enforcement:** a Q0-Q10 ↔ Q0-Q5
   cross-reference table is a deliverable of this memo's implementation,
   but it is a lookup aid, not a merge — the independent-axes rule is what
   the engine enforces.

This respects Dallas's preference (the 10 tiers stay canonical for claim
trust) while honoring the discovery (Ecology's quarantine is a different
job and cannot be collapsed into a trust scale without destroying it).

## 5. Implementation plan (post-verdict)

**Phase A — engine seam (the actual patch):**
1. Import faos_engine_extension.py into the Ecology tree (or lift to a
   shared module under docs/).
2. Build the gate adapter: FAOS gate stage calls
   `select_empowerment_mode` (Ecology) instead of binary approve; the
   five-mode outcome feeds FAOS's gate result states (TRUE/FALSE/PARTIAL/
   INCONCLUSIVE/BLOCKED).
3. Config merge: Ecology layers + FAOS blocks (evidence ladder, state
   lineage, absence register, non-op registry, typed metrics) using
   faos_architecture.yaml as the template; quarantine = the two-scale
   typing from Section 4.

**Phase B — close discipline wraps the dojos:**
4. Dojo sessions close through FAOS's 6-pass instrumented close
   (victory/defect/dissent/proxy/boundary/transfer) — dojos currently
   have a debrief template but no mandatory close contract.

**Phase C — verification:**
5. New verifier (verify_integration.py) asserting: gate calls the mode
   selector; quarantine is two-typed; close wraps dojos; both existing
   verifier suites still pass.
6. Witness run: one dojo session executed through the merged pipeline.

**Deferred (documented, not built):** BCW/BCT layer (activation criteria
in DEFERRED_PACKAGES.md); rclone automation (Q8: manual upload stands);
astral persona compatibility (Q3.2: deferred by choice).

## 6. Decisions for Dallas (bite-sized, per his workflow)

- D1. **Quarantine reconciliation:** accept Section 4 (two scales, typed,
  independent axes, FAOS-clearing-never-licenses-Ecology-use)?
  (yes / revise / keep separate with no mapping table)
- D2. **Gate mechanics:** Ecology mode selection returns FAOS result
  states as mapped above (ACT→TRUE, SCAFFOLD→PARTIAL, ASK→INCONCLUSIVE,
  DEFER→PARTIAL, STOP→BLOCKED)? (yes / different mapping — specify)
- D3. **Close discipline:** dojos close through the 6-pass instrumented
  close? (yes / debrief template suffices for now)
- D4. **Scope of Phase A:** full engine import now, or the gate adapter
  only (pipeline wiring next)? (full / adapter first)
- D5. **Where the memo lands:** keep as docs/Ecology/Foundation/
  FAOS_Ecology_Integration_Memo.md, or move to the isolated FAOS folder /
  the merged estate? (keep / move)

## 7. Open risks (stated honestly)

- **Schema drift (known pattern):** the campaign already carries a
  documented pattern of four planetary-mapping tables drifting. The
  two-quarantine-scales typing is the same failure mode waiting to happen —
  the verifier (Phase C) must assert the typing, not just the files.
- **Q11 enforcement depth:** the gate adapter makes the boundary
  enforceable at the engine level — but only where the engine runs. Until
  the gateway actually executes dojo sessions, enforcement is
  architectural, not runtime-proven. The witness run (Phase C step 6) is
  the honest boundary of that claim.
- **MAPPED-NOT-INSTANTIATED items:** S0-S9 item lifecycle and
  absence-gating become real here (they were designed in the meld). If
  Phase A lands without them, they stay design artifacts — the memo should
  not claim otherwise.
