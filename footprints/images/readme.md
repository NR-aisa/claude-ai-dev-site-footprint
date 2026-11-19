# Images

## Rules (user-settled)
- Plan v2: swap an image ONLY if it literally shows the old
  SEO/staffing offer, for a similar-style image already in the
  Media Library, same placement/size, recording the swap. Never
  delete from the Media Library.
- Phase 1 audit 2026-11-16 (all 21 published pages): NO image
  literally shows the old SEO/staffing offer in frame.
- Generated photos allowed (user 2026-11-16) ONLY if they look
  like a real photoshoot, not AI-generated type (unretouched skin,
  pores, uneven tone; hands separated, simple poses; imperfect
  light, one main source; never a glowing bulb; never a detailed
  city background; grain, hair strands, fabric weave, gradual
  focus falloff, partially cut-off objects, muted non-uniform
  colour; judge at pixel level against the benchmark of two
  developers pointing at a code monitor; one at a time, user
  approves each before it goes live).
- Real photos must be copyright-safe (Pexels/free licence; no
  Figma Drive unknowns, no Getty/iStock, no watermarks, no
  unverified sources). WordPress stores no licence field — the
  only library evidence is the "pexels-photo-" file naming.
- Keep every generation, including rejected ones. Never generate
  a fake face for a real named person.

## Swaps applied
- 2026-11-16 (real Pexels, user approved): Services 03 duplicate
  7988079 → 574070-1 (media 1980); Landing hero → 1181676-1
  (media 1964); blog cost post featured image → 4050315-1
  (media 1604). Home testimonial portraits for Mark Johnson and
  Sarah Thompson REMOVED (text/names/stars kept, like Lisa Garcia).
- Generated replacements (3 JPGs, same man/green hoodie, #1 very
  dark/tired) REJECTED by user 2026-11-16 — NOT used, kept in
  workspace/stock-training/claude-ai-dev-replacements/.
- 2026-11-17 (Fix 4, client feedback: images already used on
  another website can be called plagiarised by Google — change a
  once-used image a bit with AI, then use it): 3 AI-changed images
  went live — Claude Code 13737, AI Agents 13738, Claude API
  13739 (see evidence.md). Honest caveat at the time: #2 (AI
  Agents) barely changed — almost the same photo; #1/#3 changed
  a bit; all three still very close to the originals, so they may
  not be enough for Google duplicate detection. User approved
  "ok update" (apply as-is).
## How to use this folder

1. Read `readme.md` (what/why/decisions), then `evidence.md` (IDs, URLs,
   verification), then `log.md` (step-by-step, including what went wrong).
2. Before editing this area again, make a per-page draft backup first —
   see `tools/wp-preflight-backup/` — and record it in `log.md`.
3. Verify live as a **logged-out visitor** before reporting anything done.
   A signed-in / admin-bar view is not evidence.
