---
name: knowledge-base-vaults
description: "Use when creating a linked Obsidian-compatible project wiki."
category: note-taking
---

# Knowledge-Base Vaults

Use this class-level workflow when a project needs a durable wiki/knowledge layer rather than only generated reports or application files. The default implementation is an Obsidian-compatible vault, but the information architecture should remain portable Markdown.

## Core principle

Separate the **editable human knowledge layer** from the **operational source of truth**:

- Vault notes contain business rules, workflows, decisions, research, data-model explanations, and links.
- Databases, scripts, generated reports, and dashboards remain in the project directory unless there is a strong reason to duplicate them.
- Use pointer notes to connect the vault to generated artifacts instead of copying volatile output into prose notes.

This boundary prevents the wiki from becoming stale or accidentally becoming the database.

## Workflow

1. **Inspect before creating.** Identify the project root, existing design/readme/reports, source-of-truth database, and any existing vault configuration. Do not invent the content model before reading the project materials.
2. **Choose a durable location.** Prefer a vault inside persistent project storage, beside (not inside) generated outputs. Resolve the actual absolute path before writing.
3. **Create a navigable spine.** Start with `Home.md` and linked class-level pages such as Business Overview, Operating Workflow, Marketplace/Domain Model, Data Model, Sources and Limitations, Roadmap, and Project Artifacts.
4. **Use numbered folders only for broad areas.** A practical default is `00 Inbox`, `01 Operations`, `02 Market Intelligence` (or domain equivalent), `03 Research`, `04 Reference`, and `05 Templates`. Keep evergreen landing pages such as `Home.md`, `Roadmap.md`, and `Research.md` at the vault root when wikilinks benefit from stable, unambiguous targets.
5. **Configure the vault.** For Obsidian, create `.obsidian/app.json` and `.obsidian/appearance.json` with conservative settings. Configure new notes and attachments to land in intended folders; do not put credentials or volatile databases in the vault.
6. **Write useful notes, not placeholders.** Each page should include current status, practical rules, links to related pages, and explicit evidence/provenance conventions where relevant. Preserve uncertainty labels such as `VERIFIED`, `ASSUMED`, and `UNVERIFIED`.
7. **Add an inbox and reusable template.** Include an inbox capture page and at least one template for recurring observations or research. Capture date, context, source, evidence label, caveats, action, and related links.
8. **Verify mechanically.** Parse the JSON configuration, count/inspect Markdown notes, extract `[[wikilinks]]`, and confirm every link resolves either by exact path or by note basename. Also verify expected project pointers exist and that no accidental executable/embedded content was introduced.
9. **Report the handoff clearly.** Give the user the exact vault path, explain what stays outside the vault, and state what was actually verified. Distinguish ad-hoc verification from a canonical test suite.

## Information architecture guidance

- `Home.md`: orientation, status, conventions, links.
- Operations: business model, weekly workflow, decision rules, KPI definitions.
- Domain intelligence: planned dashboards, taxonomy, metrics, data model, source limitations.
- Research: source notes and annotated evidence.
- Reference: pointers to reports, databases, design documents, and scripts.
- Templates: recurring capture formats.
- Inbox: unprocessed ideas, voice-note transcriptions, scans, and show observations.

## Pitfalls

- Do not claim the vault is in Google Drive, Obsidian Sync, or publicly hosted unless an external sync/publishing action was actually completed.
- Do not silently move the operational database into the vault; link to it.
- Do not create only a pretty index page. The value is the linked structure and recurring capture workflow.
- Do not rely solely on nested-folder wikilinks when stable root landing pages make resolution clearer; verify links rather than assuming Obsidian resolves every path the same way.
- Do not copy generated HTML into Markdown and call that a wiki. Keep the generated artifact as a linked reference.

## Supporting detail

See `references/obsidian-vault-verification.md` for the compact verification recipe and known-good configuration shape.
