# Animation & Motion

## Table of Contents

- [Core Principles](#core-principles)
- [Timing Scale](#timing-scale)
- [Easing](#easing)
- [Common Animations](#common-animations)
  - [Fade In Up](#fade-in-up)
  - [Fade In Left](#fade-in-left)
  - [Scale In](#scale-in)
- [Staggered Animations](#staggered-animations)
  - [CSS Custom Property Approach](#css-custom-property-approach)
- [Hover Transitions](#hover-transitions)
- [Reduced Motion](#reduced-motion)
- [Progressive Disclosure](#progressive-disclosure)
  - [Summary/Details Pattern](#summarydetails-pattern)

## Core Principles

1. **Subtle and purposeful** — Animations should enhance, not distract
2. **Staggered reveals** — Build content progressively for visual interest
3. **Consistent timing** — Use a predictable rhythm
4. **Respect preferences** — Support reduced motion

## Timing Scale

| Token | Duration | Usage |
|-------|----------|-------|
| fast | 0.15s | Micro-interactions, hovers |
| normal | 0.3s | Standard transitions |
| slow | 0.6s | Page elements, reveals |
| slower | 0.8s | Hero animations |

## Easing

```css
:root {
  --ease-out: cubic-bezier(0.33, 1, 0.68, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

- **ease-out** — Default for most animations (elements arriving)
- **ease-in-out** — For continuous motion or loops
- **ease-spring** — For playful, bouncy interactions

## Common Animations

### Fade In Up
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-up {
  animation: fadeInUp 0.6s ease-out;
}
```

### Fade In Left
```css
@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.animate-fade-left {
  animation: fadeInLeft 0.6s ease-out;
}
```

### Scale In
```css
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-scale-in {
  animation: scaleIn 0.3s ease-out;
}
```

## Staggered Animations

For lists or grids, stagger each item:

```css
.stagger-item {
  opacity: 0;
  animation: fadeInUp 0.6s ease-out forwards;
}

.stagger-item:nth-child(1) { animation-delay: 0.1s; }
.stagger-item:nth-child(2) { animation-delay: 0.2s; }
.stagger-item:nth-child(3) { animation-delay: 0.3s; }
.stagger-item:nth-child(4) { animation-delay: 0.4s; }
.stagger-item:nth-child(5) { animation-delay: 0.5s; }
.stagger-item:nth-child(6) { animation-delay: 0.6s; }
```

### CSS Custom Property Approach
```css
.stagger-item {
  opacity: 0;
  animation: fadeInUp 0.6s ease-out forwards;
  animation-delay: calc(var(--index, 0) * 0.1s);
}
```

```html
<div class="stagger-item" style="--index: 0">First</div>
<div class="stagger-item" style="--index: 1">Second</div>
<div class="stagger-item" style="--index: 2">Third</div>
```

## Hover Transitions

```css
.hover-lift {
  transition: transform 0.2s ease-out, box-shadow 0.2s ease-out;
}

.hover-lift:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}
```

## Reduced Motion

Always respect user preferences:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Progressive Disclosure

For revealing content on interaction:

```css
.disclosure-trigger {
  cursor: pointer;
}

.disclosure-content {
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.3s ease-out, opacity 0.3s ease-out;
}

.disclosure-content.is-open {
  max-height: 500px; /* Adjust as needed */
  opacity: 1;
}
```

### Summary/Details Pattern
```html
<details class="disclosure">
  <summary class="disclosure-summary">View details</summary>
  <div class="disclosure-body">
    Expanded content here...
  </div>
</details>
```

```css
details.disclosure summary {
  cursor: pointer;
  font-weight: 600;
  padding: 16px 0;
}

details.disclosure[open] .disclosure-body {
  animation: fadeInUp 0.3s ease-out;
}
```
