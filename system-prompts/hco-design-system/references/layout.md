# Layout Patterns

## Table of Contents

- [Core Principles](#core-principles)
- [Spacing Scale](#spacing-scale)
- [Page Structure](#page-structure)
- [Common Layout Patterns](#common-layout-patterns)
  - [1. Centered Content](#1-centered-content)
  - [2. Sidebar + Content](#2-sidebar--content)
  - [3. Card Grid](#3-card-grid)
  - [4. Stacked List](#4-stacked-list)
  - [5. Multi-Column](#5-multi-column)
- [Responsive Considerations](#responsive-considerations)
- [Container Widths](#container-widths)
- [Z-Index Scale](#z-index-scale)

## Core Principles

1. **Generous spacing** — Use ample whitespace; when in doubt, add more
2. **Clear visual hierarchy** — Guide the eye with size, weight, and position
3. **Logical sections** — Group related content visually
4. **Progressive disclosure** — Show summary first, reveal details on demand

## Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| xs | 8px | Tight element gaps |
| sm | 16px | Related item spacing |
| md | 24px | Component internal padding |
| lg | 48px | Section gaps |
| xl | 64px | Page padding, major sections |
| xxl | 80-110px | Hero spacing |

## Page Structure

```css
.page {
  padding: 64px;  /* Generous page margins */
  display: flex;
  flex-direction: column;
  gap: 48px;      /* Space between major sections */
}
```

## Common Layout Patterns

### 1. Centered Content
Best for: Hero sections, titles, single-focus pages

```css
.layout-centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 64px;
}
```

### 2. Sidebar + Content
Best for: Category pages, galleries with context

```css
.layout-sidebar {
  display: flex;
  gap: 48px;
}

.sidebar {
  width: 100-150px;
  flex-shrink: 0;
  border-right: 4px solid var(--bg-dark);
  padding-right: 28px;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 48px;
}
```

### 3. Card Grid
Best for: Feature lists, comparisons, galleries

```css
.layout-cards {
  display: flex;
  gap: 16-24px;
}

.card {
  flex: 1;
  border-radius: 12-16px;
  padding: 24px;
  box-shadow: 0 4px 6px -4px rgba(0,0,0,0.1),
              0 10px 15px -3px rgba(0,0,0,0.1);
}
```

### 4. Stacked List
Best for: Roadmaps, numbered items, sequential content

```css
.layout-list {
  display: flex;
  flex-direction: column;
  gap: 0;  /* Items touch via borders */
  max-width: 800-900px;
}

.list-item {
  display: flex;
  align-items: flex-start;
  gap: 24px;
  padding: 40px 0;
  border-bottom: 1px solid var(--border-dark);
}
```

### 5. Multi-Column
Best for: Comparisons, progressive content, features

```css
.layout-columns {
  display: flex;
  gap: 48px;
}

.column {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
```

## Responsive Considerations

For web projects, adapt the fixed presentation dimensions:

```css
/* Base (mobile) */
.page { padding: 24px; }
.section-gap { gap: 32px; }

/* Tablet (768px+) */
@media (min-width: 768px) {
  .page { padding: 48px; }
  .section-gap { gap: 40px; }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .page { padding: 64px; }
  .section-gap { gap: 48px; }
}

/* Large (1440px+) */
@media (min-width: 1440px) {
  .page { max-width: 1440px; margin: 0 auto; }
}
```

## Container Widths

| Type | Width | Usage |
|------|-------|-------|
| Narrow | 600-800px | Text-heavy content |
| Medium | 900-1000px | Mixed content |
| Wide | 1200px | Cards, galleries |
| Full | 100% (max ~1800px) | Full-width layouts |

## Z-Index Scale

```css
:root {
  --z-base: 0;
  --z-raised: 1;
  --z-overlay: 10;
  --z-modal: 100;
  --z-tooltip: 1000;
}
```
