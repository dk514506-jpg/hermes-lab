---
name: persistent-vault-web
description: "Use when keeping one vault and generating a companion site."
version: 1.0.0
metadata:
  hermes:
    tags: [obsidian, vault, static-site, html, documentation, publishing]
---

# Persistent Vault and Web Publishing

## When to use

Use when a user wants an editable Obsidian knowledge base to remain stable across sessions while a readable webpage is generated from the latest notes and operational artifacts.

## Core boundary

Maintain exactly one canonical vault directory. Do not create a new vault for every update and do not make the user repeatedly download replacement archives.

Use three layers:

1. **Canonical editable layer:** one persistent `obsidian-vault/` directory containing Markdown notes, links, templates, and vault configuration.
2. **Operational layer:** SQLite data, scripts, CSV capture templates, and generated reports outside the vault when automation needs structured data.
3. **Presentation layer:** a generated, dependency-free HTML site built from the current vault plus selected operational artifacts.

The webpage is a projection, not a second editable source of truth. Changes to prose and structure happen in the vault; the site is regenerated after changes.

## Workflow

1. Resolve and record the canonical vault path before editing.
2. Inspect the existing vault tree and `Home.md`; preserve its folders and wikilink conventions.
3. Edit notes in place with targeted patches or full-file rewrites only when necessary.
4. Add new notes under the appropriate existing folder and link them from `Home.md` or a relevant index.
5. Generate the webpage from the current vault. Include navigation, status labels, artifact links, and a clear generated timestamp.
6. Keep the webpage self-contained when possible: inline CSS/SVG, no external scripts, no CDN dependencies.
7. Validate that all intended notes are represented, links resolve or are explicitly marked as project-relative, and no stale “not yet built” language remains after the artifact exists.
8. Package or commit the same vault only when requested; do not make packaging the default delivery mechanism.

## Pokémon business application

For the Pokémon market project, the canonical project is the persistent `/opt/data/pokemon-business/obsidian-vault/` directory. The website should unify business overview, operating workflow, store-visit experiment, ticker universe, observation ingestion, Quote Board, inventory, future opportunity screens, research, limitations, and roadmap.

Keep the ticker universe and market observations in structured CSV/SQLite files; link to their workflow notes from the vault.

## Delivery and version control

If a remote repository is available, use it as the durable collaboration home for the same vault and project files. First inspect the authenticated repository, reconcile it with the local project, and avoid silently overwriting either side. Commit changes with a descriptive message and report the commit/branch only after verifying the commit exists.

A downloadable archive may be offered as an optional backup, but it should not be the normal update loop.

## Pitfalls

- Do not generate a fresh Obsidian vault for every session or every revision.
- Do not let the static webpage become a manually edited fork of the notes.
- Do not claim the site is current unless it was regenerated after the latest vault edits.
- Do not expose gitignored database files, secrets, or private source material in a public webpage.
- Do not treat a private GitHub URL returning 404 unauthenticated as proof that the repository does not exist; authenticate and verify before reviewing or syncing it.

## Supporting detail

See `references/persistent-project-layout.md` for the Pokémon-specific layout and synchronization checklist.
