# Typography

## Table of Contents

- [Font Families](#font-families)
  - [Display Font: VC Nudge](#display-font-vc-nudge)
  - [Body Font: Manrope](#body-font-manrope)
  - [Code Font: System Monospace](#code-font-system-monospace)
- [Type Scale](#type-scale)
- [Line Heights](#line-heights)
- [CSS Variables Template](#css-variables-template)
- [Heading Styles](#heading-styles)
- [Body Styles](#body-styles)
- [Usage Guidelines](#usage-guidelines)

## Font Families

### Display Font: VC Nudge
- **Weight:** ExtraBold (800)
- **Usage:** Headings and titles **at 40px or above only**
- **Style:** Always uppercase
- **Letter spacing:** -0.01em
- **File:** `fonts/VCNudge-ExtraBold.woff`
- **Threshold rule:** Text below 40px must use Manrope Bold (700) instead

```css
@font-face {
  font-family: 'VC Nudge';
  src: url('fonts/VCNudge-ExtraBold.woff') format('woff');
  font-weight: 800;
  font-style: normal;
  font-display: swap;
}
```

### Body Font: Manrope
- **Weights:** 400 (regular), 500 (medium), 600 (semibold), 700 (bold)
- **Source:** Google Fonts
- **Usage:** Body text, UI elements, descriptions

```html
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Code Font: System Monospace
- **Stack:** Menlo, Monaco, Courier New, monospace
- **Usage:** Code snippets, technical labels, formulas

## Type Scale

| Token | Pixels | Font | Usage |
|-------|--------|------|-------|
| Display | 72–180px | VC Nudge | Hero titles, section headings |
| Heading | 40–60px | VC Nudge | Card headings, feature titles |
| Lead | 24–30px | Manrope Bold (700) | Subheadings, lead text |
| Body | 18–20px | Manrope (400–600) | Body text, UI elements, labels |
| Caption | 14–16px | Manrope | Captions, metadata |

## Line Heights

- **Headings:** 0.85–1.0 (tight)
- **Body text:** 1.4–1.7 (comfortable reading)
- **UI elements:** 1.2–1.4

## CSS Variables Template

```css
:root {
  /* Font Families */
  --font-display: 'VC Nudge', sans-serif;
  --font-body: 'Manrope', sans-serif;
  --font-mono: 'Menlo', 'Monaco', 'Courier New', monospace;

  /* Font Sizes */
  --text-display: 72px;   /* responsive: clamp(48px, 8vw, 180px) */
  --text-heading: 48px;   /* 40-60px range */
  --text-lead: 26px;
  --text-body: 18px;
  --text-caption: 14px;
}
```

## Heading Styles

```css
/* VC Nudge — only at ≥ 40px */
.heading-display {
  font-family: var(--font-display);
  font-size: var(--text-display);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: -0.01em;
  color: var(--text-primary);
}

.heading-section {
  font-family: var(--font-display);
  font-size: var(--text-heading);
  line-height: 0.85;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: -0.01em;
}

.heading-card {
  font-family: var(--font-display);
  font-size: 48px;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: -0.01em;
}
```

## Body Styles

```css
.text-lead {
  font-family: var(--font-body);
  font-size: var(--text-lead);
  font-weight: 700;
  color: var(--text-primary);
}

.text-body {
  font-family: var(--font-body);
  font-size: var(--text-body);
  font-weight: 400;
  color: var(--text-secondary);
  line-height: 1.6;
}

.text-caption {
  font-family: var(--font-body);
  font-size: var(--text-caption);
  font-weight: 400;
  opacity: 0.5;
}
```

## Usage Guidelines

- **VC Nudge ≥ 40px only** — below 40px, use Manrope Bold (700) instead
- VC Nudge always gets: uppercase, `letter-spacing: -0.01em`, weight 800
- Use **Manrope 600-700** for emphasis within body text
- Keep **uppercase text** limited to headings and labels for readability
- Ensure **font smoothing** is enabled for crisp rendering
