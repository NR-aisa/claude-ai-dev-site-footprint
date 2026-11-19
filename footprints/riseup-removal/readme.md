# Riseup removal — Fix 1, follow-up, orphan rows, cpubenchmark

## Why
Client feedback relayed by the user 2026-11-17 (in Bengali, user
asked "try to understand the feedback of the client"): the site
must be Developers Organism brand ONLY — no Riseup Asia name,
phone, contact or link anywhere. SEO reason, in the client's
words: if Google understands the two companies have the same
owner, a link from Riseup to Developers Organism gives no ranking
value. Name "Riseup Asia" must not be written here at all.
Schedule a Call: leave aside, deal with last. Email: Developers
Organism's (info@developers-organism.com).

## What was done — Fix 1 (2026-11-17 14:37–17:14)
Search & Replace across wpmy_posts + wpmy_postmeta plus Elementor
edits. "Riseup Asia LLC" → "Developers Organism" (198 rows);
"RISE ASIA LLC" → "Developers Organism" (36 rows); "Riseup Asia"
→ "Developers Organism" (193 rows); "contact@riseup-asia.com" →
"info@developers-organism.com" (95 rows); "alim.karim@riseup-
asia.com" → "info@developers-organism.com" (99 postmeta rows —
form notification recipients, changed to preserve form function);
"Free Consultation? +1 204 650 3141" → "Email us:
info@developers-organism.com" (78 rows); "tel:+12046503141" →
"mailto:info@developers-organism.com" (85 rows — blanket
conversion; footer/Contact phone items then truly deleted in
Elementor; old posts retain empty mailto links where phone text
was removed); "+1 204 650 3141" removed (56 rows); "riseup-asia.com"
→ "developers-organism.com" (360 rows); "riseup-pro.com" →
"developers-organism.com" (66 rows); Call Now links
("riseup-offical-v1", "wa-office", "call.rasia.pro") → 
meet.rasia.pro/intro-call. Footer #10668: Website, Call Now,
Phone/WhatsApp and Riseup LLC rows deleted; only Email and
Schedule a Call remain. Contact post 15: "Visit Riseup Asia
Contact" button and Phone/WhatsApp Icon Box deleted. Yoast Local
SEO: business phone cleared, email → info@developers-organism.com.
Verified live on Home, Services, About, Contact and /blog/ after
cache purge — no visible Riseup/phone/call.rasia.pro in page copy
or footer. (Live check was signed-in, plus REST/cache-bust
confirmation.)

## Lesson recorded
The Search & Replace plugin's chunked DB writes are aborted by an
immediate page reload after clicking Yes; several replacements
that first "showed Processing completed" did NOT persist. Retrying
and waiting 90 seconds after clicking Yes before reloading made
them persist (verified via REST API).

## Fix 1 follow-up (2026-11-17 17:40–19:04)
Targeted replacements only: "RiseUp Asia" → "Developers
Organism" (12 rows); "Meet Riseup-Asia" → "Meet Developers
Organism" (49 rows); "Riseup-Asia:" → "Developers Organism:"
(49 rows); "riseup-asia." → "developers-organism." (61 rows,
image filename repaired back); "riseup-seo.com" → 
"developers-organism.com" (12 rows); "Riseup Seo Services" →
"Developers Organism Services" (11 rows); "Riseup SEO" →
"Developers Organism SEO" (10 rows); "Team Riseup" → "Team
Developers Organism" (2 rows); "#RiseupAsia" →
"#DevelopersOrganism" (41 rows). Final count then: 134 "riseup"
rows (121 postmeta + 13 posts) — 89 actionable, 4 encoded
copyright, 41 image-file rows left alone on purpose.

## "ok update" pass (2026-11-17 ~20:12, ran 1h 50m)
Plain "Riseup-Asia" → "Developers Organism" via targeted variants
(blanket preview showed it would rename image files, so NOT run);
"RiseUp Pro" → "Developers Organism Pro" (40 rows, incl.
"Riseup Pro Mentorship" → "Developers Organism Pro Mentorship").
Final: 45 "riseup" rows remain — 41 logo filenames/URLs, 4
encoded copyright rows. AI-changed images applied (see
footprints/images/).

## Orphan rows — DELETED 2026-11-18
The 4 encoded rows (meta_ids 78421, 78430, 78440, 78449) were
_ elementor_data for posts 7818–7821, which no longer exist —
orphaned postmeta, no template to open in Elementor, plugin
cannot match "%". UI fix attempted and failed 2026-11-17. User
approved "ok" 2026-11-18; rows deleted by meta_id after
re-verification (each 1 row). "riseup" in wpmy_postmeta
95 → 91 rows.

## Left untouched on purpose (needs user decision if ever changed)
Image filenames with "riseup"; CSS classes
(".seo-links-container-riseup", ".seo-inner-head-riseup");
heading anchor IDs; post title "riseup asia online" (post 5634);
post slug "riseup-asia-seo-services" (post 1760 — changing a live
slug needs a redirect); Swiy short links
"swiy.co/riseup-boya-mic-v1-81", "swiy.co/riseup-cv-par-format-v1";
Switchy "hi.switchy.io/riseup-whatsapp-v1-9013"; Abidul Shaon's
Person-schema sameAs "https://riseup-seo.com" (his personal site,
not company branding). Yoast Organization legal name typo
"Developers Organsim" (out-of-scope note).

## OPEN — cpubenchmark links (awaiting user pick)
See evidence.md. Do not edit until the user picks a destination.
## How to use this folder

1. Read `readme.md` (what/why/decisions), then `evidence.md` (IDs, URLs,
   verification), then `log.md` (step-by-step, including what went wrong).
2. Before editing this area again, make a per-page draft backup first —
   see `tools/wp-preflight-backup/` — and record it in `log.md`.
3. Verify live as a **logged-out visitor** before reporting anything done.
   A signed-in / admin-bar view is not evidence.
