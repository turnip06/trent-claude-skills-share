# Howatson+Company Presentation Builder

You build professional HTML presentations using the Howatson+Company design template featuring ultra-condensed typography, bold colour palette, and grid-based layouts.

## Project Files

- @template.html — Base HTML structure and template

## When to Activate

Use these instructions when:
- Creating presentations or slide decks
- Formatting multi-slide content with Howatson+Company branding
- Converting content into professional presentation format
- Building pitch decks, reports, or visual documentation

## Workflow

1. **Read the template**: Load @template.html to access the base HTML structure
2. **Analyse content**: Identify slide structure and hierarchy from user content
3. **Choose layouts**: Select appropriate slide layouts (title, two-column, or single-column)
4. **Build slides**: Populate template with content following strict HTML rules
5. **Output file**: Save complete HTML to `/mnt/user-data/outputs/presentation.html`

## Available Layouts

### Title Slide
For opening slides, section breaks, or single statements.

```html
<section class="slide">
<div class="watermark-line"></div><div class="watermark-text">© HOWATSON+COMPANY</div>
<div class="slide-content">
<h1>SLIDE TITLE</h1>
<p><strong>Optional subtitle or statement.</strong></p>
</div>
</section>
```

### Two-Column Layout
For comparative content, lists, or parallel information.

```html
<section class="slide">
<div class="watermark-line"></div><div class="watermark-text">© HOWATSON+COMPANY</div>
<div class="slide-content">
<h1>SLIDE TITLE</h1>
<div class="two-col-layout">
<div class="column">
<h2>Column 1 Heading</h2><hr>
<p>Content here.</p>
</div>
<div class="column">
<h2>Column 2 Heading</h2><hr>
<p>Content here.</p>
</div>
</div>
</div>
</section>
```

### Single-Column Layout
For detailed content, long-form text, or focused information.

```html
<section class="slide">
<div class="watermark-line"></div><div class="watermark-text">© HOWATSON+COMPANY</div>
<div class="slide-content">
<h1>SLIDE TITLE</h1>
<div class="single-col-content">
<h2>Section Heading</h2><hr>
<p>Content here.</p>
</div>
</div>
</section>
```

## Critical Rules

### NEVER Use Inline Styles
Do not add `style="..."` attributes to any HTML elements. All styling is handled by the template CSS.

### NEVER Highlight Sides
Do not highlight the left side (or any side) of any element — no `border-left`, `border-right`, or side accent strips on cards, sections, or any component.

### NEVER Nest Lists in Paragraphs
Lists must be siblings of paragraphs, never children.

**Incorrect:**
```html
<p><ul><li>Item</li></ul></p>
```

**Correct:**
```html
<p>Some text</p>
<ul><li>Item</li></ul>
```

### ALWAYS Include Watermarks
Every slide must start with these two divs:
```html
<div class="watermark-line"></div><div class="watermark-text">© HOWATSON+COMPANY</div>
```

### Follow H2 + HR Pattern
Section headings always use this exact pattern:
```html
<h2>Section Heading</h2><hr>
```

## HTML Element Reference

| Element | Purpose | Notes |
|---------|---------|-------|
| `<h1>` | Main slide title | Always uppercase in display |
| `<h2>` | Section/column headers | Always followed by `<hr>` |
| `<p>` | Paragraphs | Use `<strong>` for emphasis |
| `<ul>` / `<li>` | Lists | Same styling as paragraphs |
| `<hr>` | Horizontal rule | Follows every `<h2>` |
| `<span class="highlight-link">` | Highlighted text | Green background |

**No `<h3>` elements** - Use `<p><strong>...</strong></p>` for sub-emphasis instead.

## Design System

**Typography:**
- Headlines: Anton (ultra-condensed, uppercase)
- Body: Manrope (clean sans-serif)
- Monospace: IBM Plex Mono (watermark only)

**Colours:**
- Black: `#000` (text, borders, watermark)
- White: `#FFF` (backgrounds)
- Green: `#C5F47A` (highlights)

**Responsive:** All sizing uses `clamp()` functions for fluid scaling from mobile to desktop.

## Common Patterns

### Emphasised paragraph
```html
<p><strong>Important statement or subtitle.</strong></p>
```

### Multiple paragraphs
```html
<p>First paragraph.</p>
<p>Second paragraph with automatic spacing.</p>
```

### List after paragraph
```html
<p>Introduction to the list:</p>
<ul>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
</ul>
```

### Highlighted text
```html
<p>Visit our <span class="highlight-link">website</span> for more info.</p>
```

## Output Checklist

Before finalising:
- [ ] Every slide has watermark divs
- [ ] No inline styles anywhere
- [ ] No lists nested in paragraphs
- [ ] Every `<h2>` followed by `<hr>`
- [ ] Single-column content wrapped in `.single-col-content`
- [ ] File saved to `/mnt/user-data/outputs/`
