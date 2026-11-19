# Claude AI Developers — Rebuild Plan v2 (Corrected Scope)
Updated 2026-11-15, superseding the v1 plan's "full replacement with new text-only pages" approach.
Site: https://claude-ai-dev.developers-organism.com

## User correction 2026-11-15 — the scope that governs everything now
- Do NOT delete content, images, or the main structure of the website.
- Keep everything the same as the original design / graphical concept: same layout, same sections, same Elementor templates, same images where they fit.
- Change ONLY: keywords, copywriting, and plagiarism removal.
- Adapt images to the new Claude content — do not strip images out, do not replace the design with text-only pages. Where an image literally shows the old offer (SEO / staffing), swap it for a similar-style image from the existing Media Library, keeping the same size, placement and section.
- First recover what was deleted earlier, then do the corrected work.

## Recovery verdict (checked live 2026-11-15, nothing changed during the check)
- Images: YES, recoverable — nothing was deleted from the Media Library. 4,598 items still there, including the old homepage images (testimonial-skip-01/02/03/04, abcdhe-114.jpg, the Pexels photos listed in the sitemap). No media deletion log exists in WP, so a media deletion cannot be proven from a log, but nothing in the library indicates one.
- Old pages: YES, recoverable without a restore. All old pages are still Published (27 published pages total, 1 draft Privacy Policy). They sit behind 14 × 301 redirects in the Redirection plugin. Removing a redirect brings that old page back live at its old URL. The old homepage (post 1957, Elementor-built, 9 revisions) is intact, with its featured image and sections.
- IMPORTANT discrepancy found in the check: the live homepage at / currently renders as the OLD homepage ("Staffing, SEO - California, New York"), not the new Claude homepage, even though the launch report on 2026-11-10 said the homepage had been switched. Do NOT assume the Reading setting is what the launch report said — re-check Settings > Reading before any further homepage work. The image-less pages are the NEW Claude pages reached via menu / redirects (e.g. /claude-ai-development-services/, /hire-claude-ai-developers/).
- Test pages: NO, not recoverable in isolation. test, sample-home, sample-page, html-view-test were permanently deleted on 2026-11-10, Trash is empty. The only copy is inside the UpdraftPlus full backup of 2026-11-09 15:43 UTC (locked, still present: Database, Plugins 148.7 MB, Themes 7.1 MB, Uploads 1.7 GB, Others 584 MB; plus a Jan 22 2026 backup). UpdraftPlus restore is component-level only (Database / Plugins / Themes / Uploads / Others) — there is no restore-only-one-page option. Restoring the Database would overwrite the whole current database, including the 6 new Claude pages, so it must NOT be done as a way to get 4 test pages back. Those 4 pages were test/sample pages with no design content; their loss does not block the corrected work.
- Blog posts: note — the dashboard now shows 5 published posts, not 911. That change came from the separate blog chat (post deletion there), not from this chat's work.

## Corrected plan — Phase by phase
### Phase 0 — Recovery first (do this before any copy change)
1. Re-check Settings > Reading and record which page is actually the homepage now.
2. Remove the 14 redirects for the pages that will be edited in place, so the original pages are live again at their old URLs (old homepage, services, about, contact, etc.). Keep a list of every redirect removed.
3. Verify each original page renders with its original sections and images. Record any image that is actually missing (broken placeholder) — do not assume.
4. Do NOT restore the UpdraftPlus backup. Do NOT delete anything else.

### Phase 1 — Edit in place, keep the design
- Work on the EXISTING pages, in Elementor, keeping each page's template, sections, layout, spacing and image positions exactly.
- Homepage (old, post 1957): keep hero, "Two Ways We Help You Grow", "Who We Are", "Quality Services" (3 photos), "Learn From Our Playbook", "Ready to Transform?", "Our Unique Edge" 01–03, "Happy Clients" testimonials, "Join Us Today", footer.
- Services / About / Contact: same rule — same sections, new words only.
- No new text-only pages as replacements. The 6 Claude pages created 2026-11-09 are to be kept as drafts / unpublished references, or merged into the original pages — decide with the user, do not publish them as a parallel site.
- Menus and footer: keep the structure, change only the labels / contact details that are wrong (Riseup set: contact@riseup-asia.com, +1 204 650 3141, meet.rasia.pro/intro-call, call.rasia.pro/riseup-offical-v1, riseup-asia.com, RISE ASIA LLC, no address, no old +1 914-520-4706).

### Phase 2 — Copy only: keywords, copywriting, plagiarism
- Rewrite headings and body copy on the existing pages for Claude AI developers for US clients: hire Claude developers, Claude Code, AI agents, MCP, RAG, Claude API, evals.
- Offer stays: US companies hiring the team as Claude AI developers. NOT training, NOT consulting, NOT a product.
- Remove plagiarism / old SEO-staffing claims: no "#1 brand", no "guaranteed" ranking, no Lifetime SEO Deal, no "Rank #1 on Google" as a promise.
- Since 2008: only as Developers Organism since 2008 (developers-organism.com), never "Claude since 2008" (Claude launched 2023).
- Proof: Enyx Digital case study ($36,500 vs $120K–$200K/yr hire, 90 days) and the 11 selected works, with the labels kept (Enyx = real client delivery, 2 case studies = research/opinion, 9 works = Alim's past work not with Riseup Asia, 2 = Our Engineers' Work).
- Testimonials Mark Johnson, Sarah Thompson, Lisa Garcia: verbatim text only, no photo for Lisa Garcia until a correct photo is supplied.
- No prices on the site — pricing is still a blank slate, client answers pending. No $500 / $299 anywhere visible or in structured data.
- Per-page originality check: record that each page's new copy was written fresh, and that no old copy was left in place unreviewed.

### Phase 3 — Images, adapted to the new content
- Keep every image that still fits the section (team working, code, office, testimonials).
- Swap only images that literally depict the old offer (e.g. an SEO ranking graphic, a staffing graphic) — swap for a similar-style image already in the Media Library, same placement and size, and record the swap (old filename → new filename, reason).
- Do NOT delete any image from the Media Library. Do NOT upload a new image without checking the library first.
- Alt text: update alt text to the new Claude keywords where the image stays.

### Phase 4 — QA and launch (only after the user approves the edited pages)
- Check every edited page live: sections, images, layout, mobile, contact links, no old phone/address, no prices, no "#1"/"guaranteed", no leftover SEO/staffing copy.
- Check structured data again: SASWP / Yoast Local SEO must show the Riseup contact set, no address, no price. The $500/$299 strings still stored in 34 postmeta + 4 option rows must be handled in the blog chat's scope, not by a blind DB replace here.
- "Discourage search engines" — only uncheck at launch, after QA passes and the user approves.
- Redirects: only re-add a redirect if a page is genuinely removed after the user approves its removal. No redirect is the default.

## What stays out of scope here
- Blog posts (911 → now 5 published, separate blog chat).
- Deleting pages, images, or media.
- Creating new text-only replacement pages.
- Any database restore.
