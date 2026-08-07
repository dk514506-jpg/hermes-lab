# Phase 13 Plan — The Live Wire (estate → Hermes skill module + first live session)

Project: Motivational Ecology Agent Architecture
Plan date: 2026-08-07
Status: PLAN — written before execution. Dallas directive: "proceed with
assumptions and complete phase 13." The phase that turns the verified
estate into a callable governance module on the Hermes harness — LINK, not
replace (Dallas's framing: Hermes stays the harness; the estate becomes a
domain-governance module ON it).

## What the live wire is

Hermes is the container (the harness running this conversation: the agent
loop, model access, memory, plugins, skills at ~/.hermes/skills/). The
Ecology estate (GitHub_PoC/) is content + governance — dojos, gate,
quarantine, close. Phase 13 links them:

1. The estate becomes a **Hermes skill** — `motivational-ecology` in
   ~/.hermes/skills/ — so that when a conversation enters coaching
   territory, the agent's behavior is governed by the machinery (the
   dojo state machine, the empowerment gate, the two-typed quarantine,
   the 6-pass close) instead of freeform instinct.
2. The skill references the estate IN PLACE (GitHub_PoC/ stays the source
   of truth; the skill is the trigger + instructions + runnable wrapper).
3. The FIRST LIVE POST-MELD SESSION runs through the merged gateway — a
   real LLM-mediated Ambivalence_Dojo session with the gate consulted at
   each stage, quarantine enforced, 6-pass close recorded. This is the act
   that CLEARS the absence-register entry `post_meld_live_llm_session`
   (class never-recorded → recorded) — the estate's own "architectural
   only until a platform is wired" boundary, now crossed honestly.

## Deliverables

### D1 — The skill module: `motivational-ecology` at ~/.hermes/skills/

- SKILL.md (frontmatter per Hermes skill spec): trigger conditions
  (coaching territory = user describes stuck habit/ambivalence/conflict/
  goal), the gate precedence (STOP > DEFER > ASK > SCAFFOLD > ACT), the
  discipline carried (no argument against resistance, no premature
  closure, identity-level reframes require confirmation, user-owned
  meaning, 6-pass close), and the estate paths it references.
- scripts/run_gate.py — wrapper that loads the merged engine
  (Phase10_Integration) and returns a gate decision + quarantine ruling
  for a given context. Deterministic, callable from the skill.
- scripts/run_dojo_session.py — the live-session driver: walks the real
  dojo dialogue_state_machine.json, generates coach turns (LLM-mediated),
  consults the gate at each stage, enforces quarantine, writes the
  6-pass close record.
- references/estate-map.md — pointer file: where each piece lives
  (canonical tree, phase dirs, FAOS engine), so a fresh session can
  navigate the estate.

### D2 — Gate wired into the conversation path

- The skill's scripts make the machinery CALLABLE; the skill's SKILL.md
  makes it APPLIED. Verification: hermes skills list shows
  motivational-ecology enabled; the scripts run standalone (exit 0).

### D3 — First live post-meld session (clears the absence entry)

- Run ONE real Ambivalence_Dojo session through the merged gateway via
  run_dojo_session.py: a coaching conversation (scenario persona, per the
  acceptance-test convention) with gate decisions at each stage, quarantine
  enforced, and a full 6-pass close record written to
  GitHub_PoC/logs/live_session_001/.
- Update the absence register: post_meld_live_llm_session →
  class=recorded, blocks=nothing (first live session exists), with the
  record path as the anchor.
- The session record is the honest evidence: real LLM turns, real gate
  outputs, real close.

### D4 — Mirror sync (housekeeping)

- Hermes_Agent_Harness is missing Material_Arrangement_Scan +
  Feedback_Ecology_Map + the witness scripts + docs/. Sync it to the
  canonical state so the one-to-one correspondence the campaign
  convention calls for is restored. (Identified when Dallas asked where
  the harness lives.)

### D5 — verify_phase13.py + gate chain

- Checks: skill exists + enabled (hermes skills list), scripts run
  (exit 0), live session record exists + complete (6-pass close, gate
  decisions, quarantine rulings), absence entry flipped to recorded,
  mirror synced, legacy gate green.
- verify_all.py chains verify_phase13.py (13 → 14 verifiers).

## Review round (per campaign convention)

- Locus validation (7-check) + DeepSeek outside judge (adversarial).
- Sublative revision round; calibration log + journal updates.

## Out of scope

- Replacing or modifying the Hermes harness itself (link, not replace).
- Always-on dojo protocol for every conversation (the skill triggers only
  in coaching territory; meta/design/planning conversations stay freeform).
- The NPT registered-not-built mechanisms (still awaiting runtime signals).
- Autopoietic_Boundary_Check (indefinite hold).

## Decision points for Dallas (bite-sized)

- P13-D1: approve the skill-module design (estate referenced in place,
  not copied into the skill)?
- P13-D2: approve the live session convention (scenario persona, per the
  acceptance-test precedent) as the first post-meld session — versus a
  real session with you directly?
- P13-D3: approve clearing the absence entry after the first recorded
  live session?
