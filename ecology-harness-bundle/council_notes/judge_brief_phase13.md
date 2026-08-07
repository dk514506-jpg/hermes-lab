# Phase 13 Judge Brief — The Live Wire (estate → Hermes skill module)

Judge: DeepSeek (nous portal deepseek-v4-flash-0731) — adversarial outside judge
Locus: independent validator (separate pass)

## What to review

Read these artifacts (in order):
1. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase13_Plan.md
   (the plan + Dallas's directive: "proceed with assumptions")
2. /home/greenknight/.hermes/skills/motivational-ecology/SKILL.md
   (the live-wire skill — the trigger conditions + discipline + estate map)
3. /home/greenknight/.hermes/skills/motivational-ecology/scripts/run_gate.py
   (the callable empowerment gate wrapper)
4. /home/greenknight/.hermes/skills/motivational-ecology/scripts/run_dojo_session.py
   (the live-session driver)
5. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase13_Wiring/verify_phase13.py
   (the verifier)
6. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase10_Integration/faos_ecology_config.yaml
   (absence register — the honest-boundary check)
7. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/GitHub_PoC/logs/live_session_20260807-221115Z/session.json
   (the first session record)

Context: Phase 13 wires the verified estate onto the Hermes harness as the
`motivational-ecology` skill — LINK, not replace (Dallas's explicit
framing). The skill triggers only in coaching territory; meta/design/
planning conversations stay freeform. The absence register's
post_meld_live_llm_session entry was updated to class=human-session-pending
— the platform is WIRED (deterministic driver session demonstrates the
machinery), but a genuine human-facing live LLM session is honestly
recorded as the remaining runtime act. The mirror (Hermes_Agent_Harness)
was synced to canonical (10 packages, witnesses, docs, graph, T2R) and
verify_phase7 was updated to Phase 13-era expectations.

## Success criteria

Judge against:
A. Does the skill faithfully carry the estate's discipline (gate
   precedence, no-argument-against-resistance, no-premature-closure,
   identity confirmation, user-owned meaning, 6-pass close)?
B. Is the honest boundary maintained — nothing overclaimed? (The absence
   register says human-session-pending, NOT recorded. The session record
   says platform wiring demonstration. Does anything claim a genuine live
   human session happened?)
C. Is the wiring real — do the scripts actually load the estate and run
   (not stubs, not paths that would break on another machine)?

## What to return (structured)

1. VERDICT: DEPLOY / REVISE / BLOCK (one line)
2. Score 0-5 with one-line justification
3. KERNEL — what is strong and should be preserved exactly as-is (max 5)
4. WEAKNESSES — numbered, each with severity HIGH/MED/LOW and a concrete fix
5. HONESTY CHECK — anything that overclaims: does the absence entry tell
   the truth? does the session record tell the truth? does the skill
   claim more than it delivers? Are the hardcoded paths (expanduser("~"))
   a portability problem worth flagging?
6. DISCIPLINE CHECK — Valens: does the skill carry the discipline
   correctly? Does the gate wrapper preserve the mode precedence and the
   two-typed quarantine load-bearing rule? Does run_dojo_session honor
   guards (HOLD/retreat semantics)?
7. RECOMMENDED REVISIONS — the minimal list that would move you to DEPLOY.

Be adversarial. The campaign's history: judges caught wholesale
pass-throughs, absence entries overclaimed as recorded, registries
pruned to fake completeness, verifier docstrings claiming checks they
don't run. Assume this phase has an analogous hidden flaw and find it.
READ THE ACTUAL CODE — do not trust docstrings.
