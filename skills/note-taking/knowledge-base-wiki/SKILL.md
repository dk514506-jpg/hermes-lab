---
name: knowledge-base-wiki
description: "Use when building a linked project wiki or knowledge base."
---

# Project Knowledge-Base / Wiki Design

Use this skill when a project needs an editable wiki, linked reference system, or durable knowledge layer alongside executable code, databases, and generated artifacts. Prefer a class-level knowledge base over a single long page: organize stable concepts into linked notes, keep raw captures separate, and preserve a clear boundary between human-edited prose and machine-generated data.

## Core architecture

1. **Choose a durable root** inside persistent storage or the user's designated sync location.
2. **Create a vault-level home note** that explains purpose, current status, navigation, conventions, and links to the main project artifacts.
3. **Organize by information lifecycle**, not creation order:
   - `00 Inbox` — unprocessed ideas, field notes, attachments
   - `01 Operations` — business rules, workflows, SOPs
   - `02 Market Intelligence` or domain analysis — models, observations, decisions
   - `03 Research` — sources, evidence, annotated bibliography
   - `04 Reference` — pointers to code, reports, databases, external artifacts
   - `05 Templates` — repeatable note formats
4. **Use wikilinks for conceptual navigation** and relative file links only for adjacent project artifacts.
5. **Keep generated artifacts outside the vault** when scripts or databases produce them. Link to them rather than duplicating them.

## Obsidian initialization

When setting up an Obsidian vault, create `.obsidian/app.json` and `.obsidian/appearance.json` only when configuration is useful and safe. Practical defaults:

- attachments under `00 Inbox/Attachments`
- new notes under `00 Inbox`
- `alwaysUpdateLinks: true`
- wikilinks rather than Markdown links
- modest custom accent color, without depending on plugins or themes

Do not assume a vault exists. Resolve `OBSIDIAN_VAULT_PATH` first; if absent, choose an explicit durable project-local vault path and tell the user exactly where it is.

## Note design

Every durable note should have a descriptive title, clear status where relevant (`DESIGN`, `ACTIVE`, `VERIFIED`), concise purpose and scope, related-note links, evidence/provenance labels when facts or data are involved, and a short next-action or links section when operational.

For data-heavy projects, define a repeatable observation template with date, entity, condition/state, value, source, evidence label, and interpretation. Separate verified facts from manual seeds, estimates, and unverified leads.

## Verification gate

Before declaring the vault ready:

- confirm expected `.obsidian` JSON parses
- confirm required folders and notes exist
- enumerate `*.md` notes
- extract `[[wikilinks]]` and verify every target resolves by path or unique basename
- verify templates contain all required fields
- verify seed/demo data is explicitly labeled non-live or assumed when it is not sourced from a live/verified feed
- if delivering to the user, package the vault and test the archive listing/extraction

A verification command should emit real counts and fail on missing links or required fields. Do not call an ad-hoc check a canonical test suite.

## Delivery

For hosted/container environments, provide both the absolute source path and a downloadable managed-file URL when available. If an archive utility is missing, use a standard-library or available archive alternative rather than claiming the archive exists. Rebuild the archive after content changes and validate it before delivery.

## Pitfalls

- Do not confuse a static HTML wiki with an editable Obsidian vault; they serve different purposes.
- Do not duplicate the operational database, generated reports, or scripts into prose notes unless the user explicitly wants a snapshot; link to them instead.
- Do not present historical manual comps as current market prices. Label them `ASSUMED` and explain their intended use.
- Do not create notes with dangling wikilinks. If a target is referenced, create the target note or remove the link.
- Avoid stuffing several unrelated pseudo-pages into one note just to satisfy navigation; use real target notes for stable concepts.
- If existing skills overlap (for example, a domain operations skill and an Obsidian mechanics skill), keep this skill focused on cross-project architecture and verification rather than duplicating detailed commands.

## Supporting reference

See `references/pokemon-market-wiki-setup.md` for the validated Pokémon-market vault pattern and lessons from its initial setup.
