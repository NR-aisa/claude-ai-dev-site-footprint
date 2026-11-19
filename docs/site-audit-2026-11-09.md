# Claude AI Developers rebuild — site audit + US keyword map
Prepared 2026-11-09 ~14:10 Asia/Dhaka (08:10 UTC), before the user confirms the rebuild.
Source: live check of https://claude-ai-dev.developers-organism.com/ and its sitemaps, plus web search 2026-11-09.

## What the user asked (2026-11-09 07:44 UTC, side chat "Edit WordPress copywriting")
Fully replace claude-ai-dev.developers-organism.com — separate from main developers-organism.com —
into a site about "Claude AI Developers", targeting American clients. Read the whole site
architecture and keywords, understand the copy, remove what does not fit, remove plagiarism
related to the domain, and research what US people actually search for.
Assistant replied 07:44 UTC asking the user to verify understanding first, with two checks still open:
1. Claude (Anthropic) vs Cloud AI?
2. Offer = US companies hire the team as Claude AI developers, or training / a product?

Do NOT start rewriting until those two are confirmed. This audit is groundwork only.

## Live homepage audit (checked 2026-11-09 08:08 UTC)
Title: "Local SEO Service in USA | Developers Organism"
H1-ish copy: "Trustworthy SEO and American Staffing #1"
- "We are the #1 brand for Trustworthy SEO and premier American Staffing… California and New York"
- Sections: Two Ways We Help You Grow; Who We Are — "Pioneering Software Development Since 2008";
  Quality Services: Lifetime SEO Deals, Custom Software Development, Social Media Management;
  Learn From Our Playbook; Ready to Transform?; Our Unique Edge: Lifetime SEO Deal / Custom Software
  Development / Open-Source Commitment; Happy Clients testimonials; Join Us Today.
- Contact: +19145204706, N Gould St, Sheridan, 56 82801, 840. Hours Mon–Sun 00:00–23:59.
  Price range: start from $500. Additional details: Local SEO service in USA, $299 USD.
- Testimonials: Mark Johnson, Sarah Thompson, and "Lisa Garcia" — the Lisa Garcia photo shows a
  bearded man in a black turtleneck, a name/photo mismatch to fix or drop, not reuse.
- No mention of Claude, Anthropic, Claude Code, AI agents, MCP, or RAG anywhere on the homepage.
- Images are stock Pexels photos, not team/product proof.

## Site architecture (page-sitemap.xml, checked 2026-11-09 08:10 UTC)
25 pages (matches MEMORY: 910 posts / 25 pages, WP 7.1.4, Astra):
Home (/), about, services, contact, careers, sales-with-seo, virtual-assistant-for-ceos,
why-our-seo-claim-is-crazy-for-ranking-number-1, landing-page-for-leads, hiring-form,
job-test-form, apply-for-careers-job-application-form, thank-you-page-for-job-application,
sample-home, sample-page, test, html-view-test, imprint, disclaimer,
cookie-policy-eu, cookie-policy-uk, privacy-statement-eu, privacy-statement-uk.
Sitemaps also list post, category, post_tag, author, attachment, video, geo, news, bitforms.
Implication: there is no Claude service page to edit — the rebuild needs new pages, and most
existing pages (SEO, staffing, virtual assistant, careers forms) do not fit the new positioning.
Decision needed: delete / redirect / keep (legal pages only) — do not just rewrite the homepage
and leave SEO/staffing pages live under a Claude brand.

## Trust / plagiarism risks to remove, not carry over
- "#1 brand" / "guaranteed digital visibility" / "Lifetime SEO" — unsubstantiated superlatives;
  rewrite from real proof or drop.
- "Since 2008" vs the current brand story — verify before reusing on a Claude site.
- Testimonials with stock photos and a name/photo mismatch — do not carry over; replace with
  verifiable US client proof or remove the section.
- Generic service lists (SEO, social media, virtual assistant) — off-position for Claude developers.

## WP Auto Blog warning (timely)
WP Auto Blog was connected to this same subdomain today, 2026-11-09 05:57 UTC, default Post Status:
Publish, nothing published/scheduled yet. If auto-blogging starts on the old SEO/staffing topics,
it will publish off-brand content onto the new Claude site. Pause / retarget blog topics to
Claude development before any schedule is set.

## What US buyers actually search for (web search 2026-11-09)
Clusters, with the language buyers use:
1. Hire: "hire Claude developers", "hire Claude Code developers", "Claude developers for hire"
   — Toptal's page is the top result; buyers compare vetted freelancers.
2. Agency: "Claude Code development agency", "best Claude Code development agencies in the USA"
   — a 2026 roundup lists 5 verified US firms; buyers check Clutch reviews, team size, delivery model.
3. Cost / models (from AY Automate guide, updated ~9 days ago):
   full-time $190k–$320k base in the US, 6–12 weeks to start; contractor $80–$200/hr, 2–4 weeks;
   specialist agency $8k–$60k/mo retainer, 1–2 weeks; fractional lead $5k–$15k/mo, 2–3 weeks.
   This cost comparison is exactly the page US buyers land on — the new site should answer it
   in its own words, not copy it.
4. Build: "Claude API", "Claude Code / Agent SDK", "MCP servers", "RAG pipelines", "AI agents",
   "forward deployed AI engineer" — production work: agents, MCP integrations, evals, monitoring,
   security, deployment via Anthropic API / Bedrock / Vertex / Foundry, Python or TypeScript.
5. Proof buyers ask for: production LLM features shipped (not chatbot demos), structured outputs,
   prompt/context design, handling bad model responses, sub-agent architecture, CLAUDE.md context.

## Proposed new information architecture (draft, for user approval)
- Home: Hire Claude AI Developers (US) — outcome, proof, engagement models, cost guide, CTA.
- Services: Claude Code development / AI agents / Claude API integration / MCP + RAG / evals & production support.
- Hire / Engagement: dedicated developer, project, retainer — with the cost/speed comparison above.
- Work / Proof: real shipped examples only (no stock testimonials).
- About, Contact (keep +19145204706 only if still correct), legal pages (keep).
- Blog: retarget WP Auto Blog to Claude topics only, after the rebuild.

## Still unknown / to verify at delivery
- Claude vs Cloud, and the exact offer (hire team vs training vs product).
- Whether +19145204706, Sheridan address, $500/$299 pricing, "Since 2008" stay.
- Which existing pages to redirect vs delete; whether 910 old posts stay, are retargeted, or are hidden.
- No plagiarism scan was run — "remove plagiarism" needs a per-page originality check during rewrite, not assumed from this audit.
