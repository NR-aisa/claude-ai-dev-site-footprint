# Leftover pages

Pages edited in place per Plan v2 (user 2026-11-15: "do the leftover
pages done properly according to the master plan").

## What
- `/sales-with-seo/` → "Grow Sales with Claude AI" — hero, About,
  3 benefit cards, Who This Is For, FAQ, 3 steps rewritten; form
  and TidyCal untouched; no image swaps.
- `/virtual-assistant-for-ceos/` (post 9607) → "Claude AI Assistant
  for CEOs" — a Claude AI assistant (drafting, summarising, meeting
  notes, inbox triage), explicitly NOT a human assistant;
  "$8,000/week" claim removed; robot Lottie kept; form/TidyCal
  untouched.
- `/careers/` (post 12595) → "Careers — Join Developers Organism"
  — listings kept.
- 4 form pages rewritten around forms only (fields untouched):
  Apply (7937), Hiring Form (10997), Job Test (11144), Thank You
  (9819).
- Transparency page — real page is post 9906, slug
  `/why-our-seo-claim-is-crazy-for-ranking-number-1/` (the old-plan
  slug is a 404, no such page exists). Retitled "How We Work with
  Claude — Transparent and Production-First"; copy rewritten;
  #1/guaranteed/$50/$5,000/old phone/email/Sheridan removed;
  BOOK A CALL → meet.rasia.pro/intro-call; WHATSAPP NOW renamed
  CALL NOW → call.rasia.pro/riseup-offical-v1; YouTube "#1 on
  Google" video widget and Ahrefs slider widgets removed as widgets
  (files stay in Media Library).

## Unresolved — transparency page footer (post 9906)
Live page shows no site footer, no in-content footer, and STEP 3
missing live (STEP 1/2 only appear after scrolling). Tried:
template Default→Full Width (lead form now renders), Disable
Footer No, footer #10668 Entire site/Published, all WP caches
purged. Likely stale edge cache above WordPress (no Cloudflare API
key to purge) and/or unsaved Elementor preview changes, or a
WPCode/HFCM snippet that could not be checked (access denied).
Needs host/Cloudflare purge or owner re-publishing footer #10668.

## Design notes
- Sales With SEO (7753) and Virtual Assistant (9607) are Elementor
  Canvas landing pages by design — no Astra header/footer, own
  in-content footer/TidyCal — left as-is.
- Hiring and Job Test are near-duplicates (same H1, same 9-step form).
- Career forms: Bit Form id 2 (Apply) and Elementor Pro Form
  (Hiring/Job Test) — "WordPress + SEO Specialist" → "Claude AI
  Developer"; levels → Claude AI Developer
  (Novice/Intermediate/Expert); H1 overlap fixed (animation off,
  bottom margin 0→20px); footer fixed on Apply and Job Test
  (Canvas→Full Width). Apply shows a duplicated in-content logo
  under the header — left in place.
## How to use this folder

1. Read `readme.md` (what/why/decisions), then `evidence.md` (IDs, URLs,
   verification), then `log.md` (step-by-step, including what went wrong).
2. Before editing this area again, make a per-page draft backup first —
   see `tools/wp-preflight-backup/` — and record it in `log.md`.
3. Verify live as a **logged-out visitor** before reporting anything done.
   A signed-in / admin-bar view is not evidence.
