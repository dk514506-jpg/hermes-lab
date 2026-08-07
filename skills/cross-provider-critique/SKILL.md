---
name: cross-provider-critique
description: "Use when running outside judges from other APIs."
---

# Cross-Provider Critique Rounds

### Purpose
Get an INDEPENDENT critical voice on built artifacts (skill packages, harnesses,
documents, research syntheses) by running a judge model from a DIFFERENT
provider/API than the one that built the work. The judge has no campaign
context — it reads the actual files and reports what it finds. This is the
"outside judge" mechanism for review rounds: two independent judges converging
on a finding means it is real; a single judge's claim is a self-report until
you verify it.

### Trigger Conditions
- User asks to "involve outside judges from other APIs," "get a second
  opinion," "critique the output with Claude," or run a review round with
  independent voices.
- A build (Council or solo) finished and the user wants a truthfulness /
  packaging / governance audit before finalizing.
- You want to check whether claims in your own artifacts (evidence flags,
  inventory counts, edge sets) survive an adversarial reader.

### The Mechanism (proven invocation)
Write the judge brief to a FILE, then invoke Hermes with a short query pointing
at it. Long inline prompts break under nohup/background shell quoting
("unexpected EOF while looking for matching quote" — real failure).

```bash
# 1. Write the brief to council_notes/judge_brief.txt (or similar):
#    role, target path, what to read, the 4-6 assessment axes,
#    "name real files", "do NOT invent file contents; only report what you
#    actually read", output file path.

# 2. Run the judge in the BACKGROUND with notify_on_complete=true:
hermes chat -q "Read the judge brief at <path>/judge_brief.txt and execute it fully. Write your complete critique to <path>/judge_<provider>_<target>.txt" -m claude-sonnet-4-5 --provider anthropic
#    DeepSeek variant: -m deepseek-v4-flash --provider deepseek
```

Verified provider/model combos (2026-08-06):
- `claude-sonnet-4-5 --provider anthropic` — works; produces the deepest reads
- `deepseek-v4-flash --provider deepseek` — works; does real machine-checking
  (edge-set diffs, greps, count tallies) when the brief asks for it
- `gemini --provider gemini` — may 429 (quota); check `hermes auth list` first
- `openai-api gpt-4o*` — authenticates but 400s with "Unsupported parameter:
  'reasoning.effort'" when config.yaml has `reasoning_effort: medium`; only use
  OpenAI models that accept the parameter, or fix the config first

### Pitfalls (all hit live)
1. **Nohup + long inline prompt = shell-quote explosion.** `nohup hermes chat -q
   "<300-word prompt>" > file 2>&1 &` dies with "unexpected EOF while looking
   for matching quote" (conda shell hooks compound it). ALWAYS brief-to-file,
   then a short -q query. Background with the terminal tool (not shell nohup)
   so Hermes tracks the process.
2. **The 300s foreground timeout is too short** for a judge reading a large
   tree (~140 files). Run background + notify_on_complete; expect 3-8 minutes.
3. **`| tail -5` buffers everything** until the process exits — you cannot
   watch progress. Poll for the output FILE instead.
4. **Conda init noise in captured output is harmless** — it's shell startup
   chatter on the 2>&1 stream, not a judge failure.
5. **Judges are self-reports.** A critique may claim "verified X" when it only
   skimmed. Before integrating any finding: machine-check it yourself (grep the
   file, count the edges, diff the paths). In this campaign the judges were
   accurate, but one number (75 missing edges) turned out to be 206 in the full
   diff — verify, don't trust.
6. **Ask the judge to be specific**: "name real files," "what did you actually
   read vs infer," "machine-check X if you can." Specificity is what makes the
   critique integrable.
7. **A judge that exits in 2-3s with 0 tool calls is an API-level failure, NOT
   a transient flake** (hit live 2026-08-06: Anthropic "Your credit balance is
   too low" — three retries all died identically at startup). The conda block
   in the output is a red herring. Diagnose with a trivial probe:
   `hermes chat -q "Reply with exactly: ALIVE" -m <model> --provider <provider>`
   — the real error (credit/auth/quota/parameter) surfaces there. A retry loop
   is useless against API rejection; switch providers or surface the billing
   constraint to the user.
8. **Probe EVERY provider before dispatching judges.** Providers rot silently:
   pool keys go stale (OpenAI 401), quotas exhaust (Gemini 429), credit runs
   out (Anthropic 400 mid-campaign). One `hermes chat -q "Reply with exactly:
   X"` per candidate takes seconds and prevents a mid-round dead judge. Keep
   ≥2 verified voices so one failure doesn't kill the round — and when the
   user says "stop using provider X," re-dispatch the round on a verified
   alternative rather than treating the round as lost.

### Workflow (Dallas's preferred shape — plan BEFORE executing)
1. **Plan the revision process in writing first.** Dallas's standing
   preference: "plan out your revision process and proposed improvements before
   executing your editorial vision." Write the plan (what you'll fix, in what
   order, what the verifier will assert) before touching files.
2. Dispatch judges (2 providers preferred for convergence).
3. Read both critiques fully. Extract the kernel (what's strong — preserve),
   the weaknesses (negate), and the concrete recommendations (raise).
4. Verify each finding against the actual artifacts.
5. Execute the revisions, mapping each to its finding (R1/R2/... labels help).
6. Lock every fix into a durable verifier check so the gap cannot regress.
7. Re-run the full verification suite; update continuity records.

### Judge-driven corrections go into the calibration log
Every accepted judge finding ends up in the campaign's Calibration_Log.md as a four-
column row (phase/round | finding artifact-referenced | fix applied | verifier guard) —
"a correction with no verifier guard is one revision away from regressing." When a
finding is mechanical to fix, make it mechanical to guard too. Guard classes that
recurred in the Phase 7 harness round (each became a verify_phase7.py / shipped-
verifier check):
- cross-referenced documents missing from the packaged tree (README claimed 5 docs,
  only 2 shipped) → assert presence of every cross-referenced file
- index/package divergence (75 unindexed edges) → declare the index a curated subset
  + endpoint-validity check (full diff stays a build-time manual audit — say so)
- quarantine state living only in the index → per-package quarantine markers, checked
- stale pre-packaging paths (Phase3_Skills/, Phase6_Dojo/) → grep guard
- the verifier itself not shipped with the tree → ship a lightweight self-locating
  verify_harness.py for consumers
- count drift between index and artifact (47 vs 48 T2R entries) → assert exact counts
The Phase 8 master-rubric/calibration-log patterns live in `ecology-dojo-authoring`
(references/phase8_evaluation_docs.md) — load that skill when authoring the log.

### Integration Discipline
- Sublative method: preserve the kernel, negate the weak, raise the level.
- Convergent findings from 2 independent judges = confirmed; fix first.
- A judge's recommendation is a hypothesis until it matches the artifacts —
  apply the same evidence discipline to the critique as to the work.
- Record the critiques on disk (council_notes/judge_*.txt) so the revision
  round is auditable.

### Support Files
- `references/judge-round-playbook.md` — exact brief template, invocation
  commands, the verified provider table, and a worked example (harness judge
  round, 2026-08-06) with the full pitfall transcript.
- `references/whole-project-review.md` — the whole-project review shape
  (phases 1-N): review_rubric.md dimensions A-G, self-assessment-before-verdict,
  decision memos for user-sovereignty items, and the worked Ecology Phases 1-8
  example (4.7/5 DEPLOY). Load this when the user asks to review the whole
  campaign output, not just a single phase.
- `references/validator-rounds-and-public-packaging.md` — THREE patterns that
  extend review rounds into public deliverables: (1) the VALIDATOR pattern —
  a truthfulness checker that verifies numbered claims against primary files,
  plus the round-2 discipline (verify the FIXES, not the document; expect
  PARTIALs and newly-exposed residuals); (2) PUBLIC PoC PACKAGING tripwires —
  quick start must run against what ships, ship flagship evidence RAW not as
  curated extracts, timezone notes for UTC/local date traps, "proven"→
  "demonstrated" for n=1, anchor every checkable claim with DOIs, sweep for
  archive-root names in shipped files, and the "find the 23rd error" close;
  (3) VOICE MATCHING for shareable outputs — when the user provides their own
  writing as a tone reference (blog, Drive), draft predominantly in their
  register then punch it up (more mature/wise/insightful), keep docs/ neutral,
  and carry the home-lab-not-workplace scope framing.
  Load this when a review round is followed by "package this for GitHub" or
  "write a report for an external audience."

### Trigger addition (validator / public packaging)
- User asks for a report or package for an external audience (GitHub, Discord,
  blog) built from campaign artifacts, or wants "multiple rounds of review,
  revision, and resynthesis" on such a deliverable → load
  `references/validator-rounds-and-public-packaging.md` and run BOTH the
  validator round-2 loop and the skeptic-proofing checklist before delivery.
