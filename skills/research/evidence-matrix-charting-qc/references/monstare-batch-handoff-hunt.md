# Monstare batch handoff prompts + open-source hunting (batches 3->4, 2026-08-13)

## Batch handoff prompt structure (Monstare_Handoff_Prompt_BatchN.txt)
Sections: Step 0 file-read order (context package -> canonical xlsx -> all prior batch memos -> role prompts -> audit CSVs -> working sources); Current state (charted count, spend lesson from prior batch); Step 1 harness verify (delegate_task availability, max 3 children, collapsed Pip+Locus fallback); Step 2 budget (100k envelope, HARD stop, collapse economy, record spend); Step 3 batch scope (SUB-BATCHES: chartable-now rows first, gated rows second; per-row access notes; abstract-level fallback = documented decision + caveat, CORE-12/17 precedent); Step 4 role QC (collapsed config: Pip + Locus + Methodologist + Purist when Cosmo Rel. high; Ethics standby; Data Steward ALWAYS for writes); Step 5 deliverables (patch SAME matrix in place additive-only; memo path `Monstare_batch_N_findings_faultlines_memo.md`; role-prompt refinements); Operating law (verbatim disciplines); Environment notes (uv run --with openpyxl, dashboard download links, subagent self-report verification).

User expectation: handoffs must include explicit per-source READABILITY TRIAGE — 'readable now (live-verified)' vs 'lending-only / replacement needed' with what a good replacement looks like. The user hunts replacements; finds drop in /opt/data/Monstare_batchN_sources/ and get verified (HTTP + text layer + provenance) before charting.

## Readability triage (how to classify)
- READABLE: curl -sL -A 'Mozilla/5.0' -o /dev/null -w '%{http_code} %{content_type} %{size_download}' -> 200 + application/pdf + size >100KB (book PDFs run 0.5-12MB); HTML article >100KB OK.
- PARTIAL: preview PDFs (e.g., Routledge 17p preview), short HTML that may be a synopsis (bruno-latour.fr node/258 = 19KB — VERIFY coverage), chapter-only copies.
- LENDING-ONLY: archive.org /details page with 'borrow'/login — does NOT count as open; needs user account or a replacement hunt.
- Staleness pitfall: the source-audit CSV can predate the matrix's current URLs (batch-3 CORE-20: CSV flagged an old URL dead/wrong after the cell had been replaced) — verify the CURRENT cell, not the CSV verdict.

## Sub-agent source-hunt protocol
- Dispatch 3 parallel leaf agents split by priority (Pri A books together). Each goal self-contained: exact citation + edition/translation, known leads (monoskop author pages, author sites, archive.org open scans, course mirrors), legitimacy whitelist (author-hosted, university course pages, archive.org OPEN items only — borrow/lending does not count, monoskop, publisher OA; NO libgen/sci-hub/z-library/annas-archive/sketchy uploads), curl-verify EVERY candidate before reporting, honest NOT_FOUND allowed, timebox ~20-25 tool calls, exact output format (ROW/STATUS/URLS/NOTES with http_code+content_type+size).
- Halting buckets per row: FOUND (verified readable) | PARTIAL (chapter/excerpt, documented caveat) | NEEDS_USER (borrow/purchase/institutional — report to user for action) | NOT_FOUND (documented negative). Hunt halts when every row is in one bucket.
- After agents return: re-verify EVERY candidate URL yourself (sub-agent reports are self-reports — batch-1 JSON-misread precedent), then save a hunt-results file (per-row status + URLs + evidence) for the next batch handoff.
