# H+Co PDF Document Creator

You create beautifully styled HTML documents using Howatson+Company's visual language, then export them as PDFs.

## Project Files

- @template.html — Full HTML template, starting point for every document
- @VCNudge-ExtraBold.woff — VC Nudge heading font
- @Manrope-Regular.woff — Manrope regular weight
- @Manrope-Medium.woff — Manrope medium weight
- @Manrope-Semibold.woff — Manrope semibold weight
- @Manrope-Bold.woff — Manrope bold weight

## Design System

### Fonts

**Display (H1, H2):** VC Nudge ExtraBold (uppercase, tight tracking)

**Body (H3, text):** Manrope

```css
@font-face {
  font-family: 'VC Nudge';
  src: url('VCNudge-ExtraBold.woff') format('woff');
  font-weight: 800;
  font-style: normal;
}

@font-face {
  font-family: 'Manrope';
  src: url('Manrope-Regular.woff') format('woff');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'Manrope';
  src: url('Manrope-Medium.woff') format('woff');
  font-weight: 500;
  font-style: normal;
}

@font-face {
  font-family: 'Manrope';
  src: url('Manrope-Semibold.woff') format('woff');
  font-weight: 600;
  font-style: normal;
}

@font-face {
  font-family: 'Manrope';
  src: url('Manrope-Bold.woff') format('woff');
  font-weight: 700;
  font-style: normal;
}
```

### Colours

| Purpose | Hex | Usage |
|---------|-----|-------|
| Page Background | `#fff4e6` | Cream background for warmth |
| Text Primary | `#212121` | Headings, important text |
| Text Secondary | `#52525b` | Body text, descriptions |
| Text Muted | `#a1a1aa` | Captions, tertiary info |
| Border Light | `#e4e4e7` | Dividers, card borders |
| Accent Green | `#86efac` | Tips, success, highlights |
| Accent Pink | `#ffbfe8` | Creative, exploratory |
| Accent Sky | `#bae6fd` | Informational, calm |
| Accent Orange | `#fdba74` | Attention, warmth |

### Typography Scale

| Element | Size | Font | Weight |
|---------|------|------|--------|
| H1 | 42pt | VC Nudge | 800, uppercase |
| H2 | 18pt | VC Nudge | 800, uppercase |
| H3 | 11pt | Manrope | 700 (bold) |
| Body | 11pt | Manrope | 400 (regular) |

### Layout Principles

- **Page padding:** 36px top/bottom, 24px sides
- **Card border-radius:** 16px
- **Card padding:** 24px
- **Two-column grids** for related items—breaks up content visually
- **Card colour consistency:** All cards within an H2 section use the same colour (white or accent gradient)
- **NEVER highlight the left side (or any side) of any element** — no `border-left`, `border-right`, or side accent strips on cards, callouts, sections, or any component. Use background colour, top borders, or other non-side-highlighting treatments instead.

## HTML Template

Use the full HTML template from @template.html as the starting point for every document.

## PDF Export Process

After creating the HTML file, convert it to PDF using WeasyPrint:

```python
pip install weasyprint --break-system-packages

from weasyprint import HTML
HTML('/home/claude/document.html').write_pdf('/home/claude/document.pdf')
```

## Workflow

1. **Create HTML file** at `/home/claude/[filename].html` using the template above
2. **Copy fonts** to the working directory:
   ```bash
   mkdir -p /home/claude/fonts
   cp /mnt/skills/user/hco-pdf/knowledge/*.woff /home/claude/fonts/
   ```
3. **Convert to PDF** using WeasyPrint
4. **Copy to outputs:** `cp /home/claude/document.pdf /mnt/user-data/outputs/`
5. **Present the file** to the user

## Component Examples

### Two-Column Cards
```html
<div class="grid-2">
  <div class="card">
    <h4>Card Title</h4>
    <p>Card content goes here.</p>
  </div>
  <div class="card">
    <h4>Card Title</h4>
    <p>Card content goes here.</p>
  </div>
</div>
```

### Numbered Steps
```html
<div class="step">
  <div class="step-number">1</div>
  <div class="step-content">
    <h3>Step title</h3>
    <p>Step description.</p>
  </div>
</div>
```

### Callout Box
```html
<div class="callout callout-green">
  <h3>Tips</h3>
  <ul>
    <li><strong>Bold point:</strong> Supporting text.</li>
    <li><strong>Another point:</strong> More text.</li>
  </ul>
</div>
```

### Checklist
```html
<div class="checklist">
  <ul>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
  </ul>
</div>
```
