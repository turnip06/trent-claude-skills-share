# Design Principles — Slide Designer

The audience is designers. Every slide must look like a designer made it. No generic AI aesthetics, no template energy, no "good enough."

## Table of Contents

- [Visual Language](#visual-language)
- [The Signposting System (Consistent Across Every Slide)](#the-signposting-system-consistent-across-every-slide)
  - [Elements](#elements)
  - [Rules](#rules)
  - [Implementation](#implementation)
- [Typography](#typography)
  - [Font Stack](#font-stack)
  - [Type Rules](#type-rules)
  - [Type as Design](#type-as-design)
  - [Text as Texture](#text-as-texture)
- [Color System](#color-system)
  - [Primary Palette (Dark Mode — Default)](#primary-palette-dark-mode--default)
  - [Bold Color Slides (Use Sparingly — 2-4 Per Deck)](#bold-color-slides-use-sparingly--2-4-per-deck)
  - [Accent Colors (On Dark Slides)](#accent-colors-on-dark-slides)
  - [Color Rules](#color-rules)
- [Layout](#layout)
  - [Grid & Spacing](#grid--spacing)
  - [Composition Patterns](#composition-patterns)
  - [Each Slide Is Different (But Connected)](#each-slide-is-different-but-connected)
  - [What to Avoid](#what-to-avoid)
- [Image Slides](#image-slides)
  - [Background Images](#background-images)
  - [Screen Recording Placeholders](#screen-recording-placeholders)
- [Micro-Graphics & Detail Elements](#micro-graphics--detail-elements)
- [Transitions & Polish](#transitions--polish)
- [Anti-Patterns (Things That Scream "AI Made This")](#anti-patterns-things-that-scream-ai-made-this)

## Visual Language

**Mood:** Bold, expressive, contemporary graphic design. Not safe corporate keynote — closer to an agency portfolio, a zine, or a gallery poster. Each slide should feel like it could exist as a standalone piece of graphic design.

**References:** Acid Graphics, Neo-Brutalism, Kinetic Editorial. Think ClubRare identity, Holographik studio work, Swiss Punk typography. Confident, slightly raw, unapologetically graphic.

**Venue context:** Bar in Surry Hills. Projected. Dim lighting. People holding beers. Slides must read from the back of the room and hold attention against ambient noise and conversation.

## The Signposting System (Consistent Across Every Slide)

This is the connective tissue of the deck. While each slide gets its own compositional personality, a **persistent micro-typography system** appears on every slide in consistent positions. This creates cohesion without monotony.

### Elements

- **Top-left:** Speaker name or event identifier in small caps (`TRENT MICHAEL` or `PROCESS 002`), 12–14px, uppercase, tracked wide (0.1em+)
- **Top-center or top-right:** Section label (`THE BORING STUFF` / `NEW TERRITORY` / `ACTUAL CREATIVE WORK` / `THE HONEST BIT`), same small caps treatment, updates per act
- **Bottom-right:** Slide number, monospaced or tabular, subtle (`01` / `14` / `27`)
- **Optional top-right:** A consistent micro-detail — could be a date (`05.03.26`), a category label (`CRAFT` / `INDUSTRY` / `PRACTICAL`), or a URL

### Rules

- Always the same typeface, same weight (400–500), same size range (12–16px)
- Always `--text-muted` color or similar low-contrast treatment — visible on close inspection, invisible at a glance
- Fixed positions on every slide. Never moves. This is the grid the audience unconsciously learns.
- On dark slides: `rgba(255,255,255,0.25)`. On light/colored slides: `rgba(0,0,0,0.3)`.
- These elements should feel like metadata — printed on the slide, not designed into it. Think receipt text, technical annotations, specimen sheet margins.

### Implementation

```html
<!-- Signposting layer — same on every slide -->
<div class="slide-meta">
  <span class="meta-tl">TRENT MICHAEL</span>
  <span class="meta-tc">THE BORING STUFF</span>
  <span class="meta-br">06</span>
</div>
```

```css
.slide-meta {
  position: absolute;
  inset: 0;
  padding: 40px 60px;
  pointer-events: none;
  z-index: 10;
}
.slide-meta span {
  position: absolute;
  font-family: var(--font-body);
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.25);
}
.meta-tl { top: 40px; left: 60px; }
.meta-tc { top: 40px; left: 50%; transform: translateX(-50%); }
.meta-br { bottom: 40px; right: 60px; }
```

## Typography

### Font Stack

- **Display / Headlines:** Use a bold, characterful sans-serif. Recommendations in order:
  - `"Space Grotesk"` (Google Fonts) — geometric, slightly quirky, great at large sizes
  - `"Inter"` weight 800–900 — clean, professional, excellent metrics
  - For maximum impact slides, consider ultra-condensed display weight — type that fills the frame edge-to-edge like the "Cinematic Approach" reference
- **Body / Secondary:** `"Inter"` 400–500 or `"Space Grotesk"` 400
- **Micro-detail / Signposting:** `"Inter"` 400–500, small, tracked wide
- Load via Google Fonts CDN in the HTML

### Type Rules

- **Headlines: BIG.** Minimum 80px for main statements. 120–200px for single-word or short-phrase slides. On maximum-impact slides, type can go edge-to-edge at 200–300px+, filling the entire frame.
- **Extreme scale contrast.** The reference slides mix 200px+ display type with 12px metadata on the same canvas. This contrast IS the design. Don't be afraid of tiny text next to massive text.
- **Uppercase sparingly.** Use for section title cards and signposting only. Mixed case for statements and quotes.
- **Letter-spacing:** Tight on headlines (-0.02em to -0.04em). Wide on micro-text (0.08em to 0.15em). This contrast reinforces hierarchy.
- **Line-height:** Headlines 0.85–0.95 (tight, stacked lines should nearly touch). Body 1.4–1.6.
- **Max width:** Body text never wider than 900px. Headlines can span full width or even bleed off-edge.
- **No orphans.** If a headline wraps, control where it breaks. Use `<br>` to force intentional line breaks.
- **Weight contrast:** Use weight to create hierarchy. Bold + Light in the same slide creates natural emphasis.

### Type as Design

On typography-only slides, the text IS the visual:
- Type can fill the entire slide — letters cropped by the frame edge, like a zoomed-in poster
- Vary scale dramatically (one word huge, the rest small — see ClubRare reference)
- Layer text at different opacities or colors for depth
- Consider text interacting with imagery — type behind/in front of photos, masked by images
- A single word at 250px that bleeds off the bottom of the frame is more powerful than a neatly centered paragraph

### Text as Texture

Small type can function as a visual element, not just information:
- Blocks of tiny metadata-style text (like the ClubRare header row) create visual texture
- Justified small text in grid blocks reads as a design element at presentation distance
- Caption-style annotations near images or key moments add editorial credibility
- This is where the signposting system earns its keep — it's not just wayfinding, it's graphic design

## Color System

### Primary Palette (Dark Mode — Default)

```css
--bg-dark: #0a0a0a;        /* Near-black — default slide background */
--bg-pure-black: #000000;   /* True black — for maximum contrast / pause moments */
--text-primary: #ffffff;     /* White — primary text on dark */
--text-secondary: #888888;   /* Mid-grey — supporting text */
--text-muted: #555555;       /* Dark grey — subtle labels, signposting */
```

### Bold Color Slides (Use Sparingly — 2-4 Per Deck)

Not every slide needs to be dark. The references show that bold, saturated background colors create standout moments. Use these for section transitions, key statements, or emotional shifts.

```css
--bg-electric-yellow: #CCFF00;  /* Acid yellow — maximum energy, used for section breaks */
--bg-cobalt: #0038FF;           /* Deep blue — digital, confident */
--bg-olive: #4A5D23;            /* Muted olive — unexpected, earthy */
--bg-hot-pink: #FF1493;         /* Hot pink — bold accent slide */
```

When using bold backgrounds:
- Text goes dark (`#000000` or `#0a0a0a`) on light backgrounds
- Text goes white on dark colored backgrounds
- Signposting adjusts: `rgba(0,0,0,0.3)` on light, `rgba(255,255,255,0.25)` on dark
- One bold-color slide per section maximum. They're punctuation, not the sentence.

### Accent Colors (On Dark Slides)

```css
--accent-coral: #FF6B6B;    /* Warm coral — human, approachable */
--accent-cyan: #22D3EE;     /* Electric cyan — sharp, modern */
--accent-amber: #FFD93D;    /* Warm amber — attention, highlight */
--accent-violet: #A78BFA;   /* Soft violet — creative, unexpected */
```

### Color Rules

- **Dark backgrounds by default.** `#0a0a0a` for most slides.
- **Bold color for punctuation.** 2-4 slides in the deck get a saturated color background. These mark section transitions or key emotional moments.
- **One accent max per slide.** Accent colors highlight a single word or element.
- **Accent for meaning, not decoration.** If a word is accented, it should be the most important word.
- **No safe gradients.** No linear-gradient from teal to purple. If using a gradient, it's functional (dark overlay on images) not decorative.
- **Color clash is allowed.** The references use complementary color tension (olive + pink, blue + yellow). This is intentional dissonance, not a mistake.

## Layout

### Grid & Spacing

- **Slide dimensions:** 1920×1080px (16:9, fixed)
- **Signposting zone:** 40–60px from edges (where persistent meta lives)
- **Content zone:** Starts at 120px from edges (where main content lives)
- **But rules are meant to be broken.** On maximum-impact slides, content can push into the signposting zone or even bleed off-frame. The signposting stays consistent; the content is what varies.

### Composition Patterns

**Bottom-left anchor:** Statement text bottom-left, massive negative space above and right. Confident, editorial. Works for quotes and thesis statements.

**Full-frame type:** Headline fills the entire slide edge-to-edge. Ultra-condensed weight. Image or color visible through/behind the letterforms. (See "Cinematic Approach" reference.)

**Extreme negative space:** Tiny text block centered in a vast empty field. 95% of the canvas is empty. Conveys confidence and exclusivity. (See "Introducing 4:3" reference.)

**Centered single element:** One word or phrase dead center, large. Nothing else except signposting.

**Split composition:** Left 40% text, right 60% image (or vice versa). Clean dividing line or generous gap.

**Full-bleed image:** Image covers entire slide. Text overlaid with dark gradient or positioned in naturally dark area.

**Stacked hierarchy:** Large headline top, smaller supporting text below with generous gap (48–80px). Both left-aligned.

### Each Slide Is Different (But Connected)

This is the critical principle. The references show slides that are compositionally distinct — one is 95% negative space, the next fills every pixel with type, the next layers image and text. What makes them feel like a deck:

1. The **signposting system** appears in the same positions on every slide
2. The **type palette** is consistent (same display + body fonts throughout)
3. The **color logic** follows a pattern (dark default, bold color for transitions)
4. The **level of craft** is consistent (every slide feels equally considered)

Don't make every slide the same layout. Make every slide the best version of what that content needs, then let the signposting system tie them together.

### What to Avoid

- **Same layout repeated.** If three slides in a row use the same composition, redesign one.
- **Centered everything.** Centering is the default of people who can't compose. Use it only for the extreme-negative-space pattern.
- **Even spacing.** Asymmetry is more dynamic. Unequal margins create visual tension.
- **Floating text.** Every text element should feel anchored — to an edge, to a grid line, to another element.
- **Busy slides.** If there are more than 3 content elements on a slide (excluding signposting), remove one.
- **Drop shadows, glows, soft borders.** These are crutches. Use contrast and space instead.

## Image Slides

### Background Images

- Apply a dark gradient overlay for text readability, but the gradient can be directional (heavier where text sits)
- Images can interact with type — type in front of AND behind images (layering/masking)
- High-contrast, desaturated, or monochrome images won't compete with text
- Full-bleed images should feel cinematic, not stock

### Screen Recording Placeholders

For slides that will contain screen recordings:
- Show a styled container (dark rounded rectangle, subtle border)
- Include the signposting system as normal
- A minimal play icon (CSS triangle in circle) centered in the container
- Small label: `SCREEN RECORDING` in muted metadata style
- Maybe include a duration hint: `≤45s` in the same metadata style
- The placeholder should feel designed, like a film slate — not like missing content

## Micro-Graphics & Detail Elements

Beyond the signposting text, consider small graphic elements that add craft:

- **Thin rules/lines** — A 1px horizontal line spanning part of the slide, separating zones or adding structure
- **Small geometric marks** — A tiny circle, square, or dash used as a bullet alternative or section marker
- **Bracket/parenthetical details** — `(01/27)` or `[CRAFT]` style annotations near content
- **Underscored keywords** — Small underline on a key word in small supporting text (see "ALWAYS" and "BRING" in the Cinematic reference)

These details are invisible from the back of the room but reward the people in the front row. They signal craft to the designers in the audience.

## Transitions & Polish

- No CSS animations — slides are static frames designed for screenshotting and projection
- Design each slide as if it will appear suddenly — it needs to work at first glance
- **Visual rhythm across the deck:** Vary density, alternate type-heavy and image-heavy, punctuate with bold color
- After every 4-5 dense slides, give the audience a breather (negative space, simple statement, black slide)

## Anti-Patterns (Things That Scream "AI Made This")

- Perfectly centered text with equal margins on all sides
- Generic color choices (pure blue `#0000FF`, pure red `#FF0000`)
- Every slide using the same safe composition
- Evenly spaced bullet points
- Safe gradient backgrounds
- Everything at the same medium scale (no extreme small, no extreme large)
- Rounded corners on everything
- Stock-photo-energy imagery
- No signposting or micro-detail — just headline + nothing
- Slides that feel "placed" rather than "composed"
- Playing it safe when the content calls for boldness
