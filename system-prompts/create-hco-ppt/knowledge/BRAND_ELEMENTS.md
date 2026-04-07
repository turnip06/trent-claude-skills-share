# Brand Elements Reference

> **Template Version**: Standardized (semantic `{{type.element}}` placeholders)

## Table of Contents

- [Slide Dimensions](#slide-dimensions)
- [Typography](#typography)
  - [Fonts Used](#fonts-used)
  - [Line Spacing](#line-spacing)
  - [Font Sizes by Element](#font-sizes-by-element)
- [Colors](#colors)
  - [Primary Palette](#primary-palette)
  - [Accent Colors (Use Sparingly)](#accent-colors-use-sparingly)
  - [Color Rules](#color-rules)
- [Sidebar / Watermark](#sidebar--watermark)
  - [Structure](#structure)
  - [Positioning](#positioning)
  - [Sidebar Presence by Slide](#sidebar-presence-by-slide)
  - [Watermark Text](#watermark-text)
  - [Color Matching Rule](#color-matching-rule)
- [Special Element: Slide 22 Copyright](#special-element-slide-22-copyright)
- [Placeholder Format](#placeholder-format)
  - [Examples](#examples)
  - [Regex Pattern](#regex-pattern)
- [Content Transforms](#content-transforms)
- [Placeholder Reference](#placeholder-reference)

## Slide Dimensions

| Property | Value |
|----------|-------|
| Width | 13.33 inches |
| Height | 7.50 inches |
| Aspect Ratio | 16:9 |

---

## Typography

### Fonts Used

| Font | Usage | Weight | Rules |
|------|-------|--------|-------|
| **VC Nudge Black** | Headlines, titles, numbers | Black | UPPERCASE only. Short titles. |
| **Manrope Light** | Body text, captions | Light (300) | 11pt typical |
| **Manrope** | Pre-headers, medium emphasis | Regular (400) | 12-16pt |
| **IBM Plex Mono** | Sidebar watermark only | Regular | 10.67pt, rotated 90° CCW |

### Line Spacing

| Font | Line Spacing | Setting |
|------|--------------|---------|
| **VC Nudge Black** | 0.7× (70%) | Multiple at 0.7 |
| **Manrope** | Default (1.0×) | Single |
| **IBM Plex Mono** | Default (1.0×) | Single |

### Font Sizes by Element

| Element | Font | Size |
|---------|------|------|
| Title slide client name | VC Nudge Black | 28pt |
| Section divider number (01) | VC Nudge Black | ~400pt (bleeds off page) |
| Section divider title | VC Nudge Black | Inherited from placeholder |
| Statement text | VC Nudge Black | 48pt |
| Statistics grid title | VC Nudge Black | 48pt |
| Statistics values (00%) | VC Nudge Black | Large (inherited) |
| Thank you text | VC Nudge Black | 239pt |
| Pre-header | Manrope | 12-16pt |
| Heading 2 | Manrope Light | 14pt |
| Body text | Manrope Light | 11pt |
| Captions | Manrope Light | 8-11pt |
| Watermark | IBM Plex Mono | 10.67pt |

---

## Colors

### Primary Palette

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| Black | #000000 | (0, 0, 0) | Primary text, backgrounds |
| Cyan | #7DD3E8 | (125, 211, 232) | Accent, section backgrounds, highlight text |
| White | #FFFFFF | (255, 255, 255) | Backgrounds, text on dark |

### Accent Colors (Use Sparingly)

| Color | Usage |
|-------|-------|
| Pink | Section accent |
| Green | Section accent |
| Yellow | Section accent |

### Color Rules

1. **One color per section maximum**
2. **Colored backgrounds pair with BLACK text** (not white)
3. **Keep accent colors minimal**
4. **Cyan text on black background** for statement slides

---

## Sidebar / Watermark

### Structure

The sidebar consists of:
1. **Vertical line** - 1px black, full slide height
2. **Watermark text** - "© HOWATSON+COMPANY" rotated 90° counter-clockwise

### Positioning

| Element | Position |
|---------|----------|
| Sidebar group | left: 0.00in, top: 0.00in |
| Sidebar width | 0.20in |
| Sidebar height | 7.50in (full slide height) |

### Sidebar Presence by Slide

**Slides WITH sidebar:**
- 5 (statement-dark)
- 13 (statistics-grid)
- 14 (numbered-rows)
- 15 (two-panel-compare)
- 17 (image-text-right)
- 18 (fullbleed-image)
- 19 (image-gradient-text)
- 20 (bold-title-image)
- 24 (thank-you)
- 26 (single-stat)

**Slides WITHOUT sidebar:**
- 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 16, 21, 22, 23, 25, 27, 28

> **Note**: This is intentional by design. Dark/branded slides have sidebar, content-heavy white slides do not.

### Watermark Text

```
© HOWATSON+COMPANY
```

### Color Matching Rule

**Sidebar color ALWAYS matches headline color:**
- Black headline on light background → Black sidebar
- White headline on dark background → White sidebar
- Black headline on cyan background → Black sidebar

---

## Special Element: Slide 22 Copyright

Slide 22 (storyboard-8) has a unique copyright placement:

| Property | Value |
|----------|-------|
| Text | "© Howatson+Company" |
| Font | IBM Plex Mono |
| Size | 10.67pt |
| Position | Top-right: (11.49in, 0.19in) |

This is NOT the sidebar watermark - it's a separate text element.

---

## Placeholder Format

All content placeholders use the format:

```
{{slide_type.element_name}}
```

### Examples

| Placeholder | Description |
|-------------|-------------|
| `{{title.client_name}}` | Client name on title slide |
| `{{section.number}}` | Section number (01, 02, etc.) |
| `{{stats.value_1}}` | First statistic value |
| `{{three_col_text.heading_2}}` | Second column heading |

### Regex Pattern

To find all placeholders:
```regex
\{\{[a-z_]+\.[a-z_0-9]+\}\}
```

---

## Content Transforms

When replacing placeholders, apply these transforms:

| Element Type | Transform |
|--------------|-----------|
| Headlines | UPPERCASE |
| Section numbers | Zero-padded (01, 02, 03...) |
| Client name | Prefix with "+" |
| Body text | None (preserve case) |
| VC Nudge headlines | 0.7 line spacing |

---

## Placeholder Reference

For the complete list of placeholder prefixes and slide types, see **TEMPLATE_CATALOG.md**.

For detailed placeholder tokens per slide, see **SLIDE_DETAILS.md**.
