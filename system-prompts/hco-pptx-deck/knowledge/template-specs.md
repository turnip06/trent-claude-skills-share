# Howatson+Company Template - Exact Specifications

## Table of Contents

- [Presentation Setup](#presentation-setup)
- [Typography System](#typography-system)
  - [Primary Fonts](#primary-fonts)
  - [Type Sizes (by slide type)](#type-sizes-by-slide-type)
- [Colour Palette (RGB Values)](#colour-palette-rgb-values)
  - [Colour Usage Rules](#colour-usage-rules)
- [Layout Specifications](#layout-specifications)
  - [Slide 1: Cover Slide](#slide-1-cover-slide)
  - [Slide 3: Section Divider](#slide-3-section-divider)
  - [Slide 7: 3-Column Content Slide](#slide-7-3-column-content-slide)
  - [Slide 10: 5-Column Image Grid](#slide-10-5-column-image-grid)
  - [Slide 16: Split Image/Text Layout](#slide-16-split-imagetext-layout)
  - [Slide 22: Video Storyboard Grid](#slide-22-video-storyboard-grid)
- [Vertical Branding Element (Standard on Most Slides)](#vertical-branding-element-standard-on-most-slides)
- [Critical Implementation Rules (python-pptx)](#critical-implementation-rules-python-pptx)
  - [Font Names](#font-names)
  - [Multi-Line Text](#multi-line-text)
  - [Shadow Removal (MANDATORY)](#shadow-removal-mandatory)
  - [Sidebar Rules](#sidebar-rules)
  - [Underlines](#underlines)
  - [Section Divider Headlines](#section-divider-headlines)
- [Grid System](#grid-system)
- [Common Element Specifications](#common-element-specifications)
  - [Underlines (Heading Dividers)](#underlines-heading-dividers)
  - [Rounded Buttons (Download Links)](#rounded-buttons-download-links)
  - [Image Treatments](#image-treatments)
- [Implementation Notes](#implementation-notes)
  - [Working with VC Nudge Black Font](#working-with-vc-nudge-black-font)
  - [Working with Manrope Font](#working-with-manrope-font)
  - [Embedding Fonts in PPTX](#embedding-fonts-in-pptx)
- [Quality Control Checklist](#quality-control-checklist)
- [EMU Reference (for python-pptx)](#emu-reference-for-python-pptx)

## Presentation Setup

**Slide Dimensions:**
- Width: 13.33 inches (33.87 cm) [12,192,000 EMUs]
- Height: 7.5 inches (19.05 cm) [6,858,000 EMUs]
- Aspect Ratio: 16:9
- Orientation: Landscape

**Guides/Margins:**
- Left margin: 0.37 inches
- Right margin: 0.37 inches  
- Top margin: 0.36 inches
- Bottom margin: 0.36 inches
- Content area: ~12.59" × 6.78"

## Typography System

### Primary Fonts

**VC Nudge Black** (Condensed sans-serif)
- Use for: All headlines, section numbers, display type
- Weight: Regular (naturally ultra-bold and condensed)
- Always uppercase
- Tracking: Tight (0 or negative)

**Manrope Light**
- Use for: Body text, subheadings, secondary content
- Weights: Light (300), Regular (400), Bold (700)
- Regular case (sentence case or title case)

**IBM Plex Mono** or **Suisse Int'l**
- Use for: Small labels, captions, technical text
- Usually uppercase
- 8-10pt size

### Type Sizes (by slide type)

**Cover Slide (Slide 1):**
- Main display text: 180-220pt (VC Nudge Black)
- Client name: 28pt (VC Nudge Black, uppercase)
- Presentation name: 28pt (VC Nudge Black, uppercase)

**Section Divider (Slide 3):**
- Section number: 350-400pt (VC Nudge Black)
- Section title: 80-90pt (VC Nudge Black, uppercase)

**Content Headlines:**
- Primary headline: 60-80pt (VC Nudge Black, uppercase)
- Secondary headline ("Heading 2"): 20-24pt (Manrope)

**Body Text:**
- Primary: 16-18pt (Manrope Light)
- Secondary: 14pt (Manrope Light)

**Captions/Labels:**
- Small labels: 8-10pt (IBM Plex Mono or Suisse Int'l)

## Colour Palette (RGB Values)

```
BLACK:   #000000  (0, 0, 0)
WHITE:   #FFFFFF  (255, 255, 255)
BEIGE:   #EDDAC1  (237, 218, 193)
GREY:    #E0E0E0  (224, 224, 224)

CYAN:    #76DBEC  (118, 219, 236)
BLUE:    #3D72FE  (61, 114, 254)
LIME:    #E0EA53  (224, 234, 83)
RED:     #FF4F4D  (255, 79, 77)
PINK:    #E972E2  (233, 114, 226)
GREEN:   #00B948  (0, 185, 72)
```

### Colour Usage Rules

- **Black backgrounds:** Cover slides, high-impact slides
- **White backgrounds:** Content-heavy slides, text-focused pages
- **Accent colour backgrounds:** Section dividers, emphasis slides
- **Pair accent colours with black** text or shapes (never with white text)
- **Use beige** for placeholders, soft backgrounds, video frames

## Layout Specifications

### Slide 1: Cover Slide

**Background:** Black (#000000)

**Main Title Text:**
- Text: Company name (e.g., "HOWATSON+COMPANY")
- Font: VC Nudge Black, 180-220pt, white, uppercase
- Position: Fills most of slide width
- Layout: Text wraps around central image, creating knockout effect
  - Top portion of text above image
  - Bottom portion of text below image

**Central Image:**
- Position: Center of slide
- Size: Approximately 11.8" × 6.4" (but can vary)
- Placement: Sits in "middle" of display text
- Treatment: Greyscale or full colour

**Client Name:**
- Text: "+ CLIENT NAME"
- Font: VC Nudge Black, 28pt, white, uppercase
- Position: Top left (0.19", 2.69")
- Size: ~3.0" × 0.57"

**Presentation Name:**
- Text: "PRESENTATION NAME" (2-3 lines)
- Font: VC Nudge Black, 28pt, white, uppercase
- Position: Top right (9.86", 2.78")
- Size: ~3.0" × 0.85"
- Alignment: Right-aligned

**Vertical Branding:**
- Text: "HOWATSON+COMPANY"
- Font: Manrope or IBM Plex Mono, 8pt, white
- Position: Far left edge, rotated -90°
- Runs vertically along left margin

---

### Slide 3: Section Divider

**Background:** Accent colour (e.g., Cyan #76DBEC, or Blue, Lime, etc.)

**Section Number:**
- Text: "01", "02", etc.
- Font: VC Nudge Black, 350-400pt, black
- Position: Left side, overlapping left edge (-1.76", 0.86")
- Size: ~9.4" × 7.5" (fills nearly full height)
- Placement: Number bleeds off left edge

**Section Title:**
- Text: "SECTION TITLE" (customise)
- Font: VC Nudge Black, 80-90pt, black, uppercase
- Position: Right of number (5.09", 0.86")
- Size: ~8.05" × 6.09"
- Alignment: Left-aligned, centered vertically

**Vertical Branding:**
- Text: "HOWATSON+COMPANY"
- Font: Manrope or IBM Plex Mono, 8pt, black
- Position: Far left edge, rotated -90°

---

### Slide 7: 3-Column Content Slide

**Background:** White (#FFFFFF)

**Main Headline:**
- Text: E.g., "WE LIKE TO USE WHITE FOR CONTENT HEAVY PAGES"
- Font: VC Nudge Black, 60-80pt, black, uppercase
- Position: Top left (0.7", 0.7")
- Size: Full width minus margins (~12" wide)
- Max: 2-3 lines

**Column Layout:**
- Number of columns: 3
- Column spacing: ~0.5" gutters
- Each column width: ~3.9"
- Starts at: Y = ~3.8"

**Column Headers:**
- Text: "Heading 2"
- Font: Manrope, 20-24pt, black
- Underline: Black line, 2pt weight
- Position: Top of each column

**Body Text:**
- Font: Manrope Light, 16-18pt, black
- Line spacing: 120-140%
- Paragraph spacing: 12-16pt between paragraphs
- Alignment: Left-aligned
- Width: Column width

**Vertical Branding:**
- Text: "HOWATSON+COMPANY"
- Font: Manrope or IBM Plex Mono, 8pt, black
- Position: Far left edge, rotated -90°

---

### Slide 10: 5-Column Image Grid

**Background:** White (#FFFFFF)

**Main Headline:**
- Text: E.g., "PHOTOS WITH CAPTIONS"
- Font: VC Nudge Black, 60-80pt, black, uppercase
- Position: Top left (0.7", 0.7")

**Grid Layout:**
- Number of columns: 5
- Column spacing: ~0.3" gutters
- Each column width: ~2.3"
- Image height: ~2.3" (square aspect ratio)
- Starts at: Y = ~2.4"

**Image Placeholders:**
- Size: 2.3" × 2.3" square
- Border: None or 1pt grey
- Background: Beige (#EDDAC1) if placeholder

**Per Column:**

**Heading 1:**
- Font: Manrope Bold, 14-16pt, black
- Position: Below image, 0.1" gap

**Subheading:**
- Font: Manrope, 12-14pt, black
- Position: Below Heading 1

**Body Text:**
- Font: Manrope Light, 12-14pt, black
- Position: Below subheading
- Max: 3-4 lines

**Vertical Branding:**
- Text: "HOWATSON+COMPANY"
- Position: Far left edge, rotated -90°

---

### Slide 16: Split Image/Text Layout

**Background:** White (#FFFFFF)

**Layout Split:**
- Left section: 40% width (text)
- Right section: 60% width (image)

**Left Section - Text Area:**

**Main Headline:**
- Text: "HEADING 1"
- Font: VC Nudge Black, 60-80pt, black, uppercase
- Position: (0.7", 1.2")
- Max width: ~5"

**Body Text:**
- Font: Manrope Light, 16-18pt, black
- Position: Below headline, (0.7", ~3.5")
- Width: ~4.8"
- Paragraphs: 2-3 paragraphs max
- Line spacing: 140%

**Right Section - Image:**
- Position: Starts at ~5.5" from left
- Size: ~7.5" wide × full height (~6.8" tall)
- Bleed: Image can extend to right edge
- Treatment: Full colour or greyscale

**Vertical Branding:**
- Text: "HOWATSON+COMPANY"
- Position: Far left edge, rotated -90°

---

### Slide 22: Video Storyboard Grid

**Background:** White (#FFFFFF)

**Main Headline:**
- Text: E.g., "60\" BRAND FILM"
- Font: VC Nudge Black, 60-80pt, black, uppercase
- Position: Top left (0.7", 0.7")

**Grid Layout:**
- Grid: 4 columns × 2 rows (8 frames total)
- Frame spacing: ~0.3" gutters horizontally, ~0.5" vertically
- Each frame width: ~2.9"
- Each frame height: ~1.6" (16:9 ratio)
- Starts at: Y = ~2.4"

**Frame Placeholders:**
- Size: 2.9" × 1.6" (16:9)
- Background: Beige (#EDDAC1)
- Border: Optional 1pt grey

**Frame Captions:**
- Position: Below each frame, 0.1" gap
- Font: Manrope Light, 10-12pt, black
- Format:
  - Line 1: Scene description (regular)
  - Line 2: "VO: [voiceover text]" (bold)

**Vertical Branding:**
- Text: "HOWATSON+COMPANY"
- Position: Far left edge, rotated -90°

---

## Vertical Branding Element (Standard on Most Slides)

**Text:** "HOWATSON+COMPANY"
**Font:** Manrope or IBM Plex Mono, 8-10pt
**Colour:**
- Black on white/light backgrounds
- White on black/dark backgrounds
**Position:** Far left edge (X = ~0.05")
**Rotation:** -90° (counter-clockwise)
**Vertical Position:** Approximately centered vertically

**Implementation in python-pptx:**
```python
# Add vertical branding text box
left = Inches(0.05)
top = Inches(3.0)
width = Inches(0.2)
height = Inches(4.0)

txBox = slide.shapes.add_textbox(left, top, width, height)
tf = txBox.text_frame
tf.text = "HOWATSON+COMPANY"

# Format text
p = tf.paragraphs[0]
p.font.name = "Manrope"
p.font.size = Pt(8)
p.font.color.rgb = RGBColor(0, 0, 0)  # or white on dark slides

# Rotate text box
txBox.rotation = 270  # or -90
```

---

## Critical Implementation Rules (python-pptx)

### Font Names
- Headline font: `"VC Nudge Black"`
- Body font: `"Manrope"` or `"Manrope Light"`
- Check installed fonts with `fc-list | grep -i "vc nudge"`

### Multi-Line Text
When creating multi-line headlines, format EACH paragraph:
- Do NOT rely on `\n` with single font assignment
- Loop through paragraphs and apply font to each
- Use `tf.add_paragraph()` for additional lines

```python
# WRONG - only first line gets font
tf.text = "LINE 1\nLINE 2"
p = tf.paragraphs[0]
p.font.name = "VC Nudge Black"  # Only applies to LINE 1!

# CORRECT - format each paragraph
for i, line in enumerate(lines):
    if i == 0:
        p = tf.paragraphs[0]
    else:
        p = tf.add_paragraph()
    p.text = line
    p.font.name = "VC Nudge Black"  # Applies to each line
```

### Shadow Removal (MANDATORY)
ALL shapes require explicit shadow removal:
- Text boxes
- Rectangles (image placeholders)
- Connector lines (underlines)
- Any other shapes

```python
from pptx.oxml.ns import qn

def remove_shadow(shape):
    spPr = shape._element.spPr
    for effect in spPr.findall(qn('a:effectLst')):
        spPr.remove(effect)
    for shadow in spPr.findall('.//' + qn('a:outerShdw')):
        shadow.getparent().remove(shadow)
    for style in spPr.findall(qn('a:effectRef')):
        spPr.remove(style)
```

### Sidebar Rules
1. Line position: Y=0 to Y=7.5 (FULL slide height, edge-to-edge)
2. Color: ALWAYS match heading color
   - White/light backgrounds → BLACK
   - Black backgrounds → WHITE
   - Colored backgrounds (cyan, blue, lime) → BLACK (NOT white, NOT accent color)

### Underlines
- Use `MSO_CONNECTOR.STRAIGHT` (not RECTANGLE)
- Width: 1pt
- No shadow
- Position: Immediately below text baseline

```python
from pptx.enum.shapes import MSO_CONNECTOR

connector = slide.shapes.add_connector(
    MSO_CONNECTOR.STRAIGHT,
    Inches(x1), Inches(y1),
    Inches(x2), Inches(y2)
)
connector.line.color.rgb = color
connector.line.width = Pt(1)
remove_shadow(connector)
```

### Section Divider Headlines
- Vertical alignment: `MSO_ANCHOR.BOTTOM`
- Position: Lower-right quadrant of slide
- Line spacing: 0.85 for tight headlines

---

## Grid System

**Horizontal Grid:**
- Left margin: 0.37"
- Right margin: 0.37"
- Content area: 12.59" wide
- Common column widths:
  - 2 columns: 6.15" each (0.3" gutter)
  - 3 columns: 3.96" each (0.5" gutters)
  - 5 columns: 2.31" each (0.3" gutters)

**Vertical Grid:**
- Top margin: 0.36"
- Bottom margin: 0.36"
- Content area: 6.78" tall
- Headline zone: Top 2.0"
- Content zone: 2.4" to 6.8"

---

## Common Element Specifications

### Underlines (Heading Dividers)
- Weight: 2pt
- Colour: Black
- Length: Full column width or text width
- Gap below text: 0.1"

### Rounded Buttons (Download Links)
- Border radius: 24pt (fully rounded ends)
- Border: 2pt black
- Fill: None (transparent) or white
- Padding: 0.3" horizontal, 0.15" vertical
- Text: Manrope, 14-16pt, black

### Image Treatments
- Full bleed: Extend to slide edges
- Greyscale: Common on cover slides and editorial layouts
- Borders: Rare; usually images are borderless
- Aspect ratios: 16:9 for large images, 1:1 for thumbnails

---

## Implementation Notes

### Working with VC Nudge Black Font

VC Nudge Black is a condensed display typeface. Key characteristics:
- **Condensed form:** Characters are narrow
- **Black weight:** Bold, high-impact headlines
- **Always uppercase:** Designed for display use in all caps
- **Tight spacing:** Default tracking is already tight; don't increase

### Working with Manrope Font

Manrope is a modern geometric sans-serif. Required weights:
- **Manrope Light (300):** Body text
- **Manrope Regular (400):** Subheadings
- **Manrope Bold (700):** Emphasis

If Manrope is not available:
1. **Install it:** Google Fonts - https://fonts.google.com/specimen/Manrope
2. **Fallback:** Montserrat Light/Regular
3. **Alternative:** DM Sans Light/Regular

### Embedding Fonts in PPTX

To ensure fonts display correctly:
```python
from pptx import Presentation

prs = Presentation()
prs.core_properties.embed_fonts = True
```

Or manually:
1. File > Options > Save
2. Check "Embed fonts in the file"
3. Select "Embed all characters"

---

## Quality Control Checklist

Before delivering any presentation:

**Dimensions & Setup:**
- [ ] Slide size is 13.33" × 7.5" (16:9)
- [ ] Margins are consistent (0.36-0.37")

**Typography:**
- [ ] VC Nudge Black used for all headlines (uppercase)
- [ ] Manrope Light used for body text
- [ ] Font sizes match specifications
- [ ] No font substitutions (Arial, Helvetica, etc.)

**Colours:**
- [ ] All colours match exact hex values
- [ ] Black is pure black (#000000)
- [ ] White is pure white (#FFFFFF)
- [ ] Accent colours are from approved palette

**Layout:**
- [ ] Vertical "HOWATSON+COMPANY" branding present
- [ ] Grid alignment is precise
- [ ] Column widths are equal
- [ ] Gutters are consistent
- [ ] Text doesn't overflow boxes

**Visual Consistency:**
- [ ] Compare against reference screenshots
- [ ] Check spacing and padding
- [ ] Verify alignment
- [ ] Confirm image positioning

**File Quality:**
- [ ] Fonts are embedded
- [ ] Images are high resolution (300 DPI)
- [ ] No compression artifacts
- [ ] File size is reasonable (<50MB)

---

## EMU Reference (for python-pptx)

English Metric Units (EMUs) conversion:
- 1 inch = 914,400 EMUs
- 1 cm = 360,000 EMUs  
- 1 point = 12,700 EMUs

**Slide dimensions in EMUs:**
- Width: 12,192,000 EMUs
- Height: 6,858,000 EMUs

**Common conversions:**
```python
from pptx.util import Inches, Pt, Cm

# Use these helpers
Inches(1.0)    # = 914,400 EMUs
Pt(12)         # = 152,400 EMUs
Cm(2.54)       # = 914,400 EMUs
```
