# Color Palette

## Brand Colors (Category System)

Use these colors to create visual hierarchy and categorization:

| Name | Hex | Usage |
|------|-----|-------|
| Pink | `#ffbfe8` | Creative, exploratory, highlight |
| Sky Blue | `#bae6fd` | Informational, calm, structured |
| Green | `#86efac` | Success, edit, transformation |
| Orange | `#fdba74` | Trainable, attention, warmth |

## Background Colors

| Name | Hex | Usage |
|------|-----|-------|
| Cream | `#fff4e6` | Primary page background |
| Light | `#fff7ed` | Cards, content containers (white replacement) |
| Warm | `#fff7ed` | Semantic alias for warmth emphasis |
| Dark | `#212121` | Inverted sections, footers |

## Text Colors

| Name | Hex | Usage |
|------|-----|-------|
| Primary | `#212121` | Headings, important text |
| Secondary | `#52525b` | Body text, descriptions |
| White | `#ffffff` | Text on dark backgrounds |

> **Muted text:** Apply `opacity: 0.5` to the element. For elements with children that should stay full opacity, use `color: rgba(33, 33, 33, 0.5)` on light backgrounds or `color: rgba(255, 255, 255, 0.5)` on dark backgrounds instead.

## Accent Colors (Extended Palette)

For data visualization, tags, or decorative elements:

| Name | Hex |
|------|-----|
| Type Blue | `#b3e5fc` |
| Subject Green | `#81c784` |
| Environment Purple | `#d4a5ff` |
| Camera Orange | `#ffb366` |
| Lighting Pink | `#ffbfe8` |
| Composition Cyan | `#80deea` |
| Colour Yellow | `#fdd275` |
| Details Red | `#ff9999` |

## CSS Variables Template

```css
:root {
  /* Brand Colors */
  --color-pink: #ffbfe8;
  --color-sky: #bae6fd;
  --color-green: #86efac;
  --color-orange: #fdba74;

  /* Backgrounds */
  --bg-cream: #fff4e6;
  --bg-warm: #fff7ed;
  --bg-light: #fff7ed;    /* White replacement — use for cards, containers */
  --bg-dark: #212121;

  /* Surfaces (category tints at 40% opacity) */
  --surface-pink: rgba(255, 191, 232, 0.4);
  --surface-sky: rgba(186, 230, 253, 0.4);
  --surface-green: rgba(134, 239, 172, 0.4);
  --surface-orange: rgba(253, 186, 116, 0.4);

  /* Text */
  --text-primary: #212121;
  --text-secondary: #52525b;
  --text-white: #ffffff;
  /* Muted text: use opacity: 0.5 instead of a fixed color */

  /* Borders */
  --border-light: #e4e4e7;
  --border-dark: #000000;
}
```

## Usage Guidelines

- Use **category colors** sparingly for emphasis, not as primary backgrounds for large sections
- Prefer **cream/warm backgrounds** over pure white for a softer, more approachable feel
- Maintain **sufficient contrast** between text and backgrounds
- Use **dark backgrounds** for footers, callouts, or to create visual separation
