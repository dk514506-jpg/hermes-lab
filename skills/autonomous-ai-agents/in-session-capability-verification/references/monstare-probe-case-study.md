# Monstare Probe Case Study (2026-08-13) — Worked Example of the Misread Class

## What happened

A leaf subagent (delegation `deleg_1131ee68`, run 2026-08-13 16:27:23) was dispatched to verify whether a multi-agent orchestration harness was functional in the current Hermes session for the Monstare project. The parent session had already dispatched it via `delegate_task` — which is itself positive evidence the capability was functional — but the probe was asked to independently verify.

## The probe's findings (what it got right)

- The kanban board at `/opt/data/kanban/` is real and was used: a poplar-agency board with `kanban.db` (127 KB SQLite), 4 task attachment directories with real markdown files, and 4 task logs showing real agentic work on Aug 11. The board is a Poplar.agency board only — no Monstare board exists.
- agent.log shows `delegate_task` completions on Aug 8, Aug 10, Aug 11 (3 completions), and Aug 13 (the probe itself), with subagent sessions spawned via `run_agent` on thread `async-delegate_0`. On Aug 11, the kanban dispatcher spawned 4 subagents through the board. The harness infrastructure has been used.
- `cronjob` is not a shell binary (`which cronjob` fails), and `tool_search` for "cronjob" found no match from the leaf child's perspective. The leaf could not confirm `cronjob` at runtime because it does not have the tool.

## The probe's misread (what it got wrong)

The probe concluded: **`delegate_task` is "gated/unavailable" in this session**, blocked by `_check_kanban_orchestrator_mode` returning False.

How it reached that conclusion:
1. `tool_search("delegate_task multi-agent delegation")` — found no match (leaf child scope).
2. `tool_describe("delegate_task")` — rejected: "not a deferrable tool."
3. `tool_call("delegate_task", ...)` — rejected: "not a deferrable tool."
4. Observed the `_check_kanban_orchestrator_mode` warnings in agent.log.
5. Concluded the capability is gated/unavailable.

## Why that conclusion is wrong

The probe IS a leaf child dispatched BY `delegate_task`. The parent log line at 16:27:23 reads:

```
2026-08-13 16:27:23,512 INFO [20260813_160151_c3d8b9] tools.async_delegation: Dispatched async delegation batch deleg_1131ee68 (1 task(s), session_key=20260813_160151_c3d8b9)
2026-08-13 16:27:23,513 INFO [20260813_160151_c3d8b9] agent.tool_executor: tool delegate_task completed (0.20s, 1496 chars)
```

The parent session HAS `delegate_task` and just used it. The leaf child does NOT inherit `delegate_task` — that is the intended design, which is exactly why role prompts in the Monstare v3 handoff (section 5.3) must carry full context inline. The probe's inability to call `delegate_task` is EXPECTED and is NOT evidence the parent lacks it.

## The log evidence that reconciles the conflict

`_check_kanban_orchestrator_mode` returned False **on the same days** that `delegate_task` completed successfully:

| Date | delegate_task completions | orchestrator_mode warnings |
|---|---|---|
| 2026-08-08 | 1 | 1 |
| 2026-08-10 | 1 | 2 |
| 2026-08-11 | 3 | 7 |
| 2026-08-13 | 1 | 1 |

If the warning were a hard gate on async delegation, there would be no delegate_task completions on those days. The co-occurrence proves the warning gates a DIFFERENT set of kanban-orchestrator-specific tools, not the async delegation path. The probe mistook a co-occurring warning for the cause of a limitation that was actually just the leaf-child scoping.

## The correction written into the v3 handoff

The Monstare_Context_Window_Handoff_Package_v3.txt gained a "Diagnostic Probe Notes" section (added after the probe returned) that:

- Records the probe's findings with the misread corrected.
- Explains why leaf children can't call `delegate_task` (intended design).
- Confirms the harness build spec (section 5) is viable: Pip (main session) has `delegate_task` and can spawn role subagents; role subagents don't have it, so prompts are self-contained.
- Adds the caveat that the next chat window must still smoke-test CORE-01 in Step 1 to confirm `delegate_task` is live in THAT session, since session state can change between chats.

## Lessons for future sessions

1. **When a leaf says "tool X is unavailable," check whether the leaf is the role that's supposed to have X.** If X is a parent/orchestrator tool, the leaf's negative is expected and is not evidence.
2. **When a log warning co-occurs with successful usage, the warning is not the cause of whatever limitation you're investigating.** Check co-occurrence before concluding.
3. **A smoke test from the correct role resolves these disputes cheaply.** A 1-row delegate dispatch from the parent costs a few hundred tokens and settles whether `delegate_task` works in the current session. The Monstare probe was unnecessary in the sense that the parent already had the answer — but it surfaced a real risk (the next session might have inherited the misread) and the correction was worth writing.
4. **Handoffs should record the evidence source for every capability claim.** The v2 handoff asserted an "operating posture" with 7 roles as if the harness existed. It didn't say who would run those roles, how, or from what tool. The v3 build spec fixes that by specifying `delegate_task` as the mechanism, role prompts as the binding, and a smoke test as the gate. The next handoff should carry the same level of mechanism specificity for any capability it depends on.
