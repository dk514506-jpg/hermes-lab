# Case Study — hermes-lab runtime bundle gate (2026-08-07)

Audit + repair of `dk514506-jpg/hermes-lab`'s "Motivational Ecology" runtime bundle. The README advertised a one-liner (`curl → tar → python3 council_notes/verify_all.py → "expect exit 0"`, "any machine, incl. cloud"). On a fresh cloud container the gate failed **12 of 14** verifiers. This is the complete failure→fix map.

## Failure classes found (with evidence)

| Class | Evidence | Why it failed |
|---|---|---|
| Hardcoded machine paths (7 of 14 failed from this + deps) | `council_notes/verify_phase3.py:7` — `ROOT = "/home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase3_Skills"`; same in `council_notes/phase2_api_probe.py:14-15` and `Phase3_Skills/_verify_skills.py:12` | README claimed "machine-specific absolute paths scrubbed" — the scrub reached the repo tree, not the bundle's verifiers. Fails on every machine except the author's. |
| Env-dependent reads (4 checks) | `verify_phase9.py:25,84` — reads `~/Documents/digital_brain/valens_wiki/` (an Obsidian vault that isn't and won't be shipped): 2 register cross-links + wiki synthesis + journal entry | The bundle can never satisfy these; they are home-lab-only checks run as hard FAILs. |
| Path drift (content present, verifier looks elsewhere) | `verify_phase13.py:63` — `SKILL = ~/.hermes/skills/motivational-ecology` (the author's *installed* copy) while the bundle ships the skill at `<root>/skill/` (with `references/estate-map.md` present) → verifier crashed at `open(SKILL/SKILL.md)` | Two layouts (home-lab vs bundle); verifier only knew one. |
| Undocumented deps (7 verifiers) | `ModuleNotFoundError: No module named 'yaml'` / `jsonschema not installed` | README one-liner omitted the install step; on PEP-668 systems bare `pip install` fails anyway. |
| Bypassed resolver | `estate_path.py` at bundle root implements `$ECOLOGY_ESTATE_ROOT → walk-up → home-lab fallback` — correct, unused by the offenders; `verify_phase13.py` and `skill/scripts/run_gate.py` had their own correct inline copies | The mechanism existed; the verifiers drifted from it. |

What PASSED despite the mess: `verify_phase8` and `verify_harness` — the ones written with relative paths and pure stdlib. That pins the failure on packaging, not the design (a key adjudication point).

## Fixes applied (all in a repackaged bundle)

1. **Route stragglers through the existing resolver** — `verify_phase3.py`, `phase2_api_probe.py`, `_verify_skills.py` now `sys.path.insert` the bundle root and import `ESTATE_ROOT` from `estate_path.py`; ROOT/OUT paths derive from it.
2. **Env-conditional SKIP** — `verify_phase9.py` wiki checks: `if os.path.isdir(WIKI): <assert> else: print("[SKIP] ... not shipped in bundle")`. Home-lab keeps full strictness; bundle gate stays honest.
3. **Bundle-first SKILL resolution** — `verify_phase13.py`: `_BUNDLE_SKILL = <root>/skill` if it exists, else `~/.hermes/skills/motivational-ecology`. The bundle's own skill/ is what the gate now verifies.
4. **Pinned deps + bootstrap** — `requirements.txt` (PyYAML>=6.0, jsonschema>=4.0) + `bootstrap.sh` (uv venv else `python3 -m venv`; installs requirements). README one-liner now `./bootstrap.sh && .venv/bin/python council_notes/verify_all.py`.
5. **Anti-drift manifest + verifier** — new `estate_manifest.json` (canonical: phase3 skills + required files, 10 skill packages, 5 dojos + 7 artifacts, 4 evidence files, 6 role→planet mappings) + new `council_notes/verify_tables.py` (dir sets == manifest, no missing/extra; per-package core files; evidence files; role→planet table rows in shipped markdown match canonical tokens). Wired into `verify_all.py` as verifier #14. `dirs()` excludes `__pycache__`/hidden dirs (the gate creates them).
6. **Clean-room CI + repo-side checker** — `.github/workflows/cleanroom.yml` (ubuntu-latest; repo table check + fetch release bundle + bootstrap + gate) and `scripts/verify_tables_repo.py` (parses the two SKILL.md role→planet tables against the canonical mapping).

## Results

- Gate: 12/14 failed → **15/15 pass, exit 0** (14 original + anti-drift).
- `verify_tables_repo.py` immediately caught **4 real drifts** the campaign memo had documented ("four planetary-mapping tables drifting"): `multi-agent-pipeline/SKILL.md` rows for Researcher (Jupiter/Moon/Pisces vs canonical Mercury/Scorpio), Orchestrator (Saturn vs Sun/Capricorn), Tester (Mars vs Venus/Taurus), Builder (Sun vs Mars). Left designed-to-fail until the owner picked a direction — then reconciled (see below).
- **Gap flagged, not fabricated:** the bundle ships no `live_session_*` record despite the skill claiming one "demonstrated" — `verify_phase13` SKIPs with a KNOWN-GAP comment instead of inventing a record. This is the never-fabricate rule in action.

## Calibration lessons (checker false-positive fixes)

- Role-cell normalization must `replace("**", "")`, strip `(notes)`, and split `A / B` cells — `strip("*")` misses mid-string `**` and silently drops rows.
- Decide token strictness per table: the astral table carries full circuit arcs ("Mercury/Scorpio → Jupiter/Moon"); the pipeline table shows only the primary signature ("Mercury in Scorpio"). Requiring full-arc tokens everywhere produces noise that drowns the real drift. Require PRIMARY tokens; full arc only where the format carries it.

## Tooling note

The sandbox lifecycle guard crashed (`open: embedded null character in path`) on ANY command referencing a uv-venv `bin/python` path. Workaround that also became the recommended pattern: `uv pip install --target <dir> pyyaml jsonschema` then run with `PYTHONPATH=<dir>` — subprocesses inherit PYTHONPATH so the whole gate chain gets deps without a venv interpreter path in the command.

## Semantic reconciliation — option A (single-home canonical)

The two role tables conflicted on 4 of 6 roles (Researcher, Orchestrator, Tester, Builder) plus a taxonomy mismatch (Analyst vs Validator). **Adjudication:** the `multi-agent-pipeline` table is internally consistent — every planet appears exactly once (Mercury→Scout, Jupiter/Moon→Researcher, Venus→Validator, Saturn→Orchestrator, Sun→Builder, Mars→Tester) and agrees with the astral skill's own §2.1/§2.2 single-home usage; §7.1 assigns Mercury/Scorpio to BOTH Scout and Researcher and swaps Sun↔Mars. Verdict: pipeline table canonical; §7.1 drifted.

**Fix applied:**
- §7.1 arcs rewritten so each **starts at the home signature** — Orchestrator `Saturn/Capricorn → Sun/Capricorn`, Researcher `Jupiter/Moon in Pisces → Venus/Taurus`, Builder `Sun/Capricorn → Mars/Capricorn`, Tester `Mars/Capricorn → Venus/Taurus` (Scout was already consistent).
- Taxonomy unified: `Analyst` → `Validator` (same gate/prep function, same Venus/Taurus home).
- Reconciliation documented as a dated blockquote IN the file; `estate_manifest.json` mappings gained `home` + `arc` fields; both checkers now assert **arc-start == home** (arc cells split on "→"; the pre-arrow part must contain the home tokens).
- Result: repo checker flipped 4-drift-FAIL → **exit 0** (all six rows consistent in both tables); bundle gate stayed 15/15.

The invariant is now enforced, not documented: any future edit that starts an arc away from home fails CI.
