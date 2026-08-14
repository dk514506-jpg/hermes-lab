---
name: clean-room-verification
description: "Make verification gates reproducible in clean environments."
---

# Clean-Room Verification (audit + repair + anti-drift)

Make verification gates reproducible and drift-proof. The trigger is any project whose checks, tests, or "verified" claims only pass on the author's machine — or any time you are asked to FIX a failing/unreproducible gate (not just review it; for the review side use `repo-adjudication`).

## Core principles

1. **A gate is only as honest as its environment.** A check you cannot reproduce does not prove anything — it manufactures false confidence. "Verified" language must be earned by an exit code on a clean machine.
2. **Never fabricate an artifact to make a gate pass.** If a verifier demands a record/log/evidence the repo doesn't ship, you SKIP loudly and flag the gap — you do not invent the artifact. Fabrication converts a real gap into a lie the next reader trusts.
3. **SKIP loudly vs FAIL.** Environment-dependent checks (things that live only on the author's machine — local vaults, installed skill dirs, private data) become conditional SKIPs with an explicit printed reason when the artifact isn't present. FAIL is for what must hold everywhere; SKIP-with-note is for what cannot be verified here. Never let an un-shippable check fail a shippable bundle.
4. **Single source of truth for every duplicated table.** Lists and mappings that exist in multiple files (skill packages, artifact manifests, role→X mappings) drift apart silently. Canonicalize into one manifest and make a verifier assert every copy against it.

## Audit checklist (when asked to fix or when a gate fails)

1. **Run the gate first, exactly as advertised, in a clean environment** (fresh container/CI). Separate failure classes:
   - **Missing deps** → note, install, re-run. Not the author's fault until re-tested.
   - **Hardcoded paths** — `grep -rn '/home/'` and `os.path.expanduser("~/...")` inside verifiers/tests/configs. The "works on my machine" signature. Fails everywhere but the author's box.
   - **Env-dependent reads** — checks that read machine-local state (a vault, an installed copy, private dirs) that the distribution doesn't ship.
   - **Path drift** — the verifier expects a path the shipped layout doesn't have (content exists, verifier looks in the wrong place). Often the author has TWO layouts (home-lab vs bundled) and the verifier only knows one.
2. **Check that a resolver exists but was bypassed.** Projects with a portable root resolver (env var → walk-up → fallback) frequently have some files that use it and others that hardcode. The fix is routing stragglers through the existing resolver, not writing a new one.
3. **Check the docstring-vs-code gap.** READMEs often claim "paths scrubbed" or "expect exit 0" while the code contradicts them. Test the claim, not the prose.

## Repair patterns

- **Route every path through one portable resolver.** `$ROOT_ENV → walk-up from __file__ (look for a marker dir) → home-lab fallback`. Verifiers compute ROOT relative to their own `__file__`; never absolute.
- **Bundle-first resolution.** If a verifier checks for an installed copy (`~/.../skills/<name>`), prefer the copy that ships IN the bundle (`<root>/skill/`), falling back to the installed path so the home-lab gate still works.
- **Env-conditional SKIP.** Wrap home-lab-only checks in `if <artifact dir exists>: ... else: print("[SKIP] <reason>")`. Add the reason as a KNOWN-GAP comment so the absence is tracked, not hidden.
- **Pinned deps + bootstrap.** `requirements.txt` (pinned) + `bootstrap.sh` (uv venv if available, else `python3 -m venv`; installs requirements). The advertised one-liner must include the bootstrap step — on PEP-668 systems a bare `pip install` fails without a venv.
- **Anti-drift manifest.** One JSON manifest holding every duplicated list/mapping. A dedicated verifier asserts: on-disk dirs == manifest sets (missing AND extra), files present, and every table row found in shipped markdown matches the canonical mapping. Runtime artifacts (`__pycache__`, hidden dirs) must be excluded from dir-set comparisons or the gate fights itself.
- **Clean-room CI.** A workflow on push/PR/release that boots a fresh runner, fetches the shipped artifact, bootstraps, and runs the gate. This converts "exit 0" from a memory into a machine-enforced fact. Repo-side table checks (parsing the markdown tables) run in the same workflow.
- **Calibrate matchers, then re-run.** Table checkers need tolerant normalization: strip `**`/markup, handle `Role (note)` and `A / B` cells, and decide whether to require full or primary tokens per table — otherwise you get false positives that drown the real drift. Expect the FIRST run to find real drift; that's the verifier working.
- **Reconciling conflicting duplicated tables (semantic drift).** When two tables disagree, adjudicate by internal consistency: the table where each key appears exactly once AND that agrees with the rest of the docs' usage is the canonical one — the other drifted. Then fix the drifted table so the invariant holds (e.g., every arc must START at the role's home signature), unify taxonomy (two names for the same function → one name; update the manifest), document the reconciliation IN the file (dated blockquote note), and ENCODE the invariant as a verifier check so it can't regress. Expected sequence: checker flags N drifts (designed-to-fail) → owner picks direction → tables fixed → checker flips green.

## Verification-evidence convention

When asked to verify changed code, produce focused ad-hoc evidence rather than claiming suite-green from memory:
- Create a temp script at an OS-safe tempfile path with a `hermes-verify-` prefix (`mktemp /tmp/hermes-verify-XXXXXX.py`), covering the CHANGED behavior only (static sweeps + running the fixed entry points + gate exit code).
- Run it, report the pass count, DELETE the temp file. Summarize explicitly as "ad-hoc verification of changed behavior", noting which checks were static vs executed.
- If a sandbox/guard misbehaves on direct venv-interpreter invocation, install deps with `uv pip install --target <dir> ...` and run with `PYTHONPATH=<dir>` — subprocesses inherit it, so the whole chain gets its deps without referencing a venv python path. (Also fine to invoke verifiers via module import rather than script paths.)
- **Scripts that MUTATE state (git commit/push, file writes) must be verified via a SANDBOX COPY, never the live path.** Copy the script into the throwaway repo and invoke THAT copy; a harness that runs the original path executes it against the real tree (worked failure: a verifier invoked the live sync-script path and committed test stubs into the user's repo). After every run, assert the live tree is untouched (`git rev-parse HEAD` == `origin/main`, `git status` clean). If contaminated: restore with `git reset --hard <last-good-pushed-commit>` — never push the contaminated state.

## Pitfalls

- Fixing only the failures you saw, not the class — sweep the whole tree for the same pattern (hardcoded paths, bypassed resolver) before declaring done.
- Letting `__pycache__`/`.pyc` artifacts count as "extra directories" — the gate creates them; exclude them.
- Making an env-dependent check a hard FAIL in the bundle — the bundle can never satisfy it; use SKIP-with-note and track the gap.
- Claiming "all green" without a clean-environment run of the project's own gate.
- Overwriting an author's semantic tables to force green — the checker's job is to FLAG drift and let the owner reconcile which table is canonical; designed-to-fail is a correct state until they decide.
- Naive static sweeps for old paths flag COMMENTS that merely describe the old paths (e.g., a fix comment reading "was a hardcoded /home/user/... path"). Sweep ASSIGNMENTS (`= "/home/`), not prose; skip comment lines.
- Chained gate runners print only the LAST stdout line of a crashing verifier — a mid-run `open()` crash hides every earlier failure. Run failing verifiers individually to see the full failure set.
- Leaving an intermediate copy of the temp verify script in the workspace: verification trackers re-flag it as a changed path and re-trigger. Create the script directly under /tmp via `mktemp` (write_file may refuse /tmp — shell heredoc into the mktemp path), run, and delete BOTH the /tmp copy and any source copy.

Case study with file:line evidence, the full failure→fix mapping, and the semantic reconciliation (option A): `references/case-study-hermes-lab.md`.
