# Image Guidelines

## Table of Contents

- [When to Use Images](#when-to-use-images)
- [Placeholder Images](#placeholder-images)
  - [Common Categories](#common-categories)
- [Image Styling](#image-styling)
  - [Standard Image Container](#standard-image-container)
  - [Aspect Ratios](#aspect-ratios)
  - [Image with Dark Overlay](#image-with-dark-overlay)
- [Icon Usage](#icon-usage)
  - [SVG Icons](#svg-icons)
- [Background Patterns](#background-patterns)
  - [Subtle Texture](#subtle-texture)
  - [Gradient Background](#gradient-background)
- [Accessibility](#accessibility)

## When to Use Images

- **Hero sections** — Set the visual tone
- **Feature showcases** — Demonstrate concepts visually
- **Galleries** — Compare options side by side
- **Breaking up text** — Add visual interest to long content
- **Data visualization** — Explain complex ideas

## Placeholder Images

Use Unsplash for high-quality placeholders:

```html
<!-- Random image at specific dimensions -->
<img src="https://source.unsplash.com/800x600" alt="Description">

<!-- Specific category -->
<img src="https://source.unsplash.com/800x600/?nature" alt="Nature scene">
<img src="https://source.unsplash.com/800x600/?technology" alt="Technology">
<img src="https://source.unsplash.com/800x600/?business" alt="Business">

<!-- Specific image by ID (consistent) -->
<img src="https://images.unsplash.com/photo-{ID}?w=800&h=600&fit=crop" alt="Description">
```

### Common Categories
- `?nature` — Landscapes, organic textures
- `?technology` — Devices, abstract tech
- `?business` — Professional, corporate
- `?minimal` — Clean, simple compositions
- `?texture` — Backgrounds, patterns
- `?architecture` — Buildings, structures

## Image Styling

### Standard Image Container
```css
.image-container {
  border-radius: 12px;
  overflow: hidden;
}

.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}
```

### Aspect Ratios
```css
.aspect-16-9 { aspect-ratio: 16/9; }
.aspect-4-3 { aspect-ratio: 4/3; }
.aspect-1-1 { aspect-ratio: 1/1; }
.aspect-3-4 { aspect-ratio: 3/4; }
```

### Image with Dark Overlay
```css
.image-overlay {
  position: relative;
}

.image-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to top,
    rgba(33, 33, 33, 0.8) 0%,
    transparent 50%
  );
}
```

## Icon Usage

### SVG Icons
Prefer inline SVGs for flexibility:

```html
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
  <!-- paths -->
</svg>
```

```css
.icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.icon--sm { width: 16px; height: 16px; }
.icon--md { width: 24px; height: 24px; }
.icon--lg { width: 40px; height: 40px; }
.icon--xl { width: 80px; height: 80px; }
```

## Background Patterns

### Subtle Texture
```css
.bg-texture {
  background-color: var(--bg-cream);
  background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23000000' fill-opacity='0.02'%3E%3Ccircle cx='1' cy='1' r='1'/%3E%3C/g%3E%3C/svg%3E");
}
```

### Gradient Background
```css
.bg-gradient {
  background: linear-gradient(
    135deg,
    var(--bg-cream) 0%,
    var(--bg-warm) 100%
  );
}
```

## Accessibility

- Always provide meaningful `alt` text
- Use `alt=""` for decorative images
- Ensure sufficient color contrast over images
- Provide text alternatives for image-only content

```html
<!-- Informative image -->
<img src="chart.png" alt="Sales increased 25% in Q4 2024">

<!-- Decorative image -->
<img src="decoration.png" alt="" role="presentation">
```
