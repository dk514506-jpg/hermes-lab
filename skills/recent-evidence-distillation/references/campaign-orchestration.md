# Campaign Orchestration — Parent-Side Playbook

Validated on the Motivational-Ecology research campaign (Phase 1: Foundation
Reconstruction, Phase 2: Recent Evidence Review), 2026-08-06. This is the
parent-side counterpart to the member-side distillation workflow in SKILL.md.

## The full sequence

1. **Read the research plan / charter first.** Extract the phase list, the
   artifact classes, and the declared deliverables. Map the phase's required
   outputs (e.g. Foundation_Matrix.md, Construct_Map.md,
   Theory_to_Routine_Interface.md for Phase 1; Recent_Evidence_Digest.md,
   Annotated_Bibliography.md, Contrary_Findings_and_Limits.md for Phase 2).
2. **Set up the governed output structure** (e.g. `docs/<Project>/Foundation/`
   + `council_notes/`). Skeleton every deliverable with `_pending_` cells,
   declared conventions in the header, and a Source Fidelity Register section.
   Structure first, content second.
3. **Probe the journal APIs** (see scripts/journal_api_probe.py) into
   `council_notes/<phase>_api_seed.jsonl` + `.md`. Declare the window
   convention in the registry header (e.g. primary 2025+, 2024 flagged
   pre-window, canonical anchors at any date).
4. **Dispatch the council** — delegate_task, up to 3 parallel subagents, one
   per framework-cluster/area-cluster. Every brief must contain:
   - The exact deliverable schema (section headers verbatim)
   - The declared window convention
   - The seed-registry path ("start here; extend, don't re-derive")
   - Evidence discipline (VERIFIED/RECONSTRUCTED/UNVERIFIED/canonical anchor)
   - Anti-fabrication rules (never invent DOIs; drop 404s; flag retractions;
     exclude pseudoscholarly sources)
   - Word budget (e.g. 700-1100 per area)
   - "Output ONLY the structured deliverable"
   - A list of the curl-able keyless APIs they may use directly
5. **While council runs:** create the next phase's skeletons, read existing
   project registers (open questions, project atlas) so outputs connect rather
   than duplicate.
6. **Assemble** when the consolidated result re-enters: fill skeletons from
   council distillations, consolidate the source-fidelity + retraction +
   contrary-findings registers. Preserve witness conflicts (12-vs-14 TDF
   domains), don't harmonize.
7. **Cross-provider critique pass** — pin a different model API for an
   independent review of the assembled artifacts (contrary-findings work must
   not be the same voice that wrote the synthesis).

## Model-API verification (which model APIs to ping, and how)

The council members themselves run on the configured model API (e.g.
deepseek-v4-flash via DeepSeek). For independent/cross-provider work:

### Nous Portal direct access (OAuth device-code cred)
- Credential lives in `~/.hermes/auth.json` under `credential_pool.nous[0]`
  with fields: `agent_key` (scope inference:invoke), `inference_base_url`
  (e.g. https://inference-api.nousresearch.com/v1), `portal_base_url`.
- List models:
  `curl -s <inference_base_url>/models -H "Authorization: Bearer $AGENT_KEY"`
- Chat completion: POST `<inference_base_url>/chat/completions` with
  `{"model":"<namespaced-id>","messages":[...],"max_tokens":N}`.
- Model IDs are NAMESPACED: `deepseek/deepseek-v4-flash-0731` (canonical slug
  `deepseek-v4-flash-20260731`), `anthropic/claude-opus-5`, `openai/gpt-5.5`,
  `~provider/model-latest` for floating tags. A date-stamped tag like
  `:0731` in a user request maps to a Portal model id like
  `deepseek/deepseek-v4-flash-0731` — check `/models` before assuming it
  exists anywhere else (the DeepSeek first-party API only exposes
  `deepseek-v4-flash` / `deepseek-v4-pro`).
- V4-family models return `reasoning_tokens` in usage; the DeepSeek provider
  profile sets `extra_body.thinking` — mirror that wire shape when calling
  the Portal directly.

### Portal token expiry + why to verify through Hermes, not raw curl

- Nous Portal OAuth tokens are SHORT-LIVED JWTs (~60 min). After expiry,
  direct calls 403 (models endpoint) or 500 with `error code: 1010`
  (Cloudflare TLS/UA fingerprint block on hand-rolled urllib). The stored
  `expires_at` / `agent_key_expires_at` in auth.json shows the expiry —
  `hermes auth status <provider>` silently refreshes the token (rewrites
  auth.json; expiry rolls forward). Run that first when direct calls start
  403ing.
- Prefer Hermes's own provider machinery over hand-rolled HTTP:
  `hermes chat -q "ping" -m <namespaced-id> --provider nous` — the provider
  profile supplies the correct tags/session pinning and OAuth refresh, and
  bypasses the Cloudflare fingerprint block entirely. Use curl only for
  keyless journal APIs.
- **Model flip mechanics:** `hermes config set model.default <id>`,
  `model.provider <name>`, `model.aliases.<alias> <provider>/<id>`; alias
  works in-session via `/model <alias>` but `hermes chat -m` needs the FULL
  id (aliases are not resolved by -m). The CURRENT session keeps its
  start-of-session model (pinned; never hot-swap — prompt-cache invariant);
  new sessions pick up the default. Pin council/delegation models via
  `delegation.provider` / `delegation.model` in config.yaml so subagents run
  on the same build as requested.

### Provider key validation before relying on it
- `hermes status` shows a key as "✓ present" even when the stored key is
  ROTATED/INVALID (the credential pool stores only a `secret_fingerprint`,
  not the live key). Presence ≠ validity.
- Test with a real API call before depending on the provider:
  - Anthropic: `curl -s https://api.anthropic.com/v1/messages -H "x-api-key:
    $KEY" -H "anthropic-version: 2023-06-01" ...` — model aliases drift;
    `claude-sonnet-4-5` works, `claude-sonnet-4-20250514` is not_found.
  - DeepSeek: `GET https://api.deepseek.com/v1/models`.
- **Key-rotation workflow** (user keeps master keys in a desktop file, e.g.
  `~/Desktop/API Keys`, with labeled entries):
  1. Pull the live key from the master file (awk between label lines).
  2. Update BOTH `~/.hermes/.env` AND `~/.hermes/hermes-agent/.env`
     (they can hold different stale values).
  3. Reconcile `auth.json` credential_pool entry: set `secret_fingerprint`
     to `sha256(<new key>)` so the pool's fingerprint matches.
  4. Re-run the API ping to confirm.
- NEVER echo the key into output; use `tr -d ' \r\n"` when extracting, and
  only print length/prefix for confirmation.

## Rate-limit etiquette for the journal APIs

- OpenAlex: burst-throttles with HTTP 429 under rapid repeated full probes
  (re-running a whole probe loop several times in a row will trip it).
  Backoff pattern that works: exponential `2 * 2**i`, honoring the
  `Retry-After` header when present.
- Semantic Scholar: ~1.2s sleep between calls; can return empty on rate
  limit — treat empty as "try again later", not "no results".
- arXiv: ~3s sleep between queries.
- A single API can rate-limit while others stay healthy — the probe script
  must isolate per-API failures (one API's 429s must not abort the others).

## Council-created skills

Council subagents can write skills (they inherit skill_manage). When a
subagent creates one mid-campaign (curator logs "Self-improvement review
'<name>' created"), review it for: (a) session-specific vs class-level scope,
(b) leaked parent-context references (e.g. persona harness names), (c)
whether its pitfalls are accurate. The session's subagent-created skill was
high quality and was adopted as the class umbrella; the governance question
(whether council members may create skills autonomously) belongs to the user.
