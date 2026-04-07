# Layout Decision Guide

Reference for resolving ambiguous slide type mappings during Phase 3 approval.

## Table of Contents

- [When to Show Layout Options](#when-to-show-layout-options)
  - [Unambiguous (No Choice Needed)](#unambiguous-no-choice-needed)
- [Ambiguity Categories](#ambiguity-categories)
  - [1. Statement Slides](#1-statement-slides)
  - [2. Image + Text Layouts](#2-image--text-layouts)
  - [3. Multi-Column Layouts (3 Items)](#3-multi-column-layouts-3-items)
  - [4. Multi-Column Layouts (2 Items)](#4-multi-column-layouts-2-items)
  - [5. Data Presentation](#5-data-presentation)
  - [6. Process / Sequential Steps](#6-process--sequential-steps)
- [Usage in Phase 3](#usage-in-phase-3)

## When to Show Layout Options

Only present choices when content could validly map to multiple layouts. For unambiguous content, just list the slide in the compact table.

### Unambiguous (No Choice Needed)

| Content | Layout | Index |
|---------|--------|-------|
| Presentation title | `title` | 0 |
| H1 section heading | `section-divider` | 2 |
| End of deck | `thank-you` | 23 |
| Script/dialogue format | `script-page` | 20 |
| Storyboard frames | `storyboard-8` | 21 |
| 5 photos with captions | `photo-gallery-5` | 9 |

---

## Ambiguity Categories

### 1. Statement Slides

**Trigger**: Blockquote content (`>` in markdown) or key insight text

**Options**:

| Option | Index | Visual | Best For |
|--------|-------|--------|----------|
| `statement-dark` | 4 | Black bg, cyan text, sidebar | Bold declarations, serious tone |
| `statement-light` | 5 | Cyan bg, black text | Optimistic, bright tone |
| `break-light` | 3 | Cyan bg, centered, no quotes | Transition, bridge between sections |

**Default**: `statement-dark`

**Compact ASCII**:
```
[A] statement-dark   [B] statement-light  [C] break-light
┌────────────────┐   ┌────────────────┐   ┌────────────────┐
│░░░░░░░░░░░│▌│░│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
│░ "{{txt}}" │▌│░│   │▓ "{{txt}}" ▓▓▓▓│   │▓▓▓ {{txt}} ▓▓▓▓│
│░░░░░░░░░░░│▌│░│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
└────────────────┘   └────────────────┘   └────────────────┘
 Black, bold          Cyan, bright         Transition
```

---

### 2. Image + Text Layouts

**Trigger**: Text content paired with an image reference

**Options**:

| Option | Index | Visual | Best For |
|--------|-------|--------|----------|
| `text-image-right` | 15 | White bg, text left, image right | Editorial focus, reading-first |
| `image-text-right` | 16 | Cyan accent, image left, text right | Visual feature highlight |
| `fullbleed-image` | 17 | Full photo with text overlay | Hero impact, minimal text |

**Default**: `text-image-right`

**Compact ASCII**:
```
[A] text-image-right [B] image-text-right [C] fullbleed-image
┌────────┬───────┐   ┌───────┬────────┐   ┌────────────────┐
│ HEAD   │       │   │▓▓▓▓▓▓▓│ HEAD   │   │▒▒▒▒▒▒▒▒▒▒▒│▌│▒│
│ body   │ [IMG] │   │▓[IMG]▓│ body   │   │▒▒ {{txt}} │▌│▒│
│ ...    │       │   │▓▓▓▓▓▓▓│ ...    │   │▒▒▒▒▒▒▒▒▒▒▒│▌│▒│
└────────┴───────┘   └───────┴────────┘   └────────────────┘
 Text focus           Image focus          Visual impact
```

---

### 3. Multi-Column Layouts (3 Items)

**Trigger**: 3 parallel items, features, or concepts

**Options**:

| Option | Index | Visual | Best For |
|--------|-------|--------|----------|
| `three-column-text` | 6 | White bg, heading + body per column | Dense text, detailed info |
| `three-column-images` | 7 | White bg, image + heading + body | Visual items with descriptions |
| `three-column-bubbles` | 10 | White bg, bubble tags + body | Features with visual indicators |
| `solid-bubbles` | 11 | Cyan bg, 3 bubbles + text | Key highlights, visual emphasis |

**Default**: `three-column-text`

**Compact ASCII**:
```
[A] 3-col-text       [B] 3-col-bubbles    [C] solid-bubbles
┌────────────────┐   ┌────────────────┐   ┌────────────────┐
│ TITLE          │   │ TITLE          │   │▓▓ TITLE ▓▓▓▓▓▓│
├────┬────┬──────┤   ├────┬────┬──────┤   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
│ H1 │ H2 │ H3   │   │(1) │(2) │(3)   │   │▓ (1) (2) (3) ▓▓│
│txt │txt │txt   │   │txt │txt │txt   │   │▓ txt txt txt ▓▓│
└────┴────┴──────┘   └────┴────┴──────┘   └────────────────┘
 Dense text           Tagged items         Key highlights
```

---

### 4. Multi-Column Layouts (2 Items)

**Trigger**: 2 parallel items or comparison

**Options**:

| Option | Index | Visual | Best For |
|--------|-------|--------|----------|
| `two-column-text` | 8 | White bg, two equal columns | Parallel points |
| `two-panel-compare` | 14 | Split cyan/white, structured | Side-by-side comparison |

**Default**: `two-column-text`

**Compact ASCII**:
```
[A] two-column-text  [B] two-panel-compare
┌────────────────┐   ┌────────────────┐
│ TITLE          │   │▓▓▓▓▓▓▓▓│       │
├───────┬────────┤   ├────────┼───────┤
│ H1    │ H2     │   │▓ LEFT  │ RIGHT │
│ body  │ body   │   │▓ items │ items │
└───────┴────────┘   └────────┴───────┘
 Parallel points      Structured compare
```

---

### 5. Data Presentation

**Trigger**: Numeric values with labels (e.g., "47%", "$143B", "3.2x")

**Options**:

| Option | Index | Visual | Best For |
|--------|-------|--------|----------|
| `statistics-grid` | 12 | Split black/cyan, up to 6 stats | Multiple metrics showcase |
| `solid-bubbles` | 11 | Cyan bg, 3 large values | 3 key metrics with context |
| `numbered-rows` | 13 | Numbered sections | Metrics with detailed breakdown |

**Default**: `statistics-grid` (up to 6 stats), `solid-bubbles` (3 stats)

**Compact ASCII**:
```
[A] statistics-grid  [B] solid-bubbles    [C] numbered-rows
┌───────┬────────┐   ┌────────────────┐   ┌────────────────┐
│░TITLE░│▓ 47%  ▓│   │▓▓ TITLE ▓▓▓▓▓▓│   │▓ 01 TITLE ▓│▌│▓│
│░desc ░│▓ 3.2x ▓│   │▓(47%)(3.2x)($)▓│   │ H1    │ H2  │▌│
│░░░│▌│░│▓ $143B▓│   │▓ txt txt txt ▓▓│   │ body  │ body│▌│
└───────┴────────┘   └────────────────┘   └────────────────┘
 Multi-stat grid      Visual metrics       Detailed breakdown
```

---

### 6. Process / Sequential Steps

**Trigger**: Numbered steps, phases, or sequential workflow

**Options**:

| Option | Index | Visual | Best For |
|--------|-------|--------|----------|
| `numbered-rows` | 13 | 2 numbered sections with columns | 2 high-detail steps |
| `timeline-process` | 22 | 6 steps with image + callouts | 3-6 step visual workflow |

**Default**: `numbered-rows` (2 steps), `timeline-process` (3+ steps)

**Compact ASCII**:
```
[A] numbered-rows    [B] timeline-process
┌────────────────┐   ┌────────────────┐
│▓ 01 STEP ONE▓▓│   │▓▓ HEADER ▓▓▓▓▓│
│ col1  │ col2  │   │▓[IMG]│ 1 2 3  │
│▓ 02 STEP TWO▓▓│   │▓▓▓▓▓▓│ 4 5 6  │
│ col1  │ col2  │   │▓▓▓▓▓▓│ >call  │
└────────────────┘   └────────────────┘
 2 detailed steps     Visual workflow
```

---

## Usage in Phase 3

1. **Parse content** and identify content type for each slide
2. **Check ambiguity**: Does content match an ambiguity trigger?
   - No: Add to unambiguous table
   - Yes: Queue for layout choice
3. **Present choices**: Show side-by-side ASCII with brief descriptions
4. **Apply selection**: Use chosen layout index in slide_specs
