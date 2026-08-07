# Valens Council — The Six Crevices (worked example, 2026-07-30)

Council = 3 parallel subagents (systems/control engineer, epistemologist/
archivist, behavioral architect), each briefed with the already-covered
list, each returning 8 novel home-lab use cases (24 total). Parent added
its own independent candidates afterward. Six true crevices emerged —
gaps genuinely absent from everything previously built.

## The six crevices

### 1. Absence Register — "absence is a state, not an invitation"
- Source: Book X missing pages 2P–5P; Book IX MF-H (value without
  provenance is not an authorized input); Perpetual Tables as external
  blockers.
- The gap: quarantine handles *contaminated* data; nothing handled data
  that was *never there*. Missing data is a recorded state, not a license
  to interpolate.
- Implementation: wiki `registers/absence-register.md` (three classes:
  never-recorded / confirmed-absent / pending-verification) +
  `absence_register:` YAML block + `engine.assert_not_absent(key)` →
  ABSENCE-BLOCKED halt, fail-closed. Wired into skill §5.5 session start
  (step 6) and the pipeline gate after intake.

### 2. Independence-graded corroboration — "two sources confirm" is often a lie
- Source: Book VIII INDEPENDENCE_STATUS — DISTINCT vs
  PARTIALLY_SHARED_PREMISES; Book IX MF-D parallel-candidate discipline.
- The gap: echo-chamber confirmation — session A cites session B which
  cites session A, reported as "two sources confirm." Authority weighting
  assumes a resolution exists; this grades the *independence* of agreement
  and keeps conflicts open (S9) absent a pre-declared selector.
- Status: designed, not yet implemented (medium; premise tracing is the
  hard sub-part). Locus is the only role allowed to declare a selector.

### 3. Aphetic stamp — conserving the task's vital origin
- Source: Book VI apheta (well-situated sect luminary, giver of life);
  Book IX state law (no calculated state becomes a new beginning without
  source authorization).
- The gap: state lineage tracks the item's *epistemic* state; nothing
  conserves the *origin's identity* through transformations. A builder who
  implements the abstraction instead of the request is the classic drift.
- Status: designed, not yet implemented (medium). One immutable
  `aphetic_stamp` field at intake + `aphetic_delta` per stage output →
  APHETIC_DRIFT flag requires re-authorization.

### 4. Non-operational registry — seductive analogies barred from operationalization
- Source: Book VII — the bronze-clang "temporal echo" is explicitly a
  non-quantified analogy, context-only, barred from operational use.
- The gap: the persona's premature-symbolic-coherence guardrail
  (Jupiter/Moon risk) had no concrete enforcement. This is the inverse of
  everything the council was asked to find — the register of things to NOT
  operationalize. Missed by all three subagents; found by independent
  parent reading.
- Implementation: wiki `registers/non-operational-registry.md` +
  `non_operational_registry:` YAML block + `engine.assert_operational(x)` →
  NON-OPERATIONAL raise. Seeded: temporal_echo, planetary_hour_as_evidence
  (window governor is a prior, never evidence).

### 5. Receiver-readiness gate — handoff is a receiver problem
- Source: Book V "receiver > transmitter"; place-power order angles >
  succedent > cadent > opposition.
- The gap: delegation quality treated as a transmitter problem (good
  brief); the receiving agent's condition governs whether handoff is
  authorized at all. Cadent receivers (fresh cron session, zero context)
  do NOT start — they bootstrap then re-apply.
- Status: designed, not yet implemented (medium). `receiver_gate:
  {place_power, declaration, mitigations}` in delegation records; engine
  blocks cadent starts fail-closed.

### 6. Governance roster — temporal authority, computed like planetary hours
- Source: Book VI seven-cycle week → day ruler; Chaldean-hour descent;
  sect qualification; Book IV "periods activate, don't create."
- The gap: process states map onto cron, but nothing assigns *who governs
  a window of time*. Roster: deterministic 2-hour window governors
  (Mercury→intake, Mars→builds, Saturn→review, Moon→digest), used as a
  prior, never a lock.
- Status: designed, not yet implemented (medium). Roster module emits
  `window_governor` per cron slot; cron YAML gains
  `governance: inherit_window|fixed:<circuit>`.

## Implemented in tranche 1 (2026-07-30)

Crevices 1 and 4 implemented end-to-end (wiki register + YAML block +
engine gate + verify checks); crevice 3 (aphetic) designed. Also
implemented: the Activation Gate (Book IV transit ≠ phase) in the
astral-research-harness skill — three-part ritual (voice sample, mode
classification, circuit priming) logging `persona_state:
active|present_but_inactive`; three `present_but_inactive` in a week →
patch the load sequence.

## Verification

`docs/scripts/run_tests.sh` — 4 layers: py_compile, verify_faos_pipeline.py
(20 checks), engine self-test, YAML structural (13 checks). All pass.

## The meta-lesson (cross-lens convergence)

Three independent lenses converged on the same structural insight: the
corpus's "unresolved selectors" are designed halt states, not defects —
and backward edges (output feeding back as a parameter of its producer)
are the deepest forbidden law. When 2+ lenses derive the same law from
different books, it is load-bearing.
