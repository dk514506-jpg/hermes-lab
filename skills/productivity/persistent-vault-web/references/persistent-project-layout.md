# Persistent Pokémon Project Layout

Use one project and one editable vault rather than producing replacement archives.

```text
pokemon-business/
├── obsidian-vault/       # canonical editable Markdown vault
├── web/                  # generated site, if separated from root
├── scripts/              # import/build/verification code
├── templates/            # field-capture and ticker CSVs
├── data/                 # SQLite state; normally gitignored
├── reports/              # generated reports; normally gitignored
├── schema.sql
└── README.md
```

Current local canonical vault: `/opt/data/pokemon-business/obsidian-vault/`.

Synchronization checklist:

1. Read `obsidian-vault/Home.md` and inspect the existing tree.
2. Patch notes in place; preserve folders and `[[wikilinks]]`.
3. Add links for every new note from Home or a relevant index.
4. Generate the HTML projection after edits.
5. Verify the generated site reflects the new note and does not expose secrets, SQLite state, or private material.
6. Offer a tar archive only as an explicit backup, not as the default update loop.
7. If GitHub is authenticated, inspect the remote before syncing and reconcile rather than overwriting.

The webpage is read-only presentation. The vault remains the human editing surface; structured market data remains in CSV/SQLite and is linked from the notes.
