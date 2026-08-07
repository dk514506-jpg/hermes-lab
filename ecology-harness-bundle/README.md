# Motivational Ecology — Runtime Bundle

The complete, self-contained runtime of the Motivational Ecology harness.
Drop this bundle anywhere (home lab, cloud files area, a fresh machine)
and the machinery runs. No dependency on the home-lab paths.

## Layout

```
<root>/
├── estate_path.py          portable estate resolution (env -> walk-up -> home lab)
├── GitHub_PoC/             canonical estate: skills/ (10 pkgs), routines/ (5 dojos),
│                           lattices/, governance/, evidence/, meld/, verify/, docs/
├── Phase10_Integration/    merged engine: faos_ecology_engine.py (gate + quarantine
│                           + 6-pass close), faos_ecology_config.yaml, verify_integration.py
├── Phase11_Intervention/   BCW/BCT layer: phase11_intervention.py (Q7), verify_phase11.py
├── Phase12_Activation/     conditional packages: phase12_conditional_packages.py, verify_phase12.py
├── Phase13_Wiring/         live-wire verifier: verify_phase13.py
├── Phase8_Evaluation/      calibration log + evaluation
├── council_notes/          campaign gate: verify_all.py (14 verifiers) + verdicts
└── skill/                  the motivational-ecology Hermes skill (SKILL.md + scripts)
```

## Quick start

```bash
# 1. Run the gate (deterministic, no LLM):
python3 skill/scripts/run_gate.py --meaning medium --branching medium

# 2. Run a platform-wiring dojo demonstration (deterministic walk):
python3 skill/scripts/run_dojo_session.py --dojo Ambivalence_Dojo

# 3. Run the full campaign gate (14 verifiers):
python3 council_notes/verify_all.py
```

## Path resolution

The scripts find the estate automatically:

1. `$ECOLOGY_ESTATE_ROOT` — explicit override (set it if the bundle sits in a
   non-standard location).
2. Walk-up — scripts locate `GitHub_PoC/` relative to their own position
   (works for the standard bundle layout).
3. Home-lab fallback — `~/.hermes/hermes-agent/docs/Ecology/Foundation/`.

On a cloud instance: place the bundle anywhere, then either set
`ECOLOGY_ESTATE_ROOT=/path/to/bundle` or just run the scripts from inside
the bundle — walk-up handles it.

## Honest boundaries (read this)

- The session driver (`run_dojo_session.py`) is a PLATFORM-WIRING
  DEMONSTRATION: deterministic machinery walk (gate + quarantine + 6-pass
  close). It generates NO coach turns, involves NO LLM and NO human.
- The absence register (Phase10_Integration/faos_ecology_config.yaml,
  entry `post_meld_live_llm_session`) records class=human-session-pending:
  the genuine human-facing live LLM session is the remaining runtime act.
- Runtime logs are excluded from this bundle (see GitHub_PoC/logs/.gitkeep).
- The Valens book corpus (copyrighted translation) is NOT included.

## Verification

```bash
python3 council_notes/verify_all.py   # full campaign gate — expect exit 0
python3 Phase13_Wiring/verify_phase13.py   # live-wire verifier
```

## Skill install (Hermes)

The `skill/` directory is the `motivational-ecology` Hermes skill. To use
it in a Hermes agent, copy `skill/` to `~/.hermes/skills/motivational-ecology/`
(or use `hermes skills install` from a repo/tap).
