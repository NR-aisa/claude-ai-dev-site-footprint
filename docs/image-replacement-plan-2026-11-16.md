# Claude AI Developers — Image Replacement Plan (High Level)
Site: https://claude-ai-dev.developers-organism.com/
Date: 2026-11-16
Status: PLAN ONLY — no images replaced yet. User approval needed before execution.

## Goal
Replace only the images that do not fit the new site — Claude AI developers for US clients hiring the team — with images that fit the page's actual content, section by section. Keep the design, layout, templates and image placements exactly as they are. Change the picture, not the page.

## What "fits" means here
An image fits if it passes all five:
1. **Subject matches the copy next to it** — e.g. a Claude Code section shows a developer working with code / an AI coding tool, not a generic SEO chart or a staffing meeting.
2. **It looks like real work, not a stock cliché** — real developers, real desks, real screens with code, no fake handshakes, no shouting into phones, no "growth arrow" clip art.
3. **It looks like the US client audience** — professional, modern office / remote-work setting, diverse team, clean and credible for a hiring decision.
4. **It is realistic, not AI-looking** — unretouched skin, natural light, grain, fabric, imperfect depth of field. When the bar is "must not look generated", a darkened real photo beats a perfect generation.
5. **No leftover old offer in the frame** — no SEO dashboards, no "#1 on Google", no staffing/recruitment imagery, no old branding, no readable text that contradicts the new copy.

## Current state (from the 2026-11-15/16 live checks)
- Media Library is intact: 4,598 items, including the old homepage / Pexels photos. Nothing was deleted, so most replacements can come from images already in the library.
- Most pages were edited in place, keeping their original images. That means many images are still the OLD images, now sitting next to NEW Claude copy.
- Known image spots:
  - **Home (post 1957):** hero + Who We Are + 3 service cards + Playbook / Enyx + testimonials (Lisa Garcia photo already removed) + Join Us.
  - **Services (post 13):** 5 numbered rows, 4 distinct images — 01 Claude Code, 02 AI Agents, 03 Claude API (reuses the 02 image), 04 MCP & RAG, 05 Evals. Same image reused for 02 and 03 is a known weakness.
  - **About (post 12):** team / working photos, alt text already fixed (posts 1972, 1973).
  - **Contact (post 15):** mostly text + form + TidyCal; little imagery to replace.
  - **Grow Sales with Claude AI (/sales-with-seo/):** hero + benefit cards.
  - **Claude AI Assistant for CEOs (/virtual-assistant-for-ceos/):** robot Lottie kept — that one fits, do not replace.
  - **Sales Growth with Claude AI (/sales-growth-with-seo/):** hero photo of diverse developers working on software — already fits, keep.
  - **Landing Page for Leads (/landing-page-for-leads/):** hero meeting photo — fits, keep unless a stronger one is found.
  - **Careers / Apply / Hiring / Job Test:** form pages, minimal imagery; a team-working photo at the top would fit, nothing else needed.
  - **How We Work with Claude (post 9906, transparency page):** no footer rendering live (separate blocked issue); images here should show process / code review / evals, not SEO metrics.
  - **Footer:** Dev logo + social icons only, no photo to replace.

## Phase 1 — Audit (read-only, 1 pass)
For every published page, list each image with: page, section, current file name, what it actually shows, what the copy next to it says, and a verdict: KEEP / REPLACE / REMOVE.
- Verdict REPLACE only if the image literally shows the old SEO / staffing offer, or clearly contradicts the new copy.
- Verdict REMOVE only if no fitting image exists and the section looks better with no image than with a wrong one (rare — prefer REPLACE).
- Record the audit in a table; user approves the REPLACE list before any swap.

## Phase 2 — Image briefs, per page (the core of the plan)
Each replacement gets a one-line brief before sourcing: subject, setting, people, screen content, mood, and what to avoid. Draft briefs:

### Home
- Hero: one developer at a desk, laptop with code + a Claude-style AI panel, calm focused work, warm imperfect light. Not a team posing at a camera.
- Who We Are: two developers discussing code at a monitor, pointing at real code, blinds / office background.
- Service cards (3): (a) Claude Code — close on hands + keyboard + code on screen; (b) AI Agents — a workflow / agent running tasks on a monitor, one person watching; (c) Claude API & RAG — documents / data flowing into a code view, no charts.
- Playbook / Enyx: keep the existing project image if it shows real product work; if it shows SEO, replace with a law-tech / document-drafting desk scene.
- Testimonials: no photos — text only, as now. Do not re-add Lisa Garcia's old photo.

### Services (5 rows — each row needs its OWN image)
- 01 Claude Code Development: developer writing code with an AI assistant panel visible.
- 02 AI Agents: an agent/automation running — monitor with a task list / workflow, person supervising, not touching the keyboard.
- 03 Claude API Integration: API / code connecting to a product — screen with code + a simple app UI. Must be a DIFFERENT image from 02.
- 04 MCP Servers & RAG: documents / knowledge base feeding into a search or chat view.
- 05 Evals & Production Support: code review / testing — two people reviewing a screen, or a test-results screen.

### About
- Team at work: real team, working normally, no posed group photo, no one leaning over anyone.
- Journey / Since 2008: an older office / early-team photo if one exists in the library; otherwise a timeless desk-and-code shot. Do not fake a 2008 photo.

### Grow Sales with Claude AI + Sales Growth with Claude AI
- Hero: a developer + a client-facing dashboard / sales workflow on screen, not a generic "sales growth" chart.
- Benefit cards: Claude Code tools, AI agents, evals — same subjects as Services, different crops/angles so the site does not repeat the same photo.

### Claude AI Assistant for CEOs
- Keep the robot Lottie. No photo replacement needed. If a photo is added, it should be a CEO/executive at a desk with a laptop summarising a meeting — not a human assistant.

### Careers / Apply / Hiring / Job Test
- One team-working photo at the top of Careers only. Form pages: no images inside the form; keep them clean.

### How We Work with Claude (transparency page)
- Process steps (STEP 1/2/3): code review, evals/testing, production handover — one small, real photo per step, or no photos if they would clutter the steps. No SEO-metric screenshots.

## Phase 3 — Sourcing (in this order)
1. **Media Library first (4,598 items).** Search it for a real photo that already matches the brief, same placement/size. This is the Plan v2 rule and the fastest, safest route.
2. **Figma Drive real-photo library** (the user's realistic-stock-image set, 631 clean photos) — real photos, already vetted for realism. Darken / crop to fit the layout; do not pre-blend for slides here, these are web images.
3. **Licensed stock (Pexels / Unsplash style, already in the library where possible).** Only if 1 and 2 have nothing that fits. Check the licence, keep the source in the audit table.
4. **Realistic generation — allowed by user 2026-11-16, ONLY if it looks like a real photoshoot, not AI-generated.** User: "yes generated photos are accepted but make sure the photos look real photoshoot like current images are, not ai generated type". That means: unretouched skin, visible pores, uneven tone, fine lines, natural shine, stray hairs, no smoothing/beauty filter; hands clearly separated, simple poses, no background faces; light imperfect (one main source, hard shadows or mixed temperatures, blown highlights or dark corners, never even studio light); never show a glowing bulb in frame, never show a detailed city background (blinds, curtains, or plain out-of-focus background instead); grain/noise in shadows, individual hair strands, fabric weave and creases, gradual focus falloff, partially cut-off background objects, muted non-uniform colour. Judge at pixel level against the real-photo benchmark (two developers pointing at a code monitor). One image at a time, user approves each before it goes live. If a generation looks AI-clean, discard it and use a real photo instead.

## Phase 4 — Replacement (execution, after user approves the Phase 1 list)
- One page at a time, in Elementor, same widget, same placement, same size/crop as the old image.
- Swap the image file only — do not move, resize or restyle the section.
- Update the image alt text to describe the new image in Claude terms (same pattern as the About alt-text fix on 2026-11-15).
- Record every swap: page, section, old file → new file, source (library / Figma Drive / stock / generated), and why the old one did not fit.
- Never delete from the Media Library. Old files stay, in case a swap needs to be undone.
- Publish, purge cache, verify live as a logged-out visitor before moving to the next page.

## Phase 5 — QA (before reporting done)
For each swapped page, live-check:
- The new image loads, is sharp, and is the right image for that section.
- No old SEO / staffing image remains on that page.
- No broken image, no stretched / squashed crop, no text cut off.
- Alt text is correct. The page layout did not shift.
- Footer, forms and CTAs still render (including the transparency page footer issue, which is separate and still blocked).

## What is NOT in this plan
- No new pages, no layout redesign, no template changes.
- No logo change, no colour / font change.
- No pricing images, no "#1" / "guaranteed" claims in images.
- No TidyCal changes (left for last, per user).
- No image deletions from the Media Library.
- No bulk replacement — each swap is approved in the audit list first.

## Decisions needed from the user before execution
1. Approve the approach: Media Library first, Figma Drive second, stock third, generation last resort only — or tell me a different order.
2. Approve the Phase 1 audit list (KEEP / REPLACE / REMOVE per image) once it is produced.
3. Confirm whether generated images are allowed at all for this site, or real photos only. — ANSWERED 2026-11-16: YES, generated photos accepted, but they must look like a real photoshoot like the current images, NOT AI-generated type (see Phase 3, item 4 for the full realism rules).
4. Confirm the Services 02/03 duplicate is a priority fix (give 03 its own image).
