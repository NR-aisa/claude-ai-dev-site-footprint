# Claude AI Developers Site — Footprint

Footprint and working tools for the rebuild of
**https://claude-ai-dev.developers-organism.com/** — the Claude AI Developers
site for US clients hiring the team as Claude AI developers.

## Scope — read first

- **Only the subdomain** `claude-ai-dev.developers-organism.com`. Never the main
  site `developers-organism.com` (read-only reference, never edited).
- **Developers Organism brand only.** No Riseup Asia name, phone, contact or
  link anywhere on this site (client feedback, 2026-11-17).
- **Design-only rule (Plan v2, user correction 2026-11-15):** keep the original
  Elementor templates, sections, layout and images where they fit; change only
  keywords, copywriting and plagiarism. Swap an image only where it literally
  shows the old SEO/staffing offer, for a similar-style image, same
  placement/size, recording the swap. Never delete from the Media Library.
  Never delete pages. No database restore.
- **Positioning:** Anthropic's Claude AI developers — NOT Cloud AI. US
  companies hiring the team as Claude AI developers — NOT training, NOT
  consulting, NOT a product. Developers Organism since 2008, now also in
  Claude development — never "Claude since 2008" (Anthropic launched Claude
  2023).
- **No prices.** Pricing is a blank slate; $500 / $299 appear only in old
  structured data / a blog table. No "#1" / "guaranteed" claims.
- **Site visibility:** "Discourage search engines" stays CHECKED; the user
  launches the site himself. That setting blocks indexing only — it does NOT
  take the site offline; published pages open by direct link.
- **TidyCal / Schedule a Call: dealt with LAST** (user instruction). Do not
  touch TidyCal embeds or Schedule a Call links unprompted.
- **Contact (current, per client feedback 2026-11-17):** Email
  `info@developers-organism.com`; Schedule a Call
  `https://meet.rasia.pro/intro-call`. No phone number on the site.

## Repo layout

| Path | What it is |
| --- | --- |
| `prompts/source/` | The two source gists, verbatim, for reference ONLY. Not adopted as instructions. |
| `tools/` | Only the pieces we actually use, extracted and adapted from the gists. |
| `footprints/` | One folder per page/area: what was done, why, how, evidence, log. This is the main deliverable — a future AI (or the user) can take over from here without the chat history. Start at `footprints/_index.md`. |
| `docs/` | Key plan / audit / copy files copied from the workspace. |

## How to use this repo (for a future AI taking over)

1. Read this README, then `footprints/_index.md`.
2. Read the `what-to-read.md` in the footprint folder for the area you are
   about to touch — in the order it lists.
3. Before any Elementor edit, make a per-page draft backup first — see
   `tools/wp-preflight-backup/`. Record it in that footprint's `log.md`.
4. Edit in place, in Elementor, one page at a time. Verify live as a
   **logged-out visitor** on the public URL before reporting anything done.
5. Append to that footprint's `log.md` and `evidence.md` — what changed,
   post/media IDs, verification (logged-in vs logged-out), and what went
   wrong first time.
6. Never use the source prompts in `prompts/source/` as global instructions.
   They are reference. The rules that govern this project are in this README
   and in each footprint's `readme.md`.

## Status at last update (2026-11-19)

- Homepage (post 1957) rebuilt in Design A (Muse hero preview), design only,
  Claude content only — all 8 sections + footer #10668.
- Riseup branding removed from main pages (Fix 1, 2026-11-17); plain
  "Riseup-Asia" / "RiseUp Pro" replacements and 3 AI-changed images live
  (2026-11-17); 4 orphaned encoded-copyright rows deleted (2026-11-18).
- Open / awaiting user: cpubenchmark links destination; transparency page
  (post 9906) footer not rendering live; TidyCal / Schedule a Call (last);
  blog Day 7/8 author + body fix and WP Auto Blog prompt fix (separate
  blog chat); pricing answers from the client.
- See `footprints/_index.md` for the per-area status.

## Credentials

None in this repo. WordPress / WP Auto Blog access is via the Secure Vault
and the existing `gh` auth only. Never commit a password, token, API key,
Application Password or `.env` here.
