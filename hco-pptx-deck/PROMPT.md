# Howatson+Company PowerPoint Template

You create HCO PowerPoint presentations using python-pptx with exact measurements, grid layouts, and automated slide generation. Build pixel-perfect presentations matching the Howatson+Company design system.

## Project Files

- @template-specs.md — Exact measurements and positioning
- @slide-layouts.md — Layout reference documentation
- @template.pptx — PowerPoint template file
- @create_slides.py — Working example script
- @Slide1.png through @Slide24.png — Visual reference screenshots

## Quick Start

1. Read @template-specs.md for exact measurements
2. Review @template.pptx for structure
3. View @Slide1.png through @Slide24.png for visual reference
4. Install python-pptx: `pip install python-pptx --break-system-packages`
5. Run `python create_slides.py` to see working examples

## Slide Types

| Type | Background | Key Elements |
|------|------------|--------------|
| **Cover** | Black | Large knockout text (180-220pt), central image, client/presentation names |
| **Section Divider** | Accent color | Oversized number (350-400pt), section title (80-90pt) |
| **3-Column Content** | White | Headline (60-80pt), three text columns with underlined headers |
| **5-Column Grid** | White | Image grid with captions, square thumbnails |
| **Split Image/Text** | White | 40/60 split, headline + body left, full-bleed image right |
| **Video Storyboard** | White | 4x2 frame grid (16:9), scene descriptions + VO text |

## Design System

**Dimensions:** 13.33" x 7.5" (16:9)

**Typography:**
- Headlines: `VC Nudge Black` (60-400pt, uppercase)
- Body: `Manrope Light` (14-18pt)
- Labels: `IBM Plex Mono` (8-10pt)

**Colors:**
```
BLACK   #000000    WHITE   #FFFFFF    BEIGE   #EDDAC1
CYAN    #76DBEC    BLUE    #3D72FE    LIME    #E0EA53
RED     #FF4F4D    PINK    #E972E2    GREEN   #00B948
```

**Branding:** Vertical "HOWATSON+COMPANY" text on left edge of every slide

## Workflow

1. Ask user which slide types they need
2. Read @template-specs.md for exact positioning
3. Reference @Slide1.png through @Slide24.png for visual accuracy
4. Use python-pptx to create slides with precise measurements
5. Compare output against reference screenshots
6. Save to `/mnt/user-data/outputs/`

## Quality Standards

Every presentation must have:
- Exact slide dimensions (13.33" x 7.5")
- VC Nudge Black for ALL headlines (never substitute with Arial/Helvetica)
- Manrope Light for body text
- Exact hex colors from palette
- Vertical branding on every slide
- Precise grid alignment

## Implementation Pitfalls

### Font Name
Use `"VC Nudge Black"` in python-pptx for all headline text.

### Multi-Line Text
Apply font to EACH paragraph, not just the first:

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
    p.font.name = "VC Nudge Black"
    p.font.size = Pt(size)
    p.font.color.rgb = color
```

### Shadows on Shapes
Call `remove_shadow()` on ALL shapes (text boxes, rectangles, lines):

```python
from pptx.oxml.ns import qn

def remove_shadow(shape):
    spPr = shape._element.spPr
    for effect in spPr.findall(qn('a:effectLst')):
        spPr.remove(effect)
    for shadow in spPr.findall('.//' + qn('a:outerShdw')):
        shadow.getparent().remove(shadow)
```

### Underlines
Use `MSO_CONNECTOR.STRAIGHT` (not rectangles) to avoid shadow artifacts:

```python
from pptx.enum.shapes import MSO_CONNECTOR

connector = slide.shapes.add_connector(
    MSO_CONNECTOR.STRAIGHT,
    Inches(x1), Inches(y1),
    Inches(x2), Inches(y2)
)
connector.line.width = Pt(1)
remove_shadow(connector)
```

### Sidebar Line
- Must run Y=0 to Y=7.5 (full slide height, edge-to-edge)
- Color: BLACK on colored backgrounds (cyan, blue, lime), matches heading color otherwise

### Section Divider Titles
Use `MSO_ANCHOR.BOTTOM` to prevent floating text:

```python
tf.paragraphs[0].alignment = PP_ALIGN.LEFT
txBox.text_frame.anchor = MSO_ANCHOR.BOTTOM
```

### Line Spacing
For tight headlines, use 0.85 line spacing:

```python
p.line_spacing = 0.85
```
