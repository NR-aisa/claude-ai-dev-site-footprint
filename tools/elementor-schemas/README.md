# elementor-schemas — Flexbox containers, widget schemas, semantic IDs

Taken from: `prompts/source/wordpress-elementor-modernization-prompt.md`,
§3 (Elementor architecture primer) and §6 (AST schemas & widget catalog,
§6.1–§6.15).

## What it is

A reference for building Elementor pages the modern way, so future edits
don't have to re-discover widget IDs by description (the way every
browser task on this site had to — `ed07c78`, `4d446a7`, `c730265`…).

## What was taken, what was left out

- Taken: the `_elementor_data` model (JSON AST in `wp_postmeta`),
  Flexbox Container (`e-con`) layout, the widget schemas in
  `schemas.md`, semantic lowercase IDs + BEM classes + scoped CSS,
  the documentation-header contract for new step files.
- Left out: pushing raw `_elementor_data` via REST as the normal edit
  method (edits here stay in Elementor's editor — a malformed JSON push
  can break a page beyond easy repair); the pluggable-step pipeline
  machinery; the 400-step budget.

## Key facts (from gist 2, §3)

- Elementor stores layout in `wp_postmeta` under `_elementor_data`
  (serialized JSON array of containers/widgets — a recursive AST).
- `_elementor_edit_mode = "builder"`; `_elementor_version` records the
  Elementor version; `_elementor_page_settings` holds the page template
  (`elementor_header_footer` / `elementor_canvas` / `default`);
  `_elementor_css` is the cached compiled CSS — clearing it forces a
  recompile.
- Legacy model: section → column → widget. Modern model (use this):
  top-level Flexbox Container (`elType: "container"`, `isInner: false`,
  `container_type: "flex"`, `flex_direction: "column"|"row"`,
  `gap`, `align_items`, `justify_content`) with nested inner containers.

## Files

- `schemas.md` — container + widget schemas and the semantic-ID /
  scoped-CSS pattern, with the Claude site's actual widget IDs listed
  for cross-reference.
