# Template Catalog (Google Slides)

Quick reference for all 31 usable slide layouts in the Howatson+Company Google Slides template.

> **Template source**: Converted from `ppt-template-v2.pptx` to native Google Slides format.
> **Template ID**: `1lfJZ1ndsa8hiz1abE5L7kilb98DL6WlHLWLW4lC7yTI`
> **Placeholder format**: `{{slide_type.element_name}}`
> **Note**: Slide 28 (`highlights`) was removed during PPTX→Google Slides conversion (it caused a 400 error). Use `bullet-list` as an alternative. The script auto-translates PPTX indices → Google Slides indices, so **use PPTX indices** (matching the original `create-hco-ppt` catalog) in your slide specs.

## Table of Contents

- [Slide Index Mapping](#slide-index-mapping)
- [Content-to-Slide Matching](#content-to-slide-matching)
- [Google Slides API Notes](#google-slides-api-notes)
  - [Placeholder Replacement](#placeholder-replacement)
  - [Slide Duplication](#slide-duplication)
  - [Key Differences from PPTX Workflow](#key-differences-from-pptx-workflow)
  - [Font Mapping (PPTX → Google Slides)](#font-mapping-pptx--google-slides)

## Slide Index Mapping

Use these indices when specifying `template_index` in slide specs.

| Slide # | Index | Type ID | Placeholders |
|---------|-------|---------|--------------|
| 1 | 0 | `title` | `{{title.*}}` |
| 2 | 1 | _(instructions - skip)_ | - |
| 3 | 2 | `section-divider` | `{{section.*}}` |
| 4 | 3 | `break-light` | `{{break.*}}` |
| 5 | 4 | `statement-dark` | `{{statement_dark.*}}` |
| 6 | 5 | `statement-light` | `{{statement_light.*}}` |
| 7 | 6 | `three-column-text` | `{{three_col_text.*}}` |
| 8 | 7 | `three-column-images` | `{{three_col_images.*}}` |
| 9 | 8 | `two-column-text` | `{{two_col_text.*}}` |
| 10 | 9 | `photo-gallery-5` | `{{photo_gallery.*}}` |
| 11 | 10 | `three-column-bubbles` | `{{three_col_bubbles.*}}` |
| 12 | 11 | `solid-bubbles` | `{{solid_bubbles.*}}` |
| 13 | 12 | `statistics-grid` | `{{stats.*}}` |
| 14 | 13 | `numbered-rows` | `{{numbered_rows.*}}` |
| 15 | 14 | `two-panel-compare` | `{{compare.*}}` |
| 16 | 15 | `text-image-right` | `{{text_image.*}}` |
| 17 | 16 | `image-text-right` | `{{image_text.*}}` |
| 18 | 17 | `fullbleed-image` | `{{fullbleed.*}}` |
| 19 | 18 | `image-gradient-text` | `{{gradient.*}}` |
| 20 | 19 | `bold-title-image` | `{{bold_title.*}}` |
| 21 | 20 | `script-page` | `{{script.*}}` |
| 22 | 21 | `storyboard-8` | `{{storyboard.*}}` |
| 23 | 22 | `timeline-process` | `{{timeline.*}}` |
| 24 | 23 | `thank-you` | (static) |
| 25 | 24 | `bullet-list` | `{{bullet_list.*}}` |
| 26 | 25 | `single-stat` | `{{single_stat.*}}` |
| 27 | 26 | `heading-paragraph` | `{{heading_paragraph.*}}` |
| 28 | ~~27~~ | ~~`highlights`~~ | ~~`{{highlights.*}}`~~ *(removed — broke conversion)* |
| 29 | 27 | `horizontal-split` | `{{horizontal.*}}` |
| 30 | 28 | `split-title-content` | `{{split.*}}` |
| 31 | 29 | `final-thought` | `{{final.*}}` |

---

## Content-to-Slide Matching

| Content Pattern | Best Slide Type | Index | Placeholder Prefix |
|-----------------|-----------------|-------|-------------------|
| Document title / presentation name | `title` | 0 | `title` |
| Major section heading (# H1) | `section-divider` | 2 | `section` |
| Key quote, insight, or thesis | `statement-dark/light` | 4/5 | `statement_dark/light` |
| 3 parallel points/features | `three-column-text` | 6 | `three_col_text` |
| 3 items with images | `three-column-images` | 7 | `three_col_images` |
| 2 parallel points or comparison | `two-column-text` | 8 | `two_col_text` |
| Statistics, metrics (up to 6) | `statistics-grid` | 12 | `stats` |
| Sequential steps or process | `numbered-rows` | 13 | `numbered_rows` |
| Side-by-side comparison | `two-panel-compare` | 14 | `compare` |
| Long-form text with image | `text-image-right` | 15 | `text_image` |
| Hero/feature image | `fullbleed-image` | 17 | `fullbleed` |
| Photo collection | `photo-gallery-5` | 9 | `photo_gallery` |
| Video script or dialogue | `script-page` | 20 | `script` |
| Simple bullet list, takeaways | `bullet-list` | 24 | `bullet_list` |
| Single hero statistic | `single-stat` | 25 | `single_stat` |
| Heading with body paragraph | `heading-paragraph` | 26 | `heading_paragraph` |
| ~~Key callout statements~~ | ~~`highlights`~~ | ~~27~~ | *(not available in Google Slides template)* |
| Two-section layout (e.g., TELL/ASK) | `horizontal-split` | 28 | `horizontal` |
| Split layout with title on left | `split-title-content` | 29 | `split` |
| Closing thought or final insight | `final-thought` | 30 | `final` |
| End of presentation | `thank-you` | 23 | (none) |

---

## Google Slides API Notes

### Placeholder Replacement

The script uses `replaceAllText` scoped to specific slide pages via `pageObjectIds`.
This is more reliable than positional replacement since Google Slides handles
text runs differently than PowerPoint.

### Slide Duplication

Uses `duplicateObject` which preserves all formatting, backgrounds, shapes,
and images — equivalent to the PPTX `duplicate_slide()` function.

### Key Differences from PPTX Workflow

| Aspect | PPTX (create-hco-ppt) | Google Slides (create-hco-slides) |
|--------|----------------------|----------------------------------|
| Output | Local `.pptx` file | Google Slides URL |
| API | python-pptx | Google Slides API via `gws` CLI |
| Text replace | Per-run with formatting preservation | `replaceAllText` (formatting preserved natively) |
| Slide copy | Deep XML clone with rId mapping | `duplicateObject` (API handles it) |
| Fonts | VC Nudge Black, Manrope, IBM Plex Mono | Anton (headlines), Manrope (body) |
| Validation | LibreOffice → PDF → screenshots | Open URL in browser |

### Font Mapping (PPTX → Google Slides)

| PPTX Font | Google Slides Font | Reason |
|-----------|-------------------|--------|
| VC Nudge Black | Anton | VC Nudge not available in Google Fonts; Anton is the closest match (bold condensed sans) |
| Manrope Light | Manrope | Available in Google Fonts |
| IBM Plex Mono | IBM Plex Mono | Available in Google Fonts |
