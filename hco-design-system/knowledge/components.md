# UI Components

## Table of Contents

- [Cards](#cards)
  - [Standard Card](#standard-card)
  - [Category Card](#category-card)
  - [Image Card](#image-card)
- [Chips & Tags](#chips--tags)
  - [Rounded Chip](#rounded-chip)
  - [Inline Text Box](#inline-text-box)
- [Buttons](#buttons)
  - [Primary Button](#primary-button)
- [Number Indicators](#number-indicators)
  - [Numbered Circle](#numbered-circle)
- [Callout Boxes](#callout-boxes)
  - [Overlay Box](#overlay-box)
  - [Decision Box](#decision-box)
- [Progress Indicators](#progress-indicators)
- [Vertical Text (Sidebar Labels)](#vertical-text-sidebar-labels)

## Cards

### Standard Card
```css
.card {
  background: var(--bg-light);
  border-radius: 16px;
  border: 2px solid var(--border-light);
  padding: 24px;
  box-shadow: 0 4px 6px -4px rgba(0,0,0,0.1),
              0 10px 15px -3px rgba(0,0,0,0.1);
}
```

### Category Card
```css
.card-category {
  padding: 24px;
  border-radius: 16px;
  outline: 3px solid currentColor;
  outline-offset: -3px;
}

.card-category--pink { background: var(--surface-pink); }
.card-category--sky { background: var(--surface-sky); }
.card-category--green { background: var(--surface-green); }
.card-category--orange { background: var(--surface-orange); }
```

### Image Card
```css
.card-image {
  background: var(--bg-dark);
  border-radius: 12px;
  overflow: hidden;
}

.card-image__media {
  width: 100%;
  aspect-ratio: 16/9;
  object-fit: cover;
}

.card-image__footer {
  padding: 14px 24px;
  background: var(--bg-dark);
}

.card-image__title {
  color: var(--text-white);
  font-weight: 700;
  font-size: 18px;
}

.card-image__description {
  color: rgba(255, 255, 255, 0.5);
  font-size: 14px;
}
```

## Chips & Tags

### Rounded Chip
```css
.chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 50px;
  font-family: var(--font-body);
  font-size: 18px;
  font-weight: 600;
  color: var(--text-primary);
  background: transparent;
  border: 2px solid var(--text-primary);
}

/* Color variants — mid-tone saturated hues for legibility */
.chip--pink   { color: #d946a8; border-color: #d946a8; }
.chip--sky    { color: #0284c7; border-color: #0284c7; }
.chip--green  { color: #16a34a; border-color: #16a34a; }
.chip--orange { color: #ea580c; border-color: #ea580c; }
```

### Inline Text Box
```css
.text-box {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 6px;
  font-weight: 500;
  line-height: 1.6;
}
```

## Buttons

### Primary Button
```css
.btn {
  font-family: var(--font-body);
  font-size: 18px;
  font-weight: 600;
  padding: 16px 32px;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.btn--primary {
  background: var(--bg-dark);
  color: var(--text-white);
}

.btn--secondary {
  background: var(--bg-light);
  color: var(--text-primary);
  border: 2px solid var(--border-dark);
}
```

## Number Indicators

### Numbered Circle
```css
.number-circle {
  width: 48px;
  height: 48px;
  background: var(--bg-dark);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.number-circle__text {
  font-family: var(--font-body);
  font-weight: 600;
  font-size: 20px;
  color: var(--text-white);
}
```

## Callout Boxes

### Overlay Box
```css
.callout {
  background: rgba(255, 191, 232, 0.5);
  mix-blend-mode: multiply;
  border-radius: 8px;
  padding: 12px 24px;
}

.callout__text {
  font-size: 18px;
  line-height: 1.5;
  color: var(--text-secondary);
}
```

### Decision Box
```css
.decision-box {
  background: var(--bg-light);
  border-radius: 12px;
  padding: 24px 32px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 2.5px 5px -2.5px rgba(0,0,0,0.1),
              0 5px 7.5px -1.25px rgba(0,0,0,0.1);
  outline: 2.5px solid #d4d4d8;
}

.decision-bullet {
  width: 16px;
  height: 16px;
  background: var(--bg-dark);
  border-radius: 50%;
  flex-shrink: 0;
}
```

## Progress Indicators

```css
.progress-indicator {
  position: fixed;
  bottom: 40px;
  right: 40px;
  background: var(--bg-light);
  padding: 12px 20px;
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  font-size: 16px;
  color: #666;
}

.progress-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  background: #D97643;
  border-radius: 50%;
  margin-left: 4px;
}
```

## Vertical Text (Sidebar Labels)

```css
.vertical-label {
  font-family: var(--font-display);
  font-size: 70px;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: -0.01em;
  transform: rotate(270deg);
  transform-origin: center center;
  white-space: nowrap;
}
```
