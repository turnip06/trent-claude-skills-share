> **When to use:** Use this skill for creating HCO PowerPoint presentations with detailed slide design, visual validation, and an 8-phase workflow including user approval. For quick python-pptx template-based generation, see `hco-pptx-deck`. For Google Slides output, see `create-hco-slides`.

# HCO Presentation Skill

## Contents
- [Quick Start](#quick-start)
- [Image References](#image-references)
- [Workflow](#workflow-checklist) (8 phases)
- [Content Rules](#content-rules)
- [Utility Scripts](#utility-scripts)
- [References](#references)
- [Troubleshooting](#troubleshooting)


## Dependencies

```bash
pip install python-pptx python-pptx-text-replacer pdf2image
```

**System requirement**: LibreOffice (`soffice`) for PPTX-to-PDF conversion in visual validation.


## Quick Start

**Input** (markdown):
```markdown
# Client: Acme Corp
# Title: Q4 Brand Strategy

## 01 THE CHALLENGE
> We need to reach Gen Z without alienating core customers.

### Key Stats
- 47% of Gen Z discover brands on TikTok
- 3.2x higher engagement with authentic content
- $143B annual spending power
```

**Output**: `acme-corp_q4-brand-strategy.pptx` with title slide, section divider, statement slide, and statistics grid.

**Naming**: Output files use descriptive names based on content: `{client}_{title}.pptx`


## Image References

Use `[IMAGE: description]` syntax to specify images that need manual replacement:

```markdown
## Product Showcase
[IMAGE: Hero product photo - lifestyle shot]
[IMAGE: Product detail - close-up of features]

### Team
[IMAGE: CEO headshot]
[IMAGE: Team group photo]
```

Image references are tracked during parsing and listed in the final summary (Phase 8) for manual replacement in PowerPoint.


## Workflow Checklist

**IMPORTANT**: All 8 phases are mandatory. Phase 7 (Visual Validation) and Phase 8 (Final Summary) must not be skipped.

### Phase 1: Parse Input
- [ ] Extract H1/H2 headers, bullets, quotes, stats
- [ ] Identify client name and presentation title
- [ ] Flag content exceeding length constraints

### Phase 2: Map to Slides

Match content patterns to slide types using **docs/TEMPLATE_CATALOG.md**.

Common mappings:
- H1 headings → `section-divider` (index 2)
- Key quotes → `statement-dark/light` (index 4/5)
- Statistics → `statistics-grid` (index 12)
- Bullet lists → `bullet-list` (index 24)
- Hero stat → `single-stat` (index 25)
- Title + body → `heading-paragraph` (index 26)
- Key callouts → `highlights` (index 27)
- End → `thank-you` (index 23)

**Image tracking**: When parsing, collect all `[IMAGE: ...]` references and note which slide they belong to. Track in format: `(slide_number, slide_type, image_description)`.

**Log gaps**: If content doesn't map cleanly to an existing template, log to **docs/SELF_IMPROVEMENT.md** before proceeding with best-available alternative.

### Phase 3: User Approval

Present slide mapping using a two-part format: compact list for clear mappings, side-by-side ASCII choices for ambiguous layouts. See **docs/LAYOUT_DECISIONS.md** for triggers and templates.

#### Step 1: Show Unambiguous Slides

For slides with clear content-to-layout mapping, display a compact table:

```
UNAMBIGUOUS SLIDES (N slides)
═════════════════════════════
#  | Type            | Content Preview
---|-----------------|----------------------------------
1  | title           | +ACME CORP / Q4 BRAND STRATEGY
2  | section-divider | 01 THE CHALLENGE
5  | thank-you       | (static)
```

**Unambiguous mappings** (no choice needed):
- Title slide → `title`
- Section headers → `section-divider`
- End of deck → `thank-you`
- Script format → `script-page`
- Storyboard → `storyboard-8`

#### Step 2: Present Ambiguous Choices

When content could map to multiple layouts, show side-by-side ASCII comparison.

**Example (statement slide):**
```
LAYOUT CHOICE: SLIDE 3
══════════════════════
Quote: "We need to reach Gen Z..."

  [A] statement-dark   [B] statement-light  [C] break-light
  ┌────────────────┐   ┌────────────────┐   ┌────────────────┐
  │░░░░░░░░░░░│▌│░│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
  │░ "We nee.."│▌│░│   │▓ "We nee.." ▓▓▓│   │▓▓ We need.. ▓▓▓│
  │░░░░░░░░░░░│▌│░│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
  └────────────────┘   └────────────────┘   └────────────────┘
   Black, bold          Cyan, bright         Transition

Choice [A/B/C, Enter=A]:
```

**Ambiguity triggers** (see docs/LAYOUT_DECISIONS.md):
1. **Statement**: blockquote → dark/light/break (3 options)
2. **Image+Text**: text + image → text-right/image-right/fullbleed (3 options)
3. **Multi-column**: 2-3 items → varies by count and visual style
4. **Data**: numeric stats → grid/bubbles/rows (3 options)
5. **Process**: sequential steps → rows/timeline (2 options)

#### Step 3: Confirm Final Order

After all choices, show complete slide list:

```
FINAL SLIDE ORDER
═════════════════
1. title
2. section-divider
3. statement-dark [CHOICE]
4. statistics-grid
5. thank-you

Proceed? [Y/n]:
```

**Status flags**: `[OK]`, `[AUTO-FIX]`, `[OVERFLOW]`, `[MISSING]`, `[SPLIT]`

#### Step 4: Show Required Images

If any `[IMAGE: ...]` references were found, display before approval:

```
REQUIRED IMAGES (manual replacement needed)
═══════════════════════════════════════════
Slide | Type              | Image Description
------|-------------------|----------------------------------
3     | photo-gallery-5   | Hero product photo - lifestyle shot
3     | photo-gallery-5   | Product detail - close-up of features
7     | text-image-right  | CEO headshot
12    | fullbleed-image   | Team group photo

Note: These images must be manually added in PowerPoint after generation.
```

**Wait for user approval** before proceeding.

**Log requests**: If user requests a layout variation, color, or design element not available, log to **docs/SELF_IMPROVEMENT.md**.

### Phase 4: Generate Code

Use functions from `scripts/generate_presentation.py`:

```python
from scripts.generate_presentation import (
    duplicate_slide,
    replace_placeholder,
    generate_output_filename,
)
```

**Key functions**:
- `duplicate_slide(prs, index)` - Copies slide preserving image/chart relationships
- `replace_placeholder(slide, token, text)` - Replaces text preserving formatting
- `generate_output_filename(client, title)` - Creates descriptive filename from content

See **docs/SLIDE_DETAILS.md** for exact placeholder tokens per slide type.

### Phase 5: Execute

1. Run the generated Python script
2. Use `generate_output_filename(client_name, title)` for descriptive naming (e.g., `acme-corp_q4-strategy.pptx`)
3. Report: "Created [filename] with [N] slides"

### Phase 6: Programmatic Validation

```bash
python scripts/validate_presentation.py {output_filename}.pptx -v
```

Checks: no remaining `{{placeholders}}`, font consistency, image presence, thank-you slide last.

If validation fails, return to Phase 4.

**Log failures**: If validation detects unreplaced tokens, broken images, or font substitution, log to **docs/SELF_IMPROVEMENT.md** (may indicate placeholder gaps or template issues).

### Phase 7: Visual Validation (MANDATORY)

**THIS PHASE IS REQUIRED. DO NOT SKIP.**

You MUST visually compare every generated slide against the template screenshots. This catches formatting issues that programmatic validation cannot detect.

#### Step 1: Export Generated Slides as Images

**First, verify LibreOffice is installed:**

```bash
which soffice || echo "LibreOffice not installed - install from https://www.libreoffice.org/"
```

If LibreOffice is not installed, stop and ask the user to install it before proceeding.

**Then export slides:**

```python
from pdf2image import convert_from_path
import subprocess
import shutil
import os

# Verify LibreOffice is installed
if not shutil.which("soffice"):
    raise RuntimeError("LibreOffice required. Install from https://www.libreoffice.org/")

# Use the generated filename (e.g., "acme-corp_q4-brand-strategy.pptx")
pptx_path = output_filename  # Set by Phase 5
pdf_path = pptx_path.replace(".pptx", ".pdf")
output_dir = "generated_screenshots"

os.makedirs(output_dir, exist_ok=True)

# Convert PPTX to PDF using LibreOffice
subprocess.run([
    "soffice", "--headless", "--convert-to", "pdf",
    "--outdir", ".", pptx_path
], check=True)

# Convert PDF pages to images
images = convert_from_path(pdf_path, dpi=150)
for i, img in enumerate(images, 1):
    img.save(f"{output_dir}/Slide{i}.jpeg", "JPEG")
```

#### Step 2: Visual Comparison (YOU MUST DO THIS)

**EXPLICIT INSTRUCTIONS - Follow these exactly:**

For each slide in your generated presentation, you MUST:

1. **Use the Read tool** to view the generated slide:
   ```
   Read: generated_screenshots/Slide1.jpeg
   ```

2. **Use the Read tool** to view the template screenshot (use semantic name from TEMPLATE_CATALOG.md):
   ```
   Read: assets/template-screenshots/title.jpeg
   ```

3. **With both images loaded, carefully compare:**
   - **Layout**: Are elements in the correct positions?
   - **Typography**: Are fonts correct (VC Nudge Black for headlines, Manrope for body)?
   - **Colors**: Are brand colors preserved (black #000000, cyan #7DD3E8)?
   - **Sidebar**: Is the sidebar present/absent as expected?
   - **Images**: Are all images visible and correctly positioned?
   - **Text content**: Is placeholder text replaced (no `{{tokens}}` visible)?
   - **Spacing**: Are margins and padding consistent with template?

4. **Repeat for each slide** (Slide1, Slide2, ... SlideN)

**Do not skip this step. Do not summarize. Actually read and compare every slide image.**

#### Step 3: Document Discrepancies

Create a comparison report:

```
VISUAL COMPARISON REPORT
========================
Slide 1 (title):
  - Template: [describe what you see]
  - Generated: [describe what you see]
  - Discrepancies: [list specific issues or "None"]

Slide 2 (section-divider):
  - Template: [describe what you see]
  - Generated: [describe what you see]
  - Discrepancies: [list specific issues or "None"]
...
```

#### Step 4: Fix and Retry Loop

**If ANY discrepancies are found:**

1. Identify the root cause (wrong placeholder, missing style, incorrect index)
2. Return to Phase 4 and fix the generation code
3. Re-run Phases 5, 6, and 7
4. **Repeat until all slides match the template**

**Only proceed to completion when visual validation passes with zero discrepancies.**

**Log issues**: If visual comparison reveals layout issues, missing elements, or formatting problems that indicate template limitations, log to **docs/SELF_IMPROVEMENT.md**.

### Phase 8: Final Summary

After visual validation passes, output the completion summary:

```
═══════════════════════════════════════════════════════════════
PRESENTATION COMPLETE
═══════════════════════════════════════════════════════════════

Output: acme-corp_q4-brand-strategy.pptx
Slides: 12
Validation: PASSED

REQUIRED IMAGES - MANUAL REPLACEMENT NEEDED
────────────────────────────────────────────
The following images must be manually added in PowerPoint:

Slide 3 (photo-gallery-5):
  • Hero product photo - lifestyle shot
  • Product detail - close-up of features

Slide 7 (text-image-right):
  • CEO headshot

Slide 12 (fullbleed-image):
  • Team group photo

INSTRUCTIONS:
1. Open acme-corp_q4-brand-strategy.pptx in PowerPoint
2. Navigate to each slide listed above
3. Right-click the placeholder image → "Change Picture"
4. Select the appropriate image file
5. Save the presentation

═══════════════════════════════════════════════════════════════
```

**If no images required**, output simpler summary:

```
═══════════════════════════════════════════════════════════════
PRESENTATION COMPLETE
═══════════════════════════════════════════════════════════════

Output: acme-corp_q4-brand-strategy.pptx
Slides: 12
Validation: PASSED
Images: No manual image replacement needed

═══════════════════════════════════════════════════════════════
```


## Content Rules

**NEVER rewrite user text** without explicit approval.

**Auto-transforms** (applied automatically):
- Headlines → UPPERCASE
- Section numbers → zero-padded ("1" → "01")
- Client names → + prefix ("Acme" → "+Acme")

**Sidebar rule**: Sidebar color always matches headline color on that slide.

See **docs/BRAND_ELEMENTS.md** for complete typography and color guidelines.


## Utility Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/validate_presentation.py` | Programmatic validation | `python scripts/validate_presentation.py output.pptx -v` |
| `scripts/generate_presentation.py` | Core generation functions | Import functions or see `if __name__ == "__main__"` example |

**Visual validation**: No script - you must use your vision capabilities to compare generated slides against `assets/template-screenshots/Slide*.jpeg`.


## References

| Document | Contents |
|----------|----------|
| docs/TEMPLATE_CATALOG.md | Slide types, indices, content-to-slide mapping |
| docs/LAYOUT_DECISIONS.md | Ambiguity triggers, decision tables, when to show options |
| docs/ASCII_TEMPLATES.md | ASCII art templates for Phase 3 previews |
| docs/SLIDE_DETAILS.md | Placeholder tokens, positions, screenshots |
| docs/BRAND_ELEMENTS.md | Typography, colors, sidebar rules |
| docs/VALIDATION_CHECKLIST.md | QA procedures, common issues |
| docs/SELF_IMPROVEMENT.md | Template gaps and feature requests log |
| docs/summary-changes.md | V2 changelog and technical details |

**Template file**: `assets/ppt-template-v2.pptx` (28 slides)
**Screenshots**: `assets/template-screenshots/{type-id}.jpeg` (e.g., `title.jpeg`, `bullet-list.jpeg`)


## Troubleshooting

### "Placeholder not found" warnings
**Cause**: Placeholder may be fragmented across XML runs
**Fix**: V2 functions handle this automatically via paragraph-level text reconstruction

### Fonts reverting to Arial/Calibri
**Cause**: Font properties not preserved during replacement
**Fix**: Use `replace_placeholder()` which preserves font properties

### Images missing after slide duplication
**Cause**: rId relationships not copied
**Fix**: Use `duplicate_slide()` which copies all relationships

### Run fragmentation issues
**Cause**: PowerPoint splits text like `{{title` + `.name}}`
**Fix**: V2 checks full paragraph text, handles multi-run replacement

### Visual validation discrepancies
**Cause**: Programmatic validation passes but slides don't match template visually
**Fix**: Compare each slide against `assets/template-screenshots/{type-id}.jpeg` (e.g., `title.jpeg`). Check layout, fonts, colors, sidebar presence. Return to Phase 4 and fix generation code.

### LibreOffice conversion fails
**Cause**: `soffice` not installed or not in PATH
**Fix**: Install LibreOffice, or use alternative: open PPTX manually and export slides as images
