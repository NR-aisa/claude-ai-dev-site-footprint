# Blog — `/blog/`

## What
Blog listing (posts page) + the WP Auto Blog 30-day plan. Blog
scheduling itself lives in a separate chat ("Claude AI Blog –
30-Day Auto Blog Plan", chat 19e5ad3f); this folder records only
what was done to the blog from the site side.

## Why / decisions
- 2026-11-10: Phase A — UpdraftPlus backup re-confirmed, WXR
  export 41.4 MB saved, then 1,005 posts permanently deleted
  (911 published + 89 drafts + 5 trash). Pages untouched.
- WP Auto Blog un-paused 2026-11-10 (Post Status Draft → Publish).
  Day 1 published 2026-11-10, ~2,900 words (over the 1,200–1,800
  plan), fixed and verified. Days 2–30 scheduled Nov 11–Dec 9 at
  09:00 (WordPress UTC+0; WP Auto Blog shows no timezone — schedule
  runs on UTC, landing 04:00 New York, NOT 09:00 New York).
- Authors (user rule 2026-11-16, supersedes the 2026-11-10
  rotation): do NOT use Naimur Rahman as a blog author; use foreign
  names, keeping Alim Karim. 8 new Author-role users created
  (IDs 55–62, @developers-organism.com): Mark Johnson, Sarah
  Thompson, Lisa Garcia, James Carter, Emily Davis, Michael Brown,
  Jessica Wilson, David Miller. Assignments Nov 10–16: Mark,
  Sarah, Lisa, Alim, James, Emily, Michael. Jessica Wilson and
  David Miller have 0 posts yet, next in rotation. For those
  Nov 10–16 assignments Naimur appears as author on NO post —
  but see Open below: the Nov 17–19 posts published through
  WP Auto Blog have since shown blank/Naimur bylines, so do not
  read this as "no post anywhere".
- Author photos: Gravatar only — no upload field on this site, no
  author box on post pages (byline shows small circular avatar).
  Alim Karim and Abidul Shaon have real Gravatar photos; the 8
  foreign names have none (all Gravatars return 404). See
  `author-photos/` in this folder.
- Blog listing (Fix 3, 2026-11-17): Masonry and Highlight First
  Post turned OFF in Astra Customizer; CSS equal-height cards with
  title/excerpt ellipsis (full text stays in HTML for crawlers).

## Open / awaiting user
- Day 7 ("Getting Started with Claude Code", published 2026-11-17
  09:00 UTC): blank byline on /blog/ + leaked WP Auto Blog prompt
  line in its body (contact@riseup-asia.com / +1 204 650 3141).
  Fix offered (author Jessica Wilson + body cleanup), awaiting yes.
- Day 8 ("Claude Agent SDK Explained", published 2026-11-18
  09:00 UTC): same leaked line (line 225), blank byline; /blog/
  now shows Day 7 bylined Naimur Rahman instead of blank (reason
  unknown — do not claim one).
- WP Auto Blog prompt fix offered 2026-11-18 (email →
  info@developers-organism.com, drop the WhatsApp number, leave
  Schedule a Call alone), awaiting yes. If approved it stops Day 9
  (2026-11-19) leaking; it does not fix live Day 7/8.
- 2026-11-19 post ("Building AI Agents with Claude: From Prompt
  to Production Feature", published 2026-11-19 09:00 UTC): the
  same leaked line is live in its body — verified by text crawl
  2026-11-19 10:22 UTC (line 216: "Schedule a Call
  https://meet.rasia.pro/intro-call, email
  contact@riseup-asia.com, WhatsApp +1 204 650 3141."). Byline
  rendering is inconsistent between checks: a visual logged-out
  check at 09:22 UTC read "By Naimur Rahman", while the 10:22 UTC
  text extraction of /blog/ shows "By" with no name. Re-check
  visually before any author change; do not claim one byline
  from text extraction alone. Next scheduled post: 2026-11-20
  09:00 UTC. The correct author for the Nov 19 post is NOT
  recorded (rotation after David Miller is not established).
  Day-number note: tracking calls Nov 19 "Day 9"; the 30-day
  plan file lists it as Day 10 — use date + title.
- Days 6–30 move from 09:00 to 14:00: user said "ok start"
  2026-11-15 — read as go-ahead for the time move, NOT as approval
  of the recovery step. (Blog-chat scope.)
## How to use this folder

1. Read `readme.md` (what/why/decisions), then `evidence.md` (IDs, URLs,
   verification), then `log.md` (step-by-step, including what went wrong).
2. Before editing this area again, make a per-page draft backup first —
   see `tools/wp-preflight-backup/` — and record it in `log.md`.
3. Verify live as a **logged-out visitor** before reporting anything done.
   A signed-in / admin-bar view is not evidence.
