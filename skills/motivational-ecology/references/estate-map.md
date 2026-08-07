# Motivational Ecology — Estate Map

Where every piece of the estate lives. The skill references the estate IN
PLACE — this map is how a fresh session (or a friend's machine) navigates
it.

## Canonical estate (source of truth)

```
~/.hermes/hermes-agent/docs/Ecology/Foundation/GitHub_PoC/
├── skills/           10 skill packages (8 original + Material_Arrangement_Scan + Feedback_Ecology_Map)
├── routines/         5 practice dojos (dialogue_state_machine.json etc.)
├── governance/       estate safeguards + valens_operating_logics.md
├── lattices/         lattice_index, T2R_traceability (52 entries), skill_graph_index
├── evidence/         the verified evidence base
├── meld/             Phase 9 Valens × Ecology meld + witness run scripts
├── logs/             runtime logs (live_session_*, witness_*, acceptance_test_*)
├── docs/             Phase 3 architecture + safeguards + verification
├── verify/           in-tree verifier (verify_harness.py)
└── DEFERRED_PACKAGES.md, README.md, handoff_notes.md
```

## Mirror (consumer-facing copy)

```
~/.hermes/hermes-agent/docs/Ecology/Foundation/Hermes_Agent_Harness/
```
Same shape, synced to canonical through Phase 13.

## Engine dirs (the plumbing — outside both trees)

| Dir | What |
|---|---|
| `.../Phase10_Integration/` | Merged engine (faos_ecology_engine.py: gate + quarantine + close), merged config (faos_ecology_config.yaml, absence register), verify_integration.py |
| `.../Phase11_Intervention/` | BCW/BCT layer (phase11_intervention.py: Q7 arbitration, skill_load→trend), verify_phase11.py |
| `.../Phase12_Activation/` | Conditional packages executable (phase12_conditional_packages.py), verify_phase12.py |
| `.../Phase13_Wiring/` | verify_phase13.py |
| `.../council_notes/` | Campaign gate: verify_all.py (14 verifiers) + per-phase verifiers + judge/Locus verdicts |

## FAOS upstream (docs level)

```
~/.hermes/hermes-agent/docs/faos_engine_extension.py
~/.hermes/hermes-agent/docs/triage_faos_integration.yaml
~/.hermes/hermes-agent/docs/scripts/run_tests.sh
```

## Valens wiki

```
~/Documents/digital_brain/valens_wiki/
├── syntheses/    ecology-valens-meld.md, valens-operating-logics.md
├── registers/    absence-register.md, non-operational-registry.md
└── journal/      dated entries
```

## Running the gate

```bash
python3 ~/.hermes/skills/motivational-ecology/scripts/run_gate.py --help
python3 ~/.hermes/skills/motivational-ecology/scripts/run_dojo_session.py --list
```
