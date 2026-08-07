---
name: recent-evidence-distillation
description: Distill recent evidence into a verified structured review.
---

# Recent-Evidence Distillation & Verification

Class of task: "recent-evidence distillation", "recent evidence review", seed-registry
expansion rounds, council-notes style reviews with a strict post-2024/2025+ window, or any
task demanding 6-10+ verified real papers with per-paper status labels. Governed by the
astral-research-harness persona when that harness is active (Researcher circuit,
evidence-ladder discipline); this skill is the operational playbook.

## Workflow (5 steps)

1. **Read the seed registry / prior corpus first.** It already contains pre-verified
   entries with DOIs, venues, and citation counts. Reuse them as anchors; don't re-derive.
   (Example: `docs/Ecology/Foundation/council_notes/phase2_api_seed.md`.)
2. **API discovery** — OpenAlex works endpoint (keyless, rich metadata). See playbook.
3. **Parallel verification** via `web_extract` (max 5 URLs per call) — prefer publisher
   pages, PMC, arXiv abs pages, doi.org resolution. Batch independent fetches.
4. **Fallback verification** when publisher fetch fails (ScienceDirect/firecrawl timeouts,
   paywalled JS-only pages) — Semantic Scholar Graph API, PubMed E-utilities, CrossRef.
5. **Label + assemble** the deliverable in the exact format below.

## API playbook

### OpenAlex (`https://api.openalex.org/works`)
- Query: `?filter=<filters>&sort=cited_by_count:desc&per-page=7`
- Filters: `from_publication_date:2025-01-01,to_publication_date:<today>` and
  `title_and_abstract.search:"theoretical domains framework"` — `AND` between quoted
  phrases works (`"self-determination theory" AND "generative"`).
- **PITFALL (cost ~an hour of silent debugging):** never pre-encode `%22` into the filter
  string before `urllib.parse.quote()`. `quote()` encodes `%` → `%2522`, the API receives
  literal `%22`, and every query returns `count=0` with **no error**. Use literal `"`
  characters in the filter string and let `quote(filter_str, safe=':,-')` do the encoding.
  Same class of bug for `%20` — let the encoder handle all of it.
- Abstracts: reconstruct from `abstract_inverted_index` (word → position map).
- Rate limits: HTTP 429 under burst — exponential backoff (2·2^i seconds,
  honor the `Retry-After` header) between lookups. A full multi-query probe
  can legitimately take minutes when the pool is hot; that's the limiter
  working, not a hang.
- **PITFALL (multi-word queries return count=0 with no error):** OpenAlex
  treats an unquoted multi-word search string as ONE exact phrase. For
  multi-concept queries, build explicit expressions —
  `title_and_abstract.search:"theoretical domains framework" OR "COM-B"` —
  or wrap a single phrase in quotes. Bare `theoretical domains framework
  COM-B` matches nothing silently.
- Metadata gotchas: book publisher/venue can differ from expectations. Example: Yuk Hui's
  *Machine and Sovereignty* is **University of Minnesota Press 2024 (open access,
  CC BY-NC-ND)**, DOI 10.5749/9781452973685 — commonly miscited as MIT Press.

### Semantic Scholar Graph API (fallback when publisher page fails)
- `https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>?fields=title,abstract,year,venue,authors.name,externalIds`
- Sleep ~1.2s between calls. Abstracts are often absent → that's **record-level**
  verification only (title/venue/year/authors confirmed, abstract unavailable) — say so.

### PubMed E-utilities (PMID → record)
- `esummary.fcgi?db=pubmed&id=<pmid>&retmode=json` → title, journal, pubdate, authors.
  Use for 2026-in-window items that haven't reached other indexes.

### CrossRef (retraction + record check)
- `https://api.crossref.org/works/<doi>` → the `title` field carries the
  `RETRACTED ARTICLE:` prefix when retracted. The `event` field may be empty even for
  retracted records — check the title marker, then verify the publisher notice before
  citing the retraction itself. Check meta-analyses in hot fields (GenAI-education has a
  real retraction rate — e.g., Wang & Fan, HSSC 2025, DOI 10.1057/s41599-025-04787-y).

### Books / canonical anchors
- Guessing publisher URLs (`mitpress.mit.edu/978...`) fails. Resolve
  `https://doi.org/<doi>` instead — lands on the publisher/Manifold page with full
  metadata, license, and often open-access text. For canonical anchors (Beer,
  Maturana & Varela, Morozov), citing the standard edition is fine — mark "canonical
  anchor" and note "not fetched" when true.

## Verification status labels (use verbatim in deliverables)

- **VERIFIED** = fetched the source (abstract at minimum). Add scope nuance:
  "record-level" (metadata via API, abstract unavailable), "landing page only"
  (title/venue/DOI confirmed, full text paywalled).
- **UNVERIFIED** = search/index record only (e.g., registry entries not re-fetched).
- **RECONSTRUCTED** = agent-applicability inference, explicitly labeled, never presented
  as doctrine (e.g., "closed-loop ≠ organizational closure" — philosophy kept as
  philosophy).
- **canonical anchor** = pre-window classics — cite standard editions, mark as anchors.

## Deliverable format (user's spec — reproduce exactly)

Per area, in order:
1. **Key papers 2025-2026** — bullets: `year — authors — "Title." Venue. DOI. **STATUS**.`
   1-2 sentence finding each. Prioritize 2025-2026; canonical anchors excepted.
2. **Key papers 2024 (pre-window, foundational only)** — same bullet shape.
3. **Convergent findings** — what the verified corpus agrees on.
4. **Contrary/conflicting findings** — disagreements, retractions, opinion-vs-empirical.
5. **Gaps** — what the literature does not yet cover.
6. **Agent-architecture implications** — actionable, labeled RECONSTRUCTED where
   inferential.
7. **Source fidelity flags** — sample sizes, single-country samples, opinion articles,
   preprints, retractions, paywalled-only verification, pseudoscholarly sources to exclude.
Optional cross-area **Synthesis** (3-5 sentences). Word budget ~700-1100 per area;
a dense bullet list is preferred over prose. When the task says "Output ONLY the
structured deliverable", output exactly that plus at most a compact work summary
(what was done / found / files / issues).

## Parent-side campaign orchestration (multi-phase review campaigns)

When you (the parent) run a multi-phase literature review as a council campaign —
not just a single distillation — follow this sequence. Validated on the
Motivational-Ecology Phase 1/2 campaign (2026-08): skeleton-first assembly,
journal-API seeding, parallel council dispatch, cross-provider critique.

1. **Declare conventions before dispatching.** Window (e.g. "post-2024" = 2025+
   primary, 2024 flagged), evidence labels, and artifact locations go in the
   brief AND the skeletons — never assumed later.
2. **Skeleton-first.** Create the deliverable skeletons (matrix/construct-map/
   interface tables; digest/bibliography/contrary-findings registers) with
   `_pending_` cells BEFORE the council returns. Structure first, content
   second. Bake evidence labels and guardrail columns (empowerment boundary,
   atrophy check, quarantine rule) into the skeletons.
3. **Seed registry from journal APIs.** Probe OpenAlex/PubMed/arXiv/S2 into a
   `council_notes/<phase>_api_seed.{jsonl,md}` (see
   `scripts/journal_api_probe.py`). Give council members the seed path — they
   extend it, they don't re-derive.
4. **Dispatch council:** up to 3 parallel subagents, one per area-cluster. Each
   brief MUST carry: exact deliverable schema, declared window, seed-registry
   path, evidence discipline, "Output ONLY the structured deliverable". Tell
   them they may curl the keyless APIs themselves.
5. **Watch live_transcripts paths, don't poll.** The consolidated result
   re-enters as a message when ALL members finish.
6. **Assemble into skeletons; consolidate registers.** Source-fidelity
   register, retraction flag register, contrary-findings register — filled from
   the council's flags, not re-derived.
7. **Cross-provider critique pass.** After assembly, run an independent review
   on a DIFFERENT model API (Anthropic/OpenAI/Nous Portal) so the
   contrary-findings work is not the same voice that wrote the synthesis.
   Verify the provider key actually works before relying on it — see
   `references/campaign-orchestration.md` (Nous Portal direct access +
   key-rotation workflow).

Support files:
- `references/campaign-orchestration.md` — full parent-side playbook incl.
  model-API verification (Nous Portal direct access, provider key rotation).
- `references/council-critique-rounds.md` — the 3-lens critique pattern
  (evidence / architecture / governance critics) + revision-round workflow
  for quality-gating an assembled deliverable; user's sublative framing
  (preserve kernel, negate limitations, raise the level).
- `references/json-schema-verification.md` — validation battery + authoring
  pitfalls for JSON Schema artifacts (state_schema.json files, estate schemas).
- `scripts/journal_api_probe.py` — parameterized OpenAlex/PubMed/arXiv/S2
  probe that writes the seed registry.

## Phase artifact authoring (post-assembly; validated on Ecology Phase 5)

When a campaign phase produces structured artifacts beyond the digest
(schemas, operational-procedure docs, indexes), follow the Phase 3–5 pattern:

1. **Carry the evidence discipline into the artifact itself.** Thresholds and
   rules inside a schema or procedure get per-item VERIFIED/RECONSTRUCTED
   flags; numeric cutoffs are labeled "calibration anchors, not doctrine"
   (Contrary_Findings D1). Ground each rule in a VERIFIED finding; mark
   operationalizations RECONSTRUCTED. This is what makes a schema an evidence
   document, not just a type declaration.
2. **Resolve canonical-state-variable drift in the artifact, citing the
   traceability register.** When a metric has aliases across packages (e.g.
   skill_load_score vs skill_load_trend vs skill_load_metric), the new schema
   declares the canonical name, marks derived variables as derived, and cites
   `Phase3_Skills/T2R_traceability.json` canonical_state_variables — do not
   silently pick a name.
3. **Verification is a committed per-phase script, not inline checks.** The
   repo convention is `council_notes/verify_phaseN.py`: `check()` helper
   printing `[PASS|FAIL]`, a `fails` list, exit 0/1, all JSON artifacts parsed
   + structurally asserted, verifiers chained via `verify_all.py`. Write the
   durable script BEFORE declaring done; inline heredoc verification is
   ephemeral and the system will ask for re-runnable evidence.
4. **JSON Schema artifacts get a four-part battery** (see
   `references/json-schema-verification.md`): meta-schema validity, realistic
   conformance instance, negative tests, `$ref` integrity. This caught two
   real bugs in Phase 5 (`const` on prose fields; required-but-undefined
   property) that plain parsing would have missed.
5. **Truthfulness review of Council output before declaring done.** When
   asked to review/criticize/revise assembled artifacts "for accuracy and
   truthfulness to the project as a whole": verify EVERY evidence citation
   against the source artifacts (digest, bibliography, contrary-findings
   register) rather than trusting the writer's flags. Grep each author-year
   key in the digest and compare flags. Real Phase-5 catches: Jose 2025 is an
   OPINION article per the digest quality register yet was cited as plain
   VERIFIED in skill_atrophy_risk_check.md; CALM-IT (Nguyen 2026) is an arXiv
   preprint cited unflagged in scaffolding_fade_rules.md. Fix = edit the
   artifact AND add a durable verifier guard asserting the caveat text
   ("opinion"/"commentary", "preprint") survives — drift like this is exactly
   what the post-assembly review exists to catch, and it recurs every phase.

## Anti-fabrication rules

- Never invent DOIs, PIIs, or article numbers. A guessed URL that 404s is **dropped and
  noted**, never replaced with plausible-looking output. Discard and move on.
- Flag quality classes explicitly: opinion articles (not empirical), arXiv preprints
  ("Preliminary Work"), retracted papers, pseudoscholarly self-published content
  (LinkedIn "third-order cybernetics" essays, Zenodo mirror-theory items) — exclude from
  the evidence base and say so in flags.
- Cite article numbers only when confirmed; DOI + journal + year is always safe.
- Workspace hygiene: temp query scripts (`*_queries.py`) get deleted at the end; the
  deliverable is saved to the campaign's notes directory (e.g., council_notes/) if one
  exists.
