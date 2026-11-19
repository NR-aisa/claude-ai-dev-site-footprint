# Menus — Main Menu (7), Footer Menu (198)

## What / decisions
- 2026-11-16 (user: "yes fix it"): both menus became Home (front
  page post 1957, /), Services (post 13, /services/), About
  (post 12, /about/), Contact (post 15, /contact/). Hire and Work
  removed from both menus ONLY — drafts NOT deleted/published
  (7 drafts remain). GET STARTED already linked to /contact/,
  BOOK A CALL to meet.rasia.pro/intro-call. Verified live
  logged-in AND logged-out: every header click lands on the clean
  published URL, no ?page_id= anywhere.
- 2026-11-16: Blog (/blog/) added to both menus, order Home /
  Services / About / Blog / Contact, verified live logged-out.

## Why — the investigation
- User screenshot 2026-11-16 showed a plain Services page. It was
  NOT /services/ — it was draft 13511, a plain classic-editor text
  page (176 words, no Elementor, no images/banner, two H1s). The
  header Services menu linked to ?page_id=13511; Hire → draft
  13513; Work/About/Contact → drafts; only Home was the original
  front page. A menu link is not a redirect — the menu item pointed
  directly at the draft; a logged-out visitor would get a 404.
- Menus are all flat — no sub-items anywhere; no menu history in
  wp-admin, so NO evidence any dropdown ever existed. Only record
  would be the 2026-11-09 15:43 backup database, NOT read/restored.

## Raw-URL CTA (same day)
- Exactly 3 published pages, one occurrence each — Home (post
  1957, widget 51c0f17), Services (post 13, widget 9ffeb5f),
  About (post 12, widget 511a3d5) — plain unlinked text "Book a
  call — https://meet.rasia.pro/intro-call — or email
  contact@riseup-asia.com" in a Heading widget. Introduced in the
  Nov 15 rewrite (revisions 13585/13593/13599, by Naimur Rahman).
  Before: no meet link as text; button was "Get Started" →
  /contact/, line under it was a phone line ("OR Call Us:
  +19145204706" Home / "Free Consultation? +19145204706"
  Services, About).
- Fix: all three replaced with "Free Consultation? +1 204 650
  3141" linked tel:+12046503141. Later superseded by Fix 1
  (2026-11-17): "Email us: info@developers-organism.com".
## How to use this folder

1. Read `readme.md` (what/why/decisions), then `evidence.md` (IDs, URLs,
   verification), then `log.md` (step-by-step, including what went wrong).
2. Before editing this area again, make a per-page draft backup first —
   see `tools/wp-preflight-backup/` — and record it in `log.md`.
3. Verify live as a **logged-out visitor** before reporting anything done.
   A signed-in / admin-bar view is not evidence.
