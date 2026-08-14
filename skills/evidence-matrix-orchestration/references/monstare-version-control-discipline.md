# Version Control Discipline for Evidence Matrix Projects

The user corrected the agent after batches 4-5 for working without version control and creating new chart files instead of editing the matrix in place. This reference captures the correct workflow.

## The problem

After charting 70 rows across multiple batches, the agent had:
- No `.git` repository initialized
- Created new markdown files for each batch (charting_drafts, memos, etc.)
- The canonical Excel matrix was being patched but without any version history
- No remote backup to GitHub

This meant there was no way to track changes, revert mistakes, or collaborate.

## The correct workflow

### 1. Initialize git at project start

```bash
cd /opt/data
git init
git config user.email "agent@nousresearch.com"
git config user.name "Hermes Agent"
```

### 2. Create a proper `.gitignore`

Patterns to include:
```
.cache/
.env
.hermes/
.hermes_history
.local/
.npm/
.ssh/
node_modules/
node_modules
lazy-packages/
lsp/
*.log
```

Verify with `git check-ignore -v <pattern>` that:
- Monstare project files are NOT ignored
- Sensitive files (.env, .ssh) ARE ignored
- Build artifacts (node_modules, .cache) ARE ignored

### 3. Commit after each batch

```bash
git add Monstare_*.xlsx Monstare_*.md Monstare_*.txt
git add Monstare_batch*_sources/ scripts/monstare_*.py
git commit -m "Batch N: [scope] — [rows charted] — [key findings]"
```

### 4. Push to remote

```bash
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin master
```

If `gh` CLI is not available, authentication requires either:
- HTTPS with personal access token (via `git config credential.helper store`)
- SSH key authentication

### 5. The matrix is the operational database — edit in place

The canonical Excel matrix is the single source of truth. Do NOT create new chart files for each batch. Instead:
- Patch the matrix additively (openpyxl, `data_only=False` to preserve formulas)
- Memos and drafts are continuity frames, NOT replacements for the matrix
- Each patch is a commit; each commit is a recoverable state

## Lesson learned

The user expected version control from the start. The agent should have:
1. Initialized `.git` before any work began
2. Set up `.gitignore` to protect sensitive files
3. Committed the initial state
4. Pushed to the remote repo
5. Committed after each batch

This is now a first-class project setup requirement, not an afterthought.
