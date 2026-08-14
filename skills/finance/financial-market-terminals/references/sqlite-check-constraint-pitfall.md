# SQLite CHECK Constraint Ordering Pitfall (3.53.4)

**Evidence label:** VERIFIED — reproduced against SQLite 3.53.4 via in-memory test; fix applied to `schema_terminal.sql` and confirmed working.

**Status:** 2026-08-13 — captured. This is a provider/environment quirk, not a durable rule. When the environment upgrades SQLite, recheck.

## Symptom

A `CREATE TABLE` statement with a table-level `CHECK` constraint followed by more columns fails with a generic parse error:

```
sqlite3.OperationalError: near "TEXT": syntax error
```

The error points at the first column *after* the `CHECK` constraint, not at the `CHECK` itself. This makes the root cause hard to spot by reading the error alone.

## Reproduction

```sql
CREATE TABLE t (
    id INTEGER PRIMARY KEY,
    x TEXT,
    CHECK ((x = 'raw' AND y IS NULL) OR (x = 'graded' AND y IS NOT NULL)),
    y TEXT
);
```

In SQLite 3.53.4 this fails with `near "y": syntax error`.

## Root cause

In SQLite 3.53.4, a table-level `CHECK` constraint at the end of the column list is treated as the end of the column definitions. Any columns declared after it are parsed as stray tokens outside the column list, producing a generic syntax error. The column order in the `CREATE TABLE` statement matters: the `CHECK` must appear *after* all columns it references, with no columns following it.

This is a parser limitation in this SQLite version, not a SQL standard violation. Newer SQLite versions may handle it differently — recheck when the environment upgrades.

## Fix

Move the trailing columns *above* the `CHECK` constraint:

```sql
CREATE TABLE t (
    id INTEGER PRIMARY KEY,
    x TEXT,
    y TEXT,
    CHECK ((x = 'raw' AND y IS NULL) OR (x = 'graded' AND y IS NOT NULL))
);
```

## What was fixed in this session

`/opt/data/Pokemans/schema_terminal.sql` had `terminal_instruments` defined with `tier`, `active_from`, `active_to` declared *after* a table-level `CHECK` constraint on `(condition_type, raw_condition, grader, grade)`. The fix moved those three columns above the `CHECK`, and also moved `created_at` above the `CHECK` (it was after too).

Before:
```sql
    era TEXT,
    CHECK ((condition_type = 'raw' AND raw_condition IS NOT NULL AND grader IS NULL AND grade IS NULL)
        OR (condition_type = 'graded' AND grader IS NOT NULL AND grade IS NOT NULL AND raw_condition IS NULL)
        OR condition_type = 'unknown')),
    tier TEXT,
    active_from TEXT,
    active_to TEXT,
    created_at TEXT NOT NULL,
```

After:
```sql
    era TEXT,
    tier TEXT,
    active_from TEXT,
    active_to TEXT,
    created_at TEXT NOT NULL,
    CHECK ((condition_type = 'raw' AND raw_condition IS NOT NULL AND grader IS NULL AND grade IS NULL)
        OR (condition_type = 'graded' AND grader IS NOT NULL AND grade IS NOT NULL AND raw_condition IS NULL)
        OR condition_type = 'unknown'),
```

## Diagnosis pattern

When a `CREATE TABLE` fails with a vague `near "X": syntax error` where `X` is a column name that looks perfectly fine:

1. Check if there's a table-level `CHECK` (or `FOREIGN KEY` or `UNIQUE` at table scope) before column `X` in the statement.
2. Try moving columns after that constraint to before it.
3. Test in an isolated in-memory DB: `sqlite3.connect(':memory:').execute(sql)`.
4. Also test with `executescript()` vs `execute()` — `executescript()` splits on `;` and can fail on comments containing semicolons (a separate pitfall: a comment like `-- foo; bar` breaks `executescript()` because the semicolon terminates the statement early).

## Related pitfalls

- **Comment semicolons and `executescript()`:** `executescript()` splits the input on `;` and executes each piece. A comment containing a semicolon (`-- Design artifact: raw observations remain immutable; analytics are projections.`) becomes two statements, and the second half (`analytics are projections.`) is not valid SQL. Fix: rephrase the comment to avoid semicolons, or use `execute()` for single statements. This was a second bug found in the same `schema_terminal.sql` during this session.

## Verification

For schema artifacts:

1. Execute the SQL in an isolated in-memory SQLite DB (`sqlite3.connect(':memory:')`).
2. Assert required tables exist.
3. Insert representative rows that exercise the CHECK constraint (both `raw` and `graded` rows).
4. Confirm constraints reject invalid rows (e.g. `graded` row with `raw_condition` set, or `raw` row with `grader` set).

Call this **ad-hoc verification** unless the canonical suite also ran.

## See also

- `pokemon-tcg-business-ops/references/psa-json-archive.md` — the PSA archive that exercised this schema.
- `financial-market-terminals/SKILL.md` — the class-level terminal-building workflow and verification guidance.
