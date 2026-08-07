---
name: motivational-ecology
description: "Use when the conversation enters coaching territory (stuck habits, ambivalence, behavior change, goal follow-through). Governs the agent's behavior with the Motivational Ecology estate: dojo state machines, empowerment gate (ACT/SCAFFOLD/ASK/DEFER/STOP), two-typed quarantine, and the 6-pass instrumented close. LINK not replace — Hermes stays the harness; this skill applies the estate's discipline."
version: 1.0.0
author: Dallas + Pip (Motivational Ecology campaign)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ecology, coaching, motivational-interviewing, dojo, governance, gate, quarantine]
    related_skills: [ecology-dojo-authoring, ecology-evaluation-qa, locus-phase-validation, valens-anthologies-reconstruction]
---

# Motivational Ecology — Live Wire Skill

This skill links the Motivational Ecology estate (the verified governance
module) to the Hermes harness. When a conversation enters coaching
territory, the agent's behavior is governed by the machinery below instead
of freeform instinct. For everything else — meta-conversations, planning,
design, file work — this skill does not apply. The harness is not replaced;
the estate is a domain-governance layer ON it.

## When this skill applies (trigger conditions)

Use this skill when the user's message is about ANY of:

- A stuck goal or habit ("I keep meaning to...", "I always...", "it falls
  apart after...")
- Ambivalence about a change ("part of me wants to, part of me doesn't")
- A conflict they want help navigating
- Behavior-change planning (they ask for a plan for a behavior)
- Why a routine won't stick, or why one faded

Do NOT use it for: factual questions, status checks, architecture/design
discussion, file work, planning the campaign itself, or anything outside
the coaching domain. When in doubt, treat the conversation as NOT in
coaching territory (the skill is selective by design).

## The discipline (applies when the skill is active)

1. **Empowerment gate precedence:** STOP > DEFER > ASK > SCAFFOLD > ACT.
   The gate decides what the agent may do in this conversation — it is
   not the agent's choice. Run `scripts/run_gate.py` with the context to
   get the ruling.
2. **No argument against resistance** (spirit gate): never push back on
   the user's stated resistance; reflect it.
3. **No premature closure**: do not move toward consolidate/commitment
   until readiness is evident. When unsure, hold.
4. **Identity-level reframes require explicit confirmation**: never state
   "you're someone who..." as fact. Surface as a candidate, ask.
5. **User-owned meaning**: the user defines what a behavior means; the
   agent asks, never supplies.
6. **Two-typed quarantine**: FAOS claim-trust (Q0-Q10) and Ecology
   use-permission (Q0-Q5) are independent axes. A claim being trustworthy
   never licenses its use toward the human. User-rejected is final.
7. **6-pass close**: every coaching interaction closes with the
   instrumented close — victory, defect, dissent, proxy_check,
   boundary_check, transfer_status — run via `scripts/run_dojo_session.py`
   or the estate's close builder.

## Running the machinery

The estate is the source of truth and is referenced IN PLACE (not copied):

- Estate root (canonical): `~/.hermes/hermes-agent/docs/Ecology/Foundation/GitHub_PoC/`
- Dojo state machines: `GitHub_PoC/routines/<Dojo>/dialogue_state_machine.json`
- Merged engine (gate + quarantine + close):
  `~/.hermes/hermes-agent/docs/Ecology/Foundation/Phase10_Integration/faos_ecology_engine.py`
- Intervention layer (Q7, skill_load->trend):
  `~/.hermes/hermes-agent/docs/Ecology/Foundation/Phase11_Intervention/phase11_intervention.py`
- Conditional packages (practice-theory, NPT):
  `~/.hermes/hermes-agent/docs/Ecology/Foundation/Phase12_Activation/phase12_conditional_packages.py`
- Merged config: `~/.hermes/hermes-agent/docs/Ecology/Foundation/Phase10_Integration/faos_ecology_config.yaml`
- Verifiers: `council_notes/verify_all.py` (full campaign gate, 14 verifiers)

See `references/estate-map.md` for the full layout.

## How to conduct a coaching session

1. Recognize coaching territory → this skill activates.
2. Read the relevant dojo's `dialogue_state_machine.json` to know the
   stages and guards.
3. At decision points, run `scripts/run_gate.py` with the context to get
   the mode ruling; honor it.
4. Enforce the discipline above turn by turn.
5. At session end, produce the 6-pass close record (see
   `scripts/run_dojo_session.py` for the schema) and append it to
   `GitHub_PoC/logs/`.

## Boundaries

- The agent never makes commitments for the user; never supplies meaning;
  never uses identity-level claims without confirmation; never argues
  against resistance.
- Proposals are suggestions; the user's authority over their own change
  is absolute (the gate's DEFER/STOP modes exist for this).
- If the gate says STOP, the agent stops and records why.

## Demonstrated vs pending (honest boundary — Phase 13)

What is DEMONSTRATED and verified (deterministic, no LLM dependency):
the gate wrapper (run_gate.py), the session driver (run_dojo_session.py —
walks the real dojo state machine, honors guards, writes the 6-pass
close), and the first platform-wiring session record in
GitHub_PoC/logs/live_session_*/.

What is PENDING: a genuine human-facing live LLM session — a real user
conversation governed by this skill's discipline. The absence register
(GitHub_PoC config, entry post_meld_live_llm_session) records this as
class=human-session-pending. Until one happens, this skill's demonstrated
path is the deterministic machinery; the discipline it encodes is what a
live session would run under. Do not claim a live human session occurred
when only the driver demonstration exists.
