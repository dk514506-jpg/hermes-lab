# Obsidian Vault Verification

Use this after creating or modifying a vault. It is intentionally a compact recipe rather than a session-specific transcript.

## Checks

1. Parse `.obsidian/app.json` and `.obsidian/appearance.json` as JSON.
2. Confirm conservative settings:
   - `alwaysUpdateLinks: true`
   - `attachmentFolderPath` points to the intended inbox attachment folder
   - new notes use the intended inbox folder
   - `useMarkdownLinks: false` if wikilinks are the convention
   - a valid accent color and theme
3. Recursively enumerate `*.md` notes and require a meaningful minimum for the intended scope.
4. Extract `[[Target]]` links. Resolve each target by exact path (`Target.md`, including nested target paths) or by unique note basename.
5. Confirm project pointers (`../wiki/index.html`, reports, database, design docs) exist if the vault promises them.
6. Check that the vault contains no secrets, credentials, SQLite database, or generated output copied in by accident.

## Important distinction

A Python validation script that parses files and asserts structure is **ad-hoc verification** unless the repository has a canonical test suite that includes the vault. Report that distinction honestly.

## Known failure and fix

When a link validator reports missing root targets such as `Research` or `Roadmap`, add stable root landing notes (`Research.md`, `Roadmap.md`) rather than relying only on nested pages. This makes the vault easier to navigate and makes link resolution deterministic across tools.

## Example configuration shape

```json
{
  "alwaysUpdateLinks": true,
  "attachmentFolderPath": "00 Inbox/Attachments",
  "newFileLocation": "folder",
  "newFileFolderPath": "00 Inbox",
  "useMarkdownLinks": false
}
```
