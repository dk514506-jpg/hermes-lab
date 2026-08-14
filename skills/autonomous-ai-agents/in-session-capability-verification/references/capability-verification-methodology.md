# Capability Verification Methodology — Condensed Ladder

Use this when you need the verification steps without the full SKILL.md narrative. For the worked example and the misread patterns, see `monstare-probe-case-study.md`.

## 1. Identify the evidence source's role

| Role | What it can tell you | What it cannot tell you |
|---|---|---|
| Parent/orchestrator session | Whether parent-level tools work in this session | Nothing about leaf-child scoping |
| Leaf child / delegated subagent | Whether leaf-scoped tools work | Whether parent-level tools work (leaf is scoped down by design) |
| Shell/terminal | Whether CLI binaries and files exist on disk | Whether Hermes-internal tools are loaded in-session |

If the evidence source and the intended user of the capability are different roles, the evidence is not conclusive. Test from the intended user's role.

## 2. Confirm the capability is in the current session's tool list

- Check the directly-listed tools in the system prompt.
- Use `tool_search` by name and by action+object.
- Remember: leaf children do NOT inherit the parent's full tool set.

## 3. Test functionally from the role that will use it

- Parent: call directly with a trivial goal. Success = positive evidence.
- Leaf: a negative result is EXPECTED for parent-level tools. Do not treat it as session-level evidence.
- Shell: confirms CLI/file existence only, not in-session Hermes tool availability.

## 4. Check the logs for prior usage

- Read agent.log for prior completions of the capability.
- Co-occurrence check: if the capability's completions and a suspicious warning appear on the same days, the warning is likely not a hard gate on that capability.
- Prior completions are positive evidence the infrastructure is installed and was recently functional. They do not guarantee the next session will have it.

## 5. Reconcile conflicting evidence

When parent usage and child-probe negativity conflict, prefer the parent's evidence (the role that actually uses the capability) and treat the child's negative as a likely misread unless independently confirmed. Record the reconciliation.

## Smoke test rule

Before committing a plan to a capability, run a 1-unit smoke test from the role that will use it. Record the result. If it passes, the capability is confirmed for this session. If it fails, diagnose from the parent role before concluding the capability is gone.

## Budget rule of thumb

A verification pass should cost less than the risk of building the wrong plan. A 1-unit smoke test + log check is usually under a few thousand tokens. If the verification costs more than a small fraction of the planned work, the capability is probably not the bottleneck — simplify the verification, not the plan.
