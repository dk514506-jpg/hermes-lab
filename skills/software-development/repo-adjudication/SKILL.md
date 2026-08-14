---
name: repo-adjudication
description: "Use when a repo needs review, rating, and a fit verdict."
---

# Repository Review & Adjudication

Deliver an honest verdict on a repo someone points you at: what it actually is, strengths and weaknesses with specifics, an efficacy rating /10, and an adjudication of fit for the user's actual purpose. The cardinal rules: **never review a repo you could not read, and never trust a README claim you can execute.**

## Trigger
- "review this repo", "what do you think of <url>", "rate this", "is this useful for X"
- User asks for impressions + rating + fit adjudication (often before a bigger engagement)

## Workflow

### 1. Verify access first (never fabricate)
- `curl -s https://api.github.com/repos/<owner>/<repo>` — `full_name: null` / `message: Not Found` = not public.
- `curl -s https://api.github.com/users/<owner>/repos?per_page=100` — user exists but zero repos = private/deleted; a clone that prompts for credentials = private.
- If 404: do NOT write a review. Report the evidence (page status, API message, the account's repo count), search for similarly named repos with real metadata, and ask the user how to proceed (make it public / paste README / correct URL). Never substitute a different repo for the one they meant without asking.

### 2. Clone and inventory
- `git clone --depth 1 <url>`, then `find <repo> -type f -not -path '*/.git/*' | sort` for the tree.
- API meta: language, size, stars, created/pushed dates, default branch, release assets (`/releases`).
- Read README + any OVERVIEW/docs first, then the core files (main modules, configs, skills, scripts).
- Verify scripts are real code, not prose: `wc -l` and head a few.

### 3. Execute the claims (the differentiator)
- Run advertised commands and verification gates in a CLEAN environment (a fresh container is ideal).
- Separate failure classes — this is the crux of the whole review:
  - **Environmental:** missing dependencies. Install them and re-run before judging. Do not count these against the author until retested with deps. Prefer `uv pip install --target <dir> <deps>` + `PYTHONPATH=<dir>` (subprocesses inherit it, so whole gate chains get deps) over invoking a uv-venv `bin/python` path directly — some sandboxes/guards misbehave on venv interpreter paths. Invoking verifiers via module import instead of script paths is another safe variant.
  - **Structural:** hardcoded absolute paths (`/home/<user>/...`) or machine-local reads (`~/Documents/...`) inside verifiers/tests/configs. These fail on EVERY machine except the author's. This is the "works on my machine" signature.
- **Drift tell:** `grep -rn "/home/"` and look for `os.path.expanduser("~/...")` in verifiers — even when the README claims "paths scrubbed." A verification gate that was never run in a clean environment is the #1 quality signal. Note which checks DO pass: they are usually the ones written with relative paths and no deps — which proves the design works when the environment is handled, and pins the failure on the packaging, not the concept.

### 4. Re-check after author changes
- `git fetch origin && git diff HEAD..origin/main --stat`, then re-run the gate. Authors often push fixes in response to a review; your verdict should track the repo, not your first impression.
- If the user asks you to FIX the failures (repair the gate, stop the drift) rather than just review them, hand off to the `clean-room-verification` skill — this skill covers the verdict; that one covers the repair (portable resolvers, SKIP-vs-FAIL, anti-drift manifests, clean-room CI).

### 5. Deliverable shape
- **What it is** — one tight paragraph, not a feature list.
- **Strengths with specifics** — cite actual files/lines; hard-won knowledge and verifiable engineering beat vibes.
- **Weaknesses** — name the failure mode precisely (drift, over-engineering, ceremony-to-value ratio, unverifiable claims).
- **Rating /10 with reasoning** — a rating is only meaningful if you read the thing; say what you couldn't verify and factor it in.
- **Adjudication against the user's purpose** — a borrow-vs-skip table mapping what transfers to their use case vs what doesn't. "Good at X, wrong tool for Y."

## Pitfalls
- 404 ≠ "I'll review the spirit of it anyway." Stop and ask.
- Don't count missing-deps failures against the author until you've installed them; don't excuse structural path failures as environment issues.
- A gate that fails on its advertised use case is a FALSE-CONFIDENCE problem, not a cosmetic one — say that plainly: "a gate you can't reproduce manufactures false confidence."
- If the terminal tool starts erroring oddly on certain paths/commands (guard quirks), switch to read_file/search_files for inspection instead of fighting the shell.
