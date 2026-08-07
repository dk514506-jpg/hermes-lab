# Deferred Packages and Ops — Roadmap

Project: Motivational Ecology Agent Architecture — Harness
Date: 2026-08-06
Status: GOVERNANCE CHECKPOINT — written in the Phase 7 revision round in
response to the outside-judge critiques (Claude + DeepSeek: "a fresh reader
does not know if this is a minimum viable library or an incomplete build").

## What "deferred" means

The harness ships 8 built skill packages and 5 practice dojos — a complete,
usable minimum-viable library. Deferred items are NOT missing features; they
are deliberately held back with stated reasons and activation criteria.
Nothing in the built set depends on a deferred item at runtime.

## Deferred skill packages (graph nodes)

| Package | Reason for deferral | Activation criteria | Timeline |
|---|---|---|---|
| Autopoietic_Boundary_Check | Cybernetics observer-position check; philosophy deliberately kept as philosophy (Hui, autopoiesis as design metaphor, not literal property) | Only if the user decides the cybernetic lens should be operationalized | Indefinite hold (philosophy kept as philosophy) |

Material_Arrangement_Scan and Feedback_Ecology_Map were activated
2026-08-07 (Phase 12) via the user-request branch of their activation
criteria — they are now BUILT packages (see skill_graph_index.json and
their package directories).

Until a deferred package is built, its graph edges stay quarantined
(skill_graph_index.json `quarantined_edges`; per-package `quarantine` markers
on COMB/TDF/SDT/MI edges). Building the package activates the edges.

## Uninstantiated T2R register ops (0 of 48 — all resolved)

T2R_traceability.json maps register candidates (Theory_to_Routine_Interface.md)
to package ops. As of Phase 12, ALL 48 register candidates are resolved:
45 instantiated as package ops + 3 REGISTERED-NOT-BUILT (the NPT
participation/collective-action/monitoring mechanisms, which read runtime
signals the estate does not yet generate — documented in
Feedback_Ecology_Map/support_ops.md). No UNINSTANTIATED entries remain.

## Governance note

Deferral decisions are RECONSTRUCTED campaign policy, recorded in the Open
Questions Register (Q6-Q11) and reviewable. Activating any deferred item
requires: a stated trigger (evidence or user request), a review against the
Phase 5 safeguards, and a verifier extension before the edges un-quarantine.
