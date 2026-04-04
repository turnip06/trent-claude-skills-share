#!/usr/bin/env python3
"""
Generate an HCO-branded Google Slides presentation from a slide spec.

Uses the `gws` CLI (Google Workspace CLI) to interact with the
Google Slides and Drive APIs. Authenticated as trent.michael@howatsonco.com.au.

Pipeline:
1. Copy template → new presentation
2. Get slide structure → slide object IDs
3. Duplicate needed slides, delete unused, reorder, replace text
4. Print Google Slides URL

Usage:
    python scripts/generate_google_slides.py

Functions:
    copy_template(title) → presentation_id
    get_presentation(presentation_id) → slide data
    generate_presentation(slide_specs, client, title) → URL
"""

import json
import subprocess
import sys
import re
from typing import Any

# Template presentation ID (native Google Slides, converted from ppt-template-v2.pptx)
# Slide 28 (highlights) was removed during conversion — 30 slides total
TEMPLATE_ID = "1lfJZ1ndsa8hiz1abE5L7kilb98DL6WlHLWLW4lC7yTI"

# Map PPTX template indices to Google Slides template indices
# Highlights slide (PPTX index 27) was removed, so indices 28+ shift down by 1
PPTX_TO_GSLIDES_INDEX = {
    0: 0,    # title
    # 1: skip (instructions)
    2: 2,    # section-divider
    3: 3,    # break-light
    4: 4,    # statement-dark
    5: 5,    # statement-light
    6: 6,    # three-column-text
    7: 7,    # three-column-images
    8: 8,    # two-column-text
    9: 9,    # photo-gallery-5
    10: 10,  # three-column-bubbles
    11: 11,  # solid-bubbles
    12: 12,  # statistics-grid
    13: 13,  # numbered-rows
    14: 14,  # two-panel-compare
    15: 15,  # text-image-right
    16: 16,  # image-text-right
    17: 17,  # fullbleed-image
    18: 18,  # image-gradient-text
    19: 19,  # bold-title-image
    20: 20,  # script-page
    21: 21,  # storyboard-8
    22: 22,  # timeline-process
    23: 23,  # thank-you
    24: 24,  # bullet-list
    25: 25,  # single-stat
    26: 26,  # heading-paragraph
    # 27: REMOVED (highlights — broke Google conversion)
    28: 27,  # horizontal-split (shifted -1)
    29: 28,  # split-title-content (shifted -1)
    30: 29,  # final-thought (shifted -1)
}


# Placeholders that use Anton font — replacement text is auto-uppercased
ANTON_PLACEHOLDERS = {
    "{{bold_title.preheader}}",
    "{{bold_title.title}}",
    "{{bullet_list.title}}",
    "{{compare.heading_left}}",
    "{{compare.heading_right}}",
    "{{final.heading}}",
    "{{gradient.title}}",
    "{{heading_paragraph.heading}}",
    "{{horizontal.title_bottom}}",
    "{{horizontal.title_top}}",
    "{{image_text.heading}}",
    "{{numbered_rows.number_1}}",
    "{{numbered_rows.number_2}}",
    "{{numbered_rows.subtitle_1}}",
    "{{numbered_rows.subtitle_2}}",
    "{{numbered_rows.title_1}}",
    "{{numbered_rows.title_2}}",
    "{{photo_gallery.title}}",
    "{{script.title}}",
    "{{section.number}}",
    "{{section.title}}",
    "{{single_stat.label}}",
    "{{single_stat.value}}",
    "{{solid_bubbles.title}}",
    "{{split.title}}",
    "{{statement_dark.text}}",
    "{{statement_light.text}}",
    "{{stats.title}}",
    "{{stats.value_1}}",
    "{{stats.value_2}}",
    "{{stats.value_3}}",
    "{{stats.value_4}}",
    "{{stats.value_5}}",
    "{{stats.value_6}}",
    "{{storyboard.title}}",
    "{{text_image.heading}}",
    "{{three_col_bubbles.title}}",
    "{{three_col_images.title}}",
    "{{three_col_text.title}}",
    "{{title.client_name}}",
    "{{title.presentation_name}}",
    "{{two_col_text.title}}",
}


def run_gws(args: list[str], input_json: dict | None = None) -> dict:
    """Run a gws CLI command and return parsed JSON output."""
    cmd = ["gws"] + args
    if input_json is not None:
        cmd.extend(["--json", json.dumps(input_json)])

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    stdout = result.stdout.strip()

    if result.returncode != 0:
        error_msg = stdout or result.stderr.strip()
        raise RuntimeError(f"gws command failed: {' '.join(args)}\n{error_msg}")

    if not stdout:
        return {}

    # Handle gws "Using keyring backend" prefix
    json_start = stdout.find("{")
    if json_start > 0:
        stdout = stdout[json_start:]

    return json.loads(stdout)


def copy_template(title: str) -> str:
    """Copy the template presentation to create a new one. Returns new ID."""
    result = run_gws(
        ["drive", "files", "copy", "--params", json.dumps({"fileId": TEMPLATE_ID})],
        input_json={"name": title},
    )
    return result["id"]


def get_presentation(presentation_id: str) -> dict:
    """Get full presentation data including slide object IDs."""
    return run_gws(
        [
            "slides",
            "presentations",
            "get",
            "--params",
            json.dumps({"presentationId": presentation_id}),
        ]
    )


def get_slide_ids(presentation: dict) -> list[str]:
    """Extract ordered list of slide object IDs from presentation data."""
    return [slide["objectId"] for slide in presentation.get("slides", [])]


def resolve_template_index(pptx_index: int) -> int:
    """
    Convert a PPTX template index to the Google Slides template index.

    The PPTX template has 31 slides. The Google Slides template has 30
    (highlights slide at PPTX index 27 was removed during conversion).
    """
    if pptx_index in PPTX_TO_GSLIDES_INDEX:
        return PPTX_TO_GSLIDES_INDEX[pptx_index]
    raise ValueError(
        f"PPTX template index {pptx_index} not available in Google Slides template. "
        f"Index 27 (highlights) was removed during conversion."
    )


def execute_batch_update(presentation_id: str, requests: list[dict]) -> dict:
    """Execute a batchUpdate on a Google Slides presentation."""
    if not requests:
        return {}
    return run_gws(
        [
            "slides",
            "presentations",
            "batchUpdate",
            "--params",
            json.dumps({"presentationId": presentation_id}),
        ],
        input_json={"requests": requests},
    )


def generate_output_title(client_name: str = "", presentation_title: str = "") -> str:
    """Generate a descriptive presentation title from content."""
    client = client_name.lstrip("+").strip()
    title = presentation_title.strip()

    if client and title:
        return f"{client} — {title}"
    elif client:
        return client
    elif title:
        return title
    else:
        return "HCO Presentation"


def generate_presentation(
    slide_specs: list[dict],
    client_name: str = "",
    presentation_title: str = "",
    template_id: str | None = None,
) -> str:
    """
    Generate a complete Google Slides presentation.

    Args:
        slide_specs: List of dicts, each with:
            - 'template_index': Which template slide to use (0-based, PPTX numbering)
            - 'replacements': Dict of {placeholder: text} pairs
        client_name: Client name for title
        presentation_title: Presentation title
        template_id: Override template ID (optional)

    Returns:
        URL of the generated Google Slides presentation
    """
    global TEMPLATE_ID
    if template_id:
        TEMPLATE_ID = template_id

    title = generate_output_title(client_name, presentation_title)
    print(f"Creating presentation: {title}")

    # Step 1: Copy template
    print("  Copying template...")
    new_id = copy_template(title)
    print(f"  New presentation ID: {new_id}")

    # Step 2: Get slide structure
    print("  Reading slide structure...")
    presentation = get_presentation(new_id)
    slide_ids = get_slide_ids(presentation)
    print(f"  Found {len(slide_ids)} template slides")

    # Step 3: Resolve PPTX indices to Google Slides indices
    resolved_specs = []
    for spec in slide_specs:
        gs_index = resolve_template_index(spec["template_index"])
        resolved_specs.append(
            {
                "gs_index": gs_index,
                "replacements": spec.get("replacements", {}),
            }
        )

    # Step 4: Build batch — duplicate needed slides with custom IDs
    requests = []
    new_slide_ids = []

    for i, spec in enumerate(resolved_specs):
        source_id = slide_ids[spec["gs_index"]]
        new_page_id = f"gen_{i}"

        requests.append(
            {
                "duplicateObject": {
                    "objectId": source_id,
                    "objectIds": {source_id: new_page_id},
                }
            }
        )
        new_slide_ids.append(new_page_id)

    # Delete all original template slides
    for sid in slide_ids:
        requests.append({"deleteObject": {"objectId": sid}})

    # Reorder duplicated slides
    for position, new_id_slide in enumerate(new_slide_ids):
        requests.append(
            {
                "updateSlidesPosition": {
                    "slideObjectIds": [new_id_slide],
                    "insertionIndex": position,
                }
            }
        )

    # Replace placeholder text (scoped to each slide)
    # Auto-uppercase text going into Anton-font placeholders
    for i, spec in enumerate(resolved_specs):
        page_id = new_slide_ids[i]
        for placeholder, new_text in spec["replacements"].items():
            if placeholder in ANTON_PLACEHOLDERS:
                new_text = new_text.upper()
            requests.append(
                {
                    "replaceAllText": {
                        "containsText": {"text": placeholder, "matchCase": True},
                        "replaceText": new_text,
                        "pageObjectIds": [page_id],
                    }
                }
            )

    print(f"  Built {len(requests)} API requests")

    # Step 5: Execute
    print("  Executing batch update...")
    execute_batch_update(new_id, requests)

    # Step 6: Return URL
    url = f"https://docs.google.com/presentation/d/{new_id}/edit"
    print(f"\n  Done! {url}")
    return url


def validate_presentation(presentation_id: str) -> list[str]:
    """
    Validate a generated presentation for remaining placeholders.

    Returns list of issues found (empty = valid).
    """
    presentation = get_presentation(presentation_id)
    issues = []
    placeholder_re = re.compile(r"\{\{[a-z_]+\.[a-z_0-9]+\}\}")

    for i, slide in enumerate(presentation.get("slides", [])):
        for element in slide.get("pageElements", []):
            shape = element.get("shape", {})
            for te in shape.get("text", {}).get("textElements", []):
                content = te.get("textRun", {}).get("content", "")
                matches = placeholder_re.findall(content)
                for m in matches:
                    issues.append(f"Slide {i + 1}: unreplaced placeholder {m}")

    return issues


# --------------------------------------------------------------------------- #
# Example / CLI
# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    EXAMPLE_SPECS = [
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
        {
            "template_index": 4,  # statement-dark
            "replacements": {
                "{{statement_dark.text}}": "WE NEED TO REACH GEN Z WITHOUT ALIENATING OUR CORE.",
            },
        },
        {
            "template_index": 12,  # statistics-grid
            "replacements": {
                "{{stats.title}}": "KEY METRICS",
                "{{stats.description}}": "Our research revealed these critical insights:",
                "{{stats.value_1}}": "47%",
                "{{stats.label_1}}": "Gen Z Discovery",
                "{{stats.desc_1}}": "Find brands on TikTok",
                "{{stats.value_2}}": "3.2x",
                "{{stats.label_2}}": "Engagement",
                "{{stats.desc_2}}": "Higher with authentic content",
            },
        },
        {
            "template_index": 23,  # thank-you
            "replacements": {},
        },
    ]

    print("HCO Google Slides Generator")
    print("-" * 40)
    print(f"Template: {TEMPLATE_ID}")
    print("-" * 40)

    try:
        url = generate_presentation(
            EXAMPLE_SPECS,
            client_name="+ACME CORP",
            presentation_title="Q4 BRAND STRATEGY",
        )
        print(f"\nGenerated: {url}")

        # Validate
        pres_id = url.split("/d/")[1].split("/")[0]
        issues = validate_presentation(pres_id)
        if issues:
            print("\nValidation issues:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("\nValidation: PASSED (no unreplaced placeholders)")
    except ValueError as e:
        print(f"\nSetup needed: {e}")
        sys.exit(1)
    except RuntimeError as e:
        print(f"\nAPI error: {e}")
        sys.exit(1)
