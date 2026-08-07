# Motivational Ecology Agent Architecture

**A governed learning-and-agency-support architecture for agentic systems —
built on a 2,000-year-old epistemic discipline, verified by 9 machine checks
and 3 independent judge rounds, and demonstrated in a live acceptance test.**

> **Proof-of-concept package.** This repository ships the complete estate:
> the full 8-package skill library, the 5 practice dojos, the Phase 5
> safeguards, the evidence base, the calibration log (all 22 rows), the raw
> judge verdicts, the acceptance-test runtime record, and the in-tree
> verifier — everything needed to install, verify, and exercise it.

---

## What this is / What this is NOT / Why Valens / What you can check now

- **What this is:** a five-layer agent architecture (insight lattice → skill
  graph → safeguards → practice dojos → evidence/logs) whose central rule is
  that **the agent proposes and the human disposes — enforced structurally,
  not promised in prose**.
- **Where it runs:** a **home lab** — a personal, self-hosted Hermes setup on
  one's own machine, built for personal use: your own learning, motivation,
  and agency. **It is not a workplace or enterprise system** — no deployment
  story, no org integration, no shared infrastructure. It does not assume (or
  want) a corporate environment.
- **What this is NOT:** not astrology, not a finished coaching product, not a
  replacement for human judgment, not a product. The Valens corpus is used as
  a *source of epistemic method* — its reconstruction discipline (preserve
  witnesses, label source-vs-inference, quarantine untrustworthy claims,
  refuse premature coherence) is transposed into verifiers and guards. No
  astronomical content is used anywhere.
- **Why an astrologer's corpus:** reconstructing a 2,000-year-old text from
  corrupted manuscripts *requires* exactly the discipline an agency-preserving
  agent needs — and the corpus is a documented, checkable stress-test of that
  discipline, not a slogan. An interface is an edge, not an identity: shared
  vocabulary never repairs a missing connection, and the same holds for
  systems that say they respect judgment versus ones that provably do.
- **Corpus pointer (meld, Phase 9):** the Valens corpus itself is a frozen
  archive at `~/.hermes/hermes-agent/docs/Valens Anthologies/` (Riley
  translation + 115 reconstruction artifacts). It lives OUTSIDE this estate
  by design (Dallas Q1.1, Q1.5 — operating logics only, corpus frozen). The
  estate's operational form of the corpus is
  `governance/valens_operating_logics.md`; the meld record is `meld/`. Per
  the meld decisions: Valens is a source about METHOD, not findings; the
  corpus is exempt from evidence flags (historical archive).
- **What you can check right now:** `python3 verify/verify_harness.py`
  (passes, exit 0, against this tree). Then read the calibration log — 22
  rows of the campaign's own errors, each finding → fix → verifier guard.

## The five layers

```
                    ┌─────────────────────────────┐
                    │   MOTIVATIONAL LATTICE      │  insight engine —
                    │  (insights are hypotheses,  │  every claim is a
                    │   user-correctable)         │  hypothesis, never
                    └───────────┬─────────────────┘  a verdict
                                │ triggers T1-T6
                    ┌───────────▼─────────────────┐
                    │   SKILL GRAPH               │  8 skill packages,
                    │  (typed edges, reconciled   │  90 files, atomic
                    │   single source of truth)   │  operations
                    └───────────┬─────────────────┘
                                │ governed by
                    ┌───────────▼─────────────────┐
                    │   SAFEGUARDS (Phase 5)      │  ACT/SCAFFOLD/ASK/
                    │  empowerment boundary,      │  DEFER/STOP modes;
                    │  atrophy controls, fade     │  preserved-user-
                    │  rules                      │  decision set
                    └───────────┬─────────────────┘
                                │ exercised in
                    ┌───────────▼─────────────────┐
                    │   PRACTICE DOJOS            │  5 environments,
                    │  (ambivalence, conflict,   │  state machines,
                    │   coaching, workplace,      │  spirit gate, no-
                    │   conversation)             │  coercion rules
                    └───────────┬─────────────────┘
                                │ logged to
                    ┌───────────▼─────────────────┐
                    │   EVIDENCE + LOGS           │  runtime log schema,
                    │  (78-source evidence base,  │  append-only, consent-
                    │   retraction register)      │  scoped
                    └─────────────────────────────┘
```

## Quick start (real — runs against this tree)

```bash
# 1. Verify the estate (self-locating; checks inventory, parse, coherence)
python3 verify/verify_harness.py

# 2. Install the skills into Hermes
cp -r skills/* ~/.hermes/skills/

# 3. Run a dojo session through the ConvoDojo executor
#    (spirit gate, intensity profile, preserved-user-decision debrief are
#    enforced by the artifacts; the boundary-gate execution layer is Phase 9)
```

## The proof, in three parts

### 1. The calibration log — the campaign's own error record

`evidence/Calibration_Log.md` — **all 22 corrections**, each recorded as
**finding → fix → verifier guard**. This is the integrity proof: a system
that records its own errors (including "our verification gate claimed nine
verifiers but ran three" — caught by an outside judge, rewritten, guarded by
itself) is a system whose other claims are worth reading.

There's a truth worth sitting with: a system that can't admit its own errors
can't be trusted to protect yours. And admitting errors is structurally
easier than admitting them socially — the log doesn't have to save face, it
just has to be append-only.

Highlights:
- Row 1: a README claimed "all VERIFIED" — false; corrected; now guarded by a
  regex that fails the build on bare overclaims.
- Row 5: the flagship edge `decomposes_to COMB→TDF` was declared in the index
  but contradicted by a package's reverse edge — reconciled, direction-
  sensitive verifier added.
- Row 17: `verify_all.py` documented as "chains every verifier" but ran 3 of
  9 — rewritten as the full gate; the guard is the gate itself.
- Rows 18-20: state-variable rename missed in prose, user-agreement key
  drift, bibliography header overclaim — each fixed and guarded.

### 2. The judge verdicts — three independent review rounds (raw, unedited)

`evidence/judge_verdicts/` — the full critiques from Claude and DeepSeek via
API, each with a detailed rubric, each finding real defects that were
integrated and guarded. The final whole-project verdict: **4.7/5, DEPLOY**
(`judge_deepseek_whole_project.txt`), with the judge independently verifying
four citations against publishers live via DOI (see
`evidence/judge_verdict_summary.md` for the checkable table).

**Honest framing:** the judges are LLMs — the same model family that built
the estate. Their value is as *adversarial reviewers whose every finding was
machine-held*, not as independent human auditors. The proof is in the loop:
judges find defects, the campaign fixes them, the fixes are mechanically
guarded. Read the raw verdicts and find the 23rd error before praising the 22
fixes.

### 3. The acceptance test — the architecture ran, and the gate held

`evidence/acceptance_test_001.json` + `.debrief.md` + the gate output
(`evidence/verify_gate_output.txt`) — a live dojo session (ambivalence about
starting exercise) through the real model pipeline:

- The **spirit gate fired exactly once** at the single technique-without-
  spirit turn — flagged, never graded, corrected (per the MI fidelity rule).
- The session **logged per a strict append-only schema** (consent-scoped).
- The log's outcome field said, **by design**: *"pending — user arbitrates
  every pass."* The system refused to arbitrate for the human even in its own
  acceptance test.
- The user then **approved** it — in the record, verbatim.

**Honest caveat:** the runtime evidence is one session, one approval. The
gates are mechanical and the log is append-only, but the runtime sample is
n=1 — read the log and judge whether that matters. The boundary gate is not
yet enforced at the execution layer (Phase 9 — a declared firewall isn't a
working firewall, and we say so).

## What's in this package

```
├── README.md                  ← this file
├── skill_graph_index.json     ← the reconciled graph (full)
├── DEFERRED_PACKAGES.md       ← the honest open ledger
├── handoff_notes.md           ← continuity record
├── skills/                    ← 8 packages, 90 files (full estate)
├── lattices/                  ← insight engine: schemas, policy, examples
├── routines/                  ← 5 dojos × 7 artifacts (full)
├── governance/                ← the 5 Phase 5 safeguards (full)
├── logs/                      ← runtime log schema + acceptance record
├── evidence/                  ← 78-source base, calibration log (22 rows),
│                                raw judge verdicts, gate output
├── verify/verify_harness.py   ← the in-tree verifier (runs, exit 0)
├── docs/                      ← architecture, safeguards, verification,
│                                valens-principles
└── LICENSE
```

## The philosophy, stated plainly

- **Skill preservation is a measured objective.** The architecture tracks its
  user's skill load and fades scaffolding. The campaign applied that to
  itself (see evidence/Calibration_Log.md Q10).
- **Hypothesis-status over doctrine.** Every insight is a hypothesis, user-
  correctable; rejection is absolute (quarantine law, Q3).
- **Questions outrank conclusions.** Ambivalence is a designed halt state,
  not a defect.
- **The agent proposes; the user disposes.** Structurally, not stylistically.
- **Declared is not enforced.** A stated rule is a promise; a verifier-guarded
  rule is a fact. The whole architecture is the difference between the two.

## What we'd love feedback on

1. **The calibration-log integrity loop** — is a finding→fix→guard record
   with machine-held fixes a credible anti-circularity mechanism for
   agent-supervised agents?
2. **The spirit-gate semantics** — flagged-once-never-graded as a coaching
   invariant; is it the right design?
3. **The 47 review-enforced checks** — content-level checks the verifiers
   don't cover; how would you machine-guard them?
4. **Q6/Q10/Q11** — the honest open ledger: what would you close first?

## Status & roadmap

- **Phase 1-8: COMPLETE at the specification/verification level** — 9/9
  verifiers green (gate output shipped); 3 judge rounds integrated; acceptance
  test user-approved. The runtime layer beyond the acceptance session is
  unexercised (one session, n=1).
- **Phase 9 (scheduled):** execution-layer boundary gate (a plugin that
  refuses to run an operation without a boundary pass); intervention-design
  extension of the diagnostic layer; transposing the remaining Valens
  principles into verifier rules — 31 design questions already written.

---

*Built 2026-08-06. Questions, critiques, and collaboration welcome — the
calibration log is the fastest way in.*
