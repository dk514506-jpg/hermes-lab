# Monstare Handoff Revision v2 → v3 — Worked Example of Continuity Package Authoring After a Capability-Claim Audit

## Context

The Monstare project had a v2 handoff package that described an agentic role structure (Pip, Locus, Evidence Librarian, Methodologist, Cosmotechnic-Purist, Phenomenologist, Ethics & Cosmotechnic Auditor, Data & Instrumentation Steward) as if it were an existing "operating posture." A diagnostic probe run in the same session (delegation `deleg_1131ee68`, 2026-08-13 16:27) surfaced that the harness did not actually exist — the roles were a design, not a running system, with no prompts, no subagent bindings, and no `delegate_task` definitions. The kanban board at `/opt/data/kanban/` was a Poplar.agency board. The `hermes-lab` repo was a general skill library with no Monstare orchestrator.

This reference captures the revision process — the quality gaps found, the decisions made, the budget values drafted, the smoke-test design, and the diagnostic-probe-reconciliation pattern — as a worked example for the `in-session-capability-verification` skill's "verify before you build" discipline. The probe case study (`monstare-probe-case-study.md`) covers the misread event itself; this reference covers the revision that the misread triggered.

## What the v2 handoff claimed vs. what existed

| Claim in v2 | What actually existed | Verdict |
|---|---|---|
| "Operating roles for future chat: Pip, Locus, Evidence Librarian, ..." as an "operating posture" | A list of role names with one-line descriptions. No prompts, no spawn bindings, no delegate_task definitions. | **Exists but not functional** — a design, not a running system. |
| Implicit: the next chat window can run these roles | No mechanism specified for how the roles would be instantiated or how they would hand off to each other. | **Doesn't exist as specified.** |
| "The operative stack is: COSMOS -> ETHIC -> GRAMMAR -> ARTIFACT -> PILOT / EVIDENCE" | This is the project's conceptual stack, correctly stated, and is independent of the orchestration question. | Correct. |
| "Current built cosmos uses The Sky: Windy, Heavy/Low, Flat, Storm, Returning" | This is the project's built cosmos image, correctly stated. | Correct. |
| "Source discovery is complete enough for charting to begin" | Matrix had 129 rows, all with a readable URL/landing/access path. 0 rows charted. | Correct. |

The v2's one real failure was the role structure. Everything else in the package was accurate; the revision didn't need to redo the project understanding, the matrix state, or the operating disciplines. It needed to (a) admit the harness gap, (b) add a build spec that tells the next window how to assemble it, and (c) add cost controls and a smoke test before sending the next window into a multi-role batch.

## Quality gaps found during the revision

1. **Role structure described as functional but not built.** The largest gap. The v2 listed roles as an "operating posture" — a phrase that implies they're already in operation. They weren't. The revision had to either build the harness or admit the gap. It chose to do both: add a build spec (section 5 of v3) AND add an open issue (#8) stating the harness is not built.

2. **No mechanism for how roles would run.** Even if the roles had existed, v2 didn't say how they'd be instantiated (which tool, which prompts, which return contracts) or how they'd hand off to each other. The revision added `delegate_task` as the spawn mechanism, role prompts as the binding, and a handoff protocol between roles.

3. **No cost controls.** A 7-role, 12-row batch without budget controls is a session-budget hazard. The revision added a full cost-control section (v3 section 5.4) with session envelope, per-role budgets, batch-size discipline, source-access cost control, role-collapse economy, model-tier guidance, and hard stop conditions.

4. **No smoke test.** Sending the next window straight into a full batch with a newly built harness is risky. The revision added a 1-row smoke test (CORE-01, collapsed Pip + Locus) as Step 1 of the first-session agenda, before the full batch.

5. **Budget numbers left as placeholders.** The v3 draft had `<budget_X>` placeholders. That's acceptable for a draft, but if the package is going to be executed, the numbers should be filled in. The revision filled them in from the model pricing context (session 100,000 tokens; per-role 8,000/12,000/10,000/10,000/8,000/8,000/4,000).

6. **No diagnostic-probe reconciliation.** The probe returned a conclusion ("delegate_task is gated/unavailable") that was wrong, and the probe's own evidence (the parent had just dispatched it) contradicted that conclusion. The revision added a "Diagnostic Probe Notes" section to the handoff that records the probe's findings with the misread corrected, explains why the leaf child can't call delegate_task (intended design), and adds the caveat that the next window must still smoke-test CORE-01 in Step 1 to confirm delegate_task is live in THAT session. This is the reconciliation pattern in action: record both the probe's findings and the correction, so the next session doesn't re-litigate the same question.

## Budget values drafted for v3

These were filled in from the model pricing context of the session (upstage/solar-pro4:free via Nous). A different session with a different model should re-derive them.

| Parameter | Value | Rationale |
|---|---|---|
| Session total (5.4.1) | 100,000 tokens | Default charting session; leaves headroom for 2-3 batches with QC before hitting the 80% collapse threshold |
| Locus | 8,000 tokens | Structured report only; no source re-reading. Cheap per batch. |
| Evidence Librarian | 12,000 tokens | Highest QC budget because it may check DOI resolution, landing pages, and repository metadata. Drops to ~6,000 when all rows are open PDFs with clear DOIs. |
| Methodologist | 10,000 tokens | Empirical load-bearing rows need the most scrutiny. Priority C rows can use ~4,000. |
| Cosmotechnic-Purist | 10,000 tokens | Philosophical comprehension is the expensive dimension. Drops for Cosmo Rel. = low rows. |
| Phenomenologist | 8,000 tokens | Only spawned for Area 5/8/arousal-flow rows; skipped otherwise. |
| Ethics & Cosmotechnic Auditor | 8,000 tokens | Cross-stake check is structured and bounded. Cheap per batch. |
| Data & Instrumentation Steward | 4,000 tokens | Cheapest role — edit audit + staleness updates + patch log text. Always worth it. |
| Smoke test (1 row, collapsed) | ~3,000-5,000 tokens | Pip read + chart + Locus check on one open PDF. Well within budget. |
| Full 8-row batch estimate | ~70,000-80,000 tokens | Fits inside the 100,000 session envelope with room for one more small batch. |

Total budget check: the recommended first batch (8 rows: CORE-01, CORE-02, CORE-04, CORE-05, CORE-06, CORE-08, A1-01, HUI-2024) under the v3 decision table is a "5-8 rows, mixed areas, some high-cosmo-relevance" batch → full harness except Phenomenologist (no Area 5/8 rows). Sum of role budgets: 8k + 12k + 10k + 10k + 8k + 4k = 52k for QC, plus Pip's ~8k-12k for reading/charting 8 rows, plus source access cost (SDT PDFs are short and open; Hui 2024 is ~30 pages open access; A1-01 is longer — but for this batch we read the accessible portions, not full PDFs). Estimated total: ~70k-80k, inside the 100k session budget.

## Smoke test design and execution

**Row selected:** CORE-01 (Ryan & Deci, SDT 2000). Meets all smoke-test criteria from `smoke-test-pattern.md`:
- From the same batch as the full execution (motivational/cosmotechnic spine).
- Priority A (load-bearing).
- Readable source (open PDF on the SDT site).
- Short enough to be cheap (2000 article, ~30 pages equivalent).
- Not the most complex row in the batch (CORE-05, CORE-06, and HUI-2024 are more complex).

**Configuration:** collapsed Pip + Locus only. Did not spawn the full harness for the smoke test. The point was to confirm the charting pipeline works (Pip can read and chart a row; Locus can check it), not to exercise all seven roles.

**Execution:** Pip read the full source text (cached via web_extract earlier in the session), charted all four evidential columns plus H1/H2, Design Implication, Cosmotechnic Implication, and Causal Status, then wrote the charting to `/opt/data/Monstare_smoke_test_CORE-01_2026-08-13.md`.

**Result:** PASSED. The charting draft filled all evidential columns from the source (not seeded-text paraphrase), included explicit caveats (framework article, qualitative effect size, conceptual causal status, 2000 vs. 2017 edition caveat), and was internally consistent with the SDT source and the project disciplines. The Locus role prompt was saved to `/opt/data/Monstare_role_prompts/Locus_prompt.md` in parallel.

**What would have been a fail:** if Pip had paraphrased the matrix seed text instead of extracting from the source, or if the charting had marked the row "Verified" just because a source link exists, or if the effect-size column had been left as "[to chart]" — any of those would have failed the pass criteria and triggered diagnosis before the full batch.

## Diagnostic-probe reconciliation pattern

The diagnostic probe (delegation `deleg_1131ee68`) returned a conclusion that was wrong: "delegate_task is gated/unavailable in this session." The probe's own evidence — that the parent session had just dispatched it — contradicted that conclusion, but the probe didn't reconcile its evidence with its conclusion.

The correction was written into the v3 handoff as a "Diagnostic Probe Notes" section that:

1. **Records the probe's findings** (kanban board is real but Poplar.agency-only; agent.log shows delegate_task completions on Aug 8-13; cronjob is not a shell binary; the harness infrastructure has been used).
2. **Names the misread explicitly** ("delegate_task is gated/unavailable" is a misread).
3. **Explains why** (the probe is a leaf child; leaf children don't inherit delegate_task by design; the parent session just used it to dispatch the probe; the `_check_kanban_orchestrator_mode` warnings co-occur with delegate_task completions on the same days, so they are not a hard gate on async delegation).
4. **Confirms the harness build spec is viable** (Pip has delegate_task; role subagents don't, so prompts are self-contained — which is what section 5.3 specifies).
5. **Adds the caveat** that the next chat window must still smoke-test CORE-01 in Step 1 to confirm delegate_task is live in THAT session, since session state can change between chats.

This is the reconciliation pattern in action. The lesson for future sessions: when a probe returns a capability as unavailable, check (a) whether the probe was the role that's supposed to have that capability, and (b) whether the parent session has positive evidence of the capability (e.g. "this very probe was dispatched by X"). If both point the other way, the probe's conclusion is likely a misread, and the handoff should record both the probe's findings and the correction rather than letting the misread propagate.

## Lessons for future continuity-package authoring

1. **Verify every referenced harness artifact before describing it as functional.** This is the single most consequential step in the revision process (see `harness-verification-checklist.md`). A role list is a design; a kanban board for a different project is not the right board; a repo is not project-specific just because it's named similarly. Check each artifact's actual state before writing it into the package.

2. **When you find a non-existent harness, add both a build spec AND an open issue.** Don't just say "the harness doesn't exist" and leave it at that. Add the build spec that tells the next window how to build it, and add the open issue that makes the gap visible. The v3 did both: section 5 (build spec) and open issue #8 (the gap).

3. **Cost-control measures must be checkable, not advisory.** "Be mindful of token spend" is not a cost-control measure. A session budget envelope, a per-role budget table, a batch-size decision table, a collapse rule, and hard stop conditions are. The v3's cost-control section is the model for what a checkable cost-control section looks like.

4. **Fill budget numbers before execution, not after.** A package with `<budget_X>` placeholders is a draft. If the next window is going to execute it, fill the numbers from actual model pricing first. The v3 filled them in as part of the revision, not as a separate step.

5. **A smoke test is mandatory, not optional polish.** A 1-row smoke test with the collapsed configuration costs a few thousand tokens and confirms the harness produces usable structured output before the next window commits to a full batch. The v3 made it Step 1 of the first-session agenda, before the full batch. The smoke test was actually executed in this session (CORE-01, PASSED), which is the best possible validation of the pattern.

6. **Record the diagnostic-probe reconciliation in the handoff, not just in the session.** The probe's findings and the correction both belong in the handoff package so the next session doesn't re-litigate the same question. The v3's "Diagnostic Probe Notes" section is the model.

7. **The revision should not redo what's already accurate.** The v2's project understanding, matrix state, operating disciplines, and source-discovery status were all correct. The revision focused on the gaps (role structure, cost controls, smoke test, harness existence) and left the accurate parts intact. A revision that rewrites everything risks introducing errors in the parts that were right.

## Relationship to other references

- `monstare-probe-case-study.md` — covers the probe event itself (the misread, the log evidence, the correction). This reference covers the broader revision process that the probe triggered.
- `capability-verification-methodology.md` — the condensed verification ladder. This reference is the worked example of applying it to a real handoff revision.
- `harness-verification-checklist.md` — the step-by-step artifact verification. This reference shows the checklist applied to the Monstare v2 artifacts.
- `cost-control-checklist.md` — the cost-control section shape. This reference shows it filled in with actual numbers.
- `smoke-test-pattern.md` — the smoke test design pattern. This reference shows it executed.
