> **When to use:** Use this skill for creating HCO Google Slides presentations via the gws CLI. Outputs a shareable Google Slides URL. For PowerPoint (.pptx) output, see `hco-pptx-deck` or `create-hco-ppt`.

# HCO Google Slides Skill

## Contents
- [Quick Start](#quick-start)
- [Image References](#image-references)
- [Workflow](#workflow-checklist) (8 phases)
- [Content Rules](#content-rules)
- [Utility Scripts](#utility-scripts)
- [References](#references)
- [Troubleshooting](#troubleshooting)


## Dependencies

**System requirement**: `gws` CLI (Google Workspace CLI), authenticated as `trent.michael@howatsonco.com.au`.

```bash
# Verify gws is installed and authenticated
gws auth status
```


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

**Output**: Google Slides URL → `https://docs.google.com/presentation/d/<ID>/edit`


## Image References

Use `[IMAGE: description]` syntax to specify images that need manual replacement:

```markdown
## Product Showcase
[IMAGE: Hero product photo - lifestyle shot]

### Team
[IMAGE: CEO headshot]
```

Image references are tracked during parsing and listed in the final summary (Phase 8) for manual replacement in Google Slides.


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

### Phase 3: User Approval

Present slide mapping using a two-part format: compact list for clear mappings, side-by-side ASCII choices for ambiguous layouts.

#### Step 1: Show Unambiguous Slides

```
UNAMBIGUOUS SLIDES (N slides)
═════════════════════════════
#  | Type            | Content Preview
---|-----------------|----------------------------------
1  | title           | +ACME CORP / Q4 BRAND STRATEGY
2  | section-divider | 01 THE CHALLENGE
5  | thank-you       | (static)
```

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

#### Step 3: Confirm Final Order

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

#### Step 4: Show Required Images

If any `[IMAGE: ...]` references were found, display before approval:

```
REQUIRED IMAGES (manual replacement needed)
═══════════════════════════════════════════
Slide | Type              | Image Description
------|-------------------|----------------------------------
3     | photo-gallery-5   | Hero product photo - lifestyle shot
7     | text-image-right  | CEO headshot
```

**Wait for user approval** before proceeding.

### Phase 4: Generate Code

Build a Python script using functions from `scripts/generate_google_slides.py`:

```python
from scripts.generate_google_slides import generate_presentation

slide_specs = [
    {
        "template_index": 0,  # title
        "replacements": {
            "{{title.client_name}}": "+ACME CORP",
            "{{title.presentation_name}}": "Q4 BRAND STRATEGY",
        },
    },
    {
        "template_index": 2,  # section-divider
        "replacements": {
            "{{section.number}}": "01",
            "{{section.title}}": "THE CHALLENGE",
        },
    },
    # ... more slides
    {
        "template_index": 23,  # thank-you
        "replacements": {},
    },
]

url = generate_presentation(
    slide_specs,
    client_name="+ACME CORP",
    presentation_title="Q4 BRAND STRATEGY",
)
```

See **docs/TEMPLATE_CATALOG.md** for exact placeholder tokens per slide type.

### Phase 5: Execute

1. Run the generated Python script
2. Script copies template, applies replacements, returns URL
3. Report: "Created presentation with [N] slides: [URL]"

### Phase 6: Programmatic Validation

After generation, verify via the Slides API:

```bash
gws slides presentations get --params '{"presentationId": "<ID>"}'
```

Check:
- Correct number of slides
- No remaining `{{placeholder}}` tokens in text elements
- Slide order matches spec

If validation fails, return to Phase 4.

### Phase 7: Visual Validation (MANDATORY)

**THIS PHASE IS REQUIRED. DO NOT SKIP.**

Open the Google Slides URL in the browser and visually verify each slide.

#### Step 1: Open in Browser

Navigate to the generated URL using browser automation or ask the user to open it.

#### Step 2: Visual Comparison

For each slide, verify:
- **Layout**: Elements in correct positions
- **Typography**: Anton for headlines, Manrope for body
- **Colors**: Brand colors preserved (black #000000, cyan #7DD3E8)
- **Sidebar**: Present/absent as expected
- **Text content**: Placeholder text replaced (no `{{tokens}}` visible)
- **Spacing**: Margins and padding consistent

#### Step 3: Fix and Retry Loop

If ANY discrepancies found:
1. Identify root cause
2. Return to Phase 4 and fix
3. Re-run Phases 5, 6, and 7
4. Repeat until all slides match

### Phase 8: Final Summary

After visual validation passes:

```
═══════════════════════════════════════════════════════════════
PRESENTATION COMPLETE
═══════════════════════════════════════════════════════════════

URL: https://docs.google.com/presentation/d/<ID>/edit
Slides: 12
Validation: PASSED

REQUIRED IMAGES - MANUAL REPLACEMENT NEEDED
────────────────────────────────────────────
The following images must be manually added in Google Slides:

Slide 3 (photo-gallery-5):
  • Hero product photo - lifestyle shot

Slide 7 (text-image-right):
  • CEO headshot

INSTRUCTIONS:
1. Open the URL above in your browser
2. Navigate to each slide listed above
3. Click the placeholder image → Replace image
4. Select the appropriate image file
5. Share the presentation as needed

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
| `scripts/generate_google_slides.py` | Core generation via gws CLI | Import functions or run directly |

**Key functions**:
- `copy_template(title)` — Copies template presentation → new ID
- `get_presentation(id)` — Gets full slide structure
- `build_batch_requests(specs, slides)` — Builds API update requests
- `execute_batch_update(id, requests)` — Applies all changes
- `generate_presentation(specs, client, title)` — Full pipeline → URL


## References

| Document | Contents |
|----------|----------|
| docs/TEMPLATE_CATALOG.md | Slide types, indices, content-to-slide mapping, API notes |
| docs/BRAND_ELEMENTS.md | Typography, colors, sidebar rules, font mapping |

**Template**: Google Slides presentation (converted from `ppt-template-v2.pptx`)


## Troubleshooting

### "gws command failed" errors
**Cause**: gws CLI not authenticated or token expired
**Fix**: Run `gws auth login` to re-authenticate

### Template ID not set
**Cause**: `TEMPLATE_ID` placeholder not updated in script
**Fix**: Set the correct Google Slides template presentation ID in `scripts/generate_google_slides.py`

### Fonts showing as Arial/default
**Cause**: Anton or Manrope not available in the Google Workspace account
**Fix**: These are Google Fonts — they should auto-resolve. If not, manually add them via Google Slides → Format → Text → More fonts

### Placeholder text not replaced
**Cause**: Placeholder token doesn't match exactly (case-sensitive)
**Fix**: Verify placeholder format matches `{{type.element}}` exactly as in TEMPLATE_CATALOG.md

### "This operation is not supported" from Slides API
**Cause**: Trying to use Slides API on a PPTX file (not converted)
**Fix**: Ensure the template is a native Google Slides presentation, not a PPTX in compatibility mode

### Slide duplication creates blank slides
**Cause**: `duplicateObject` objectIds mapping incorrect
**Fix**: Check that source slide objectId exists in the presentation. Run `get_presentation()` to verify.
