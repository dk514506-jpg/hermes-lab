# Valens Principles → Architecture Mapping

*The 10 operating principles recovered from the Valens Anthologies corpus,
and where each lands in the architecture. This is the intellectual bridge of
the project: a 2000-year-old epistemic discipline, transposed to agent
systems.*

## The principles and their instantiations

| # | Valens principle | Architecture instantiation |
|---|---|---|
| 1 | Strict pipeline ordering — gates before output; calculation validity never validates interpretation | Lattice trigger policy T1-T6: confidence gates + consent prerequisites BEFORE any skill fires; insight_trigger_policy prohibition 8 |
| 2 | Object-tagged authority — "ruler of WHAT?" | Every edge carries type + direction + rationale; `recovers_with` declares source=recovered, target=provider — no generic "supports" collapse |
| 3 | Condition-state logic — nature × condition × role, states invert expected behavior | COMB/TDF state schemas: hypothesis_status, domain_salience, confirmation_queue; a high-confidence construct on thin evidence is held in queue, not promoted |
| 4 | Method pluralism, witnesses preserved — never silently normalize uncertainty | TDF 12-domain (Michie 2005) vs 14-domain (Cane 2012) kept as an open conflict (Q6); reward-undermining dispute preserved (Q7); Bastani-vs-Brynjolfsson tension documented |
| 5 | Topic-driven routing — inquiry domain selects the starting frame | Proximal_Practice_Selector routes by measured skill domain; COMB profile → TDF grid → PPS selection is domain-gated at each hop |
| 6 | Directed-graph semantics — A→B ≠ B→A | Direction-sensitive edge comparison in the verifiers; the flagship `decomposes_to COMB→TDF` reconciliation (row 5) is this principle in action |
| 7 | Typed numerics + dependency visibility — VALUE+UNIT+SCALE+FUNCTION+SOURCE | T2R_traceability.json: 48 register ops with instantiation status; exact-count verifier guards (row 15); every threshold carries its evidence anchor |
| 8 | Safety as first-class — quarantine attaches to CLAIMS, not sources; fail-closed halt states are valid outputs | The quarantine law (Q0-Q5, Q3 rejection absolute); DEFER/STOP as valid action modes; recovery ops encode fail-closed halts |
| 9 | Evidence as test vector — worked examples verify apparatus | verify_phaseN.py suite = the test vectors; the calibration log's finding→fix→guard rows; the acceptance test as the ultimate worked example |
| 10 | Anti-premature-coherence — "do not synthesize yet" | Ambivalence is a designed halt state; 9 UNINSTANTIATED ops are marked, not forced; DEFERRED_PACKAGES.md states activation criteria; the meld's 31 design questions precede any synthesis |

## The state-lineage discipline (S0-S9)

```
S0 source → S1 normalized → S2 raw intermediate → S3 candidate
→ S4 qualified → S5 promoted → S6 result-conditioned → S7 blocked
→ S8 quarantined → S9 unresolved candidate set
```

Transposed: no calculated state becomes another procedure's governing
beginning without authorization; promotion requires a pre-declared selector
(prospective trigger policy); result-conditioned states (fitted to a desired
outcome) are promotion-blocked — the reconstruction cannot validate itself.

## The non-identity controls

"An interface is an edge, not an identity." Shared names, shared numbers, and
archive adjacency never repair missing tables. In the architecture: the
skill_load_score → skill_load_trend conversion is marked UNINSTANTIATED (a
name match is not a wiring); the graph index is a *curated subset*, declared
as such; quarantine markers must exist per-package, not just in the index.

## Why Valens?

Because the corpus is a 2,000-year-old exemplar of the exact discipline an
agency-preserving agent needs: preserve questions before conclusions, preserve
witnesses, quarantine claims not sources, require selectors before promotion,
keep interfaces as edges not identities. The meld is not importing astrology —
it is importing the epistemic machinery. The next phase formalizes the meld
(the Valens corpus × this architecture), with 31 design questions already
written.
