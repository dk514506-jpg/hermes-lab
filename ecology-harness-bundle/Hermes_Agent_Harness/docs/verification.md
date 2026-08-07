# Verification — Nine Machines, One Gate

*The full verifier suite is shipped here: evidence/verify_gate_output.txt is the full-gate run. This
doc explains what each enforces and why the chain matters.*

## The full campaign gate

`verify_all.py` chains every verifier in dependency order and **fails on any
nonzero exit**:

```
verify_packages.py  → per-package op schema, SKILL.md↔atomic_ops↔edge_map consistency
verify_phase3.py    → 8 packages × 9 files, JSON validity, 16 SKILL.md sections
verify_critique_revisions.py → post-critique fixes (flagship edge, MI ops, T2R counts)
verify_phase4.py    → graph/lattice reconciliation, direction-sensitive edges
verify_phase5.py    → safeguards meta-validation + truthfulness guards (Jose/CALM-IT)
verify_phase6.py    → dojos: 257 checks, data-level evidence flags, spirit gate
verify_phase7.py    → harness tree: inventory, governance/, stale-path sweep, T2R=48
verify_phase8.py    → evaluation artifacts + meta-evaluation + flag-semantics guard
verify_harness.py   → SHIPPED in-tree: consumer-facing re-check after local edits
```

## What the verifiers actually catch (real examples from the calibration log)

| Error class | Caught by | Calibration row |
|---|---|---|
| README claimed "all VERIFIED" (false) | now: flag-semantics regex guard | 1, 22 |
| Edge direction contradiction (COMB→TDF vs TDF→COMB) | direction-sensitive edge comparison | 5 |
| Opinion article cited as plain VERIFIED (Jose 2025) | truthfulness guard | 2, 6 |
| Preprint cited without status (CALM-IT) | truthfulness guard | 7 |
| Transfer sets missing evidence anchors | data-level flag check | 8 |
| 3 of 5 safeguards absent from packaged tree | governance/ inventory | 9 |
| 75 edges absent from "single source of truth" | documented subset rule (manual audit) | 10 |
| Quarantine expressed only in index | per-package quarantine markers | 11 |
| Stale Phase3_Skills/Phase6_Dojo paths | stale-path sweep | 12 |
| Verifier not shipped in-tree | verify_harness.py root-entry check | 13 |
| T2R count drift (47 vs 48) | exact-count check | 15 |
| verify_all.py claimed 9 verifiers, ran 3 | THE GATE ITSELF (rewritten) | 17 |
| TDF state variable rename missed in prose | verify_phase4 check 6 + review | 18 |
| User-agreement key drift across dojos | verify_phase6 (either-key documented) | 19 |
| Bibliography header overclaim | review + row 20 | 20 |

## The honest boundary

47 content-level checks are review-enforced, not machine-checked (GAP markers
in the Phase 8 QA checklists). The evaluation rubric defines a Tier 1/2/3
sampling protocol for exercising them — Tier 1 (safety invariants) is
mandatory, Tier 2 (20% random) samples evidence/parity classes, Tier 3
(conditional) runs on judge concern. The distinction between machine-checked
and review-enforced is stated, never blurred.

## Why this matters

A verifier that only checks file presence gives false confidence. These
verifiers check *semantics*: edge directions, flag truthfulness, data-level
evidence presence, exact counts, stale paths, self-description accuracy. The
class of error they catch is the class that actually happens in agent-system
builds — and the calibration log proves it by naming 22 real catches.
