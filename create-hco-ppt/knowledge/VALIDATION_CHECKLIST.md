# Validation Checklist V2

Complete this checklist after generating each presentation to ensure quality.

> **Template Version**: V2 (semantic `{{type.element}}` placeholders)
> **Script Version**: V2 (with python-pptx-text-replacer support)

## Table of Contents

- [Pre-Generation Checks](#pre-generation-checks)
  - [Input Validation](#input-validation)
  - [Mapping Review](#mapping-review)
- [Post-Generation Checks](#post-generation-checks)
  - [Slide Structure](#slide-structure)
  - [Content Quality](#content-quality)
  - [Formatting](#formatting)
  - [V2: Font Consistency (NEW)](#v2-font-consistency-new)
  - [V2: Image Preservation (NEW)](#v2-image-preservation-new)
  - [Sidebar/Watermark](#sidewatermark)
- [Technical Checks](#technical-checks)
  - [File Integrity](#file-integrity)
  - [Programmatic Validation (V2)](#programmatic-validation-v2)
- [Placeholder Reference](#placeholder-reference)
- [Common Issues & Fixes](#common-issues--fixes)
  - [V2-Specific Issues](#v2-specific-issues)
- [Sign-off Template](#sign-off-template)

---

## Pre-Generation Checks

### Input Validation
- [ ] All sections from user input have been mapped to slides
- [ ] Content length fits within slide constraints
- [ ] Statistics count does not exceed 6 per statistics-grid slide
- [ ] No prohibited content (secrets, credentials, etc.)

### Mapping Review
- [ ] Slide types match content purpose
- [ ] Section numbers are sequential (01, 02, 03...)
- [ ] Thank-you slide is included as final slide
- [ ] Title slide has client name and presentation name

---

## Post-Generation Checks

### Slide Structure
- [ ] Slide count matches approved mapping
- [ ] Slides are in correct order
- [ ] Thank-you slide is last (Index 23)
- [ ] No duplicate slides where not intended

### Content Quality
- [ ] **No placeholder tokens remaining**:
  - [ ] No `{{title.*}}` placeholders
  - [ ] No `{{section.*}}` placeholders
  - [ ] No `{{stats.*}}` placeholders
  - [ ] No `{{three_col_*.*}}` placeholders
  - [ ] No other `{{type.element}}` patterns
- [ ] All user content appears correctly
- [ ] Section numbers are sequential (01, 02, 03...)
- [ ] Statistics show actual numbers

### Formatting
- [ ] All headlines are UPPERCASE
- [ ] Client name has "+" prefix
- [ ] No text overflow visible
- [ ] Fonts render correctly

### V2: Font Consistency (NEW)
- [ ] No unexpected font substitutions (Arial/Calibri replacing brand fonts)
- [ ] VC Nudge Black used for headlines
- [ ] Manrope Light used for body text
- [ ] IBM Plex Mono used for watermarks

### V2: Image Preservation (NEW)
- [ ] All images from template are visible
- [ ] No broken/missing images after slide duplication
- [ ] Image positions match template

### Sidebar/Watermark
- [ ] Sidebar elements present where expected (slides 5, 13, 14, 15, 17, 18, 19, 20, 24)
- [ ] Watermark text is "© HOWATSON+COMPANY"
- [ ] Sidebar color matches headline color

---

## Technical Checks

### File Integrity
- [ ] File opens without corruption errors
- [ ] File size is reasonable (not bloated beyond template size)
- [ ] All slides render correctly in PowerPoint
- [ ] No error dialogs on open

### Programmatic Validation (V2)

Run the V2 validation script:

```bash
# Basic validation
python scripts/validate_presentation.py output.pptx

# Verbose output (recommended)
python scripts/validate_presentation.py output.pptx -v

# With template comparison
python scripts/validate_presentation.py output.pptx --template assets/ppt-template-v2.pptx -v

# JSON output for automation
python scripts/validate_presentation.py output.pptx --json
```

**V2 Validation Checks**:
- Unreplaced placeholder detection
- Slide count validation
- Thank-you slide presence
- **Font consistency check** (detects font substitution)
- **Image presence check** (detects broken images)
- **Empty slide detection**

Example output:
```
Validating: output.pptx
--------------------------------------------------
Slides: 5
Valid: YES

INFO:
  Total slides: 5
  Thank-you slide: Present
  Fonts used: VC Nudge Black, Manrope Light
  Total images: 3

[OK] Presentation passed validation
```

---

## Placeholder Reference

For placeholder prefixes and slide indices, see **TEMPLATE_CATALOG.md**.

For exact placeholder tokens per slide type, see **SLIDE_DETAILS.md**.

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Placeholder token remains | Find-replace missed | Check exact placeholder in SLIDE_DETAILS.md |
| Text overflow | Content too long | Trim content or split slides |
| Missing slide | Wrong index used | Check TEMPLATE_CATALOG.md for correct index |
| Formatting lost | Wrong replacement method | Use V2 `replace_placeholder()` with font preservation |
| Sidebar missing | Duplicated wrong slide | Only slides 5, 13, 14, 15, 17, 18, 19, 20, 24 have sidebars |

### V2-Specific Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Placeholder not found (fragmented) | Placeholder split across XML runs | V2 handles automatically; ensure using `replace_placeholder()` |
| Images missing after duplication | Old v1 `duplicate_slide()` didn't copy relationships | Use V2 `duplicate_slide()` with relationship copying |
| Font reverted to Arial | Font properties not preserved | V2 preserves fonts; check `apply_font_properties()` called |
| python-pptx-text-replacer errors | Package not installed | Run `pip install python-pptx-text-replacer` |

---

## Sign-off Template

```
## Presentation Validation Report

**Generated**: [DATE]
**Output File**: [FILENAME]
**Slide Count**: [N]

### Checks Passed
- [ ] Slide structure verified
- [ ] No placeholder tokens remaining
- [ ] Formatting correct
- [ ] File opens without errors

### Issues Found
[List any issues or "None"]

### Approved By
[User confirmation]
```
