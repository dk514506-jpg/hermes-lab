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
| Material_Arrangement_Scan | Practice-theory (Shove) materials/competences/meanings scan; evidence synthesis not yet digested into actionable design principles | When a practice-theory synthesis is available, or user requests home-lab application | Phase 8 decision checkpoint; user-driven |
| Feedback_Ecology_Map | NPT embedding-work (May & Finch) feedback-loop map; requires the NPT longitudinal evidence digest | When NPT evidence is digested, or user requests | Phase 8 decision checkpoint; user-driven |
| Autopoietic_Boundary_Check | Cybernetics observer-position check; philosophy deliberately kept as philosophy (Hui, autopoiesis as design metaphor, not literal property) | Only if the user decides the cybernetic lens should be operationalized | Indefinite hold (philosophy kept as philosophy) |

Until a deferred package is built, its graph edges stay quarantined
(skill_graph_index.json `quarantined_edges`; per-package `quarantine` markers
on COMB/TDF/SDT/MI edges). Building the package activates the edges.

## Uninstantiated T2R register ops (9 of 48)

T2R_traceability.json maps register candidates (Theory_to_Routine_Interface.md)
to package ops. "UNINSTANTIATED" = defined in the register but not yet built
as an atomic_op in any package. Reasons:

| Group | Count | Reason |
|---|---|---|
| BCW/BCT layer ops (intervention-function selection, BCT selection) | 2-3 | BCW/BCT layer scope decision pending — the COM-B/TDF diagnostic spine is built; the intervention-design layer (BCW hub functions, BCTv1 techniques) was deferred by scope choice |
| NPT ops (embedding-work, coherence, cognitive participation) | 2-3 | Blocked on the deferred Feedback_Ecology_Map package |
| Practice-theory ops (materials arrangement, competence assembly) | 2-3 | Blocked on the deferred Material_Arrangement_Scan package |
| skill_load_score→trend conversion op | 1 | PPS writes skill_load_score; HEB derives skill_load_trend; a dedicated conversion op is pending unification (documented in T2R canonical_state_variables) |

## Governance note

Deferral decisions are RECONSTRUCTED campaign policy, recorded in the Open
Questions Register (Q6-Q11) and reviewable. Activating any deferred item
requires: a stated trigger (evidence or user request), a review against the
Phase 5 safeguards, and a verifier extension before the edges un-quarantine.
