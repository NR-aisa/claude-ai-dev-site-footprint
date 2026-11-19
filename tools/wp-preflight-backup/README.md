# wp-preflight-backup — per-page draft backup before editing

Taken from: `prompts/source/wordpress-elementor-modernization-prompt.md`,
§5 "Zero-Data-Loss Pre-Flight Backup & Automated Rollback Protocol".

## What it is

Before ANY Elementor edit to a live page on
`claude-ai-dev.developers-organism.com`, clone that page as a **draft
backup** (`<Title> - Backup [YYYY-MM-DD HH:mm:ss]`) via the WordPress
REST API, and save the full postmeta (especially `_elementor_data`) to
`backups.json` in the footprint folder for that page. If the edit fails
or the live page looks wrong afterwards, restore from the draft clone —
do not rebuild from memory.

## What was taken, what was left out

- Taken: the pre-flight draft-clone idea, the `backups.json` record,
  the rollback-first mindset.
- Left out: the "halt unless the Python prompt ran first" gate; the
  temp-SQLite / RSA credential machinery (see Credentials below); the
  automatic instant-rollback script (rollback here is manual and
  deliberate — a human checks the live page first, because an automatic
  rollback could undo a good edit that only *looked* wrong in a stale
  cache).

## Why it matters here

This is the one real gap in how the site was worked on in Nov 2026.
The project has a locked UpdraftPlus full backup (2026-11-09 15:43 UTC)
but no per-page backup. Consequences already felt:

- The 4 test pages deleted at launch (2026-11-10) are only recoverable
  from the full backup, whose database restore would overwrite the
  whole current site — so they are effectively unrecoverable.
- The transparency page (post 9906) footer never rendered live, with no
  per-page backup to compare against.
- Every Design A rebuild step (2026-11-18/19) edited post 1957 in
  place with no draft clone to fall back on.

## Credentials

**None stored anywhere.** The script takes the site URL, username and
Application Password from environment variables
(`WP_SITE_URL`, `WP_USER`, `WP_APP_PASSWORD`) at run time only.
Credentials come from the Secure Vault / the operator's own WordPress
profile (Users → Profile → Application Passwords). Never put them in a
file, in git, or in chat. The normal WordPress password is never used
for API work.

## Files

- `backup_page.py` — clone a page/post as a draft backup + save postmeta
  to `backups.json`. Supports `--dry-run` (lists what it would back up).
- `rollback.md` — manual rollback steps.

## Usage

```sh
WP_SITE_URL=https://claude-ai-dev.developers-organism.com \
WP_USER=naimur.rahman WP_APP_PASSWORD='xxxx xxxx xxxx xxxx xxxx xxxx' \
python3 backup_page.py --page-id 1957 --out footprints/homepage/backups.json --dry-run
python3 backup_page.py --page-id 1957 --out footprints/homepage/backups.json
```
