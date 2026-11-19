# Riseup removal — evidence

- Fix 1 verified live 2026-11-17: Home, Services, About, Contact,
  /blog/ — no visible "Riseup", "RISE ASIA", "riseup-asia",
  "contact@riseup-asia.com", "+1 204 650 3141", "call.rasia.pro".
  Footer: only "Email: info@developers-organism.com" and
  "Schedule a Call: meet.rasia.pro/intro-call" + "© 2026
  Developers Organism. All Rights Reserved."
- Orphan rows deleted 2026-11-18: meta_ids 78421, 78430, 78440,
  78449 (posts 7818–7821, post_exists=0, each DELETED rows=1).
  Temporary WPCode snippet (ID 13748) used for the guarded check
  + delete, then moved to Trash. "riseup" in wpmy_postmeta
  95 → 91.
- cpubenchmark — corrected count (2026-11-17 22:03–22:32, preview
  only): "forms.developers-organism.com/cpubenchmark" = **0 rows**
  in wp_posts/postmeta; "forms.riseup-asia.com/cpubenchmark" = 0
  rows there too; token "cpubenchmark" = 0 rows (incl. diagnostic
  on wpmy_bitforms_form). The dead subdomain itself was verified
  DNS NXDOMAIN 2026-11-17 15:23 UTC — but nothing on the site
  links to it, so no visitor lands on it from the site.
- What DOES exist live: **2 links, both still to
  https://forms.riseup-asia.com/cpubenchmark**, anchor text
  "Link", inside BitForm form 2 "Job Form v2" ([bitform id='2'],
  121 responses, 536 views, created Dec 3, 2025):
  1. Under "Device & Expectation:" — "PC better than 19,000 CPU
     list (Link)" (Step-1 HTML field b2-84, "Starting Note:
     Important Guidelines").
  2. Under "Share Your PC Specification:" — "CPU: (Model name,
     e.g., i9-9900K or i7-265KF) [Benchmark Ref: Link]".
  Embedded via Apply page 7937
  (/apply-for-careers-job-application-form/) and Elementor
  template 12635 "Job Applications". The links live in the form
  data, which is why Fix 1's posts/postmeta replacements missed
  them. **What the original form offered is UNKNOWN** — beyond
  being a CPU benchmark reference for applicants.
- User's options (presented, no pick yet): (1) point them to
  /contact/ (simplest, keeps Developers Organism-only rule);
  (2) remove the links entirely; (3) restore the original
  forms.riseup-asia.com/cpubenchmark — NOT recommended
  (reintroduces a Riseup link); (4) build a new Developers
  Organism equivalent form (none known to exist).
