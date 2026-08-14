# Epithet Register Construction (execution spec + worked pass, 2026-08-14)

How to flesh out the Monstare Epithet Register from a handful of worked examples into the full
register, tier by tier, without re-introducing premature coherence. This is the operational recipe
behind the register; see `Monstare_epithet_execution_spec.md` for the canonical 4-phase spec.

## The 5 dimensions (author in this order, one writing pass)
1. **Epithet** — 1-3 word signature IN THE AUTHOR'S OWN WORDS (or closest verified equivalent).
   Must be a direct phrase, surprising, evocative of THIS author. Not a generic descriptor.
   If no genuine authorial phrase can be found, write `[epithet pending authorial phrase]` — never
   invent one.
2. **Quotations** — 3-5 VERBATIM passages spanning subtle → robust tonal range, ≥1 "hidden gem,"
   each attributed (page/chapter/§). Every quote must trace to a file on disk.
3. **Tonal Signature** — the author's diagnostic register EXEMPLIFIED by the quotes, never described
   with generic adjectives. May carry ONE line of gloss naming a specific rhetorical move
   ("argues by etymology," "writes in parables," "inverts common sense," "performs the refusal").
4. **Reverie** — present-tense, concrete, sensory vignette (100-300 words by tier). NOT a summary;
   "what it is like to think with this author"; preserves their difficulty/strangeness.
5. **Recall Function** — the SPECIFIC design veto / audit criterion / pilot rule it connects to,
   phrased as a trigger ("When [artifact] invokes [epithet], it asks [specific question]").

Word targets: Tier 1 (A1) 250-300; Tier 2 (CORE) 150-200; Tier 3 (Areas) ~150.

## Anti-coherence guardrails (BINDING, authoring-time not review-time)
- No smoothing across entries; incommensurable pairs (Simondon/Winner, Stiegler/Heidegger,
  Hui/Haraway, Feenberg/Ellul) are marked `INCOMMENSURABLE with [row]: [reason]` and HELD OPEN.
- No forced tonal uniformity — the register is a choir, not a unison.
- Never fabricate a quotation or page number. Abstract-level/image-only entries get quotes labeled
  `[abstract-level — full text needed]` + a verification debt; deferred entries (no text retrieved)
  are left as `[pending]` rather than inventing a voice.

## Workflow (proven end-to-end this session)
1. **Extraction staging** — for each full-text source, extract signature passages to
   `/opt/data/Monstare_epithet_extracts/<row>_<Author>.md` using targeted pymupdf window reads:
   prospectus/intro, conclusion/closing, TOC chapter-title candidates, "the…" (definition),
   "not…" (inversion), "for…/because…" (reason). Tag each candidate TYPE + TONE. Verify text layer
   with BOTH pymupdf and pypdf (a PDF can have a garbage ToUnicode layer). For cached HTML, grep
   the `.md` cache directly. Record incommensurability notes per author.
2. **Draft** each tier into `Monstare_epithet_drafts_<tier>.md` using the 5-dimension template.
   Full-text entries use verbatim page-attributed quotes; abstract-level entries labeled.
3. **Review** (`Monstare_epithet_review_<tier>.md`): per-entry 10-item self-review + cross-entry
   review (choir-not-unison, incommensurables clash, tonal variety, hidden gems).
4. **Assemble** via a Python script that parses the drafts' `## AUTHOR ... [ROW-ID]` sections and
   writes the single live register with a tracking table. KEY: parse by the `[ROW-ID]` tag at the
   end of the header line, NOT anchored at line start (author names come first) — a start-anchored
   regex silently matches zero entries and yields a VACUOUS pass.
5. **Verify** with a structural script: every entry has all 5 dimensions; quotes carry attribution
   or abstract-level label; deferred entries are not fabricated; tracking-table rows == entry blocks;
   spot-check that a signature quote from a canonical author (Heidegger, Hui) appears verbatim in
   BOTH the register AND its extract file. Run assembly twice to confirm idempotency (no drift).

## Assembly/verification scripts (canonical, in /opt/data/scripts/)
- `assemble_register.py` — parses drafts → builds register + tracking table (edit in place).
- `hermes_verify_register.py` — structural checks on the register.
- `hermes_verify_all.py` — compiles all changed scripts + idempotency + register structural check.
  Run via an OS-safe `/tmp/hermes-verify-*.py` temp copy (write-safe root is /opt/data, so author
  the canonical under /opt/data/scripts/ and copy to mktemp to run, then clean up).

## Scope correction lesson
The register's "94 rows" scope was inherited from a phantom `CORE-21..26` (a miscounted "26/26").
Correct scope = A1(18) + CORE(20, incl. CORE-07 located-not-charted) + Areas 2/3/4/5/8(50) = 88.
Always resolve a row-set against the matrix (both current + snapshot) before trusting a memo count.
