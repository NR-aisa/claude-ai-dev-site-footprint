# Contact — log

- 2026-11-15 16:30–16:36: Plan v2 in-place edit.
- 2026-11-15 16:37–16:40: QA — Contact failed only inside the
  TidyCal embed.
- 2026-11-16 15:35–15:38: "Visit Riseup Asia Contact" button added
  (https://riseup-asia.com/contact, new tab).
- 2026-11-16 16:00–16:05: button moved to top hero, appears once;
  eyebrow "RISE ASIA LLC" → "Riseup Asia LLC".
- 2026-11-16 16:09–16:10: button centred (was left-aligned).
- 2026-11-17 (Fix 1): button deleted; Phone/WhatsApp Icon Box
  deleted. Verified live.
- 2026-11-19 09:26–09:40 UTC: user asked why a contact-form link
  shows 404. Read-only check (side chat, nothing edited) found:
  (1) the TidyCal embed on /contact/ points to
  tidycal.com/schedule-with-alim/linkedin-casual, which returns
  "404 | TidyCal" — dead target (deleted/renamed is inference,
  not observed); the working booking link used by all Book a
  Call / Schedule a Call buttons is tidycal.com/rbook/casual.
  (2) Redirection rules like /contact/ →
  /contact-claude-ai-developers/ (Draft post 13519) fired
  Nov 9–10 and are disabled now — a logged-out visitor would
  have got a 404 then; re-enabling them would bring it back.
  (3) forms.riseup-asia.com/cpubenchmark in the application
  form is 404 (see footprints/leftover-pages/ — cpubenchmark
  pick still awaiting user). Bonus: footer social links X
  (x.com/DevOrgTeam) and LinkedIn
  (linkedin.com/company/developersorganism) are dead; Facebook,
  YouTube, Instagram load. /contact/ itself and all Get a Free
  Quote / Contact buttons load fine. Awaiting user: which exact
  link they clicked, and whether they were logged in. No fix
  approved or made yet. TidyCal/Schedule a Call still "last".
