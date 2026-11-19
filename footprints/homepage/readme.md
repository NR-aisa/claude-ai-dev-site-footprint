# Homepage — post 1957, `/`

## What
The homepage. Original post 1957, Elementor-built, front page.
Sections, top to bottom: Hero (Book A Call form right) → trust bar →
Two Ways We Help You Grow → Who We Are → Quality Services → Learn
From Our Playbook (Enyx) → Our Unique Edge → Happy Clients → Join Us
Today → footer #10668.

## Why / decisions
- 2026-11-10 launch (v1) replaced the homepage with a new text-only
  page and redirects. **Corrected 2026-11-15 by the user:** "you've
  deleted all the content's images totally / you should not delete
  [them] and [the] main structure / keep everything as same as
  according to the design graphical concept / you will just mess with
  up only with the keywords, copywriting, plagiarism." Governing scope
  since then is Plan v2: recover first, edit the original page in
  place, change only keywords/copywriting/plagiarism.
- 2026-11-15 (Plan v2 edit): H1 "Hire Claude AI Developers in the
  USA"; hero eyebrow, Two Ways, Who We Are (Developers Organism since
  2008, now also Claude), Quality Services → Claude Code Development /
  AI Agents / Claude API & RAG, Playbook → Enyx ($36,500, ~90 days),
  CTA → Book a Call, Unique Edge rewritten, 3 testimonials verbatim
  with Lisa Garcia's photo removed only, Join Us Today rewritten.
- 2026-11-16: homepage padding investigated (trust bar cut off in a
  user screenshot). Found: trust-bar row c36f822, 33px padding, 60px
  gap; overflow only below ~1200px viewport / at 110–125% zoom.
  Fix 2 (2026-11-17): padding 33px → 16px, gap 60px → 24px on Laptop,
  Wrap on Tablet Landscape only.
- 2026-11-18: white pill banner "Hire a Claude Developer — Build
  with Claude Code" moved to the top of the hero, enlarged
  18px → 52px desktop (40px tablet, 36px mobile), wording unchanged.
- 2026-11-18/19: Design A rebuild (user: "bring the design here, not
  the content", Design A from the Muse hero preview). Hero white,
  navy/purple, Ubuntu headings / Poppins body, gradient pill CTAs,
  lavender results panel. All 8 sections + footer restyled, Claude
  content only — no old SEO/#1/phone/Riseup copy.

## What was rejected / corrected
- The 2026-11-10 full-replacement launch (superseded 2026-11-15).
- The launch report's claim the homepage had been switched — wrong;
  live homepage still rendered the OLD homepage until recovery.
- The homepage line "Your hire saves $150K+ — and never sleeps" does
  NOT exist (checked live + Elementor). Only $150K is the real Enyx
  headline, kept intentionally.
- Generated testimonial portraits (same man/green hoodie) rejected
  2026-11-16 — portraits removed instead, never fake faces.
## How to use this folder

1. Read `readme.md` (what/why/decisions), then `evidence.md` (IDs, URLs,
   verification), then `log.md` (step-by-step, including what went wrong).
2. Before editing this area again, make a per-page draft backup first —
   see `tools/wp-preflight-backup/` — and record it in `log.md`.
3. Verify live as a **logged-out visitor** before reporting anything done.
   A signed-in / admin-bar view is not evidence.
