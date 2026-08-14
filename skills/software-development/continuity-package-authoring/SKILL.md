---
name: continuity-package-authoring
description: Use when revising a handoff package for agentic research.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [handoff, continuity, agentic, research, revision, cost-control]
    related_skills: [project-context-recovery, council-review, hermes-agent-skill-authoring]
---

# Continuity Package Authoring

Use when authoring or revising a handoff/continuity package for an agentic research project — a document that bridges an agentic research session across context windows, carrying the project state, operating law, and next-context briefing into the next window.

## Overview

A continuity package (handoff package, context-window handoff) is the document that lets a future chat window resume an agentic research project with minimal context loss. Its job is to carry: the operational database reference, the project understanding, the current state, the operating disciplines, the next-task instruction, and any build specs the next window needs.

A continuity package is **not** the database. The database (evidence matrix, wiki, backlog, board) is separate. The package is the continuity frame.

This skill governs the act of writing or revising one. The central lesson from the Monstare v2→v3 revision: **a continuity package must not describe an agentic orchestration as functional unless it has verified that the orchestration actually exists.** If the harness doesn't exist, the package must either build it or admit the gap explicitly.

## When to Use

- The user asks you to revise, improve, or rewrite a handoff/continuity package.
- A new session is starting from a handoff package and you need to assess whether the package is accurate about what exists.
- You are writing a first-version handoff package for a project that uses agentic orchestration.
- A handoff package references a role structure, a kanban board, a harness, or an agentic setup and you need to verify those things exist.

**Don't use for:** writing a single-session plan or brief (use `plan`); recovering context for a placeholder repo (use `project-context-recovery`); reviewing built work (use `council-review`).

## Process

### 1. Read the existing package and the operational database in full

Read the handoff package first (it orients you), then the database it references (evidence matrix, wiki, board, backlog — whichever the package names as operational). Treat the database as the source of truth and the package as the continuity frame. If they conflict, the database wins.

### 2. Verify every referenced harness, board, and role structure exists

This is the most important step and the one most often skipped. For every agentic artifact the package describes as existing or functional, check:

- **Role structure / operating posture:** are there actual role prompts, subagent bindings, or delegate_task definitions that implement the roles? Or is it just a list of names with one-line descriptions? A role list is a design, not a running system.
- **Kanban board:** does the board exist at the path the package claims? Does it have the right project slug? (A board for a different project is not the right board.)
- **Agentic harness repo:** does the referenced repo exist, and does it contain a project-specific orchestrator? Or is it a general skill library with no project-specific harness?
- **Subagent/spawn mechanism:** is `delegate_task` functional in the current environment? Has it been tested?

If any referenced artifact doesn't exist, **the package must say so explicitly.** Do not describe a non-existent harness as an "operating posture" or "current built cosmos" — that creates a false continuity frame that the next window will inherit.

### 3. Identify quality gaps

With the database and the package in hand, identify:

- What the package claims that the database doesn't support.
- What the package omits that the database contains.
- What the package assumes about the next window's capabilities (agentic harness, token budget, model tier) that may not be true.
- What the package describes as "done" that is actually incomplete (e.g. "source discovery complete" vs "charting complete").
- Whether the package's next-task instruction matches the actual priority gap.

### 4. Draft the revision

The revision should carry, at minimum:

- **Purpose and normalization path** (what database it normalizes against, what it supersedes).
- **Project understanding** (telos, operative stack, current fork settlement, cosmos image, proportion guard).
- **Current state** (row counts, priority distribution, source discovery status, charting status, staleness status) — drawn from the database, not from memory.
- **Operating disciplines** (the non-negotiables).
- **Next-task instruction** (what the next window should do first, with batch size, with role configuration, with access-caveat handling).
- **Build specs for anything the next window needs to build** (role prompts, harness assembly, board creation) — with the explicit admission that it doesn't exist yet.
- **Cost-control measures** (see below).
- **Smoke test** (see below).
- **DO NOT DO NEXT** list.
- **Patch law** (what edits are permitted by default vs. require explicit instruction).
- **Open issues** (including "the harness doesn't exist yet" if applicable).
- **Handoff prompt** (the actual prompt the next window should use).

### 5. Cost-control measures (mandatory section)

Any continuity package that instructs an agentic next window to do structured work (charting, review, synthesis, build) must include a cost-control section. Without it, a full QC-layer batch can burn a session budget in one pass. The section must cover:

- **Per-session budget envelope:** a token budget for the session, with a hard stop at 95% and a collapse-to-Pip+Locus at 80%.
- **Per-role token budgets:** a table of default budgets per role, with guidance on when to increase or decrease.
- **Batch-size discipline:** max batch size, estimated cost per row, and the rule that a batch exceeding 15% of session budget should be split.
- **Source-access cost control:** don't download full PDFs for every row; prefer abstract/intro/conclusion; don't burn budget bypassing access gates.
- **Role-collapse economy:** a decision table for when to spawn the full harness vs. a collapsed configuration. The control is the decision table — don't spawn roles "just in case."
- **Model-tier guidance:** which model tier to use for the main session vs. role subagents, and the rule that a stronger model doesn't substitute for missing QC roles in a collapsed batch.
- **Hard stop conditions:** protected-floor breach that can't be resolved, budget exhaustion, consecutive QC failures, forbidden-edit detection.

The exact budget numbers are project-specific and should be filled in by the package author from the actual model pricing. Leaving them as placeholders is acceptable for a draft; the next window should fill them before executing.

### 6. Smoke test (mandatory section)

Before instructing the next window to execute a full batch, the package should specify a smoke test: a 1-row (or smallest-possible) execution with the collapsed configuration that confirms the harness produces usable structured output. The next window should not proceed to the full batch until the smoke test passes.

The smoke test row should be:
- From the same batch as the full execution.
- Load-bearing enough to be representative, but small enough to be cheap.
- A row with a readable source (not a restricted/gated one) so the test exercises the real charting path.

### 7. Write the file

Write the revised package to a versioned filename (e.g. `Monstare_Context_Window_Handoff_Package_v3.txt`), leaving the previous version in place. The previous version is the record of what the package said before the revision.

## Cost-control measures — detailed checklist

See `references/cost-control-checklist.md` for the full checklist including the per-role budget table shape, the batch-size decision table, and the hard stop conditions.

## Smoke test — detailed pattern

See `references/smoke-test-pattern.md` for the smoke test design pattern including row selection criteria, collapsed-configuration specification, pass/fail criteria, and what to record.

## Harness verification — detailed checklist

See `references/harness-verification-checklist.md` for the step-by-step verification checklist: what to check for each type of referenced artifact (role structure, kanban board, harness repo, spawn mechanism), what counts as "exists and functional" vs. "exists but not functional" vs. "doesn't exist," and how to record the verification result in the package.

## Common Pitfalls

1. **Describing a non-existent harness as functional.** The most consequential failure mode. A handoff that says "the next window should operate as Pip/Locus/Evidence Librarian/etc." when no such orchestration exists creates false continuity. The next window inherits a role list with no way to execute it. Always verify before describing.

2. **Omitting cost controls.** A continuity package that sends the next window into a multi-role batch without a budget envelope is a budget hazard. The cost-control section is mandatory, not optional polish.

3. **Skipping the smoke test.** Sending the next window straight into a full batch without confirming the harness produces usable output is risky. A 1-row smoke test is cheap insurance.

4. **Treating the package as the database.** The package is the continuity frame; the database is the source of truth. When they conflict, the database wins. Don't let the package's narrative override the database's actual state.

5. **Writing cost-control measures as vague advice.** "Be mindful of token spend" is not a cost-control measure. A cost-control measure is a budget number, a decision table, a hard stop condition, or a collapse rule — something checkable.

6. **Leaving budget placeholders unfilled in the executed package.** If the package is going to be executed by the next window, the budget numbers should be filled in (from actual model pricing) before execution. A package with `<budget_X>` placeholders is a draft, not an executable instruction.

7. **Describing source discovery as charting.** "Source discovery is complete" is not the same as "charting is complete." A package that conflates the two gives the next window the wrong priority signal.

8. **Forgetting the DO NOT DO NEXT list.** The things the next window should not do are as important as the things it should do. Without this list, the next window may regenerate the spreadsheet, remove URLs, or mark rows charted prematurely.

9. **Creating a one-session-slug-named skill instead of a class-level skill.** If you're capturing this lesson as a skill, the skill name should be `continuity-package-authoring`, not `monstare-handoff-revision`. The class is "authoring/revising continuity packages for agentic research projects," not "the Monstare handoff."

## Verification Checklist

- [ ] The package's claims about current state match the database.
- [ ] Every referenced harness, board, and role structure has been verified to exist (or the package explicitly says it doesn't).
- [ ] The package includes a cost-control section with a session budget envelope, per-role budgets, batch-size discipline, and hard stop conditions.
- [ ] The package includes a smoke test specification (1-row, collapsed configuration, pass/fail criteria).
- [ ] The package's next-task instruction matches the actual priority gap.
- [ ] The package includes a DO NOT DO NEXT list.
- [ ] The package includes a patch law (permitted vs. not permitted edits).
- [ ] The package includes open issues, including any harness-existence gap.
- [ ] The package is written to a versioned filename, leaving the previous version in place.
- [ ] If the package defines roles, each role has a spawn prompt with inputs, return contract, and budget.

## Support files

- `references/cost-control-checklist.md` — detailed cost-control checklist.
- `references/smoke-test-pattern.md` — smoke test design pattern.
- `references/harness-verification-checklist.md` — harness verification checklist.
