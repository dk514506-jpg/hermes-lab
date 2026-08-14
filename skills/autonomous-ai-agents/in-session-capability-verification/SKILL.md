---
name: in-session-capability-verification
description: "Verify a tool works before building plans that depend on it."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [verification, delegation, multi-agent, orchestration, anti-fabrication, capability-checking, before-you-build]
    homepage: https://github.com/NousResearch/hermes-agent
    related_skills: [hermes-agent, external-source-verification]
---

# In-Session Capability Verification

Verify that a tool, runtime capability, or inherited orchestration claim is actually **functional in the current session** before building a plan, handoff, or skill that depends on it. This is a different class from URL/repo existence checking (see `external-source-verification`): the question here is not "does X exist" but "can I actually use X *from this agent role, in this session, right now*."

## When to use

- The user or a handoff document claims an orchestration harness, role structure, agentic pipeline, or specific tool is already in place and functioning.
- You are about to write a plan (handoff package, skill, campaign doc) that assumes `delegate_task`, `cronjob`, kanban dispatcher, or any multi-agent mechanism works.
- A child/subagent reports a capability as unavailable and you are about to treat that as evidence the capability is gone.
- Any time a capability is "inherited" from a previous session, a prior chat window, a handoff package, or a repo README rather than confirmed in the current session.

## Core principle

**Test from the role that will actually use the capability, not from a role that cannot.** A leaf subagent cannot call `delegate_task` — that is by design, not evidence the parent lacks it. A parent session that just dispatched a subagent via `delegate_task` has positive evidence the capability is functional, even if a separate probe says otherwise. The probe's conclusion must be checked against what role produced it.

## The verification ladder

Run these in order when a capability is in question:

### 1. Identify whose perspective the evidence comes from

Before accepting any "capability X is unavailable" or "capability X is available" claim, ask: **which agent role produced this evidence?**

- Parent/orchestrator session: has the full tool set. Positive evidence here is generally reliable for the parent's capabilities.
- Leaf child / delegated subagent: gets a SUBSET of the parent's tools. Evidence from a leaf that a parent-level tool is missing is EXPECTED and is NOT evidence the parent lacks it.
- Shell/terminal: can confirm CLI tools and files but not Hermes-internal tool availability.

If the evidence source and the intended user of the capability are different roles, the evidence is not conclusive — test from the intended user's role.

### 2. Confirm the capability exists in the current session's tool list

- Check the system prompt's directly-listed tools.
- Use `tool_search` to probe for the capability by name and by action+object (e.g. "delegate_task" and "delegation task spawn").
- If the capability is a Hermes-internal tool, remember that leaf children do NOT inherit the full parent tool set — check from the parent role.

### 3. Test functionally from the role that will use it

- **Parent/orchestrator**: call the capability directly with a trivial goal. A successful dispatch is positive evidence. A failure with a clear error is negative evidence worth acting on.
- **Leaf child**: a negative result here is NOT evidence the parent lacks the capability. Do not treat a leaf's "X is not available" as grounds to conclude X is gone from the session. Instead, test from the parent.
- **Shell**: confirms CLI/file existence only. A CLI tool present on disk is not the same as a Hermes tool loaded in-session, and vice versa.

### 4. Check the logs for prior usage

- Read the session's agent.log (or the shared logs directory) for prior completions of the capability.
- Co-occurrence is informative: if `delegate_task` completions and `_check_kanban_orchestrator_mode` warnings appear on the SAME days, the warning is likely not a hard gate on that capability. A warning that coexists with successful usage is a red herring for that capability.
- Prior completions do not guarantee the capability will work in the next session (session state can change), but they are positive evidence it was functional recently and the infrastructure is installed.

### 5. Reconcile conflicting evidence before concluding

When two sources conflict (e.g. "parent just used it" vs "child probe says it's gone"), prefer the evidence from the role that actually uses the capability, and treat the other as a misinterpretation unless you can independently confirm the negative. Document the reconciliation in the plan/handoff so the next session does not re-litigate the same question.

## The misread class (most common failure mode)

The most common failure is **misattributing a role-scoped limitation to a session-wide absence**. The classic form:

- A leaf subagent probes for capability X.
- Leaf cannot call X (by design — it doesn't inherit the parent's orchestration tools).
- Leaf concludes "X is gated/unavailable/not functional."
- The next session treats X as unavailable and either abandons the plan or substitutes a weaker approach.

The correct interpretation: **the leaf's inability is expected and is not evidence about the parent.** The parent's actual usage (e.g. "this very probe was dispatched by X") is the stronger evidence.

Related misreads:
- Treating a kanban-orchestrator-mode warning as a hard gate on async delegation when the same log shows delegate_task completions on the same day.
- Treating "cronjob not found as a shell command" as evidence the Hermes `cronjob` tool is absent (it's a Hermes-internal tool, not a CLI binary).
- Treating a prior session's capability as guaranteed in the current session without a smoke test.

## Smoke test discipline

When a plan depends on a capability, run a **1-unit smoke test from the role that will use it** before committing to the full plan:

- For `delegate_task`-based orchestration: dispatch a 1-row (or 1-task) trivial delegate from the parent session and confirm usable structured output returns. Record the result.
- For `cronjob`: schedule a minimal fire-and-forget job (or confirm the tool responds) before building a campaign that depends on recurring runs.
- For kanban dispatcher: confirm the board responds and the dispatcher can spawn before building a kanban-governed workflow.

If the smoke test fails, diagnose from the parent role before concluding the capability is gone. If it passes, the capability is confirmed for this session — but note that session state can change between chats, so the next handoff should still smoke-test on arrival.

## What to record in the plan/handoff

When you verify (or fail to verify) a capability, record:

1. **What was claimed** (from the handoff, repo README, prior session, user statement).
2. **Whose perspective the evidence came from** (parent, leaf child, shell, logs).
3. **How you tested** (direct call, tool_search, log inspection, smoke test).
4. **Result** (functional / not functional / inconclusive / not tested from correct role).
5. **Reconciliation** (if conflicting evidence, what you concluded and why).
6. **Caveat** (if session-state-dependent, note that the next session must re-confirm).

## Pitfalls

- **Do not treat a leaf subagent's "tool X not available" as session-level evidence.** The leaf is often scoped down by design. Test from the parent.
- **Do not treat log warnings as hard gates without checking for co-occurring successful usage.** A warning and a successful completion on the same day mean the warning is not blocking that capability.
- **Do not inherit a capability claim across sessions without re-confirming.** Session state changes; a handoff that asserts "the harness exists" should be treated as a claim to verify, not a fact.
- **Do not confuse CLI existence with Hermes-internal tool availability.** `which cronjob` can fail while the Hermes `cronjob` tool is loaded and functional.
- **Do not conclude a capability is gone from a single negative probe without checking the probe's role and the parent's actual usage.**

## Relationship to other skills

- `external-source-verification` — handles URL/repo/artifact EXISTENCE. Use it when the question is "does this link/repo/artifact exist and is it accessible." Use THIS skill when the question is "is this tool/capability/functionality actually usable in the current session."
- `hermes-agent` — covers Hermes session mechanics, tool sets, spawning, and the delegate_task / kanban / cronjob landscape from the platform side. Use it for platform-level questions; use THIS skill for the "verify before you build" discipline.

## References

- `references/capability-verification-methodology.md` — the verification ladder in condensed form, with a worked example from the Monstare probe (2026-08-13).
- `references/monstare-probe-case-study.md` — the 2026-08-13 diagnostic probe that surfaced the misread: a leaf subagent concluded `delegate_task` was gated/unavailable; the parent session had just dispatched it. Includes the log evidence that reconciles the conflict and the correction written into the v3 handoff.
- `references/monstare-v2-v3-handoff-revision.md` — the 2026-08-13 continuity-package revision that the probe triggered: quality gaps found in the v2 handoff (role structure described as functional but not built, no cost controls, no smoke test, budget placeholders), the build spec added in v3, the budget values drafted, the CORE-01 smoke test that passed, and the diagnostic-probe reconciliation pattern written into the handoff.
- `references/role-harness-io-pattern.md` — the delegate_task role-harness I/O pattern proven on the Monstare batch-1 charting pass (2026-08-13): parent writes shared artifacts to disk (rows.json, drafts, final.json), spawns role subagents in waves of ≤3 with path-carrying prompts and exact numbered return contracts, children save reports to a reports/ dir, parent reconciles into final.json then patches the canonical artifact. Includes failure handling (re-chart marking, tie-breakers) and the rule that children flag-and-recommend, never rewrite.
