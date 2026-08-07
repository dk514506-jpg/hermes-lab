# Multi-Phase Research Campaign Recipe

Validated 2026-08-06 on the Motivational Ecology campaign (Ecology Phases 1-4,
~140 files, 4 council dispatches of 3 subagents each, plus critique + revision
rounds). The parent assembled every artifact from subagent summaries; the
campaign was registered in its own ecology (registers, atlas, journal,
handoff notes).

## Campaign shape

```
Phase N (build)  →  critique round (3 critics)  →  revision round  →  verify_N.py
     │                                                                    │
     └── outputs are governed artifacts on disk (never chat replies) ─────┘
```

Phase archetypes that work:
- **Foundation reconstruction** — council distills N frameworks from primary
  sources → parent assembles comparison matrix + construct map + theory-to-
  routine interface.
- **Recent evidence review** — council distills post-window literature per
  search area → parent assembles digest + annotated bibliography + contrary-
  findings register.
- **Skill/package build** — council writes files directly to disk (one
  package per member) → parent verifies structure.
- **Integration** — parent does precision surgery (edge conventions, naming
  normalization, quarantine), council optional.

## Dispatch brief template (every council member gets this)

Context must include:
1. **Exact output format** — per-area section schema the parent will assemble
   from. "Output ONLY the structured deliverable."
2. **Evidence discipline** — VERIFIED / RECONSTRUCTED / UNVERIFIED semantics;
   retraction flags register-only; never fabricate citations; drop 404s and
   note them.
3. **Window convention** — declared explicitly, not assumed ("primary
   2025-01-01..today; 2024 only if foundational, marked pre-window").
4. **Seed registry path** — a file of pre-verified candidates to reuse as
   anchors ("read this first; verify by fetching; expand with your own
   searches").
5. **Tool hints** — which APIs to curl (OpenAlex/PubMed/arXiv), rate-limit
   notes, "prefer the actual paper over a bare citation."
6. **Word budget** per section (700-1100 words/area works).

Subagent capabilities to remember: leaf subagents CAN write files to disk
(used for the 8-package skill build), can create skills (one auto-created
`recent-evidence-distillation` this session — user approved keeping it), and
can run terminal. They cannot delegate, clarify, or write memory.

## Phase output shapes (Ecology exemplars)

- Phase 1: Foundation_Matrix.md (8-framework comparison), Construct_Map.md
  (cross-framework relations → typed-edge seed), Theory_to_Routine_Interface.md
  (theory→AtomicOp seam: per-construct rows + op/edge candidate registers).
- Phase 2: Recent_Evidence_Digest.md (per search area + cross-area
  convergences/tensions + retraction register), Annotated_Bibliography.md
  (numbered entries, DOIs, status per entry), Contrary_Findings_and_Limits.md
  (framework critiques A1-A5, evidence-level contrary findings, review limits,
  architecture implications).
- Phase 3: 9-file HiSkill packages (SKILL.md with 16 mandated sections,
  skill_node.json, atomic_ops.json, edge_map.json, state_schema.json,
  examples/support_ops/recovery_ops/evaluation_notes) + skill_graph_index.json.
- Phase 4: reconciled skill_graph_index.json, lattice_index.json,
  skill_lattice_interface.md, insight_trigger_policy.md,
  T2R_traceability.json (register-op → package-op mapping).

## Critique round (the "sublate" pattern the user requests)

Dispatch 3 critics:
- **Epistemology & evidence** — flag consistency across files, unsupported
  claims, integrity-register handling, descriptive-vs-predictive respect.
- **Architecture & design** — do packages instantiate the theories; do
  AtomicOps match the register; do edges compose; is the boundary enforced
  in code not prose.
- **Ecology & governance** — charter fidelity, alive-vs-archival, continuity
  records, interpretive sovereignty, Valens quarantine law, self-application.

Each returns, exactly:
```
## 1. The kernel (what is genuinely strong — specific)
## 2. The limitations (what is weak or wrong — file:section)
## 3. The missing (what would raise it a level)
## 4. Concrete revision instructions (numbered, file-level)
## 5. Verdict (one sentence)
```

Critiques land in delegation summary files; copy them to council_notes/ as
critique_0/1/2_*.txt and fix the journal/handoff pointers to the REAL paths
(the critic will check that the continuity record points at existing files).

## Revision round

1. Categorize each critique point: accept / adapt / reject (with reasons).
2. Apply file-level fixes; record each in the session journal.
3. Update the stale verifier assertions — a revision round changes the state
   the old checks asserted (e.g. "pending convention notes" become 0 after
   resolution). Assert the RESOLVED state, not the pre-revision state.
4. Re-run everything; report exit codes.

## Journal-API quirks (hit this session)

- **OpenAlex phrase-quoting:** `title_and_abstract.search:"phrase"` works for
  one phrase; multi-concept queries return 0 silently — use explicit
  `OR` between quoted phrases (`"a" OR "b"`). Never pre-encode `%22` into the
  filter before `urllib.parse.quote()` — quote() re-encodes `%` → `%2522` and
  every query returns count=0 with no error. Pass literal `"` and let
  `quote(filter_str, safe=':,-')` encode.
- **OpenAlex rate limits:** HTTP 429 under bursts — exponential backoff,
  honor Retry-After header. Repeated full probe runs will trip it.
- **Semantic Scholar:** 1 req/sec unauthenticated; often rate-limited; fall
  back to publisher/PMC/arXiv fetches. Abstracts frequently absent — that's
  record-level verification only; say so.
- **arXiv:** 1 req/3s; parse Atom XML with ElementTree; check for withdrawn
  papers in the summary field (SRSUPM was withdrawn this session).
- **PubMed:** esearch → esummary two-step; good for 2026 items not yet in
  other indexes.
- **CrossRef:** retracted articles carry "RETRACTED ARTICLE:" in the title
  field — check the title marker, not just the event field.
- Seed registry (phase2_api_seed.md/.jsonl) = the deduped probe output;
  dedupe by (api, query, title, year) after re-runs.

## Verification consolidation (the durable-gate technique)

Why: the runtime re-asks for verification of changed paths when the previous
check was an inline heredoc — there's no named file to re-run.

Fix:
1. Write `verify_<phase>.py` per phase with assertions on the changed paths
   (parse, structure, conventions, counts).
2. Write `verify_all.py` — single entry point that compiles every changed
   script, parses every changed JSON, runs structural assertions, then
   subprocess-executes each verifier; one process, one exit code.
3. Run `python3 council_notes/verify_all.py`; report `exit 0` and the check
   count. That is the release gate.
4. When a test's own assertion miscounts (45 vs 47 entries), fix the test —
   the file is the source of truth, the assertion was a bad guess.

## Continuity (register the campaign in its own ecology)

- `handoff_notes.md` per campaign dir — what a fresh agent needs to re-enter
  from disk, NOT from the parent's context window.
- Session journal in the wiki vault (`journal/YYYY-MM-DD.md`) — updated per
  phase and after the revision round, with the critique verdicts.
- Open Questions Register — campaign questions get QIDs, Date Added, Related
  Projects, Status (RESOLVED/PARTIALLY RESOLVED/OPEN), Last Witnessed.
- Project Atlas — register the campaign with relation edges + answer the
  monthly review questions.
- Self-application: track what the user does unassisted per phase (Q10-style);
  councils that do all the reading/judging deskill the user the architecture
  exists to empower — schedule one unassisted user task per phase.
