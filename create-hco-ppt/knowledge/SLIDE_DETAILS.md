# Slide Details

Placeholder tokens and element specifications for each slide.
Use the `{{type.element}}` format for text replacement with python-pptx.

> **Format**: All placeholders use `{{slide_type.element_name}}` format.
> This enables simple find-replace without positional logic.

## Table of Contents

- [Slide 1: `title` (Index 0)](#slide-1-title-index-0)
- [Slide 3: `section-divider` (Index 2)](#slide-3-section-divider-index-2)
- [Slide 4: `break-light` (Index 3)](#slide-4-break-light-index-3)
- [Slide 5: `statement-dark` (Index 4)](#slide-5-statement-dark-index-4)
- [Slide 6: `statement-light` (Index 5)](#slide-6-statement-light-index-5)
- [Slide 7: `three-column-text` (Index 6)](#slide-7-three-column-text-index-6)
- [Slide 8: `three-column-images` (Index 7)](#slide-8-three-column-images-index-7)
- [Slide 9: `two-column-text` (Index 8)](#slide-9-two-column-text-index-8)
- [Slide 10: `photo-gallery-5` (Index 9)](#slide-10-photo-gallery-5-index-9)
- [Slide 11: `three-column-bubbles` (Index 10)](#slide-11-three-column-bubbles-index-10)
- [Slide 12: `solid-bubbles` (Index 11)](#slide-12-solid-bubbles-index-11)
- [Slide 13: `statistics-grid` (Index 12)](#slide-13-statistics-grid-index-12)
- [Slide 14: `numbered-rows` (Index 13)](#slide-14-numbered-rows-index-13)
- [Slide 15: `two-panel-compare` (Index 14)](#slide-15-two-panel-compare-index-14)
- [Slide 16: `text-image-right` (Index 15)](#slide-16-text-image-right-index-15)
- [Slide 17: `image-text-right` (Index 16)](#slide-17-image-text-right-index-16)
- [Slide 18: `fullbleed-image` (Index 17)](#slide-18-fullbleed-image-index-17)
- [Slide 19: `image-gradient-text` (Index 18)](#slide-19-image-gradient-text-index-18)
- [Slide 20: `bold-title-image` (Index 19)](#slide-20-bold-title-image-index-19)
- [Slide 21: `script-page` (Index 20)](#slide-21-script-page-index-20)
- [Slide 22: `storyboard-8` (Index 21)](#slide-22-storyboard-8-index-21)
- [Slide 23: `timeline-process` (Index 22)](#slide-23-timeline-process-index-22)
- [Slide 24: `thank-you` (Index 23)](#slide-24-thank-you-index-23)
- [Slide 25: `bullet-list` (Index 24)](#slide-25-bullet-list-index-24)
- [Slide 26: `single-stat` (Index 25)](#slide-26-single-stat-index-25)
- [Slide 27: `heading-paragraph` (Index 26)](#slide-27-heading-paragraph-index-26)
- [Slide 28: `highlights` (Index 27)](#slide-28-highlights-index-27)
- [Slide 29: `horizontal-split` (Index 28)](#slide-29-horizontal-split-index-28)
- [Slide 30: `split-title-content` (Index 29)](#slide-30-split-title-content-index-29)
- [Slide 31: `final-thought` (Index 30)](#slide-31-final-thought-index-30)
- [Quick Reference: All Placeholders](#quick-reference-all-placeholders)
  - [Content Slides](#content-slides)
- [Usage Example](#usage-example)

---

## Slide 1: `title` (Index 0)

**Background**: Black
**Screenshot**: `../assets/template-screenshots/title.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Client name | `{{title.client_name}}` | Prefix with "+" when replacing |
| Presentation name | `{{title.presentation_name}}` | UPPERCASE |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Client name | 0.19in | 2.70in | 3.32in | 0.57in |
| Presentation name | 9.86in | 2.78in | 3.32in | 0.85in |
| Photo | 0.19in | 0.21in | 12.96in | 7.01in |

---

## Slide 3: `section-divider` (Index 2)

**Background**: Cyan (#7DD3E8)
**Screenshot**: `../assets/template-screenshots/section-divider.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Number | `{{section.number}}` | Format: 01, 02, 03... |
| Title | `{{section.title}}` | UPPERCASE, 2-3 words max |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Number | -1.76in | 0.86in | 9.43in | 7.51in |
| Title | 5.09in | 0.86in | 8.05in | 6.09in |

---

## Slide 4: `break-light` (Index 3)

**Background**: Cyan (#7DD3E8)
**Screenshot**: `../assets/template-screenshots/break-light.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Text | `{{break.text}}` | Centered, 2-3 lines, Manrope Light 20pt |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Text | 3.79in | 3.03in | 5.76in | 1.45in |

---

## Slide 5: `statement-dark` (Index 4)

**Background**: Black
**Screenshot**: `../assets/template-screenshots/statement-dark.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Statement | `{{statement_dark.text}}` | Cyan text, VC Nudge Black 48pt, 0.7 line spacing, 1-2 lines |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Statement | 2.90in | 3.03in | 7.54in | 1.45in |

### Notes
- Has sidebar watermark
- Hidden duplicate text element was removed in standardization

---

## Slide 6: `statement-light` (Index 5)

**Background**: Cyan (#7DD3E8)
**Screenshot**: `../assets/template-screenshots/statement-light.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Statement | `{{statement_light.text}}` | Black text, VC Nudge Black 48pt, 0.7 line spacing, 1-2 lines |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Statement | 2.90in | 3.03in | 7.54in | 1.45in |

---

## Slide 7: `three-column-text` (Index 6)

**Background**: White
**Screenshot**: `../assets/template-screenshots/three-column-text.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{three_col_text.title}}` | UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Heading (col 1) | `{{three_col_text.heading_1}}` | Manrope Light 14pt |
| Heading (col 2) | `{{three_col_text.heading_2}}` | Manrope Light 14pt |
| Heading (col 3) | `{{three_col_text.heading_3}}` | Manrope Light 14pt |
| Body (col 1) | `{{three_col_text.body_1}}` | Manrope Light 11pt, ~100 words |
| Body (col 2) | `{{three_col_text.body_2}}` | Manrope Light 11pt, ~100 words |
| Body (col 3) | `{{three_col_text.body_3}}` | Manrope Light 11pt, ~100 words |

### Element Positions

| Element | Left | Top | Width |
|---------|------|-----|-------|
| Title | 0.59in | 2.00in | - |
| Heading 1 | 0.67in | 4.55in | 3.76in |
| Heading 2 | 4.95in | 4.55in | 3.76in |
| Heading 3 | 9.23in | 4.55in | 3.76in |
| Body 1 | 0.67in | 5.18in | - |
| Body 2 | 4.95in | 5.18in | - |
| Body 3 | 9.23in | 5.18in | - |

---

## Slide 8: `three-column-images` (Index 7)

**Background**: White
**Screenshot**: `../assets/template-screenshots/three-column-images.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{three_col_images.title}}` | UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Subtitle | `{{three_col_images.subtitle}}` | Below title |
| Heading (col 1) | `{{three_col_images.heading_1}}` | Manrope Light 14pt |
| Heading (col 2) | `{{three_col_images.heading_2}}` | Manrope Light 14pt |
| Heading (col 3) | `{{three_col_images.heading_3}}` | Manrope Light 14pt |
| Caption (col 1) | `{{three_col_images.caption_1}}` | Below image |
| Caption (col 2) | `{{three_col_images.caption_2}}` | Below image |
| Caption (col 3) | `{{three_col_images.caption_3}}` | Below image |

### Element Positions

| Element | Left | Top | Width |
|---------|------|-----|-------|
| Title | 0.59in | 0.58in | - |
| Subtitle | 0.59in | 1.54in | - |
| Heading 1 | 0.67in | 3.73in | 3.76in |
| Heading 2 | 4.95in | 3.73in | 3.76in |
| Heading 3 | 9.23in | 3.73in | 3.76in |
| Caption 1 | 0.67in | 4.37in | - |
| Caption 2 | 4.95in | 4.37in | - |
| Caption 3 | 9.23in | 4.37in | - |

### Notes
- Has 3 image placeholder shapes (AUTO_SHAPE)

---

## Slide 9: `two-column-text` (Index 8)

**Background**: White
**Screenshot**: `../assets/template-screenshots/two-column-text.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{two_col_text.title}}` | UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Heading (col 1) | `{{two_col_text.heading_1}}` | Manrope Light 14pt |
| Heading (col 2) | `{{two_col_text.heading_2}}` | Manrope Light 14pt |
| Body (col 1) | `{{two_col_text.body_1}}` | Manrope Light 11pt |
| Body (col 2) | `{{two_col_text.body_2}}` | Manrope Light 11pt |

### Element Positions

| Element | Left | Top | Width |
|---------|------|-----|-------|
| Title | 0.59in | 0.58in | - |
| Heading 1 | 0.63in | 3.95in | 3.76in |
| Heading 2 | 7.13in | 3.95in | 3.76in |
| Body 1 | 0.61in | 4.59in | - |
| Body 2 | 7.13in | 4.59in | - |

---

## Slide 10: `photo-gallery-5` (Index 9)

**Background**: White
**Screenshot**: `../assets/template-screenshots/photo-gallery-5.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{photo_gallery.title}}` | UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Heading 1 | `{{photo_gallery.heading_1}}` | Format: "Title\nSubtitle" |
| Heading 2 | `{{photo_gallery.heading_2}}` | Format: "Title\nSubtitle" |
| Heading 3 | `{{photo_gallery.heading_3}}` | Format: "Title\nSubtitle" |
| Heading 4 | `{{photo_gallery.heading_4}}` | Format: "Title\nSubtitle" |
| Heading 5 | `{{photo_gallery.heading_5}}` | Format: "Title\nSubtitle" |
| Caption 1 | `{{photo_gallery.caption_1}}` | Photo description |
| Caption 2 | `{{photo_gallery.caption_2}}` | Photo description |
| Caption 3 | `{{photo_gallery.caption_3}}` | Photo description |
| Caption 4 | `{{photo_gallery.caption_4}}` | Photo description |
| Caption 5 | `{{photo_gallery.caption_5}}` | Photo description |

### Notes
- Photos are in GROUP shapes
- Heading and subheading combined with newline

---

## Slide 11: `three-column-bubbles` (Index 10)

**Background**: White
**Screenshot**: `../assets/template-screenshots/three-column-bubbles.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{three_col_bubbles.title}}` | UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Bubble 1a (col 1, top) | `{{three_col_bubbles.bubble_1a}}` | Pill/tag style |
| Bubble 2a (col 2, top) | `{{three_col_bubbles.bubble_2a}}` | Pill/tag style |
| Bubble 3a (col 3, top) | `{{three_col_bubbles.bubble_3a}}` | Pill/tag style |
| Bubble 1b (col 1, bottom) | `{{three_col_bubbles.bubble_1b}}` | Pill/tag style |
| Bubble 2b (col 2, bottom) | `{{three_col_bubbles.bubble_2b}}` | Pill/tag style |
| Bubble 3b (col 3, bottom) | `{{three_col_bubbles.bubble_3b}}` | Pill/tag style |
| Body 1 | `{{three_col_bubbles.body_1}}` | Description text |
| Body 2 | `{{three_col_bubbles.body_2}}` | Description text |
| Body 3 | `{{three_col_bubbles.body_3}}` | Description text |

### Notes
- Each column has 2 bubble pills + body text
- Elements are in GROUP shapes

---

## Slide 12: `solid-bubbles` (Index 11)

**Background**: Cyan (#7DD3E8)
**Screenshot**: `../assets/template-screenshots/solid-bubbles.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Pre-header | `{{solid_bubbles.preheader}}` | Small text above title |
| Title | `{{solid_bubbles.title}}` | Large UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Bubble 1 | `{{solid_bubbles.bubble_1}}` | Right side, top |
| Bubble 2 | `{{solid_bubbles.bubble_2}}` | Right side, middle |
| Bubble 3 | `{{solid_bubbles.bubble_3}}` | Right side, bottom |
| Body 1 | `{{solid_bubbles.body_1}}` | Under bubble 1 |
| Body 2 | `{{solid_bubbles.body_2}}` | Under bubble 2 |
| Body 3 | `{{solid_bubbles.body_3}}` | Under bubble 3 |

### Element Positions

| Element | Left | Top |
|---------|------|-----|
| Bubble 1 | 7.05in | 1.21in |
| Body 1 | 7.05in | 1.91in |
| Pre-header | 0.59in | 2.32in |
| Title | 0.59in | 2.90in |
| Bubble 2 | 7.05in | 3.15in |
| Body 2 | 7.05in | 3.81in |
| Bubble 3 | 7.05in | 5.05in |
| Body 3 | 7.05in | 5.73in |

---

## Slide 13: `statistics-grid` (Index 12)

**Background**: Split Black (left) / Cyan (right)
**Screenshot**: `../assets/template-screenshots/statistics-grid.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{stats.title}}` | Large CYAN text on BLACK, VC Nudge Black, 0.7 line spacing |
| Description | `{{stats.description}}` | Below title |
| Value 1-6 | `{{stats.value_1}}` ... `{{stats.value_6}}` | Format: "42%" or "3.5M", VC Nudge Black, 0.7 line spacing |
| Label 1-6 | `{{stats.label_1}}` ... `{{stats.label_6}}` | Stat name |
| Desc 1-6 | `{{stats.desc_1}}` ... `{{stats.desc_6}}` | Brief explanation |

### Stat Box Grid (3x2)

| Position | Left | Top | Placeholder |
|----------|------|-----|-------------|
| Top-left | 7.42in | 0.87in | value_1, label_1, desc_1 |
| Top-right | 10.31in | 0.87in | value_2, label_2, desc_2 |
| Mid-left | 7.42in | 3.03in | value_3, label_3, desc_3 |
| Mid-right | 10.31in | 3.03in | value_4, label_4, desc_4 |
| Bot-left | 7.42in | 5.20in | value_5, label_5, desc_5 |
| Bot-right | 10.31in | 5.20in | value_6, label_6, desc_6 |

### Notes
- Has sidebar watermark
- Stat boxes are GROUP shapes
- Title is 48pt (reduced from original 166pt for readability)

---

## Slide 14: `numbered-rows` (Index 13)

**Background**: Cyan accent (split top/bottom)
**Screenshot**: `../assets/template-screenshots/numbered-rows.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Number 1 | `{{numbered_rows.number_1}}` | Format: "01" |
| Number 2 | `{{numbered_rows.number_2}}` | Format: "02" |
| Title 1 | `{{numbered_rows.title_1}}` | Top section |
| Title 2 | `{{numbered_rows.title_2}}` | Bottom section |
| Subtitle 1 | `{{numbered_rows.subtitle_1}}` | Top section |
| Subtitle 2 | `{{numbered_rows.subtitle_2}}` | Bottom section |
| Heading 1a | `{{numbered_rows.heading_1a}}` | Row 1, col 1 |
| Heading 1b | `{{numbered_rows.heading_1b}}` | Row 1, col 2 |
| Heading 2a | `{{numbered_rows.heading_2a}}` | Row 2, col 1 |
| Heading 2b | `{{numbered_rows.heading_2b}}` | Row 2, col 2 |
| Body 1a | `{{numbered_rows.body_1a}}` | Row 1, col 1 |
| Body 1b | `{{numbered_rows.body_1b}}` | Row 1, col 2 |
| Body 2a | `{{numbered_rows.body_2a}}` | Row 2, col 1 |
| Body 2b | `{{numbered_rows.body_2b}}` | Row 2, col 2 |

### Element Positions

| Element | Left | Top | Width |
|---------|------|-----|-------|
| Number 1 | 0.49in | 0.72in | - |
| Title 1 | 5.01in | 0.72in | - |
| Subtitle 1 | 5.02in | 1.21in | - |
| Heading 1a | 5.03in | 1.49in | 3.74in |
| Body 1a | 5.03in | 2.14in | - |
| Heading 1b | 8.97in | 1.49in | 3.74in |
| Body 1b | 8.97in | 2.14in | - |
| Number 2 | 0.49in | 3.96in | - |
| Title 2 | 5.01in | 3.96in | - |
| Subtitle 2 | 5.02in | 4.46in | - |
| Heading 2a | 5.03in | 4.74in | 3.74in |
| Body 2a | 5.03in | 5.38in | - |
| Heading 2b | 8.97in | 4.74in | 3.74in |
| Body 2b | 8.97in | 5.38in | - |

### Notes
- Has sidebar watermark
- Two numbered sections stacked vertically
- Headings are inside GROUP shapes

---

## Slide 15: `two-panel-compare` (Index 14)

**Background**: Split Cyan (left) / White (right)
**Screenshot**: `../assets/template-screenshots/two-panel-compare.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Pre-header left | `{{compare.preheader_left}}` | Left panel |
| Pre-header right | `{{compare.preheader_right}}` | Right panel |
| Heading left | `{{compare.heading_left}}` | Left panel, UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Heading right | `{{compare.heading_right}}` | Right panel, UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Subheading left | `{{compare.subheading_left}}` | Left panel |
| Subheading right | `{{compare.subheading_right}}` | Right panel |
| Bubble left 1 | `{{compare.bubble_left_1}}` | Left panel, top bubble |
| Bubble left 2 | `{{compare.bubble_left_2}}` | Left panel, bottom bubble |
| Bubble right 1 | `{{compare.bubble_right_1}}` | Right panel, top bubble |
| Bubble right 2 | `{{compare.bubble_right_2}}` | Right panel, bottom bubble |
| Body left 1 | `{{compare.body_left_1}}` | Left panel, top text |
| Body left 2 | `{{compare.body_left_2}}` | Left panel, bottom text |
| Body right 1 | `{{compare.body_right_1}}` | Right panel, top text |
| Body right 2 | `{{compare.body_right_2}}` | Right panel, bottom text |

### Element Positions

| Element | Left | Top | Width |
|---------|------|-----|-------|
| Pre-header left | 0.59in | 0.78in | - |
| Heading left | 0.59in | 1.26in | - |
| Subheading left | 0.59in | 3.72in | 5.0in |
| Bubble left 1 | 0.59in | 4.24in | - |
| Body left 1 | 0.59in | 4.90in | - |
| Bubble left 2 | 0.59in | 5.62in | - |
| Body left 2 | 0.59in | 6.28in | - |
| Pre-header right | 6.97in | 0.78in | - |
| Heading right | 6.97in | 1.26in | - |
| Subheading right | 6.97in | 3.72in | 5.0in |
| Bubble right 1 | 6.97in | 4.24in | - |
| Body right 1 | 6.97in | 4.90in | - |
| Bubble right 2 | 6.97in | 5.62in | - |
| Body right 2 | 6.97in | 6.28in | - |

### Notes
- Has sidebar watermark
- Two mirrored panels for comparison

---

## Slide 16: `text-image-right` (Index 15)

**Background**: White
**Screenshot**: `../assets/template-screenshots/text-image-right.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Heading | `{{text_image.heading}}` | UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Body | `{{text_image.body}}` | Manrope Light |

### Element Positions

| Element | Left | Top | Width | Height | Anchor |
|---------|------|-----|-------|--------|--------|
| Heading | 0.59in | 1.50in | 5.25in | 1.83in | bottom |
| Body | 0.59in | 3.75in | 4.45in | 1.99in | top |
| Image | 6.67in | 0.00in | 6.67in | 7.50in | - |

### Notes
- Image fills right half (6.67in x 7.50in)
- Heading box anchored to bottom so text grows upward

---

## Slide 17: `image-text-right` (Index 16)

**Background**: Cyan accent
**Screenshot**: `../assets/template-screenshots/image-text-right.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Heading | `{{image_text.heading}}` | UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Body | `{{image_text.body}}` | Manrope Light |

### Element Positions

| Element | Left | Top | Width | Height | Anchor |
|---------|------|-----|-------|--------|--------|
| Image | 0.00in | 0.00in | - | - | - |
| Heading | 7.72in | 1.50in | 4.50in | 1.92in | bottom |
| Body | 7.72in | 3.43in | 4.42in | 1.99in | top |

### Notes
- Image fills left half
- Has sidebar watermark
- Heading box anchored to bottom so text grows upward

---

## Slide 18: `fullbleed-image` (Index 17)

**Background**: Photo (full-bleed)
**Screenshot**: `../assets/template-screenshots/fullbleed-image.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Text | `{{fullbleed.text}}` | Centered overlay, Manrope Light 20pt |

### Element Positions

| Element | Left | Top |
|---------|------|-----|
| Image | 0.00in | 0.00in |
| Text | 3.79in | 3.03in |

### Notes
- Image fills entire slide (13.33in x 7.50in)
- Has sidebar watermark

---

## Slide 19: `image-gradient-text` (Index 18)

**Background**: Photo with gradient overlay
**Screenshot**: `../assets/template-screenshots/image-gradient-text.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{gradient.title}}` | UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Body | `{{gradient.body}}` | Multiple paragraphs |

### Element Positions

| Element | Left | Top |
|---------|------|-----|
| Title | 0.59in | 0.54in |
| Body | 0.59in | 3.36in |

### Notes
- Gradient overlay shape on left side
- Has sidebar watermark

---

## Slide 20: `bold-title-image` (Index 19)

**Background**: Photo
**Screenshot**: `../assets/template-screenshots/bold-title-image.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Pre-header | `{{bold_title.preheader}}` | Small text |
| Title | `{{bold_title.title}}` | Very large VC Nudge Black, 0.7 line spacing |

### Element Positions

| Element | Left | Top |
|---------|------|-----|
| Pre-header | 0.59in | 2.13in |
| Title | 0.59in | 2.22in |

### Notes
- Has gradient overlay on left
- Has sidebar watermark

---

## Slide 21: `script-page` (Index 20)

**Background**: White
**Screenshot**: `../assets/template-screenshots/script-page.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{script.title}}` | UPPERCASE, VC Nudge Black, 0.7 line spacing |
| Intro | `{{script.intro}}` | Left column, context |
| Dialogue | `{{script.dialogue}}` | Right column, script format |

### Element Positions

| Element | Left | Top | Width |
|---------|------|-----|-------|
| Title | 0.59in | 0.58in | 6.0in |
| Intro | 0.63in | 1.44in | 3.76in |
| Dialogue | 4.59in | 1.42in | 4.15in |
| Image 1 | 9.22in | 0.58in | 3.62in |
| Image 2 | 9.22in | 2.80in | 3.62in |
| Image 3 | 9.22in | 5.02in | 3.62in |

### Notes
- 3 stacked images on right (3.62in x 2.03in each)
- Script text contains dialogue formatting

---

## Slide 22: `storyboard-8` (Index 21)

**Background**: White
**Screenshot**: `../assets/template-screenshots/storyboard-8.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{storyboard.title}}` | Format: "60" BRAND FILM", VC Nudge Black, 0.7 line spacing |
| Caption 1-8 | `{{storyboard.caption_1}}` ... `{{storyboard.caption_8}}` | Frame descriptions |

### Frame Grid (4x2)

| Position | Left | Top | Placeholder |
|----------|------|-----|-------------|
| Row 1, Col 1 | 0.56in | 1.98in | caption_1 |
| Row 1, Col 2 | 3.67in | 1.98in | caption_2 |
| Row 1, Col 3 | 6.78in | 1.98in | caption_3 |
| Row 1, Col 4 | 9.89in | 1.98in | caption_4 |
| Row 2, Col 1 | 0.56in | 4.40in | caption_5 |
| Row 2, Col 2 | 3.67in | 4.40in | caption_6 |
| Row 2, Col 3 | 6.78in | 4.40in | caption_7 |
| Row 2, Col 4 | 9.89in | 4.40in | caption_8 |

### Notes
- Copyright in top-right (NOT sidebar)
- Each frame is 2.88in x 1.68in
- Caption format: "Scene description\nVO: Voiceover text"

---

## Slide 23: `timeline-process` (Index 22)

**Background**: Cyan (#7DD3E8)
**Screenshot**: `../assets/template-screenshots/timeline-process.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Image | `{{timeline.image}}` | Large left image |
| Header | `{{timeline.header}}` | Top header text |
| Step 1a-1d | `{{timeline.step_1a}}` ... `{{timeline.step_1d}}` | Row 1 items |
| Step 2-7 | `{{timeline.step_2}}` ... `{{timeline.step_7}}` | Process steps |
| Num 1-6 | `{{timeline.num_1}}` ... `{{timeline.num_6}}` | Step numbers |
| Callout 1-8 | `{{timeline.callout_1}}` ... `{{timeline.callout_8}}` | Right callouts |

### Notes
- Complex layout with many placeholders
- 6 numbered steps
- Callouts format: "> description"

---

## Slide 24: `thank-you` (Index 23)

**Background**: Black
**Screenshot**: `../assets/template-screenshots/thank-you.jpeg`

### Static Content

| Element | Text | Notes |
|---------|------|-------|
| Main text | `THANK YOU` | Do NOT replace - this is final text, VC Nudge Black 239pt, 0.7 line spacing |

### Notes
- "THANK YOU" is static, not a placeholder
- Text is VC Nudge Black, massive (239pt), 0.7 line spacing, bleeds off edges
- Has sidebar watermark
- Hidden duplicate text element was removed in standardization

---

## Slide 25: `bullet-list` (Index 24)

**Background**: White
**Screenshot**: `../assets/template-screenshots/bullet-list.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{bullet_list.title}}` | UPPERCASE, VC Nudge Black 48pt, 0.7 line spacing |
| Item 1 | `{{bullet_list.item_1}}` | Manrope Light 14pt, bulleted |
| Item 2 | `{{bullet_list.item_2}}` | Manrope Light 14pt, bulleted |
| Item 3 | `{{bullet_list.item_3}}` | Manrope Light 14pt, bulleted |
| Item 4 | `{{bullet_list.item_4}}` | Manrope Light 14pt, bulleted |
| Item 5 | `{{bullet_list.item_5}}` | Manrope Light 14pt, bulleted |
| Item 6 | `{{bullet_list.item_6}}` | Manrope Light 14pt, bulleted |
| Item 7 | `{{bullet_list.item_7}}` | Manrope Light 14pt, bulleted |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Title | 0.59in | 0.58in | 12.15in | 1.00in |
| Bullet box | 0.59in | 2.00in | 12.15in | 4.75in |

### Notes
- Uses single text box with 7 bulleted paragraphs (• character)
- 12pt paragraph spacing between items
- White background, no sidebar
- Use for takeaways, requirements, next steps

---

## Slide 26: `single-stat` (Index 25)

**Background**: Black
**Screenshot**: `../assets/template-screenshots/single-stat.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Value | `{{single_stat.value}}` | VC Nudge Black 200pt, Cyan (#7DD3E8), centered, 0.7 line spacing |
| Label | `{{single_stat.label}}` | VC Nudge Black 32pt, White, centered, 0.7 line spacing |
| Context | `{{single_stat.context}}` | Manrope Light 14pt, White, centered, optional |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Value | 2.90in | 1.80in | 7.54in | 2.50in |
| Label | 2.90in | 4.50in | 7.54in | 0.80in |
| Context | 2.90in | 5.50in | 7.54in | 0.50in |

### Notes
- Has sidebar watermark
- Value formats: "67%", "$4.2B", "3x", "10M+"
- Label is typically UPPERCASE
- Context line is optional for additional explanation

---

## Slide 27: `heading-paragraph` (Index 26)

**Background**: White
**Screenshot**: `../assets/template-screenshots/heading-paragraph.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Heading | `{{heading_paragraph.heading}}` | VC Nudge Black 48pt, UPPERCASE, 0.7 line spacing, anchor bottom |
| Body | `{{heading_paragraph.body}}` | Manrope Light 14pt |

### Element Positions

| Element | Left | Top | Width | Height | Anchor |
|---------|------|-----|-------|--------|--------|
| Heading | 0.59in | 1.50in | 12.15in | 1.83in | bottom |
| Body | 0.59in | 3.75in | 12.15in | 3.00in | top |

### Notes
- Heading box anchored to bottom so text grows upward
- White background, no sidebar
- Simple layout for explanatory content

---

## Slide 28: `highlights` (Index 27)

**Background**: White
**Screenshot**: `../assets/template-screenshots/highlights.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{highlights.title}}` | UPPERCASE, VC Nudge Black 48pt, 0.7 line spacing |
| Item 1 | `{{highlights.item_1}}` | Manrope Light 24pt |
| Item 2 | `{{highlights.item_2}}` | Manrope Light 24pt |
| Item 3 | `{{highlights.item_3}}` | Manrope Light 24pt |
| Item 4 | `{{highlights.item_4}}` | Manrope Light 24pt |
| Item 5 | `{{highlights.item_5}}` | Manrope Light 24pt |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Title | 0.59in | 0.58in | 12.15in | 1.00in |
| Item 1 | 0.59in | 2.00in | 12.15in | 0.70in |
| Item 2 | 0.59in | 2.90in | 12.15in | 0.70in |
| Item 3 | 0.59in | 3.80in | 12.15in | 0.70in |
| Item 4 | 0.59in | 4.70in | 12.15in | 0.70in |
| Item 5 | 0.59in | 5.60in | 12.15in | 0.70in |

### Notes
- Items have 0.90in vertical spacing (larger than bullet-list)
- Font size 24pt (vs 14pt for bullet-list) for visual emphasis
- White background, no sidebar
- Use for key callouts, headlines, or prominent statements

---

## Slide 29: `horizontal-split` (Index 28)

**Background**: Split Cyan (top) / White (bottom)
**Screenshot**: `../assets/template-screenshots/horizontal-split.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title (top) | `{{horizontal.title_top}}` | VC Nudge Black 28pt, 0.7 line spacing |
| Subtitle (top) | `{{horizontal.subtitle_top}}` | Manrope Light 12pt |
| Heading 1a | `{{horizontal.head_1a}}` | Manrope 14pt bold |
| Body 1a | `{{horizontal.body_1a}}` | Manrope Light 11pt |
| Heading 1b | `{{horizontal.head_1b}}` | Manrope 14pt bold |
| Body 1b | `{{horizontal.body_1b}}` | Manrope Light 11pt |
| Title (bottom) | `{{horizontal.title_bottom}}` | VC Nudge Black 28pt, 0.7 line spacing |
| Subtitle (bottom) | `{{horizontal.subtitle_bottom}}` | Manrope Light 12pt |
| Heading 2a | `{{horizontal.head_2a}}` | Manrope 14pt bold |
| Body 2a | `{{horizontal.body_2a}}` | Manrope Light 11pt |
| Heading 2b | `{{horizontal.head_2b}}` | Manrope 14pt bold |
| Body 2b | `{{horizontal.body_2b}}` | Manrope Light 11pt |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Cyan rectangle | 0.00in | 0.00in | 13.33in | 3.75in |
| Title (top) | 0.59in | 0.40in | 5.50in | 0.60in |
| Subtitle (top) | 0.59in | 1.00in | 5.50in | 0.40in |
| Head 1a | 0.59in | 1.60in | 5.50in | 0.40in |
| Body 1a | 0.59in | 2.00in | 5.50in | 1.50in |
| Head 1b | 6.70in | 1.60in | 5.50in | 0.40in |
| Body 1b | 6.70in | 2.00in | 5.50in | 1.50in |
| Title (bottom) | 0.59in | 4.00in | 5.50in | 0.60in |
| Subtitle (bottom) | 0.59in | 4.60in | 5.50in | 0.40in |
| Head 2a | 0.59in | 5.20in | 5.50in | 0.40in |
| Body 2a | 0.59in | 5.60in | 5.50in | 1.50in |
| Head 2b | 6.70in | 5.20in | 5.50in | 0.40in |
| Body 2b | 6.70in | 5.60in | 5.50in | 1.50in |

### Notes
- Use for two-section layouts like TELL/ASK+COLLABORATE patterns
- Each section has title, subtitle, and 2 columns of heading+body
- No sidebar

---

## Slide 30: `split-title-content` (Index 29)

**Background**: Split Cyan (left) / White (right)
**Screenshot**: `../assets/template-screenshots/split-title-content.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Title | `{{split.title}}` | VC Nudge Black 48pt, 0.7 line spacing, vertically centered |
| Heading 1 | `{{split.head_1}}` | Manrope 14pt bold |
| Body 1 | `{{split.body_1}}` | Manrope Light 11pt |
| Heading 2 | `{{split.head_2}}` | Manrope 14pt bold |
| Body 2 | `{{split.body_2}}` | Manrope Light 11pt |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Cyan rectangle | 0.00in | 0.00in | 6.67in | 7.50in |
| Title | 0.59in | 2.50in | 5.50in | 2.50in |
| Head 1 | 7.25in | 1.50in | 5.50in | 0.50in |
| Body 1 | 7.25in | 2.00in | 5.50in | 1.80in |
| Head 2 | 7.25in | 4.20in | 5.50in | 0.50in |
| Body 2 | 7.25in | 4.70in | 5.50in | 1.80in |

### Notes
- Title on colored left half, content on white right half
- 2 content sections on right side with heading+body each
- No sidebar

---

## Slide 31: `final-thought` (Index 30)

**Background**: Black
**Screenshot**: `../assets/template-screenshots/final-thought.jpeg`

### Placeholders

| Element | Placeholder | Notes |
|---------|-------------|-------|
| Heading | `{{final.heading}}` | VC Nudge Black 48pt, Cyan (#7DD3E8), 0.7 line spacing |
| Body | `{{final.body}}` | Manrope Light 16pt, White |

### Element Positions

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Heading | 1.50in | 2.20in | 10.50in | 1.50in |
| Body | 1.50in | 4.00in | 10.50in | 2.00in |

### Notes
- Has sidebar watermark (copied from statement-dark)
- Use for closing thoughts or final insights
- Heading is cyan on black, body is white on black

---

## Quick Reference: All Placeholders

### Content Slides

| Slide | Type | Placeholders |
|-------|------|--------------|
| 1 | title | client_name, presentation_name |
| 3 | section-divider | number, title |
| 4 | break-light | text |
| 5 | statement-dark | text |
| 6 | statement-light | text |
| 7 | three-column-text | title, heading_1-3, body_1-3 |
| 8 | three-column-images | title, subtitle, heading_1-3, caption_1-3 |
| 9 | two-column-text | title, heading_1-2, body_1-2 |
| 10 | photo-gallery-5 | title, heading_1-5, caption_1-5 |
| 11 | three-column-bubbles | title, bubble_1a-3b, body_1-3 |
| 12 | solid-bubbles | preheader, title, bubble_1-3, body_1-3 |
| 13 | statistics-grid | title, description, value_1-6, label_1-6, desc_1-6 |
| 14 | numbered-rows | number_1-2, title_1-2, subtitle_1-2, heading_1a-2b, body_1a-2b |
| 15 | two-panel-compare | preheader_left/right, heading_left/right, etc. |
| 16 | text-image-right | heading, body |
| 17 | image-text-right | heading, body |
| 18 | fullbleed-image | text |
| 19 | image-gradient-text | title, body |
| 20 | bold-title-image | preheader, title |
| 21 | script-page | title, intro, dialogue |
| 22 | storyboard-8 | title, caption_1-8 |
| 23 | timeline-process | image, header, step_*, num_*, callout_* |
| 24 | thank-you | (none - static content) |
| 25 | bullet-list | title, item_1-7 |
| 26 | single-stat | value, label, context |
| 27 | heading-paragraph | heading, body |
| 28 | highlights | title, item_1-5 |
| 29 | horizontal-split | title_top/bottom, subtitle_top/bottom, head_1a-2b, body_1a-2b |
| 30 | split-title-content | title, head_1-2, body_1-2 |
| 31 | final-thought | heading, body |

---

## Usage Example

```python
from pptx import Presentation

def replace_placeholder(slide, placeholder, new_text):
    """Replace a placeholder token with actual content."""
    for shape in slide.shapes:
        if shape.has_text_frame:
            if placeholder in shape.text_frame.text:
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.text = run.text.replace(placeholder, new_text)

# Example usage
prs = Presentation('../assets/ppt-template.pptx')
slide = prs.slides[6]  # Slide 7: three-column-text

replace_placeholder(slide, "{{three_col_text.title}}", "OUR KEY FINDINGS")
replace_placeholder(slide, "{{three_col_text.heading_1}}", "Insight One")
replace_placeholder(slide, "{{three_col_text.body_1}}", "The first insight shows...")

prs.save('output.pptx')
```
