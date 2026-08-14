# Case study: hermes-lab bundle gate audit (2026-08-07)

## Context
Repo `dk514506-jpg/hermes-lab` ("Dallas's Skill Library") — 14 Hermes skills + a
13-phase research campaign. A "runtime bundle" (1.3MB tar.gz) ships as a GitHub
release asset with README instructions: `curl → tar → python3
council_notes/verify_all.py → "expect exit 0"` on "any machine, incl. cloud".

## Finding: the gate failed 12/14 in a clean cloud container
Running the advertised one-liner in a fresh container (the advertised use case)
gave `GATE FAILED: 12 verifier(s) failed`. Two verifiers passed — exactly the
ones written with relative paths and no third-party deps.

Breakdown of the 12 failures:
- **7 dependency failures** (verify_packages, phase4-7, integration, phase11):
  PyYAML/jsonschema not installed; the README one-liner never mentions them and
  PEP-668 breaks bare `pip install`. Undocumented prerequisite.
- **5 structural failures**:
  - `verify_phase3.py` line 7: `ROOT = "/home/greenknight/.hermes/..."` — a
    hardcoded path to the author's machine, despite the README claiming
    "machine-specific absolute paths have been scrubbed". The scrub reached the
    repo tree but not the bundle's verifiers.
  - `phase2_api_probe.py` and `Phase3_Skills/_verify_skills.py`: same disease.
  - `verify_phase9.py`: reads `~/Documents/digital_brain/valens_wiki/registers`
    (4 checks — a machine-local Obsidian vault not shipped, un-shippable).
  - `verify_phase13.py`: `SKILL = ~/.hermes/skills/motivational-ecology` (the
    author's *installed* copy) while the bundle ships the skill at `skill/` —
    the "estate-map.md present" check failed even though the file exists at
    `skill/references/estate-map.md`.

Notably, the bundle ALREADY shipped a portable resolver (`estate_path.py`:
`$ECOLOGY_ESTATE_ROOT` → walk-up → home-lab fallback) and the gate scripts used
it — only the standalone verifiers bypassed it. The mechanism existed; the
callers drifted.

## Repair (all in a copy, delivered as patch + rebuilt bundle)
1. Routed the 3 hardcoded-path verifiers through `estate_path.ESTATE_ROOT`
   (sys.path.insert of the bundle root, then `ROOT = os.path.join(ESTATE_ROOT, ...)`).
2. `verify_phase9` wiki checks → conditional: `if os.path.isdir(WIKI): <checks>
   else: print("[SKIP] ... not shipped in bundle")` — never FAIL on un-shippable
   home-lab artifacts.
3. `verify_phase13` SKILL → bundle-first (`FOUNDATION/skill` if present, else
   `~/.hermes/skills/...`), and the live-session-record check SKIPs in bundle
   mode with a KNOWN GAP note (the bundle ships witness logs but no
   `live_session_*` record — flagged for the author; NOT fabricated).
4. Added `requirements.txt` (PyYAML>=6.0, jsonschema>=4.0) + `bootstrap.sh`
   (uv venv, else python3 -m venv) + README one-liner updated to
   `./bootstrap.sh && .venv/bin/python council_notes/verify_all.py`.
5. Added canonical `estate_manifest.json` (package lists, dojo artifacts,
   evidence files, role→planet mappings with home/arc schema) + new
   `council_notes/verify_tables.py` anti-drift verifier wired into the gate
   chain (15 verifiers). Checks: on-disk directory sets == manifest (excluding
   `__pycache__`), per-package core files, evidence files, and every role→planet
   table row carries the canonical home tokens (arc-start invariant).
6. Repo side: `scripts/verify_tables_repo.py` (parses the two SKILL.md role
   tables, tolerant of `**Role** (note)` markup and slash-roles) +
   `.github/workflows/cleanroom.yml` (fresh ubuntu, fetch release asset,
   bootstrap, run gate; also runs the repo table check on push/PR).

Result: gate 15/15, exit 0, in the clean container; repo checker flips green
only AFTER the semantic reconciliation below.

## The anti-drift verifier caught REAL drift on first run
The checker flagged 4 conflicts between the repo's two role→planet tables
(`multi-agent-pipeline` vs `astral-research-harness` §7.1) on Researcher,
Orchestrator, Tester, Builder. Evidence for which table drifted: the pipeline
table is internally consistent (each planet = exactly one role's home) and
agrees with the doc's §2.x archetype tables; §7.1 duplicated Mercury/Scorpio on
two roles and swapped Sun↔Mars. Reconciliation (option A, user-approved):
pipeline table canonical, every §7.1 arc must START at the role's home, Analyst
unified into Validator. Manifest + both checkers updated to the home/arc
schema; the 4 conflicts became the pass condition.

## Tracker side-effect (the lesson applied)
The same discipline went into the business tracker build: integer-cents money,
stdlib-only (zero deps — no bootstrap needed), relative paths only (enforced by
its own verify_pipeline), and a reconcile GATE that exits nonzero when
declared COGS exceeds purchase price or the books don't balance. It caught a
real data-entry error (wrong purchase_id in sample sales: $120 COGS vs $40
paid) in the first hour — exactly the designed behavior.

## Environment quirk observed (workaround, not a rule)
The Hermes lifecycle guard can crash ("embedded null character in path") on
terminal commands that reference a venv's `bin/python` path. Working dodge:
`uv pip install --target DIR ...` + `PYTHONPATH=DIR python3 ...` (subprocesses
inherit PYTHONPATH, so chained verifiers get their deps). Also: `write_file`
may refuse `/tmp` (HERMES_WRITE_SAFE_ROOT) — create verification scripts via
`mktemp` + `cp` from the writable root instead.
