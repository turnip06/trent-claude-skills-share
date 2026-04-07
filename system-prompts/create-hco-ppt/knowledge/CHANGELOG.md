# Changelog

## 2026-01-17
Generate presentation code, Execute script to create PPTX, Run programmatic validation, Visual validation of slides, Output final summary

## 2026-01-17
Read existing slide creation scripts for patterns, Create fix_bullet_list_slide.py to fix Index 24, Create add_template_slides_v3.py for new slides 28-30, Run scripts to update ppt-template-v2.pptx, Update TEMPLATE_CATALOG.md with new slide entries, Update SLIDE_DETAILS.md with placeholder specs, Update CHANGELOG.md, Take screenshots of updated slides, Test with validate_presentation.py

## 2026-01-17 - Slide Template Updates

### FIX: Bullet list (Index 24) now uses proper bullet formatting
- Previous implementation used 7 separate text boxes
- New implementation uses single text box with 7 bulleted paragraphs
- Added `fix_bullet_list_slide.py` script to rebuild the slide
- Bullets use • character with 12pt paragraph spacing

### FEATURE: Added horizontal-split slide (Index 28)
- Two horizontal sections: cyan (top) and white (bottom)
- Each section has title, subtitle, and 2 columns of heading+body
- 12 total placeholders for TELL/ASK+COLLABORATE content patterns
- Added via `add_template_slides_v3.py`

### FEATURE: Added split-title-content slide (Index 29)
- Vertical split: cyan (left) with title, white (right) with content
- Large title on left half, 2 content sections on right
- 5 placeholders: title, head_1, body_1, head_2, body_2
- Added via `add_template_slides_v3.py`

### FEATURE: Added final-thought slide (Index 30)
- Black background with sidebar watermark
- Cyan heading (VC Nudge Black 48pt) + white body (Manrope Light 16pt)
- 2 placeholders: heading, body
- Added via `add_template_slides_v3.py`

### Files added
- `scripts/fix_bullet_list_slide.py` - Rebuilds bullet-list with proper formatting
- `scripts/add_template_slides_v3.py` - Adds 3 new slides (indices 28-30)

### Files modified
- `assets/ppt-template-v2.pptx` - Now contains 31 slides
- `docs/TEMPLATE_CATALOG.md` - Added entries for new slides, updated count to 31
- `docs/SLIDE_DETAILS.md` - Added placeholder specs for new slides

---

## 2026-01-17
Phase 1: Parse input content, Phase 2: Map content to slide templates, Phase 3: User approval of slide mapping, Phase 4: Generate Python code, Phase 5: Execute and create PPTX, Phase 6: Programmatic validation, Phase 7: Visual validation, Phase 8: Final summary

## 2026-01-11
Parse input content, Map content to slide types, Get user approval on mapping, Generate Python script, Execute generation script, Run programmatic validation, Visual validation (compare slides), Final summary

## 2026-01-11
Create update_template_line_spacing.py script, Run script to update ppt-template-v2.pptx, Update generate_presentation.py with line spacing preservation, Update BRAND_ELEMENTS.md with line spacing documentation, Update SLIDE_DETAILS.md with line spacing notes

## 2026-01-11
Update Contents section to include Image References and 8 phases, Add Image References section after Quick Start, Update Phase 2 with image tracking, Add Step 4 to Phase 3 for Required Images display, Update Workflow Checklist header to 8 phases, Add Phase 8: Final Summary after Phase 7

## 2026-01-11
Read generate_presentation.py and SLIDE_DETAILS.md for placeholder info, Generate Python script for 25-slide GRIME-X presentation, Execute script to create output.pptx, Run programmatic validation, Visual validation against template screenshots, Output image requirements list

## 2026-01-11
Add type hints and import to generate_presentation.py, Document magic constant WIDE_SECTION_NUMBER_GLYPHS, Add error logging to silent except blocks in generate_presentation.py, Replace bare except in validate_presentation.py, Add 3 historical entries to SELF_IMPROVEMENT.md, Create test_generate.py with unit test stubs, Verify syntax and run validation

## 2026-01-11 - Smart ASCII Preview for Ambiguous Slides

### FEATURE: Phase 3 now shows ASCII options only for ambiguous layouts

**Problem**: Previous Phase 3 showed ASCII preview for ALL slides (verbose, 25+ previews).

**Solution**: Two-part approval format:
1. **Unambiguous slides**: Compact table (title, section-divider, thank-you, etc.)
2. **Ambiguous slides**: Side-by-side ASCII comparison with A/B/C options

**Ambiguity categories**:
- Statement: dark/light/break (3 options)
- Image+Text: text-right/image-right/fullbleed (3 options)
- Multi-column: varies by item count (2-6 options)
- Data: grid/bubbles/rows (3 options)
- Process: rows/timeline (2 options)

### Files added:
- `docs/LAYOUT_DECISIONS.md` - Ambiguity triggers, decision tables, compact ASCII templates

### Files modified:
- `SKILL.md` (Phase 3 rewritten with 3-step workflow)
- `docs/ASCII_TEMPLATES.md` (added compact comparison section)

---

## 2026-01-11 - V3 Bug Fixes (Image, Background, Layout)

### FIX: Images now display correctly
- Rewrote `duplicate_slide()` to build rId mapping from old to new relationships
- Updates all `r:embed`, `r:link`, `r:id` attributes in copied elements
- Fixes "The picture can't be displayed" errors

### FIX: Slide backgrounds now copy correctly
- Changed from copying only shapes (spTree) to copying entire cSld element
- cSld includes background (bg) element which was previously lost
- Fixes cyan backgrounds on statement-light, solid-bubbles, section-divider slides

### FIX: Long headlines no longer cut off
- Added `adjust_heading_height()` function
- Auto-expands text box height for content exceeding ~50 characters
- Expands upward (preserves bottom anchor) on text-image-right slides

### FIX: Section divider number/title overlap
- Added `adjust_section_title_position()` function
- Shifts title right when section number contains wide glyphs (0,2,3,6,8,9)
- Prevents "02", "03" etc. from overlapping with title text

### Files modified:
- `scripts/generate_presentation.py` (lines 98-264 rewritten)
- `scripts/generate_grime_x.py` (imports + generate_presentation_clean)

## 2026-01-11
Show ASCII preview of all 25 slides for approval, Generate Python script with slide_specs, Execute script to create output.pptx, Run programmatic validation, Perform visual validation

## 2026-01-11
Create docs/ASCII_TEMPLATES.md with all 22 slide types, Update SKILL.md Phase 3 to reference templates and show examples

## 2026-01-11
Add placeholder tokens to slide 3 using python-pptx-text-replacer, Verify tokens appear correctly in template, Run test generation and validation

## 2026-01-11
Create generation script for Grime-X presentation, Execute generation script, Run programmatic validation, Run visual validation (compare each slide to template)

## 2026-01-11
Fix YAML frontmatter in SKILL.md, Add table of contents to SKILL.md, Remove 'What's New in V2' section, Remove inline Python code block (130+ lines), Condense phase descriptions with links, Simplify content rules section, Remove duplicate tables from BRAND_ELEMENTS.md, Remove duplicate tables from VALIDATION_CHECKLIST.md, Verify line count and run checks
