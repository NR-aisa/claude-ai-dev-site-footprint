# Rollback — manual steps

Automatic rollback is deliberately NOT implemented: a live page can
look wrong for a stale-cache reason, and an automatic rollback could
undo a good edit. A human checks first.

1. Open the live page as a **logged-out visitor** (incognito) and
   confirm it is actually broken — not a stale cache. Purge SpeedyCache
   first and reload.
2. Find the draft backup in WordPress: Pages → All Pages → search
   `<Title> - Backup [timestamp]`. Its ID is in the footprint folder's
   `backups.json`.
3. Open the backup draft in Elementor and confirm it holds the
   pre-edit layout (sections, images, copy).
4. Restore: either (a) copy the backup's content back into the live
   page in Elementor and publish, or (b) set the backup draft to
   Published and re-point the menu / Reading setting to it, then delete
   the broken page only after the restored one is verified live.
5. Purge SpeedyCache + Elementor cache, verify live logged-out.
6. Record the rollback in the footprint's `log.md` — what broke, what
   was restored, from which backup ID.
