---
name: verification-gates
description: "Design/audit verification gates: exit-code, clean-room runs."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [verification, gates, clean-room, anti-drift, manifest, exit-codes, auditing, data-pipelines]
---

# Verification Gates & Clean-Room Discipline

How to build systems that **prove** their own correctness — and how to audit
systems that merely *claim* it. Two proven use cases behind this skill:
(1) auditing a repo whose README said "expect exit 0" — the gate failed 12/14
in a clean cloud container; (2) building a small-business data tracker whose
balance gate caught three real bugs in its first day (see `references/`).

## When to use

- Building any gate: reconciliation checks, CI workflows, test runners,
  "verify" scripts, data pipelines that must balance.
- Auditing a repo/project whose docs claim things are "verified", "exit 0",
  or "runs on any machine". Treat the claim as a hypothesis; run it.
- Any system where duplicated tables/lists exist across files (docs, config,
  verifiers) and drift silently.

## Core discipline (the rules)

1. **A gate is an exit-code program, runnable in a clean checkout.** No
   hidden state, no machine-specific paths, no pre-installed deps assumed.
   `exit 0` = proof, `exit 1` = failure, nothing in between.
2. **Clean-room rule:** run the gate on a fresh machine/CI before trusting any
   "verified" claim. A gate that only passes on the author's machine is not a
   gate — it manufactures false confidence. Fresh-copy test: `copytree` the
   tree to a temp dir (excluding state dirs) and run the full documented
   sequence there.
3. **Relative paths only.** Resolve roots from `__file__`. For portability
   across layouts, use a root resolver: `$ENV_VAR` override → walk up looking
   for a marker dir → home-lab fallback. Route EVERY script/verifier through
   it; the resolver existing but being bypassed is the #1 drift pattern.
4. **Environment-dependent checks → conditional SKIP with a loud note, never
   FAIL.** Checks that need a machine-local resource (a vault, an installed
   skill, a secret) must detect absence and print `[SKIP] ... (home-lab only)`
   instead of failing the gate on machines that legitimately lack it.
5. **Never fabricate artifacts to make a gate pass.** If a verifier demands a
   record/artifact the bundle doesn't ship, SKIP honestly and flag the gap in
   an absence register — don't generate fake evidence.
6. **Pinned deps + bootstrap.** `requirements.txt` + `bootstrap.sh` (uv venv,
   fall back to `python3 -m venv`). The README's documented sequence must be
   the exact sequence that works — including the dependency step. Undocumented
   prereqs = broken one-liner = broken trust.
7. **Anti-drift manifest.** When the same tables/lists appear in multiple
   files (skill lists, artifact lists, role mappings, package lists), put the
   canonical copy in one JSON/YAML manifest and add a verifier that asserts
   every on-disk table/directory against it (no missing, no extra). A table
   can no longer drift silently; the gate fails on the first divergence.
8. **Assert structural invariants, not just presence.** e.g. "arc must START
   at the home signature", "every COGS ≤ paid", "revenue − fees − shipping −
   cogs − expenses == recomputed profit". Presence checks pass while semantics
   drift.
9. **Exclude runtime artifacts from directory-set checks.** `__pycache__`,
   hidden dirs, `.venv`, generated files — the gate itself creates them; they
   must never count as drift (or the gate fights itself).
10. **Fail-loud data gates.** A reconciliation check that exits nonzero on
    mismatch is the earliest warning a business/data system can get. It WILL
    catch real data-entry errors — that's the feature.

## Auditing an existing "verified" system (checklist)

1. Clone and run the advertised gate **exactly as documented**, in a clean env.
   Capture the real exit code and per-check output.
2. Grep for hardcoded machine paths (`/home/`, `/Users/`, usernames) even when
   docs claim "paths scrubbed" — the scrub often reached the repo tree but not
   the verifiers/bundles. Separate comment mentions from real assignments.
3. Classify each failure: (a) undocumented dependency, (b) hardcoded path,
   (c) environment-dependent check (machine-local resource), (d) verifier
   expects a path/layout the bundle doesn't have (files exist, check looks
   elsewhere). Each class has a different fix.
4. Verify the fix by re-running in the same clean env — and by a fresh-copy
   run, not by "it passed on my machine".

## Ad-hoc verification workflow (proving changed behavior)

When asked to verify changes (or the runtime demands verification evidence):
- Write a focused temp script covering ONLY the changed behavior: run each
  changed verifier/step, assert exact expected values, validate generated
  artifacts (e.g. `xml.etree.ElementTree.fromstring` on generated SVGs).
- Create it under `/tmp` with an OS-safe tempfile path and a
  `hermes-verify-` prefix (`mktemp /tmp/hermes-verify-XXXXXX.py`), run it,
  then delete it. If the sandbox blocks writes outside the write root, stage
  the script in the writable root and `cp` it to the mktemp path.
- Say explicitly what it is: **ad-hoc verification of changed behavior, not
  independent suite green** — and note when the project's own canonical gate
  was part of the run.

### Static HTML / concept-site gate

For a self-contained static website, combine structural parsing with targeted
scope/content assertions rather than relying on substring counts or a browser
smoke test alone:

1. Parse with Python's stdlib `html.parser.HTMLParser`; count parsed `html`,
   `head`, and `body` start tags and assert IDs are unique. Do not count raw
   strings such as `"<head"`, because `<header>` is a false positive.
2. Assert required public-language markers and user-visible sections: concept
   status, example/non-participation disclaimer, required customer flow,
   required cards, privacy/data boundary, and the explicitly allowed location.
3. Assert forbidden locations/claims and side effects are absent. For concept
   artifacts this commonly includes excluded addresses, `mailto:`/`tel:` links,
   network calls, browser storage, invented offers/prices/hours/results, and
   outreach language. Prefer exact scope checks over broad word bans so the
   verifier does not reject a truthful disclaimer.
4. Extract inline JavaScript to a temporary file opened in **text mode** and
   run `node --check`; always unlink the extracted file in `finally`.
5. If a check script itself fails, fix and rerun it; report only the final
   exit-0 evidence, while distinguishing the ad-hoc gate from the project's
   canonical suite.

## Pitfalls (each cost real debugging)

- **A gate that runs the test suite must never be invoked from the tests.**
  If `verify_pipeline.py` runs `unittest discover`, any test that calls the
  gate recurses forever (seen live: 400s timeout, suite and gate both wedged).
  Keep the committed suite gate-free; exercise the gate in clean-room runs
  instead.
- **Module globals bound at import defeat `common.X = ...` patching in
  tests.** A module doing `from common import REPO` holds its OWN binding;
  patching `common.REPO` does not redirect it. Tests must patch the module
  attr (`report.REPO = tmp`), rebuild the temp DB per test (isolation — reuse
  of a fixed temp path carries rows between tests), and remember that
  subprocess-invoked gates use the real tree, not the temp one.
- **Prefer a committed test suite asserting known-good numbers over a
  throwaway-script ceremony.** The mktemp → run → delete ritual duplicates
  what committed tests should assert once (math, idempotency, known-good
  reconciliation values, chart XML validity, report structure). Gates should
  also structurally check the ARTIFACTS users consume — report HTML: ≥N SVG,
  no `<script>`/`src=`, complete document — otherwise a wrong chart value or
  malformed report passes (it did, until the checks were committed).
- **Bar charts need a true zero baseline.** Naive max-scaled bar rendering
  emits negative-height / off-canvas rects for negative series (e.g. negative
  net profit by route: `height="-71.7"`). Scale from `min(0, min(vals))` to
  `max(0, max(vals))` and draw each bar from the zero line. Assert `height=-`
  absent in the artifact check.
- **JSON round-trip turns int dict keys into strings.** Storing `{3: 130}` in
  a SQLite JSON column and reading it back gives `{"3": 130}`. Any `.get(int)`
  silently returns 0/None. Use `str()` lookups on snapshot data.
- **`INSERT OR IGNORE` is only idempotent with a UNIQUE constraint.** Tables
  without natural keys duplicate rows on every re-import, silently doubling
  totals. Give every importable table a natural UNIQUE key.
- **`sqlite3.Row` has no `.get()`.** Use `row["key"]` / `or` chains.
- **Verifier drift is the meta-bug.** The mechanism designed to catch drift
  can itself ship drifted (hardcoded paths inside the verifiers, expectations
  matching a layout the release doesn't have). The gate must be run clean-room
  at release time — that's what CI is for.
- **Docs that promise exit 0 without the dependency step** — the one-liner is
  part of the contract. Test it, don't read it.
- When deps are needed but the shell restricts interpreter paths (venv
  binaries, sandbox guards), install deps to a `--target` dir
  (`uv pip install --target ./pylibs ...`) and run with
  `PYTHONPATH=./pylibs python3 ...` — subprocesses inherit the env, so
  chained verifiers all get the deps.

## Support files

- `references/clean-room-audit-recipe.md` — worked case study: auditing the
  hermes-lab runtime bundle (12/14 gate failures, 4 failure classes, the full
  fix sequence, semantic-table reconciliation).
- `references/stdlib-data-tracker.md` — the small-business tracker pattern:
  integer-cents schema, natural keys, balance gates, stdlib SVG charts,
  clean-room verify script, parameterized assumptions.
