---
name: static-wiki-artifacts
description: "Build static wiki artifacts from project knowledge."
version: 1.0.0
license: MIT
---

# Static Wiki Artifacts

## Use when
Use when an existing design memo, tracker, report set, or project knowledge base should become a readable wiki/reference site without a backend, live hosting platform, or frontend framework.

## Workflow
1. **Inspect the source of truth.** Read the README, design documents, current artifact list, schema/configuration, and recent git state. Separate implemented behavior from design and roadmap items.
2. **Choose an honest publication mode.** If the user says “host as a wiki” without naming a public deployment target, build a static wiki artifact in the project and explain the hosting boundary. Do not claim a local file is publicly hosted.
3. **Organize for scanning.** Use a persistent sidebar or table of contents, concise overview, visible status labels, core concepts, current workflow, data model, sources/limitations, roadmap, and links to existing artifacts. Use responsive semantic HTML.
4. **Preserve provenance.** Mark unfinished features explicitly (`DESIGN`, `PLANNED`, `NOT YET LIVE`). Distinguish verified/current data from assumptions, seeds, and future integrations. Never turn a design memo into a claim that a product exists.
5. **Prefer one self-contained HTML file.** Inline CSS; no CDN assets, JavaScript, tracking, or external fonts unless explicitly requested. Relative links should point only to artifacts that exist.
6. **Link to operations.** Include quickstart commands, report links, event/community links, source files, and the intended next implementation step where applicable.
7. **Verify before reporting completion.** Parse with Python's standard-library HTML parser; verify title/status labels; resolve every in-page anchor and relative local link; check prohibited external-asset tags are absent.
8. **For data-backed static artifacts, build a rerunnable generator.** Read the project's canonical SQLite/CSV source rather than copying values into HTML. Keep a small explicit seed/ticker mapping when normalization is needed, and fail loudly if expected source rows are missing.
9. **Make assumptions visible in the artifact.** Use explicit `ASSUMED`, `VERIFIED`, and `PENDING` badges; show the data date/source; never render a historical extraction comp as a current market quote. Add a visible total and row count so the rendered page can be reconciled to the source.
10. **Verify the generator, not only its output.** Execute the generator during verification, then assert expected card counts, totals, provenance markers, pending fields, required links, and absence of scripts/external assets. If no canonical suite exists, report the result as ad-hoc verification.
11. **When an Obsidian vault is the editable layer, keep the executable data project separate.** Link to the generated artifact from the vault, preserve wikilink-resolvable notes, and package the vault only after regenerating and validating the artifact.

## Hosting boundary
A static wiki file is not automatically an internet-hosted website. In a managed/container environment, deliver it through managed files or name the deployment target required (GitHub Pages, Netlify, Cloudflare Pages, or the user's server). Never imply an internal process made the site public.

## Quality bar
- The first screen explains what the wiki is and who it serves.
- Navigation labels match actual section IDs.
- Mobile layout remains usable.
- Tables and code blocks are readable without a framework.
- Limitations and data freshness are visible.
- The artifact is useful before live APIs are connected.

## Supporting material
- `references/verification-pattern.md` contains the standard-library verification pattern for static wiki artifacts.

## Pitfalls
- Do not call a design memo a completed marketplace application.
- Do not invent API data, current prices, or deployment URLs.
- Do not add a fake login, edit system, or “live” badge to a static wiki.
- Do not include broken relative links to generated reports or source documents.
- Do not overbuild a backend when the immediate need is a readable knowledge base.
