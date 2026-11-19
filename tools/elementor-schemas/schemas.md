# Elementor schemas — distilled from gist 2, §6

## Flexbox Container (`elType: "container"`)

```json
{
  "id": "hero-section",
  "elType": "container",
  "isInner": false,
  "settings": {
    "container_type": "flex",
    "flex_direction": "row",
    "align_items": "start",
    "justify_content": "space-between",
    "gap": {"size": 24, "unit": "px"},
    "_element_id": "hero-section"
  },
  "elements": []
}
```

## Widget schemas (settings that matter)

| Widget | Key settings |
| --- | --- |
| Heading | `title`, `header_size` (H1–H6), `align`, typography (font_family, font_size, line_height), `title_color` |
| Text Editor | `editor` (HTML), typography, `text_color` |
| Button | `text`, `link.url`, `button_type`, `size`, `background_color` / gradient, `border_radius` |
| Image | `image.id` (Media Library ID), `image.url`, `image_size`, `caption`, `link_to` |
| Icon Box | `title_text`, `description_text`, `selected_icon`, `icon` position |
| Icon List | `icon_list[]` — `text`, `selected_icon`, `link.url` |
| Testimonial | `testimonial_content`, `testimonial_name`, `testimonial_job`, `testimonial_image` |
| Form | `form_fields[]`, `button_text`, `form_name` |
| Counter | `starting_number`, `ending_number`, `prefix`/`suffix` |
| Tabs / Accordion | `tabs[]` — `tab_title`, `tab_content` |
| Nav Menu | `menu` (menu ID), `layout` |

## Semantic IDs + scoped CSS (use on every new build)

- Every container/widget gets a lowercase hyphenated `_element_id`:
  `#hero-section`, `#hero-cta-btn`, `#quality-services`, `#footer-contact`.
- BEM classes in `_css_classes`, e.g. `hero__cta`, `card--white`.
- Component-scoped CSS in `custom_css` using `selector`, e.g.
  `selector .hero__cta { border-radius: 50px; }` — never a global
  rule that can leak into another section.

## This site's actual widget IDs (for cross-reference)

Random Elementor IDs from the Nov 2026 work — keep these in footprints
so a future editor can find the widget without re-searching:

- Homepage hero banner: "Hire a Claude Developer — Build with Claude
  Code" (moved to top, 52px, 2026-11-18)
- Homepage Quality Services widgets: `ed07c78` (Claude Code, media
  13737), `dcd7f29` (AI Agents, media 13738), `4d446a7` (Claude API &
  RAG, media 13739)
- Services widget `c730265` ("03. Claude API Integration", media 13739)
- Trust-bar row `c36f822` (padding 33px → 16px, Fix 2), parent
  `8c069a4` (1200px); Two Ways parent `ae885b1` (1140px)
- Footer template `#10668` (Entire site)
