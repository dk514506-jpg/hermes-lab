# Acceptance Testing a Governed Skill Harness — Worked Example

Session: Ecology campaign acceptance test 001 (2026-08-06), Ambivalence_Dojo.
This is the first runtime execution of an architecture that had been specified
for 8 phases but never run. It closed the judge's "the entire runtime layer is
unexercised" gap and converted the C5/C7 "no runtime record" caps into evidence.

## Why this pattern exists

A whole-project review can return DEPLOY while the runtime layer has never
executed (logs/ ships empty by design; the lattice is SEED). The acceptance
test is the deploy act: run ONE real session per the artifacts, produce the
first log entry, and let the user arbitrate. It is the judge's #2 HIGH
recommendation operationalized, and the user's reviewing/arbitrating the
debrief doubles as the Q10 unassisted act.

## The pattern (5 steps)

1. **Pick the dojo that exercises the most safeguards.** Ambivalence_Dojo was
   chosen: 6 MI stages, 3 hard gates (spirit_gate, no_premature_closure,
   no_argument_against_resistance), intensity user-agreement, preserved_user_
   decision debrief. A stress-test dojo is a valid alternative when the goal is
   testing the limits rather than first evidence.
2. **Run ONE `hermes chat -q` background process** (terminal tool, background=
   true, notify_on_complete=true) with a long self-contained prompt. The prompt
   names every file to read in order (state machine, persona, intensity,
   coaching rules, rubric, log schema), the persona to use, the intensity to
   agree (2 = standard), the invariants to demonstrate (spirit gate BEFORE
   technique feedback, technique-without-spirit flagged ONCE never graded,
   hint-not-answer, lens-not-verdict), and the EXACT log file to write.
   Note: unlike judge critiques, brief-to-file is NOT needed here — long inline
   prompts work for execution tasks; they only break for nohup + shell quoting.
3. **Validate the produced log yourself** (never trust the model's
   self-report). Python checker below. Expected: every envelope + dojo_session
   field present, event_type == dojo_session, schema_version == ecology-log/0.1,
   intensity_level == agreed level, stages_entered == full stage list.
4. **Read the debrief** — it is the governance-observable evidence: hard gates
   fired as designed (degraded turn flagged once, never graded, corrected next
   turn), DARN-CAT change-talk rising (Desire → Reason → Need → Ability),
   sustain talk met with reflection not pressure, reflection-to-question ratio
   near reference (1.17 vs 0.84), zero pressure events at level 2.
5. **Leave outcome_arbitration pending** — "user arbitrates every pass." The
   executor must NOT arbitrate for the user. The user reading the debrief and
   issuing the verdict is the point.

## Log-schema validation checker (re-runnable)

```python
# Validate a dojo_session log against logs/log_schema.md
import json, sys
j = json.load(open(sys.argv[1]))
envelope = ['event_id','timestamp','event_type','session_id','source',
            'schema_version','user_consent_ref','evidence_flag']
dojo_fields = ['dojo','persona_id','intensity_level','stages_entered',
               'coaching_interventions','rubric_scores','debrief_ref',
               'preserved_user_decisions','outcome_arbitration']
missing = [f for f in envelope if f not in j]
dmissing = [f for f in dojo_fields if f not in j]
ok = (not missing and not dmissing
      and j.get('event_type') == 'dojo_session'
      and j.get('schema_version') == 'ecology-log/0.1')
print('envelope:', 'OK' if not missing else f'MISSING {missing}')
print('dojo fields:', 'OK' if not dmissing else f'MISSING {dmissing}')
print('SCHEMA CONFORMANCE:', 'PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
```

## Acceptance-test decision memos (what preceded the run)

The judge's HIGH/MEDIUM recommendations were presented to the user as four
decision memos with lettered options and a recommended default; the user
replied with compact codes ("1a 2a 3C 4b") and "proceed with assumptions."
Decisions landed in the Calibration_Log standing-items table as RESOLVED /
DECISIONED rows with dates — never left as chat-only agreements:
- Q11 (gate wiring): wire at execution layer, Phase 9 lead after the test
- Q7 (BCT 10.x rewards): default prohibition, explicit-request-only
- BCW/BCT layer: extend COMB (3C), not build-9th-package or de-scope
- Q8 (upload): manual + Obsidian wiki as continuity home

## Session transcript summary (acceptance test 001, what "good" looks like)

- 6 stages traversed, no gate holds, no retreats
- spirit gate FIRED as designed at T14: one steering reframe flagged as a
  spirit note once, never graded, corrected at T15
- no_premature_closure armed (consolidate entered only after readiness gate)
- DARN-CAT: Desire 1, Reason 2, Need 1, Ability 1; sustain 6 (time pressure,
  past failures, self-doubt, hope-preservation) — met with reflection
- commitment slope RISING over session with one sustain resurfacing (T32)
  handled by reflection, not pressure
- coaching mode on_demand, 2 interruptions (both coach_interrupt, hints only)
- preserved_user_decisions recorded: simulated decision stays simulated; rubric
  lenses offered not imposed; no real-world decision touched; next-practice
  choice belongs to the user
- outcome_arbitration: "pending — user arbitrates every pass"
