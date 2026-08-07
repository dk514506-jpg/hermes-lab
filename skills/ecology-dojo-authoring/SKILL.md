---
name: ecology-dojo-authoring
description: Build or QA Ecology doc tree deliverables (dojos, QA checklists, evaluation rubric, calibration log).
---

# Ecology Dojo Authoring

## Purpose
Author the 7 canonical Phase 6 artifacts for a practice dojo (simulated-interlocutor
practice environment) in `~/.hermes/hermes-agent/docs/Ecology/Foundation/Phase6_Dojo/<Domain>_Dojo/`.
Each dojo adapts the Phase 3 sparring skeleton to a domain while keeping the estate
policy: persona module strictly separated from coach module, staged dialogue with
entry/exit conditions, rubrics as lenses not verdicts, calibrated pushback owned by
the user, evidence-grounded debriefs, and transfer scenarios for generalization.

## Trigger Conditions
- User asks to build a new practice dojo (`<Domain>_Dojo` with the 7 canonical artifacts)
- User asks to extend/adapt an existing dojo (new scenario, persona, rubric, or stage)
- User asks to QA/verify dojo artifacts — run the verifier, don't hand-inspect

## Grounding Files (read FIRST — they define the register)
- `Phase3_Skills/ConvoDojo_Practice_Sparring/` — canonical skeleton: SKILL.md + all 7
  artifacts are the pattern to adapt (dialogue_state_machine.json, persona_config.yaml,
  rubric.json, sparring_intensity_profile.json, in_session_coaching_rules.md,
  debrief_template.md, transfer_scenario_set.md)
- `Phase5_Safeguards/empowerment_boundary.md` + `scaffolding_fade_rules.md` — estate
  policy that binds every dojo (preserved_user_decision set, no-coercion/no-shaming/
  no-lattice-reference prohibitions, hint-over-answer gradient, fade mandatory)
- `Recent_Evidence_Digest.md` — VERIFIED claims to cite (EasyMED 2025 safety/novice
  gains, AgentForge 2026 role separation, Ma 2025 persona sanitization, Han 2026
  ~52.6% auto-coding, Shenoi 2026 Aimi MISC-2 0.84, Rudolph 2025 authenticity gap,
  Bastani 2025 hints-eliminate-harm)
- `Phase3_Skills/MI_Ambivalence_Conversation/SKILL.md` — when the domain touches MI
  (spirit gate, OARS, evocation-not-accusation, DARN-CAT)

## The 7 Canonical Artifacts (per dojo — no more, no fewer inside the dojo dir)
1. **dialogue_state_machine.json** — stages with entry_conditions/exit_conditions,
   coach_rules_ref anchors to `in_session_coaching_rules.md#<stage>`. When reusing
   the sparring 5-stage core (engage/explore/challenge/consolidate/close): KEEP stage
   ids for interface compatibility, REMAP semantics per domain, and document it in an
   `adapted_from` block (source / status / evidence / kept[] / changed[]). New stages
   allowed (e.g. Conversation added `repair`). Include transition_policy
   (advance/retreat/loop_guard/interrupt_handling) + custom_stages policy. For
   domains needing hard constraints, add a `hard_gates` array INSIDE
   transition_policy (each: id / scope / rule / optional retreat_target) —
 Ambivalence uses spirit_gate, no_premature_closure, no_argument_against_resistance;
 Conflict uses no_shaming, no_forced_agreement, deescalation_first. Gates are
 owned-specific requirements, not schema-wide: sibling dojos without gates still
 pass generic checks.
2. **persona_config.yaml** — 2-3 personas, full schema: id/name/role/context/stance
   (default_resistance, change_talk_affinity)/speech_profile (verbosity/directness/
   emotion_range)/boundary_rules/sanitization. boundary_rules MUST explicitly encode
   no-coercion, no-shaming, and no-lattice-reference for EVERY persona (three
   distinct rules, plus pushback-only-within-intensity). sanitization: audited:true +
   bias_checks + audit_date. provenance.verified flag. End with bank_rules.
3. **rubric.json** — >=2 rubrics per domain; every dimension carries an `evidence`
   field (utterance quotes / turn pairs / counts); scoring type "lens" with levels
   developing/practicing/proficient and anchoring "every score carries >=1 evidence
   quote"; rubric_use_rules MUST include lens-not-verdict; cite VERIFIED fidelity
   anchors (Aimi 0.84, Han 52.6%) as calibration references, not hard bars.
4. **sparring_intensity_profile.json** — 5 levels (warm_up/standard/challenging/
   stress/gauntlet), domain-tuned persona_behavior per level; escalation_policies
   (proficiency_gated default); a user-agreement block — canonical shape
   `user_agreement: {required: true, note: ...}` (KNOWN DRIFT — RESOLVED 2026-08-06:
   Conversation_Dojo and Coaching_Dojo shipped legacy `user_agreement_requirement`
   instead of the canonical `user_agreement`; both were normalized to the canonical
   shape in the Phase 8 round, Calibration_Log row 19 — all five dojos now conform,
   but verify_phase6.py still accepts either key for back-compat; flag any
   re-appearance of `user_agreement_requirement` when QA'ing): no escalation
   above the agreed level without explicit user agreement, and levels 4-5 need
   recorded consent (proficiency evidence may trigger an OFFER, never an
   escalation); deescalation_rules (overwhelm -> level 1);
   sycophancy_guard (agreement_rate_per_10_turns, threshold 0.8).
5. **in_session_coaching_rules.md** — Module Separation invariant (persona never
   evaluates, coach never speaks in persona); per-stage rules; **When to Interrupt**
   (between turns only, except overwhelm -> STOP; user interrupts are never blocked;
   on_demand default); **Hint-Not-Answer** scaffold ladder (5=model on request ...
   1=check after attempt, 0=none — the answer is never level 1, Bastani VERIFIED);
   On-Demand Coaching section; fade is mandatory (scaffolding_fade_rules).
6. **debrief_template.md** — sections: header, What Happened (evidence layer),
   Rubric Lenses (lens layer), Patterns Noticed (hypothesis layer, "not verdicts
   about you"), Intensity Calibration, Transfer Notes, **preserved_user_decision**
   (explicit section: what remains with the user — agent proposes, user disposes),
   User Corrections (recorded verbatim, provisional until reviewed), Calibration Log.
7. **transfer_scenario_set.md** — >=3 base + >=2 transfer scenarios (tables: id /
   target skill / context / persona refs / difficulty; transfer adds transfer_of +
   what changes); Transfer Rules section inherited from the skeleton (proficiency-
   gated, evidence not grades, gap names next target, same rubric reuse, user
   chooses); one structural axis changed per transfer scenario.

## Evidence Discipline
- Every claim flagged VERIFIED (grounded in the digest) or RECONSTRUCTED (design
  inference). Mark design decisions explicitly (e.g. "RECONSTRUCTED mapping").
- **Every structured artifact must contain BOTH "VERIFIED" and "RECONSTRUCTED"
  strings** — pitfall found live: DSM files carrying only RECONSTRUCTED failed the
  verifier; fix by adding a VERIFIED grounding line (EasyMED/AgentForge) to the
  description. Cite VERIFIED evidence in JSON descriptions too, not just markdown.
- **Flags must survive PARSING.** Verify against parsed content (json.dumps of the
  loaded object), not raw file text: YAML header comments are stripped by
  yaml.safe_load, so a persona_config.yaml whose only VERIFIED mentions sit in
  header comments fails data-level checks while a raw-text grep passes. Fix: put a
  flag-bearing line in DATA (e.g. a coach_interface entry: "the no_shaming gate is
  grounded in EasyMED 2025 (VERIFIED: ...)"). transfer_scenario_set.md files are
  the most commonly missed artifact — add an explicit flags line there too.

## Verification (house register — required before declaring done)
- The repo's QA convention is `council_notes/verify_phaseN.py` scripts (no
  run_tests.sh/pytest): `check()` helper prints [PASS]/[FAIL], collects `fails`,
  `sys.exit(1)` on any failure, "ALL PHASE N CHECKS PASSED" on success. Read
  `verify_phase5.py` for the register, then write `verify_phase6.py` etc.
- A generic per-dojo verifier lives in this skill: `scripts/verify_dojo.py <dojo_dir>`
  — run it against any dojo dir (new or existing) before declaring done.
- Checks that matter: all 7 files exist; JSON parses; YAML parses; stages have
  entry+exit conditions and coach_rules_ref anchors; adapted_from documents changes;
  persona count 2-3 with full schema; boundary rules present for EVERY persona
  (count >= personas); sanitization audited; >=2 rubrics with evidence fields and
  lens scoring; intensity 5 levels + user_agreement_requirement + sycophancy_guard;
  markdown sections present; >=3 base + >=2 transfer scenarios; **scenario persona
  refs resolve against the persona bank** (regex `p_[a-z_]+` diff); evidence flags
  in every structured artifact.
- Verifier scripts live in `council_notes/`, NOT inside the dojo directory.

### Phase-level multi-dojo verifier (several dojos building in parallel)
- Drive one generic check loop + an owned-specific block per dojo from a config
  table (DOJO_SPECS: per-dojo stages / hard gates / rubric extends bases / required
  dimensions / stance keys / scenario id prefixes).
- Attribute every check: prefix `[owned]` for dojos you authored (strict, exact
  invariants) and `[sibling]` for other agents' dojos (generic conventions only:
  inventory, parse, stage structure, persona schema + boundary keywords, lens
  rubrics, intensity policy keys, hint-not-answer, preserved_user_decision,
  transfer counts, data-level evidence flags). Never assert sibling stage families
  or gates you haven't read.
- Scenario id prefixes differ per dojo (scn_amb_, scn_conf_, scn_wk_, scn_convo_,
  scn_coach_) — read them from the files; do NOT derive from a short dojo-name
  slice (`d[:3]` maps Conflict AND Conversation to "con").
- Add a drafting-artifact check: `"wait," not in json.dumps(artifact)` catches
  self-correction notes that leaked into deliverables (found live this phase).
- Exit 1 on any failure, but report OWNED and SIBLING failures separately so the
  index agent routes them; a nonzero exit with only sibling failures still means
  your scope is green — say so in the summary.

### Phase 8 QA-checklist pattern (criteria × artifact × enforcement)
When the task is a QA *checklist* over built artifacts (Phase 8 outputs such as
Practice_Dojo_QA_Checklist.md), build per-criterion rows that each carry: exact
answering file(s), a pass condition, and an enforcement status:
- ENFORCED = a verify_phaseN.py check machine-enforces it (exit 0 gates the build)
- PARTIAL = file + semantics present, but the verifier checks presence only
- GAP = no machine check (or an owned-only check skips sibling dojos)
Method that worked: (1) read the plan for the criteria list and output contract;
(2) read the verifier SOURCE and map its check() calls to criteria — never trust
README '41/41' status lines; (3) read one owned + one sibling artifact per kind and
diff key names across siblings (schema drift like `user_agreement_requirement` vs
`user_agreement.required` only surfaces that way); (4) for harness-integration
sections, wire routines/ → executor, logs/ → log_schema, governance/ → Phase 5
docs, and give each integration check files + pass condition + enforcement; (5) ship
a gap register with concrete fixes and a bottom line. See
references/phase8_qa_findings.md for the worked example + the G1-G7 gap list.
- For the SIBLING variant of this pattern (skill-package + motivational-lattice
  checklists, audited against verify_packages.py / verify_phase4.py /
  verify_critique_revisions.py with the T2R reconciliation notes), use the
  `ecology-evaluation-qa` skill — same method, different layer + verifier map.

### Phase 8 master rubric + calibration log (Evaluation_Rubric.md / Calibration_Log.md)
The other half of the Phase 8 council split (member A): the MASTER rubric and the
campaign CALIBRATION record. Shapes that worked (see
references/phase8_evaluation_docs.md for the full worked example):

**Master rubric — one section per criterion, exactly four parts:**
1. What to look for — artifact-referenced down to the op/line (e.g. "PPS atomic_ops
   `compute_skill_load` (0..1), `detect_atrophy_risk`, `fade_scaffolds`"). Extract op
   lists LIVE from the package JSON (python json.load one-liner over each
   atomic_ops.json) — never from prose summaries, which drift.
2. Where the evidence lives — the artifact map (Phase3_Skills/, Phase5_Safeguards/,
   Phase6_Dojo/, Hermes_Agent_Harness/, evidence/).
3. Verifier guard — cite the exact check ("verify_phase7.py check 11 asserts T2R == 48
   entries") or write "NO dedicated guard" when none exists.
4. 0/1/2 ladder — 0 absent/contradicted, 1 partial (declared in prose / single
   artifact / presence-checked only), 2 structural + cross-artifact consistent +
   verifier-guarded; per-criterion refinements allowed.
HONESTY RULE: when a criterion is only presence-checked or prose-answered, say so and
cap it at 1 (C5/C7/C10 got capped this build). A rubric that overclaims enforcement
repeats the campaign's own README "all VERIFIED" error (calibration log row 1).
Protocol section: Council split (disjoint outputs), outside-judge round, score
aggregation (median of Council + judge scores, rounded; a ≥1-point disagreement forces
a written reconciliation row in the log), PASS/WARN/FAIL bands (≥1.8 / 1.2-1.79 /
<1.2), findings feed Calibration_Log.

**Post-judge additions (whole-project round, 2026-08-06) — three patterns that
came out of the Phase 8 + whole-project judge rounds:**

1. **Meta-evaluation loop.** The evaluation artifacts themselves were unguarded:
   nothing checked that the checklists cover the rubric (Claude's sharpest Phase 8
   finding). Fix (verify_phase8.py): (a) UNION coverage — all 10 rubric criteria
   must appear across the three checklists combined; (b) per-instrument assigned
   criteria — skill QA must cover criteria 1-5, lattice QA 6/7/10, dojo QA 8/9 per
   the rubric's own §1.1 sibling mapping (a naive "every checklist covers all 10"
   check false-fails — coverage is by division of labor); (c) GAP discipline —
   each checklist must contain GAP/PARTIAL markers (honest about unguarded checks).
2. **Flag-semantics guard** (closes calibration-log row 1's open proposal): a
   regex over summary READMEs/handoffs that fails on bare "all VERIFIED" /
   "everything VERIFIED" overclaims — `(all|every|everything|entirely|fully)\s+
   VERIFIED`. MUST include a correction-context exclusion (`corrected|fixed|
   downgraded|was wrong`) — the first run false-positived on a historical
   "README 'all VERIFIED' claim corrected" line that is a correction record, not
   a current overclaim. The guard proving itself on its own false-positive class
   is the sign it's calibrated.
3. **verify_all.py maintenance trap.** The campaign's aggregate gate (one verifier
   per phase) silently rotted: it chained 3 of 9 verifiers while its docstring and
   the Calibration_Log register claimed the full chain — a B3 self-description
   error in the exact class the campaign polices (DeepSeek's biggest whole-project
   catch, calibration-log row 17). Rule: EVERY time a new verify_phaseN.py is
   added, rewrite verify_all.py's VERIFIERS list in the same change; the gate's
   self-description is itself a truthfulness claim. The rewritten form runs each
   verifier as a subprocess and fails on any nonzero exit (9/9 on the final run).

**Calibration log — four-column table:** phase/round | finding (artifact-referenced,
file:line) | fix applied | verifier guard. The guard column is the point: "a correction
with no verifier guard is one revision away from regressing" — when no check exists,
write "no automated guard; review-round enforced" and optionally propose the guard.
Plus: a standing-items table (open QIDs with status + last-witnessed), a verifier
register (scope + count of every verify_phaseN.py), and a feed-forward note.

**Grounding workflow (what made the docs accurate):**
1. Read the phase plan first (council split, output contract).
2. Read the correction history — council_notes/critique_*.txt, judge_*_harness.txt,
   handoff_notes.md — they carry the exact findings with file:line refs; do NOT
   re-derive them from the artifacts.
3. Read every verify_phaseN.py SOURCE and map its check() calls to criteria; presence
   checks ≠ content enforcement (verify_phase3 asserts "Trigger Conditions" section
   exists, not that the conditions are executable).
4. Extract live facts (op lists, counts, quarantine markers) from the JSON, then write.
5. Verify placement + line counts of YOUR files only — sibling council members land
   their files in the same dir concurrently.

## Acceptance Testing (live session execution — the "never run" gap)
When the architecture has been specified but never executed, the acceptance test
converts "specified" into "observed" runtime evidence. Proven 2026-08-06 (Ecology
acceptance test 001, Ambivalence_Dojo): a single `hermes chat -q` background run
executes a REAL practice session per the artifacts, writes a conforming log, and
closes the C5/C7 "no runtime record" caps. Full worked example +
validation checker: `references/acceptance_testing.md`.

Proven invocation (long self-contained prompt is FINE here — brief-to-file is for
judge critiques, not execution tasks):
```bash
hermes chat -q "You are executing ACCEPTANCE TEST NNN. Read these files in order:
1) <dojo>/dialogue_state_machine.json (stages; hard_gates), 2) <dojo>/persona_config.yaml
(use persona <id>), 3) <dojo>/sparring_intensity_profile.json (user_agreement required;
agree intensity=2 at start), 4) <dojo>/in_session_coaching_rules.md (spirit gate BEFORE
technique feedback; technique-without-spirit flagged ONCE never graded; hint-not-answer),
5) <dojo>/rubric.json (lens not verdict), 6) <harness>/logs/log_schema.md (dojo_session
contract). Then RUN a full practice session walking ALL stages with sustain+change talk,
>=2 coach interventions (hints not answers), hard gate firing before technique feedback.
End with a debrief. Write a dojo_session log entry to <harness>/logs/acceptance_test_NNN.json
conforming EXACTLY to log_schema.md fields (envelope: event_id, timestamp, event_type=dojo_session,
session_id, source=ConvoDojo_Practice_Sparring, schema_version=ecology-log/0.1, user_consent_ref,
evidence_flag; dojo fields: dojo, persona_id, intensity_level, stages_entered,
coaching_interventions, rubric_scores with utterance quotes, debrief_ref,
preserved_user_decisions, outcome_arbitration). Reply with: (1) transcript summary,
(2) the exact JSON, (3) schema-conformance confirmation." -m <model> --provider <provider>
```
Acceptance criteria (Evaluation_Rubric §1.9): (a) session runs per the artifacts,
(b) logs conform to log_schema.md, (c) governance observable in the session flow.
Validate (b) yourself with a python checker (see the reference) — assert every
envelope + dojo field present, event_type/schema_version exact, intensity == agreed
level. The DEBRIEF is the (c) evidence: hard gates fired as designed (degraded turn
flagged once, never graded, corrected next turn), DARN-CAT change-talk rising,
sustain talk met with reflection not pressure, zero pressure events, preserved
decisions recorded. **outcome_arbitration stays `pending — user arbitrates every pass`**
— the executor must NOT arbitrate for the user; the user reviewing the debrief and
issuing the verdict IS the Q10 unassisted act. Expect 3-8 minutes runtime; the
process writes both the JSON log and a debrief markdown into logs/.

## Parallel-Build Coordination (council campaigns)
Sibling subagents build/verify the same tree concurrently, and canonical filenames
(e.g. `council_notes/verify_phase6.py`) get contested — two different siblings
wrote that file while this dojo work ran, and a blind write clobbered both.
Rules that worked:
- On any write warning naming a sibling ('modified by sibling subagent ...'),
  RE-READ the file before writing; if you can't reconcile, don't write that path.
- Don't fight over the canonical name: either unify the content into the
  phase-level artifact (the campaign's verify_all.py convention — one verifier per
  phase) or save yours under a unique scoped name and stop touching the shared path.
- Untracked files are unrecoverable via git (no history), and sibling sessions
  don't appear in your session_search — treat overwritten content as lost.
- Verification evidence is the RUN OUTPUT, not the script: a sibling may replace
  the script after you run it; the captured output is timestamped and durable.
- Sibling-owned artifacts change mid-session (Workplace_Dojo went failing ->
  passing between probe and final run). Re-probe before your final verification.
- When a task constrains output ('output ONLY the N files'), support files
  (verifiers, references) live OUTSIDE the deliverable dir (council_notes/,
  skill library), and additions are reported in the summary, not hidden.

## Pitfalls
- Do not add files beyond the 7 canonical artifacts inside the dojo dir; the user
  may constrain output ("output ONLY the N files plus a K-line summary") — deliver
  exactly that shape in the final response.
- Boundary rules must appear for every persona, not just once in the bank.
- Every rubric dimension needs an evidence field, or the verifier fails.
- Persona refs in scenario tables must match persona bank ids exactly.
- Validate JSON/YAML with python3 (json/yaml) before running the verifier.
- Keep the 5-stage core ids when adapting; remap semantics rather than renaming —
  the `adapted_from` block is what documents the change.
- Self-correction drafts leak into deliverables: an in-flight 'wait, X not Y' note
  landed inside a dialogue_state_machine.json; the verifier's drafting-artifact
  check (`"wait," not in content`) catches it — run it before declaring done.

## References
- `scripts/verify_dojo.py` — generic per-dojo verifier (statically re-runnable).
- `references/domain_adaptations.md` — Ambivalence + Conflict dojo designs (stage
  families, hard gates, rubric extensions, persona dynamics, intensity tuning),
  the phase-6 verification outcome, and the parallel-build coordination lessons.
- `references/phase8_qa_findings.md` — Phase 8 QA-checklist deliverable: exact
  verify_phase6.py coverage map (generic vs owned), the G1-G7 gap register, and
  the Phase 7 harness integration surface (routines/logs/governance contracts).
- `references/phase8_evaluation_docs.md` — master-rubric anatomy + calibration-log
  discipline: verifier→criterion map for all 10 criteria, the 16-row correction
  digest (rows 1-16 with their guards), standing items Q6-Q11, and the artifact
  source map used to ground the evaluation docs.
- `references/acceptance_testing.md` — the live-session acceptance test pattern:
  proven hermes chat invocation, log-schema validation checker (re-runnable),
  the acceptance-test decision-memo flow (compact codes → Calibration_Log), and
  the worked acceptance test 001 (Ambivalence_Dojo) transcript summary.
