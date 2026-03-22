# Template Catalog

Quick reference for all 31 usable slide layouts in the Howatson+Company template.

> **Template Version**: Standardized (semantic `{{type.element}}` placeholders)

## Table of Contents

- [Slide Index Mapping](#slide-index-mapping)
- [Complete Slide Catalog](#complete-slide-catalog)
  - [Slide 1: `title`](#slide-1-title)
  - [Slide 3: `section-divider`](#slide-3-section-divider)
  - [Slide 4: `break-light`](#slide-4-break-light)
  - [Slide 5: `statement-dark`](#slide-5-statement-dark)
  - [Slide 6: `statement-light`](#slide-6-statement-light)
  - [Slide 7: `three-column-text`](#slide-7-three-column-text)
  - [Slide 8: `three-column-images`](#slide-8-three-column-images)
  - [Slide 9: `two-column-text`](#slide-9-two-column-text)
  - [Slide 10: `photo-gallery-5`](#slide-10-photo-gallery-5)
  - [Slide 11: `three-column-bubbles`](#slide-11-three-column-bubbles)
  - [Slide 12: `solid-bubbles`](#slide-12-solid-bubbles)
  - [Slide 13: `statistics-grid`](#slide-13-statistics-grid)
  - [Slide 14: `numbered-rows`](#slide-14-numbered-rows)
  - [Slide 15: `two-panel-compare`](#slide-15-two-panel-compare)
  - [Slide 16: `text-image-right`](#slide-16-text-image-right)
  - [Slide 17: `image-text-right`](#slide-17-image-text-right)
  - [Slide 18: `fullbleed-image`](#slide-18-fullbleed-image)
  - [Slide 19: `image-gradient-text`](#slide-19-image-gradient-text)
  - [Slide 20: `bold-title-image`](#slide-20-bold-title-image)
  - [Slide 21: `script-page`](#slide-21-script-page)
  - [Slide 22: `storyboard-8`](#slide-22-storyboard-8)
  - [Slide 23: `timeline-process`](#slide-23-timeline-process)
  - [Slide 24: `thank-you`](#slide-24-thank-you)
  - [Slide 25: `bullet-list`](#slide-25-bullet-list)
  - [Slide 26: `single-stat`](#slide-26-single-stat)
  - [Slide 27: `heading-paragraph`](#slide-27-heading-paragraph)
  - [Slide 28: `highlights`](#slide-28-highlights)
  - [Slide 29: `horizontal-split`](#slide-29-horizontal-split)
  - [Slide 30: `split-title-content`](#slide-30-split-title-content)
  - [Slide 31: `final-thought`](#slide-31-final-thought)
- [Content-to-Slide Matching](#content-to-slide-matching)
- [Usage Example](#usage-example)

## Slide Index Mapping

Use these indices when duplicating slides with `duplicate_slide(prs, index)`.

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
| 24 | 23 | `thank-you` | (static - no placeholders) |
| 25 | 24 | `bullet-list` | `{{bullet_list.*}}` |
| 26 | 25 | `single-stat` | `{{single_stat.*}}` |
| 27 | 26 | `heading-paragraph` | `{{heading_paragraph.*}}` |
| 28 | 27 | `highlights` | `{{highlights.*}}` |
| 29 | 28 | `horizontal-split` | `{{horizontal.*}}` |
| 30 | 29 | `split-title-content` | `{{split.*}}` |
| 31 | 30 | `final-thought` | `{{final.*}}` |

---

## Complete Slide Catalog

### Slide 1: `title`
| Property | Value |
|----------|-------|
| **Index** | 0 |
| **Background** | Black |
| **Purpose** | Opening/cover slide |
| **Placeholders** | `{{title.client_name}}`, `{{title.presentation_name}}` |
| **Has Sidebar** | No |

---

### Slide 3: `section-divider`
| Property | Value |
|----------|-------|
| **Index** | 2 |
| **Background** | Cyan (#7DD3E8) |
| **Purpose** | Major section breaks |
| **Placeholders** | `{{section.number}}`, `{{section.title}}` |
| **Has Sidebar** | Visual only (in master) |

---

### Slide 4: `break-light`
| Property | Value |
|----------|-------|
| **Index** | 3 |
| **Background** | Cyan (#7DD3E8) |
| **Purpose** | Subsection transitions |
| **Placeholders** | `{{break.text}}` |
| **Has Sidebar** | No |

---

### Slide 5: `statement-dark`
| Property | Value |
|----------|-------|
| **Index** | 4 |
| **Background** | Black |
| **Purpose** | Key insight/quote |
| **Placeholders** | `{{statement_dark.text}}` |
| **Has Sidebar** | Yes |

---

### Slide 6: `statement-light`
| Property | Value |
|----------|-------|
| **Index** | 5 |
| **Background** | Cyan (#7DD3E8) |
| **Purpose** | Key insight/quote |
| **Placeholders** | `{{statement_light.text}}` |
| **Has Sidebar** | No |

---

### Slide 7: `three-column-text`
| Property | Value |
|----------|-------|
| **Index** | 6 |
| **Background** | White |
| **Purpose** | Dense text content |
| **Placeholders** | `{{three_col_text.title}}`, `{{three_col_text.heading_1-3}}`, `{{three_col_text.body_1-3}}` |
| **Has Sidebar** | No |

---

### Slide 8: `three-column-images`
| Property | Value |
|----------|-------|
| **Index** | 7 |
| **Background** | White |
| **Purpose** | Visual + text |
| **Placeholders** | `{{three_col_images.title}}`, `{{three_col_images.subtitle}}`, `{{three_col_images.heading_1-3}}`, `{{three_col_images.caption_1-3}}` |
| **Has Sidebar** | No |

---

### Slide 9: `two-column-text`
| Property | Value |
|----------|-------|
| **Index** | 8 |
| **Background** | White |
| **Purpose** | Comparison/parallel |
| **Placeholders** | `{{two_col_text.title}}`, `{{two_col_text.heading_1-2}}`, `{{two_col_text.body_1-2}}` |
| **Has Sidebar** | No |

---

### Slide 10: `photo-gallery-5`
| Property | Value |
|----------|-------|
| **Index** | 9 |
| **Background** | White |
| **Purpose** | Photo showcase |
| **Placeholders** | `{{photo_gallery.title}}`, `{{photo_gallery.heading_1-5}}`, `{{photo_gallery.caption_1-5}}` |
| **Has Sidebar** | No |

---

### Slide 11: `three-column-bubbles`
| Property | Value |
|----------|-------|
| **Index** | 10 |
| **Background** | White |
| **Purpose** | Features/benefits |
| **Placeholders** | `{{three_col_bubbles.title}}`, `{{three_col_bubbles.bubble_1a-3b}}`, `{{three_col_bubbles.body_1-3}}` |
| **Has Sidebar** | No |

---

### Slide 12: `solid-bubbles`
| Property | Value |
|----------|-------|
| **Index** | 11 |
| **Background** | Cyan (#7DD3E8) |
| **Purpose** | Key points highlight |
| **Placeholders** | `{{solid_bubbles.preheader}}`, `{{solid_bubbles.title}}`, `{{solid_bubbles.bubble_1-3}}`, `{{solid_bubbles.body_1-3}}` |
| **Has Sidebar** | No |

---

### Slide 13: `statistics-grid`
| Property | Value |
|----------|-------|
| **Index** | 12 |
| **Background** | Split Black/Cyan |
| **Purpose** | Data showcase (6 stats max) |
| **Placeholders** | `{{stats.title}}`, `{{stats.description}}`, `{{stats.value_1-6}}`, `{{stats.label_1-6}}`, `{{stats.desc_1-6}}` |
| **Has Sidebar** | Yes |

---

### Slide 14: `numbered-rows`
| Property | Value |
|----------|-------|
| **Index** | 13 |
| **Background** | Cyan accent (split top/bottom) |
| **Purpose** | Process/numbered (2 sections) |
| **Placeholders** | `{{numbered_rows.number_1-2}}`, `{{numbered_rows.title_1-2}}`, `{{numbered_rows.subtitle_1-2}}`, `{{numbered_rows.heading_*}}`, `{{numbered_rows.body_*}}` |
| **Has Sidebar** | Yes |

---

### Slide 15: `two-panel-compare`
| Property | Value |
|----------|-------|
| **Index** | 14 |
| **Background** | Split Cyan/White |
| **Purpose** | Side-by-side comparison |
| **Placeholders** | `{{compare.preheader_left/right}}`, `{{compare.heading_left/right}}`, `{{compare.subheading_left/right}}`, `{{compare.bubble_*}}`, `{{compare.body_*}}` |
| **Has Sidebar** | Yes |

---

### Slide 16: `text-image-right`
| Property | Value |
|----------|-------|
| **Index** | 15 |
| **Background** | White |
| **Purpose** | Editorial layout |
| **Placeholders** | `{{text_image.heading}}`, `{{text_image.body}}` |
| **Has Sidebar** | No |

---

### Slide 17: `image-text-right`
| Property | Value |
|----------|-------|
| **Index** | 16 |
| **Background** | Cyan accent |
| **Purpose** | Editorial layout |
| **Placeholders** | `{{image_text.heading}}`, `{{image_text.body}}` |
| **Has Sidebar** | Yes |

---

### Slide 18: `fullbleed-image`
| Property | Value |
|----------|-------|
| **Index** | 17 |
| **Background** | Photo (full-bleed) |
| **Purpose** | Visual impact |
| **Placeholders** | `{{fullbleed.text}}` |
| **Has Sidebar** | Yes |

---

### Slide 19: `image-gradient-text`
| Property | Value |
|----------|-------|
| **Index** | 18 |
| **Background** | Photo with gradient overlay |
| **Purpose** | Narrative/script |
| **Placeholders** | `{{gradient.title}}`, `{{gradient.body}}` |
| **Has Sidebar** | Yes |

---

### Slide 20: `bold-title-image`
| Property | Value |
|----------|-------|
| **Index** | 19 |
| **Background** | Photo |
| **Purpose** | Section opener |
| **Placeholders** | `{{bold_title.preheader}}`, `{{bold_title.title}}` |
| **Has Sidebar** | Yes |

---

### Slide 21: `script-page`
| Property | Value |
|----------|-------|
| **Index** | 20 |
| **Background** | White |
| **Purpose** | Video script/dialogue |
| **Placeholders** | `{{script.title}}`, `{{script.intro}}`, `{{script.dialogue}}` |
| **Has Sidebar** | No |

---

### Slide 22: `storyboard-8`
| Property | Value |
|----------|-------|
| **Index** | 21 |
| **Background** | White |
| **Purpose** | Video treatment (8 frames) |
| **Placeholders** | `{{storyboard.title}}`, `{{storyboard.caption_1-8}}` |
| **Has Sidebar** | No (copyright in top-right instead) |

---

### Slide 23: `timeline-process`
| Property | Value |
|----------|-------|
| **Index** | 22 |
| **Background** | Cyan (#7DD3E8) |
| **Purpose** | Workflow/process (6 steps) |
| **Placeholders** | `{{timeline.image}}`, `{{timeline.header}}`, `{{timeline.step_*}}`, `{{timeline.num_*}}`, `{{timeline.callout_*}}` |
| **Has Sidebar** | No |

---

### Slide 24: `thank-you`
| Property | Value |
|----------|-------|
| **Index** | 23 |
| **Background** | Black |
| **Purpose** | Closing slide |
| **Placeholders** | None (static "THANK YOU" text) |
| **Has Sidebar** | Yes |

---

### Slide 25: `bullet-list`
| Property | Value |
|----------|-------|
| **Index** | 24 |
| **Background** | White |
| **Purpose** | Simple vertical bullet list for takeaways, requirements, next steps |
| **Placeholders** | `{{bullet_list.title}}`, `{{bullet_list.item_1}}` through `{{bullet_list.item_7}}` |
| **Has Sidebar** | No |
| **Notes** | Uses single text box with proper bullet formatting (7 paragraphs with • characters) |

---

### Slide 26: `single-stat`
| Property | Value |
|----------|-------|
| **Index** | 25 |
| **Background** | Black |
| **Purpose** | Hero statistic with maximum visual impact |
| **Placeholders** | `{{single_stat.value}}`, `{{single_stat.label}}`, `{{single_stat.context}}` |
| **Has Sidebar** | Yes |

---

### Slide 27: `heading-paragraph`
| Property | Value |
|----------|-------|
| **Index** | 26 |
| **Background** | White |
| **Purpose** | Simple heading and body text |
| **Placeholders** | `{{heading_paragraph.heading}}`, `{{heading_paragraph.body}}` |
| **Has Sidebar** | No |

---

### Slide 28: `highlights`
| Property | Value |
|----------|-------|
| **Index** | 27 |
| **Background** | White |
| **Purpose** | Large callout statements with generous spacing for visual emphasis |
| **Placeholders** | `{{highlights.title}}`, `{{highlights.item_1}}` through `{{highlights.item_5}}` |
| **Has Sidebar** | No |

---

### Slide 29: `horizontal-split`
| Property | Value |
|----------|-------|
| **Index** | 28 |
| **Background** | Split Cyan (top) / White (bottom) |
| **Purpose** | Two horizontal sections for TELL/ASK+COLLABORATE content patterns |
| **Placeholders** | `{{horizontal.title_top}}`, `{{horizontal.subtitle_top}}`, `{{horizontal.head_1a}}`, `{{horizontal.body_1a}}`, `{{horizontal.head_1b}}`, `{{horizontal.body_1b}}`, `{{horizontal.title_bottom}}`, `{{horizontal.subtitle_bottom}}`, `{{horizontal.head_2a}}`, `{{horizontal.body_2a}}`, `{{horizontal.head_2b}}`, `{{horizontal.body_2b}}` |
| **Has Sidebar** | No |

---

### Slide 30: `split-title-content`
| Property | Value |
|----------|-------|
| **Index** | 29 |
| **Background** | Split Cyan (left) / White (right) |
| **Purpose** | Large title on left with 2 content sections on right |
| **Placeholders** | `{{split.title}}`, `{{split.head_1}}`, `{{split.body_1}}`, `{{split.head_2}}`, `{{split.body_2}}` |
| **Has Sidebar** | No |

---

### Slide 31: `final-thought`
| Property | Value |
|----------|-------|
| **Index** | 30 |
| **Background** | Black |
| **Purpose** | Closing thought slide with cyan heading and white body |
| **Placeholders** | `{{final.heading}}`, `{{final.body}}` |
| **Has Sidebar** | Yes |

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
| Key callout statements | `highlights` | 27 | `highlights` |
| Two-section layout (e.g., TELL/ASK) | `horizontal-split` | 28 | `horizontal` |
| Split layout with title on left | `split-title-content` | 29 | `split` |
| Closing thought or final insight | `final-thought` | 30 | `final` |
| End of presentation | `thank-you` | 23 | (none) |

---

## Usage Example

```python
from pptx import Presentation

# Load template
prs = Presentation('assets/ppt-template.pptx')

# Duplicate slide by index
def duplicate_slide(prs, index):
    template_slide = prs.slides[index]
    slide_layout = template_slide.slide_layout
    new_slide = prs.slides.add_slide(slide_layout)
    # Copy shapes...
    return new_slide

# Simple placeholder replacement
def replace_placeholder(slide, placeholder, new_text):
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    if placeholder in run.text:
                        run.text = run.text.replace(placeholder, new_text)

# Example: Create a three-column-text slide
slide = prs.slides[6]
replace_placeholder(slide, "{{three_col_text.title}}", "OUR KEY FINDINGS")
replace_placeholder(slide, "{{three_col_text.heading_1}}", "Insight One")
replace_placeholder(slide, "{{three_col_text.body_1}}", "Details about the first insight...")
```
