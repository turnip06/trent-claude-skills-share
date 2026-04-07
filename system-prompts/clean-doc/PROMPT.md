# Document Styling

Apply this design system to any document output for professional presentation.

## Core Principles

1. **Neutral-first palette** - Primarily grayscale with subtle semantic accents
2. **Generous spacing** - Increased padding for comfortable reading
3. **Limited type scale** - 4 sizes maximum (12px, 14px, 16px, 20px)
4. **Weight hierarchy** - Use font weight (not size) for most hierarchy
5. **Selective rounding** - Full radius for interactive elements, moderate for containers

## Critical Rules

### No Em Dashes
Never use em dashes. Use hyphens or rewrite.
```
Wrong: "Cards have 8px radius — perfect for containers"
Right: "Cards have 8px radius - perfect for containers"
```

### No Emoji Icons
Use inline SVG (Lucide-style) instead of emoji.
```html
<!-- Wrong: <span>📦</span> -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
</svg>
```

### Prevent Page Breaks
All components must have `page-break-inside: avoid; break-inside: avoid;`

## Design Tokens

### Typography
```
Font: 'Manrope', sans-serif
Sizes: 12px (xs) | 14px (sm) | 16px (base) | 20px (xl)
Weights: 400 | 500 | 600 | 700
Line Heights: 1.25 | 1.5 | 1.625
```

### Colours
```
Neutrals: #fafafa #f5f5f5 #e5e5e5 #d4d4d4 #a3a3a3 #737373 #525252 #404040 #262626 #171717

Semantic:
  Success: bg #f0fdf4 | text #166534 | border #bbf7d0
  Warning: bg #fffbeb | text #92400e | border #fde68a
  Info:    bg #eff6ff | text #1e40af | border #bfdbfe
```

### Spacing
`4px | 8px | 12px | 16px | 20px | 24px | 32px | 40px`

### Border Radius
`2px (sm) | 6px (md) | 8px (lg) | 9999px (full)`

## Component CSS

### Icons
```css
.icon { width: 20px; height: 20px; flex-shrink: 0; display: inline-block; vertical-align: middle; }
.icon-lg { width: 24px; height: 24px; }
```

### Callouts
```css
.callout {
  display: flex; gap: 16px; padding: 24px; border-radius: 8px;
  border: 1px solid #d4d4d4; background: #f5f5f5; color: #262626;
  margin: 24px 0; page-break-inside: avoid; break-inside: avoid;
}
.callout-neutral { background: #fafafa; border-color: #e5e5e5; color: #404040; }
```

### Cards
```css
.card {
  background: white; border: 1px solid #e5e5e5; border-radius: 8px;
  padding: 32px; margin: 24px 0; box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  page-break-inside: avoid; break-inside: avoid;
}
.card-title {
  font-size: 16px; font-weight: 700; color: #171717;
  margin-bottom: 16px; display: flex; align-items: center; gap: 12px;
}
```

### Tables (No Border Radius)
```css
table { width: 100%; border-collapse: collapse; margin: 24px 0; page-break-inside: avoid; }
th {
  padding: 12px 16px; font-size: 12px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.05em; color: #525252;
  background: #f5f5f5; border: 1px solid #e5e5e5; text-align: left;
}
td { padding: 12px 16px; font-size: 14px; color: #171717; border: 1px solid #e5e5e5; }
```

### Code Blocks (Single Background)
```css
.code-block {
  background: #171717; border-radius: 8px; margin: 24px 0;
  page-break-inside: avoid; break-inside: avoid;
}
.code-label { padding: 16px 24px 0; font-size: 12px; color: #a3a3a3; }
.code-block code {
  display: block; padding: 16px 24px 24px;
  font-family: 'Menlo', monospace; font-size: 13px; color: #f5f5f5;
  line-height: 1.625; white-space: pre-wrap; background: transparent;
}
```

### Badges (Inline, Coloured)
```css
.badge {
  display: inline-block; padding: 6px 14px; border-radius: 9999px;
  font-size: 12px; font-weight: 500; border: 1px solid; margin-right: 8px;
}
.badge-default { background: #f5f5f5; color: #404040; border-color: #e5e5e5; }
.badge-success { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }
.badge-warning { background: #fffbeb; color: #92400e; border-color: #fde68a; }
.badge-info { background: #eff6ff; color: #1e40af; border-color: #bfdbfe; }
```

### Grids
```css
.grid-2 {
  display: grid; grid-template-columns: 1fr 1fr; gap: 24px;
  margin: 24px 0; page-break-inside: avoid; break-inside: avoid;
}
```

## PDF Requirements

### Font Embedding (WeasyPrint)
```css
@font-face { font-family: 'Manrope'; src: url('fonts/Manrope-Regular.ttf'); font-weight: 400; }
@font-face { font-family: 'Manrope'; src: url('fonts/Manrope-Medium.ttf'); font-weight: 500; }
@font-face { font-family: 'Manrope'; src: url('fonts/Manrope-SemiBold.ttf'); font-weight: 600; }
@font-face { font-family: 'Manrope'; src: url('fonts/Manrope-Bold.ttf'); font-weight: 700; }
```

### Page Setup
```css
@page { size: A4; margin: 25mm; }
.title-page { text-align: center; padding: 60px 0 40px; border-bottom: 1px solid #e5e5e5; }
```

## Common Lucide Icon Paths

```html
<!-- Info -->
<circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>

<!-- Checkmark -->
<polyline points="20 6 9 17 4 12"/>

<!-- Warning -->
<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
<line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>

<!-- Lightbulb -->
<line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/>
<path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>

<!-- Box -->
<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
```

## Checklist Before Output

- [ ] No em dashes in text
- [ ] All icons are inline SVG
- [ ] Fonts embedded with @font-face (not CDN)
- [ ] Tables use simple borders (no border-radius)
- [ ] Code blocks have single background colour
- [ ] Badges are inline-block with colour tints
- [ ] All containers have page-break-inside: avoid
- [ ] Title page has compact spacing (60px)
