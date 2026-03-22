# Brand Elements Reference (Google Slides)

## Slide Dimensions

| Property | Value |
|----------|-------|
| Width | 13.33 inches (960pt) |
| Height | 7.50 inches (540pt) |
| Aspect Ratio | 16:9 |

---

## Typography

### Font Mapping

VC Nudge Black is not available in Google Fonts. Use Anton as the closest match.

| Role | Google Slides Font | Weight | Rules |
|------|-------------------|--------|-------|
| Headlines, titles, numbers | **Anton** | Regular | UPPERCASE only. Short titles. |
| Body text, captions | **Manrope** | Light (300) | 11pt typical |
| Pre-headers, medium emphasis | **Manrope** | Regular (400) | 12-16pt |
| Sidebar watermark | **IBM Plex Mono** | Regular | 10.67pt, rotated 90° CCW |

### Font Size Reference

| Element | Font | Size |
|---------|------|------|
| Title slide client name | Anton | 28pt |
| Section divider number | Anton | ~400pt (bleeds off page) |
| Statement text | Anton | 48pt |
| Statistics values | Anton | Large (inherited) |
| Thank you text | Anton | 239pt |
| Pre-header | Manrope | 12-16pt |
| Body text | Manrope Light | 11pt |
| Captions | Manrope Light | 8-11pt |
| Watermark | IBM Plex Mono | 10.67pt |

---

## Colors

### Primary Palette

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| Black | #000000 | (0, 0, 0) | Primary text, backgrounds |
| Cyan | #7DD3E8 | (125, 211, 232) | Accent, section backgrounds |
| White | #FFFFFF | (255, 255, 255) | Backgrounds, text on dark |

### Color Rules

1. One color per section maximum
2. Colored backgrounds pair with BLACK text (not white)
3. Cyan text on black background for statement slides
4. Keep accent colors minimal

---

## Sidebar / Watermark

Present on dark/branded slides only. Consists of:
1. Vertical line — 1px, full slide height
2. Watermark text — "© HOWATSON+COMPANY" rotated 90° CCW

**Color rule**: Sidebar color always matches headline color on that slide.

---

## Content Transforms

| Element Type | Transform |
|--------------|-----------|
| Headlines | UPPERCASE |
| Section numbers | Zero-padded (01, 02, 03...) |
| Client name | Prefix with "+" |
| Body text | None (preserve case) |

---

## Placeholder Reference

All placeholders use `{{slide_type.element_name}}` format.
See **TEMPLATE_CATALOG.md** for the complete mapping.
