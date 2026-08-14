---
name: reproducible-verification-gates
description: "Audit or build verification gates; prevent table drift."
---

# Reproducible Verification Gates & Drift Prevention

## When to use
- A repo/bundle/docs claims "verified" or "expect exit 0" and you're about to trust it from a fresh machine.
- Verifiers or gates fail in a clean environment but pass on the author's machine.
- Duplicated content tables or configs (role mappings, package/file lists, dojo lists) drift apart.
- Building a check that must prove its own numbers (P&L reconciliation, CI gates, artifact verifiers).

## Core principle
A gate is only as honest as its environment reproducibility. A gate that only passes on the author's machine is not a gate — it manufactures false confidence. "Verified" must be earned by an exit code from a clean checkout. Corollary: the mechanism designed to catch drift can itself drift (verifier path expectations, hardcoded roots) — audit the verifiers, not just the artifacts.

## Audit checklist (failure classes, in order of likelihood)
1. **Hardcoded machine paths** — grep for `= "/home/`, `= '/home/`, `/Users/`, and author usernames in verifiers/configs. Sweep non-comment lines only (or match assignment patterns) — comments that *describe* the old path trip naive regexes.
2. **Environment-dependent checks** — verifiers reading a local wiki/DB/vault (`~/Documents/...`) that isn't shipped. Fix: conditional SKIP with a loud reason ("home-lab only"), never FAIL, in shipped artifacts.
3. **Undocumented dependencies** — gate needs PyYAML/jsonschema but the one-liner never installs them; on PEP-668 systems a bare `pip install` fails. Fix: `requirements.txt` + `bootstrap.sh` (uv venv, else `python3 -m venv`) + README documents the exact sequence.
4. **Verifier-vs-layout path drift** — verifier expects `<root>/skills/<name>/references/x.md`, bundle ships `<root>/skill/references/x.md`: content exists, check looks in the wrong place. Fix: resolve from the shipped layout first, home-install fallback second.
5. **Duplicated tables, no canonical source** — same mapping appears in N docs; nothing asserts they agree. Fix: canonical manifest (JSON) + anti-drift verifier asserting on-disk sets == manifest and every derived table row carries canonical tokens.

## Fix layers (the full repair pattern)
1. **Portable root resolver**: `$ENV_VAR` → walk up from `__file__` looking for a marker dir → home-lab fallback. Ship as one module; route EVERY verifier through it.
2. **Conditional SKIPs** with explicit reasons for un-shippable home-lab checks.
3. **Pinned deps + bootstrap script**; document the exact command sequence.
4. **Clean-room CI** (GitHub Actions): fresh ubuntu, checkout, fetch release artifact, bootstrap, run gate; fail on nonzero. Triggers: push/PR/release + manual dispatch with artifact URL input.
5. **Canonical manifest + anti-drift verifier** wired into the gate chain. Add invariants beyond presence ("arc starts at home", "every planet exactly one home") to catch semantic drift, not just file drift.
6. **Fresh-copy proof**: before claiming victory, copy the whole tree (no DB, no reports, no state) and run the documented sequence green.

## Checker calibration pitfalls
- Exclude runtime artifacts the gate itself creates (`__pycache__`, hidden dirs) from directory-set comparisons.
- Tolerate markup in scanned tables: strip `**` via `.replace("**","")` (a bare `strip("*")` fails on mid-string `**`), drop parentheticals, handle slash-roles ("Critic / Tester" → Tester).
- Verify the verifier: naive checks (stripped-then-prefix compares, sweeping comments) produce false FAILs. Negative-test: it must flag exactly the known conflicts and nothing else.
- "Designed-to-fail" states are legitimate: a checker that flags known drift until reconciled IS the mechanism working.
- Arc-style cells: if a cell is "X → Y", the invariant is usually that the arc STARTS at the canonical home — check the pre-arrow segment, not the whole cell.

## Ad-hoc verification evidence pattern
When verifying changed behavior without a canonical suite: write a focused temp script — `T=$(mktemp /tmp/hermes-verify-XXXXXX.py)` (OS-safe, `hermes-verify-` prefix), run it, delete it, and report explicitly as AD-HOC verification, not suite green. If write tools block `/tmp`, write the source under the writable root and `cp` to the mktemp path (delete both). Validate generated artifacts structurally (e.g., XML-parse every SVG) rather than eyeballing. Fresh-copy tests must run the FULL documented sequence (init → import → gate → report) — skipping an intermediate step produces a false failure.

## References
- `references/hermes-lab-audit-case-study.md` — full worked case: a released "exit 0" bundle that failed 12/14 verifiers in a clean cloud container, and the repair to 15/15 green + a live semantic-drift catch.
