# Phase 11 Plan — BCW/BCT Intervention Layer + skill_load→trend

Project: Motivational Ecology Agent Architecture
Plan date: 2026-08-07
Status: PLAN — written for Dallas's review/verdict. Executes after Phase 10
(FAOS × Ecology integration, COMPLETE). This is the intervention-design
layer: converting COMB/TDF DIAGNOSIS into a behavior-change INTERVENTION
plan — the largest remaining gap in the MVP (decision 3C, whole-project
review Memo 3).

## What Phase 11 is

The COM-B diagnostic spine is built and verified (COMB_Behavioral_Diagnosis,
14 ops; TDF_Barrier_Facilitator_Grid). What does NOT exist: the successor
stage that turns a diagnosis into a planned intervention. Three ops are
registered in T2R_traceability as UNINSTANTIATED:
- canvass_full_range
- select_bct
- retrocode_delivered_plan

Dallas's decision 3C (2026-08-06): "extend COMB rather than build a 9th
package or de-scope. The three uninstantiated ops become a COMB successor
stage, gated by the Q7 arbitration rule." Activation criterion: "once the
acceptance test produces diagnostic value evidence" — the acceptance tests
(001/002) are approved and the post-meld witness runs pass; the trigger is
MET. This plan also folds in the Phase 10 handoff items (stepwise S0-S9,
confirmed-Q2 allowance) and the small skill_load→trend conversion op
(T2R uninstantiated #9).

## Decisions already made (binding)

- **Dallas 3C:** extend COMB (successor stage), not a 9th package, not de-scope.
- **Dallas Q7 (2a):** BCT 10.x reward techniques NEVER auto-selected;
  permitted only on explicit user request with Deci-undermining risk
  disclosed. Conditional allowance for already-extrinsic behaviors
  (Eisenberger & Cameron 1996) is a documented exception path, never the
  default. This is a VERIFIER ENFORCED rule, not prose.
- **Phase 10 handoff:** stepwise S0-S9 + pre-declared-selector promotion
  (Phase 10 revision R5); confirmed-Q2 allowance (self-review #3).

## Deliverables

### D1 — COMB successor stage (the intervention layer)

Three new atomic ops appended to COMB_Behavioral_Diagnosis (per 3C, the
stage lives IN COMB, marked as the successor stage):

1. **canvass_full_range** — after a diagnosis is recorded, enumerate the
   full BCTv1 technique range applicable to the diagnosed component(s),
   WITHOUT selecting. Output: a scored-but-unranked candidate list
   (technique + component target + evidence anchor). Anti-premature-
   coherence: canvassing never selects.
2. **select_bct** — apply the Q7 arbitration rule to the canvassed range:
   - BCT 10.x reward techniques: NEVER auto-selected. Selection requires
     explicit user request + Deci-undermining disclosure, OR the
     already-extrinsic exception path (documented, never default).
   - Otherwise: select by evidence strength (component fit × verified
     anchor), preserving non-selected candidates as witnesses (Valens P4).
   - Output: selected plan + rejected-with-reason list (the dissent
     record feeds the FAOS close).
3. **retrocode_delivered_plan** — after a dojo session / real interaction,
   retrocode what was actually delivered (not what was planned) into BCTv1
   labels; compare planned vs delivered; feed the difference to the
   calibration log. This is the honesty op: it measures the gap the whole
   campaign's calibration discipline exists to catch.

Each op: name, purpose, inputs, outputs, preconditions (diagnosis must
exist; boundary_gate must pass), failure modes, and a Q7-gate flag.
Follows the existing COMB atomic_ops.json schema.

### D2 — Q7 arbitration as verifier-enforced rule

- The Q7 rule becomes a machine-checked guard: a new verifier check
  asserts that no reward-technique selection path exists without the
  explicit-user-request + disclosure (or documented exception) gate.
  "BCT 10.x requires explicit user request; rule recorded" (Calibration
  Log Q7) upgrades from prose to enforcement.
- Register entry added to the estate (select_bct's arbitration record).

### D3 — skill_load→trend conversion op (T2R #9)

- The standalone op connecting PPS's `skill_load_score` to HEB's
  `skill_load_trend` (T2R canonical_state_variables): converts a score
  series into a trend state (rising/steady/falling) with a defined window
  and minimum-change threshold. This closes the last uninstantiated T2R
  entry that isn't blocked on a deferred package, and it feeds the Phase 10
  gate's W2 trigger (ACT requires skill_load_trend != falling) with REAL
  data instead of a default.

### D4 — Phase 10 handoff items

- **Stepwise S0-S9 + selector promotion** (Phase 10 R5): extend
  advance_item enforcement beyond the 3-edge blocklist to stepwise-only
  transitions + pre-declared-selector requirement at S3/S4→S5, per the
  Valens Book IX law. (This upgrades the Phase 10 "honest surface" to full
  enforcement; verify_integration.py updated accordingly.)
- **Confirmed-Q2 allowance** (Phase 10 self-review #3): identity-level use
  class becomes usable WITH explicit recorded user confirmation (the
  DEFER→confirm path), while remaining default-quarantined. Fail-closed
  default unchanged.

## Q7 arbitration rule (the load-bearing gate, stated precisely)

```
select_bct(technique, context):
  if technique in BCT_10x_REWARD:
      if context.user_explicit_request == True AND context.deci_risk_disclosed:
          ALLOW (recorded: user-requested reward technique, risk disclosed)
      elif context.already_extrinsic_behavior == True (documented exception):
          ALLOW (recorded: exception path, never default)
      else:
          DENY — never auto-selected
  else:
      ALLOW if component-fit × evidence-anchor passes
  rejected selections are preserved as witnesses (Valens P4)
```

## Verifier — verify_phase11.py

1. COMB has 17 ops (14 existing + 3 new); successor-stage marker present
2. canvass_full_range: output is unranked candidates (no selection field)
3. select_bct: Q7 gate enforced — reward techniques DENY without
   user-request+disclosure or documented exception (machine-checked path)
4. retrocode_delivered_plan: planned-vs-delivered diff output schema
5. skill_load→trend op exists; converts series → trend state with window +
   threshold; feeds gate W2 context
6. S0-S9 stepwise enforcement active (S0→S5 blocked, S1→S9 blocked,
   S3/S4→S5 requires selector)
7. Confirmed-Q2 allowance: Q2 usable only with user_confirmed flag
8. Legacy: verify_integration.py + verify_all.py + FAOS suite still pass

## Judge + revise (per campaign convention)

- Locus validation (7-check discipline) + DeepSeek outside judge
  (adversarial) — subagents with retry-then-direct on 503.
- Sublative revision round; calibration log + journal updates.

## Out of scope

- Material_Arrangement_Scan / Feedback_Ecology_Map (activation criteria
  unmet — evidence not digested, user hasn't requested)
- Autopoietic_Boundary_Check (indefinite hold)
- Gateway runtime execution (still architectural until a platform wires)
- Astral persona compatibility (deferred by choice)

## Decision points for Dallas (bite-sized)

- P11-D1: approve the 3-op COMB successor stage as specified? (yes/revise)
- P11-D2: approve the Q7 rule as machine-enforced (DENY by default,
  user-request+disclosure or documented exception only)? (yes/revise)
- P11-D3: include the Phase 10 handoff items (stepwise S0-S9 + confirmed-Q2)
  in this phase? (yes / defer to Phase 12)
- P11-D4: timeline — build now, or wait for more dojo-session diagnostic
  evidence first? (now / wait)
