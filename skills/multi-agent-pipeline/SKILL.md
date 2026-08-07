---
name: multi-agent-pipeline
description: Design config-driven multi-agent triage pipelines on Hermes.
---

# Multi-Agent Pipeline

Design pattern for autonomous, config-driven multi-agent pipelines on Hermes.
Derived from the tonbistudio/hermes-multi-agent-workflow template (392★) and
the astral-research-harness persona integration.

## Architecture: Fat Engine, Thin Skill

The one design rule that governs everything:

**The domain lives in config (triage.yaml), not in Python.**

- `engine/` — deterministic logic: dedup, scoring validation, route resolution,
  task chain construction, workspace management. Unit-testable without a model.
- `triage.yaml` — the ONE file that defines your pipeline: sources, rubric,
  research lanes, route map, paths, roles. Edit this, not the Python.
- Orchestrator SKILL.md — reduced to the few steps needing model JUDGMENT:
  scoring dimensions, classification, proposal prose. Calls engine methods
  instead of re-implementing them in prose.

### Why This Split

- **Testable.** The engine runs without a model or a live board.
- **Adaptable.** Repointing at a new domain means editing config, not code.
- **Honest boundaries.** The model does fuzzy parts (is this painful? what's a
  good proposal?). Code does crisp parts (sum the score, compare to threshold,
  look up the route, build the task cards).

## Pipeline Stages

1. Detect — Scouts (cron-driven) write reports and create intake cards
2. Dedup — Token-cosine or embedding similarity against existing item vault
3. Score — LLM-mode (model judges rubric dimensions) or heuristic fallback
4. Research — Parallel fan-out across config-defined lanes; classifier lane
   emits routing value
5. Route — Config-driven map: classification → path name
6. Prep — Pre-gate chain: synthesize, ideate, draft proposal
7. Gate — Single human approval point (Telegram/Discord/Slack)
8. Fulfill — Post-gate chain in shared persistent workspace
9. Deliver — Final stage sends the output to the human

## FAOS Extension Schema

This skill has been extended to carry **FAOS (Field-to-Action Operating System)**
semantics — the full relational-procedural operating architecture designed for
this project. All extensions are data (new YAML blocks), not engine code.

A complete worked integration file lives at:
`references/triage_faos_integration.yaml`

### Extended Config Blocks

| Extension | YAML Block | What It Adds |
|---|---|---|
| Field Perception | `perception:` | Scout outputs a relational field model before task abstraction |
| Relational World Model | `field_model:` | Entities, typed relations, governed stakes with planetary ownership |
| Evidence Ladder | `evidence_ladder:` | 5-level epistemic provenance (impression→lead→fact→claim→judgment) with non-skip enforcement |
| Shadow Route | `route.map[].shadow` | Each route carries a monitored alternative with promotion conditions |
| Task Abstraction | `paths[].task_frame` | Per-path: success condition, non-goals, boundaries, evidential standards |
| Instrumented Close | `paths[].close` + global `close:` | 6 required close passes (victory, defect, dissent, proxy, boundary, transfer) |
| Dissent Requirement | `gate.dissent_required` | Per-task dissent quota before closure can proceed |
| Learning Loop | `learning_loop:` | Post-close reflection with digest-before-calibration rule |
| Persona Integration | `astra:` | Planetary circuit map, harness skill reference |

### Key Design Rules

1. **Field before task** — Scout outputs a relational model, not just flat fields.
2. **No evidence skips** — evidence ladder enforces: no impression→judgment
   without transiting lead→fact→claim.
3. **One shadow promotion** — Only one in-place stake promotion per task before
   re-abstraction is required (FAOS §7).
4. **Digest before calibrate** — learning_loop prevents rewriting event records.
5. **All 6 close passes** — victory, defect, dissent, proxy, boundary, transfer.
   Missing any changes result from TRUE to PARTIAL/INCONCLUSIVE/BLOCKED.

### Scoring: Planetary Governors

Rubric dimensions carry `planetary_governor` mapping each criterion to its
astral function:

```yaml
rubric:
  dimensions:
    - key: persona_impact
      max: 30
      planetary_governor: Mercury/Scorpio
    - key: pipeline_confidence
      max: 25
      planetary_governor: Saturn/Capricorn
```

### HOMES/See-R Integration

- **HOMES** hardware context feeds field_model entity types (hardware topology,
  VRAM telemetry) and enables hardware-pressure route entries.
- **See-R** epistemic standards (source inventory, authority mapping, quarantine,
  verification queue) map directly onto evidence_ladder levels and close passes.

## Role Mapping (Persona → Pipeline)

When integrating with the astral-research-harness persona:

| Persona Function | Pipeline Role | Behavior |
|---|---|---|
| Mercury in Scorpio (forensic intelligence) | Scout | Detects candidates, finds seams, pressure points. Surfaces only — no scoring or routing. |
| Jupiter/Moon in Pisces (reception, pattern sense) | Researcher | Receives the whole field, detects patterns, identifies what's charged or concealed. |
| Venus in Taurus (material fidelity) | Validator | Preserves evidence texture, checks source integrity, protects valuable fragments. |
| Saturn in Capricorn (method governance) | Orchestrator | Sequences pipeline, defines limits, authorizes transitions, manages the gate. Calls engine, not prose. |
| Mars in Capricorn (disciplined critique) | Critic / Tester | Cuts weak claims, tests artifacts. Only acts after Saturn authorizes. |
| Sun in Capricorn (durable authority) | Builder | Produces finished output. Completes pipeline with verified deliverable. |

Subfunctions:
- **Fabricator** activates during `fulfill` stage — build, test, verify.
- **Reluctant Corrector** activates at the gate or when scope rails are violated.

## Config Structure (triage.yaml)

Minimal required sections:

```
name:              Pipeline slug for logs/board
board:             Hermes Kanban board name
workspace_root:    Where per-item workspaces live
sources:           Scout definitions (id, profile, cron schedule, query)
item_schema:       Fields a scout emits per candidate
dedup:             Method + thresholds
rubric:            Scoring dimensions + weights + pass threshold
research_lanes:    Parallel research steps; classifier_lane marks the router
route:             Classification to path mapping
paths:             Per-path: prep, propose, fulfill, scope rails, workspace
roles:             Abstract role to Hermes profile mapping
gate:              Channel + approval verbs
```

Full key-by-key reference: https://github.com/tonbistudio/hermes-multi-agent-workflow

## Hard-Won Gotchas (Preserve These)

These cost real debugging in production. Do not regress:

- **Keep delegate_task goal strings SHORT; put detail in context.** A very
  long `goal` field (>~600 chars) can trip the task parser with "Task N is
  missing a 'goal'" — an error that repeats identically on retry of the same
  oversized payload (hit live 2026-08-06 dispatching a 3-task Council: two
  identical failures, then success after rewriting goals compact and moving
  the long instructions into `context`). The dispatch validator sees a
  truncated/overlong goal as absent. Rule: goal = one crisp sentence naming
  the deliverable + output path; context = the detailed brief.
- **Scout profiles need the `kanban` toolset.** Scouts run via cron (not the
  dispatcher), so kanban tools aren't auto-enabled. Without it the scout writes
  a report but silently can't create the intake task.
- **Post-gate stages need persistent `dir` workspaces, not `scratch`.** Scratch
  dirs are wiped between tasks, stranding the final delivery step. `engine.py`
  already does this for `fulfill` chains — don't change it to scratch.
- **Setting status does not equal delivering.** The orchestrator is a headless
  worker; it must actually run `hermes send --to <channel>` to reach the human.
  Status fields don't notify anyone.
- **Telegram reserves `/commands`.** Gate replies carry NO leading slash
  (`approve`, not `/approve`).
- **First task in a post-gate chain must be `ready` (no blocking parent).** A
  child of the still-open triage task would sit in `todo` forever.
- **Classifier lane is single point of routing truth.** Validate its output
  against the route map before spending model calls on the wrong path. Fail loud
  (ValueError) on unknown classifications — silent drops lose items.
- **Agent sessions are delegated-child contexts: kanban CLI mutations are
  refused by design.** `hermes kanban <mutate>` from inside an agent session
  errors with "delegate_task child contexts cannot mutate Kanban tasks via
  the CLI" (guard checks `is_delegated_child_process_context()` /
  `HERMES_DELEGATED_CHILD_CONTEXT`). The agent CAN read boards/init but
  cannot create/assign/complete tasks. Humans drive the board via CLI, the
  visual dashboard (`hermes dashboard` → Kanban tab, drag-drop cards), or
  `/kanban`. Agent-side pattern: prepare a `setup_kanban.sh` script (board
  create --switch + task creates + links) for the user to run in a parent
  terminal, and mirror board state into the campaign docs. Also note:
  `HERMES_KANBAN_BOARD` is pinned into every chat session's env by main.py —
  that is normal, not a worker marker; the guard keys off the delegated-child
  context instead.

## Shared-File Coordination in Parallel Subagent Campaigns

When the pipeline runs a parallel fan-out where subagents (siblings) write to a
shared workspace — e.g., Council-built artifact campaigns with a shared
`council_notes/verify_phaseN.py` and a shared index README — file collisions
are the norm, not the exception. Protocol:

1. **Treat every sibling-write warning as a re-read signal.** If a patch or
   write fails with "modified by sibling subagent", STOP, re-read the WHOLE
   file, and re-apply against the current content. Never re-assert your own
   earlier version over theirs.
2. **A sibling's rewrite of a shared file encodes the team convention — read
   it before writing.** Their structure usually reveals the agreed design
   (e.g., a per-owner spec dict). Contribute to THAT design; do not clobber
   it with yours. Re-writing a shared verifier to your own shape destroys
   other owners' checks.
3. **Extend, don't clobber.** If the shared verifier routes work by owner
   (`spec: {owner: sibling|owned, ...}`), promote YOUR artifact to `owned`,
   fill its spec entry (stages/gates/dims/stance), and add owner-specific
   checks in the established pattern. Everyone's checks survive.
4. **Calibrate shared checks to the ACTUAL convention, not your assumption.**
   When shared-contract checks false-fail on siblings' legitimate variations
   (optional enrichment keys, glossed anchor formats like `**engage (~ Goal)**:`),
   inspect the real artifacts, relax to the shared core, re-run. Never edit
   other owners' files to make your check pass.
5. **Route findings, don't fix siblings.** Failures on artifacts you don't own
   stay attributed to their owner for the coordinator to route. Edit only your
   own deliverables.
6. **Standing per-phase verifier over one-off scripts.** When verification is
   demanded, write/run the campaign's re-runnable verifier (`check()` /
   `fails` / exit-code pattern) covering the changed paths — the
   campaign-idiomatic pytest. Expect siblings to extend it; merge their edits
   and re-run until exit 0.
7. **Evidence flags must live at DATA level.** In campaigns with
   VERIFIED/RECONSTRUCTED evidence discipline, flags inside YAML comments do
   not count — parsers strip them. Put flags in data (grounding blocks in
   JSON/YAML, flag lines in markdown).

Worked example (2026-08-06 Phase 6 dojo campaign): see
`references/shared-file-coordination.md`.

## Safety Boundaries

- **Scope rails** are the safety boundary — keep them tight.
- The template runs LLM-authored code (build path) behind one human gate.
- Never commit `.env`, `auth.json`, board `*.db`, or `work/` vault contents.
- Pre-publish: run secret-scan checklist before open-sourcing an adapted copy.

## Reference

- Full source: https://github.com/tonbistudio/hermes-multi-agent-workflow
- Astral persona integration: skill_view('astral-research-harness')
