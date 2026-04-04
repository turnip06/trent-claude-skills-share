# Self-Improvement Log

> This file logs template gaps, design requests, and feature limitations encountered during presentation generation. Review periodically to identify patterns and prioritize new template additions.

## Table of Contents

- [Quick Stats](#quick-stats)
- [Trigger Categories](#trigger-categories)
- [Log Entry Format](#log-entry-format)
- [Pending Entries](#pending-entries)
- [Resolved Entries](#resolved-entries)
- [Common Patterns](#common-patterns)

## Quick Stats
- Total Entries: 3
- Pending Review: 0
- Resolved: 3

---

## Trigger Categories

Log an entry when any of the following occur:

1. **Missing Template Types** - Content doesn't fit any of the 24 existing layouts, item counts not supported (4, 7, >8 items), hybrid layouts needed
2. **New Layout Requests** - User explicitly asks for a different arrangement or describes a layout that doesn't exist
3. **Color/Brand Variations** - User requests colors outside current palette (black, cyan #7DD3E8, white)
4. **Content Overflow** - Text too long for placeholders, too many items for template capacity
5. **Feature Requests** - Animations, embedded video/audio, interactive elements, charts/graphs beyond statistics grid
6. **Typography Variations** - Font size adjustments, font weight/style not available
7. **Accessibility & i18n** - Alt-text requirements, RTL/non-Latin script support, color contrast issues
8. **Placeholder Gaps** - Slide type exists but lacks needed placeholder tokens
9. **Validation Failures** - Unreplaced tokens, broken images, font substitution detected

---

## Log Entry Format

```markdown
### [YYYY-MM-DD HH:MM] Category: Brief Title

**Context**: What was the user trying to create?

**Gap Identified**: What template/feature was missing?

**Content Sample** (if applicable):
> Truncated example of the problematic content...

**Current Workaround**: How did Claude handle it? (if applicable)

**Suggested Solution**: What new slide/feature would solve this?

**Priority**: Low | Medium | High

---
```

---

## Pending Entries

*No entries yet.*

---

## Resolved Entries

### [2026-01-10 14:00] Validation Failure: Placeholders Not Replaced

**Context**: Generating presentations with formatted placeholders (client names, titles)

**Gap Identified**: PowerPoint XML splits text across multiple "runs" unpredictably. A placeholder like `{{title.client_name}}` was stored as `{{title` + `.client_name}}` in separate runs. V1's run-by-run replacement failed to find fragmented placeholders.

**Content Sample**:
> Run 1: "{{title" | Run 2: ".client_name}}"

**Current Workaround**: N/A - placeholder was silently skipped

**Suggested Solution**: Assemble full paragraph text from all runs before matching

**Priority**: High

**Resolution**: V2 redesigned replacement logic - see `replace_in_shape_with_formatting()` in generate_presentation.py

---

### [2026-01-10 15:30] Validation Failure: Brand Fonts Replaced with Defaults

**Context**: Headlines and body text reverting to Arial/Calibri instead of VC Nudge Black and Manrope Light

**Gap Identified**: When V1 replaced placeholder text, it updated only the text content of runs, losing font formatting (name, size, color, bold/italic).

**Content Sample**:
> Before: "{{title.client_name}}" in VC Nudge Black 36pt
> After: "+ACME" in Arial 18pt

**Current Workaround**: N/A - styling was lost

**Suggested Solution**: Capture font properties before replacement, restore after

**Priority**: High

**Resolution**: V2 added `get_font_properties()` and `apply_font_properties()` functions

---

### [2026-01-10 17:00] Validation Failure: Images Missing After Slide Duplication

**Context**: Multi-slide presentations with duplicated slides containing images showed broken image placeholders

**Gap Identified**: V1's slide duplication used `deepcopy()` which copied shape elements but not relationship IDs (rIds) linking shapes to embedded images. Duplicated slides had shape elements pointing to non-existent image relationships.

**Content Sample**:
> Slide 5 (duplicated from template slide 8): Logo sidebar visible in template, missing in output

**Current Workaround**: N/A - images were broken

**Suggested Solution**: Copy relationships from template slide to new slide: `new_slide.part.relate_to(rel.target_part, rel.reltype)`

**Priority**: High

**Resolution**: V2 `duplicate_slide()` now builds rId mapping and updates all relationship references in copied XML

---

---

## Common Patterns

*Patterns will emerge as entries accumulate. Check back after 5+ entries.*
