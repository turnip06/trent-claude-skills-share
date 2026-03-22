# H+Co Design System

Howatson+Company's visual language: **sleek, modern, novel, entertaining, and cool.**

## The H+Co Vibe

H+Co design is warm and approachable but never boring. Every output should feel polished, interactive, and delightful. Surprise users with thoughtful details. Make them want to click around and explore.

**Core feel:** Cream backgrounds, bold uppercase headings, generous breathing room, and playful interactions.

## Quick Reference

**Fonts:**
- **Headings (≥ 40px):** VC Nudge ExtraBold, uppercase, letter-spacing: -0.01em
- **Headings (< 40px):** Manrope Bold (700) — VC Nudge not used below 40px
- **Body:** Manrope (400–700 weights)
- **Font file:** `fonts/VCNudge-ExtraBold.woff`

**Colors:**
- **Backgrounds:** Cream `#fff4e6`, Light `#fff7ed`, Dark `#212121` (no pure white surfaces)
- **Accents:** Pink `#ffbfe8`, Sky `#bae6fd`, Green `#86efac`, Orange `#fdba74`
- **Text:** Primary `#212121`, Secondary `#52525b`, muted via `opacity: 0.5`

**Spacing:** Generous always — 64px page margins, 48px section gaps, 24px component padding

## Design Principles

### 1. Clear Hierarchy
Make it instantly obvious what's important. One bold focal point per section. Large VC Nudge headings grab attention; subdued Manrope body text supports without competing.

### 2. Multi-Column Over Single Column
Favor layouts that use horizontal space. Cards in rows, sidebars with content, two or three columns — single column walls of text feel flat and boring. Adapt layout to content, not the other way around.

### 3. Progressive Disclosure
**Don't show everything at once.** Let users discover content through interaction. The initial view should be clean and scannable — reward curiosity by revealing depth as users explore.

**Patterns to consider:**
- **Summaries → Details** — Show the headline or key point; let users click to expand the full story
- **Accordions** — Stack related items vertically; one open at a time keeps focus clear
- **Tabs** — Perfect for organizing parallel content (e.g., "Overview / Features / Specs")
- **Expandable cards** — Show a preview; reveal more on hover or click
- **"Read more" links** — Truncate long text blocks; invite users to continue
- **Tooltips** — Surface helpful context on hover without cluttering the layout
- **Modals/Lightboxes** — For detailed views, galleries, or focused interactions
- **Staged reveals** — Show content in steps (Step 1 → Step 2 → Step 3) rather than all at once
- **Filters & toggles** — Let users choose what they want to see rather than showing everything

**Why it matters:** Users feel overwhelmed by walls of content. Progressive disclosure respects their attention, creates a sense of discovery, and makes complex information feel manageable.

### 4. Generous Whitespace
When in doubt, add more padding. Content needs room to breathe. Cramped layouts feel cheap; spacious layouts feel premium.

### 5. Warm, Not Stark
Cream backgrounds over pure white. The palette should feel inviting and approachable, never clinical.

## Interactivity & Delight

**For HTML documents and web artifacts, bring the page to life.** Static is boring. Every element is an opportunity to create a moment of surprise, satisfaction, or joy.

### Entrance & Motion
- **Staggered fade-ins** — Elements appear one after another on page load (0.1s delays between items)
- **Slide-ins** — Content enters from the side or bottom for a dynamic feel
- **Scroll-triggered reveals** — Elements animate into view as users scroll down
- **Subtle parallax** — Background elements move at different speeds for depth
- **Loading states** — Skeleton screens or gentle pulses while content loads

### Hover & Click Responses
- **Cards that lift** — Slight translateY and shadow increase on hover
- **Buttons that respond** — Scale up slightly, change color, show a ripple effect
- **Links that invite** — Underline animations, color shifts, arrow movements
- **Image zooms** — Subtle scale on hover for galleries and thumbnails
- **Icon animations** — Icons that wiggle, bounce, or transform on interaction

### Interactive Components
- **Accordions** — Smooth expand/collapse with rotation arrows; ideal for FAQs or nested info
- **Tab bars** — Clean switching between views; use an animated underline indicator
- **Carousels/Sliders** — For showcasing multiple items in limited space; include navigation dots
- **Interactive dropdowns** — Menus that fade in with a slight delay; feel intentional, not abrupt
- **Toggle switches** — For binary choices; animate the switch smoothly
- **Progress indicators** — Show completion status; fill bars or step indicators
- **Before/After sliders** — Drag to compare two states; great for showcasing transformations
- **Sticky navigation** — Headers that follow as users scroll; appear/hide gracefully

### Micro-interactions & Polish
- **Button click feedback** — Brief scale-down or color flash confirms the action
- **Form field focus** — Borders that glow or labels that float up
- **Success/Error states** — Checkmarks that draw themselves, gentle shakes for errors
- **Copy-to-clipboard** — "Copied!" tooltip that appears briefly
- **Number counters** — Values that count up when scrolled into view
- **Typing effects** — Text that appears letter by letter for emphasis

### Delightful Surprises
- **Easter eggs** — Hidden interactions that reward exploration (e.g., click a logo 5 times)
- **Confetti or particles** — Celebrate completions or achievements
- **Sound design** — Optional, subtle audio feedback (with user control)
- **Theme toggles** — Light/dark mode switches with smooth transitions
- **Cursor effects** — Custom cursors or trailing effects for special sections

**The philosophy:** Every interaction is a conversation. When users click, hover, or scroll, the page should respond in a way that feels alive and intentional. Flat, unresponsive pages feel like talking to a wall.

**Balance matters:** Delight should enhance, not distract. Keep animations smooth (0.2–0.4s), subtle (small movements), and purposeful (guiding attention). Avoid anything that feels chaotic or slows the experience.

## Layout Philosophy

Layouts are **guidelines, not rules**. Every use case is different. The reference patterns in [references/layout.md](references/layout.md) are starting points — adapt freely based on content needs.

**Principles over prescriptions:**
- Horizontal space is your friend (multi-column, cards, grids)
- Break up long content into scannable chunks
- Use visual boundaries (cards, dividers, background shifts) to group related items
- Let the content dictate the structure

## Module References

For detailed specifications, consult these files:

| Module | Path | Contents |
|--------|------|----------|
| Colors | [references/colors.md](references/colors.md) | Full palette, CSS variables |
| Typography | [references/typography.md](references/typography.md) | Fonts, sizes, heading styles |
| Layout | [references/layout.md](references/layout.md) | Spacing, patterns, responsive |
| Components | [references/components.md](references/components.md) | Cards, chips, buttons, etc. |
| Images | [references/images.md](references/images.md) | Placeholders, styling, icons |
| Animation | [references/animation.md](references/animation.md) | Motion, staggering, disclosure |

## Example: Minimal Page Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title</title>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    @font-face {
      font-family: 'VC Nudge';
      src: url('fonts/VCNudge-ExtraBold.woff') format('woff');
      font-weight: 800;
      font-display: swap;
    }

    :root {
      --font-display: 'VC Nudge', sans-serif;
      --font-body: 'Manrope', sans-serif;
      --bg-cream: #fff4e6;
      --text-primary: #212121;
      --text-secondary: #52525b;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: var(--font-body);
      background: var(--bg-cream);
      color: var(--text-secondary);
      line-height: 1.6;
    }

    .page {
      max-width: 1200px;
      margin: 0 auto;
      padding: 64px;
    }

    h1 {
      font-family: var(--font-display);
      font-size: clamp(48px, 8vw, 72px);
      text-transform: uppercase;
      color: var(--text-primary);
      line-height: 0.9;
      margin-bottom: 24px;
    }

    .lead {
      font-size: 24px;
      max-width: 600px;
      margin-bottom: 48px;
    }
  </style>
</head>
<body>
  <main class="page">
    <h1>Page Title</h1>
    <p class="lead">Supporting description text goes here.</p>
    <!-- Content sections -->
  </main>
</body>
</html>
```

## Remember

- **Interactive over static** — If it can be clicked, animated, or revealed, it should be
- **Layouts are flexible** — Adapt patterns to content, don't force content into patterns
- **Delight is the goal** — Every H+Co output should make users want to explore
- **VC Nudge sparingly** — It's distinctive; overuse dilutes impact
- **When in doubt: more padding, more columns, more interactivity**
