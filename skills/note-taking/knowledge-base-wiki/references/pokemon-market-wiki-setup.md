# Validated Pokémon Market Wiki Setup

## Context

The Pokémon business already had an executable project at `/opt/data/pokemon-business/` containing SQLite data, scripts, generated reports, a marketplace design memo, and a static HTML wiki. The Obsidian vault was added as a separate human-edited knowledge layer rather than replacing those artifacts.

## Durable layout

```text
pokemon-business/
├── data/                       # operational SQLite source of truth
├── reports/                    # generated weekly outputs
├── scripts/                    # executable tracker pipeline
├── wiki/index.html             # static read-only HTML wiki
├── marketplace-design.md       # design memo
└── obsidian-vault/             # editable linked knowledge base
    ├── .obsidian/
    ├── 00 Inbox/
    ├── 01 Operations/
    ├── 02 Market Intelligence/
    ├── 03 Research/
    ├── 04 Reference/
    └── 05 Templates/
```

## Initial note set

- `Home.md`
- `01 Operations/Business Overview.md`
- `01 Operations/Operating Workflow.md`
- `02 Market Intelligence/Marketplace Tracker.md`
- `02 Market Intelligence/Data Model.md`
- `02 Market Intelligence/Observation Workflow.md`
- `02 Market Intelligence/Seed Observations.md`
- `02 Market Intelligence/Sources and Limitations.md`
- `03 Research/README.md` plus root `Research.md` for stable wikilink resolution
- `04 Reference/Project Artifacts.md`
- `05 Templates/Market Observation.md`
- root `Roadmap.md` for stable wikilink resolution

## Important data lesson

Historical manual extraction records were copied into a seed note only as `ASSUMED`. The source rows included Base Set Charizard HP, Base Set Blastoise MP, Dark Charizard LP, Iono NM, Charizard ex SIR NM, and Pikachu VMAX TG NM. They are UI/test fixtures, not live quotes. A future price terminal needs dated observations, buylist values, provenance, and multiple points before showing momentum or volatility prominently.

## Verification recipe

1. Parse `.obsidian/app.json` and `.obsidian/appearance.json` as JSON.
2. Enumerate Markdown notes.
3. Extract `[[target]]` links and resolve by exact path or unique basename.
4. Assert the seed note contains all six tickers and `ASSUMED`.
5. Assert the observation template contains date, card, set, condition, market comp, buylist comp, source, and evidence label.
6. Package with an available archive tool and list/test the archive.

The first implementation used a Python verification probe and `tar -czf` because `zip` was not available. The durable lesson is to use an available archive alternative, not to treat the missing utility as a product limitation.

## Delivery pattern

For the hosted Hermes dashboard, raw paths are not enough. Deliver the managed-file download URL using the relative path under `/opt/data`, for example:

```text
https://<HERMES_DASHBOARD_PUBLIC_URL>/api/files/download?path=pokemon-business/pokemon-market-obsidian-vault.tar.gz
```

## Follow-up direction

After vault setup, build the first static marketplace page from the seed universe and SQLite schema. Keep the page read-only/generated and the Obsidian vault editable. Add live APIs only after access and source terms are confirmed.
