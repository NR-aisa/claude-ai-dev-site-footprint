# Homepage — log

- 2026-11-09: Audit. Homepage entirely Local SEO + American Staffing,
  no Claude mention. 25 pages in sitemap.
- 2026-11-09/10: 6 new text-only Claude pages created as drafts
  (Home 13509). Published 2026-11-10, homepage switched, 14 redirects,
  4 test pages permanently deleted, search block UNCHECKED.
- 2026-11-15 11:11–11:15: Recovery check (read-only). Media Library
  intact (4,598 items); old pages still Published behind redirects;
  live homepage rendered as the OLD homepage, not the new one.
- 2026-11-15 15:13–15:23: Recovery Step 1. All 15 redirect rows
  disabled (Delete was inert, Disable worked); 6 new pages moved to
  Draft (Published 27→21, Drafts 1→7). All 7 original URLs verified
  loading original pages with images.
- 2026-11-15 15:23–15:52: Plan v2 in-place edit (see readme.md).
- 2026-11-15 16:37–16:40: QA core 4 pages — Home/Services/About
  passed; Contact failed only inside the TidyCal embed.
- 2026-11-16 22:49–23:09: Padding investigation (read-only). Cut-off
  reproduced only at 1025–1150px / 1366px at 110–125% zoom.
- 2026-11-17 14:19–14:30: Padding re-check, focused on padding only.
  Only non-zero horizontal padding is c36f822's 33px; row is
  border-box 1200px. Proposed fix: 33px → 10–16px + wrap/gap.
- 2026-11-17 17:14–17:23: Fix 2 applied (see evidence.md). Verified
  live logged-out at desktop; narrow widths in Elementor device
  previews, NOT a resized live window.
- 2026-11-17 20:12: "ok update" — AI-changed images applied
  (see footprints/images/).
- 2026-11-18: Hero banner moved to top, 18px → 52px. Verified live.
- 2026-11-18 23:31–2026-11-19 00:09: Design A hero rebuild. Hero
  background: dark laptop photo removed, white #FFFFFF, overlay 0.
  Banner dark navy #0F2040 Ubuntu 52px (white box now invisible on
  white). Eyebrow purple #7C3AED 15px/600/uppercase. H1 navy with
  "Claude AI Developers" in purple. Intro dark slate #334155
  Poppins 15px. Two pill CTAs added. Lavender results panel added.
  Book A Call card: white, 20px radius, soft shadow; Align Items
  → Start fixed full-height stretch (first attempt hit the wrong
  container and had no effect). Verified live logged-out.
- 2026-11-19 00:09–00:37: Design A sections 2–4 (see log in
  footprints/homepage — Two Ways equal white cards; Who We Are white
  card, photo 20px radius + shadow, "WHO WE ARE" lavender pill,
  READ MORE gradient pill; Quality Services white cards, 01/02/03
  purple badges, chevrons → purple checkmarks). Note: Who We Are has
  no 2×2 grid (only one Icon Box) — none invented. Verified live
  logged-out.
- 2026-11-19 00:37–01:16: Design A sections 5–8 + footer (Unique
  Edge white cards on navy panel; Happy Clients equal white cards,
  quote row at bottom of card; Join Us Today navy block; footer
  #10668 dark navy, logo in white badge — plain Background Color
  did not render, so navy applied via Background Overlay 100% +
  Custom CSS override). Verified live signed-in (limitation noted
  in evidence.md); /services/ spot-checked for the footer.
