# result-logger — Result[T] + structured logger + --dry-run

Taken from: `prompts/source/python-any-task-master-prompt.md`
(modules `app_errors.py`, `task_logger.py`, CLI `--dry-run` pattern).

## What it is

A small, dependency-free Python pattern for scripts that change things
(delete / replace / purge / backfill): every operation returns a
`Result` — success with a value, or a typed `AppError` — never a silent
half-failure; every step is logged to console (ANSI badges) and to a
JSON audit log; `--dry-run` previews the exact changes without mutating
anything.

## What was taken, what was left out

- Taken: `Result[T]` / `AppError`, the dual-channel logger
  (`[  OK  ]` / `[ FAIL ]` / `[ WARN ]` / `[ INFO ]` / `[ SKIP ]` /
  JSON audit lines), the `--dry-run` flag, positive booleans
  (`is_dry_run`), exit codes.
- Left out: the 400-step budget, 3 subagents, task-folder scaffolding
  mandates, the Windows-only handlers (audio restart, VMware, WhatsApp
  cache), the SQLite audit DB (a plain JSON-lines log file is enough
  here), the "never run ad-hoc shell" rule.

## Why it matters here

This project's destructive operations failed silently before: the
1,005-post blog deletion (2026-11-10) had no per-item preview; Search &
Replace runs in Fix 1 (2026-11-17) "showed completed" but did not persist
until retried with a 90-second wait. A `--dry-run` first, plus an audit
log of exactly which rows changed, would have caught both.

## Files

- `app_errors.py` — `Result` / `AppError`
- `task_logger.py` — `TaskLogger`
- `demo.py` — runnable demo: `python3 demo.py --dry-run`, then
  `python3 demo.py` (writes only to a temp dir)

## Test

```sh
python3 -m py_compile app_errors.py task_logger.py demo.py
python3 demo.py --dry-run
python3 demo.py
```
