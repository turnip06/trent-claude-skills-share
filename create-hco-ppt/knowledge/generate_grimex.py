#!/usr/bin/env python3
"""
Generate GRIME-X Creative Concepts Presentation.

25 slides using the HCO template.

Two-phase approach:
1. Duplicate slides and remove originals
2. Apply text replacements to the saved file
"""

import os
import sys

# Add parent directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from generate_presentation import (
    duplicate_slide,
    replace_placeholder,
    Presentation,
)

# Paths relative to skills/create-hco-ppt-v2/
SKILL_DIR = os.path.dirname(script_dir)
TEMPLATE = os.path.join(SKILL_DIR, "assets", "ppt-template-v2.pptx")
OUTPUT = os.path.join(SKILL_DIR, "output.pptx")

# All slide specifications
SLIDE_SPECS = [
    # Slide 1: Title
    {
        'template_index': 0,
        'replacements': {
            '{{title.client_name}}': '+GRIME-X',
            '{{title.presentation_name}}': 'CREATIVE CONCEPTS PRESENTATION',
        }
    },
    # Slide 2: Statement Dark - Hygiene Boom
    {
        'template_index': 4,
        'replacements': {
            '{{statement_dark.text}}': "WE'RE TO TALK ABOUT THE HYGIENE BOOM",
        }
    },
    # Slide 3: Text + Image - Product bottle
    {
        'template_index': 15,
        'replacements': {
            '{{text_image.heading}}': "MORE SPECIFICALLY, WHAT WE'RE GOING TO DO ABOUT IT... NATURALLY.",
            '{{text_image.body}}': '[IMAGE A: Grime-X Plant-Based Heavy Duty Spray bottle]',
        }
    },
    # Slide 4: Text + Image - Pressure diagram
    {
        'template_index': 15,
        'replacements': {
            '{{text_image.heading}}': 'WE KNOW THIS CATEGORY LIVES WITH PRESSURE FROM ALL SIDES.',
            '{{text_image.body}}': '[IMAGE B: Arrow pointing to list - Consumers, Environmental Groups, Health Regulators]',
        }
    },
    # Slide 5: Statement Light - Make people pay attention
    {
        'template_index': 5,
        'replacements': {
            '{{statement_light.text}}': 'BUT WE ALSO KNOW THAT WE HAVE TO MAKE PEOPLE PAY ATTENTION.',
        }
    },
    # Slide 6: Three Column - Today agenda
    {
        'template_index': 6,
        'replacements': {
            '{{three_col_text.title}}': 'TODAY',
            '{{three_col_text.heading_1}}': '> STRATEGY RECAP',
            '{{three_col_text.heading_2}}': '> CREATIVE CONCEPTS',
            '{{three_col_text.heading_3}}': '> SUMMARY',
            '{{three_col_text.body_1}}': ' ',
            '{{three_col_text.body_2}}': ' ',
            '{{three_col_text.body_3}}': ' ',
        }
    },
    # Slide 7: Break Light - Objective
    {
        'template_index': 3,
        'replacements': {
            '{{break.text}}': 'SELECT ONE CREATIVE CONCEPT TO DEVELOP FURTHER WITH ALL PARTNER AGENCIES',
        }
    },
    # Slide 8: Section Divider - Strategy
    {
        'template_index': 2,
        'replacements': {
            '{{section.number}}': '01',
            '{{section.title}}': 'STRATEGY',
        }
    },
    # Slide 9: Text + Image - Market leader
    {
        'template_index': 15,
        'replacements': {
            '{{text_image.heading}}': "WE'RE THE MARKET LEADER, BUT THE CATEGORY IS UNDER INCREASING PRESSURE",
            '{{text_image.body}}': '[IMAGE C: News article montage - "Study links harsh bleach to lung issues", "Parents ditching chemical cleaners", "Chlorine banned in schools"]',
        }
    },
    # Slide 10: Text + Image - Consumer solutions
    {
        'template_index': 15,
        'replacements': {
            '{{text_image.heading}}': 'CONSUMERS ARE TURNING TO SOLUTIONS THAT ARE SAFE FOR THEIR FAMILIES, THEIR PETS AND THE ENVIRONMENT',
            '{{text_image.body}}': '[IMAGE D: Forum post montage - "Cleaners irritating my dog\'s paws", "Safe heavy duty cleaner?", "Fume-free solutions?"]',
        }
    },
    # Slide 11: Solid Bubbles - Challenge stats
    {
        'template_index': 11,
        'replacements': {
            '{{solid_bubbles.preheader}}': 'THIS IS REFLECTED BY THE CHALLENGE WE IDENTIFIED IN THE BRIEF',
            '{{solid_bubbles.title}}': "PEOPLE WANT SOLUTIONS THAT ARE SAFE BUT THEY ALSO DON'T WANT THEM TO SUCK.",
            '{{solid_bubbles.bubble_1}}': '-8%',
            '{{solid_bubbles.body_1}}': 'Safe around children',
            '{{solid_bubbles.bubble_2}}': '-10%',
            '{{solid_bubbles.body_2}}': 'Safe around pets',
            '{{solid_bubbles.bubble_3}}': '-13%',
            '{{solid_bubbles.body_3}}': 'Effective Natural Solutions',
        }
    },
    # Slide 12: Statement Dark - Own the X
    {
        'template_index': 4,
        'replacements': {
            '{{statement_dark.text}}': "OWN THE 'X' IN OUR NAME BY PROVING THAT IT'S JUST AS EFFECTIVE, WHILE BEING SAFER FOR THE THINGS YOU REALLY CARE ABOUT.",
        }
    },
    # Slide 13: Statement Light - Nature is awesome
    {
        'template_index': 5,
        'replacements': {
            '{{statement_light.text}}': "BECAUSE NATURE IS F******G AWESOME IT'S POWERFUL IT'S REAL IT'S REJUVENATING AND IT'S RUTHLESS. WHEN IT NEEDS TO BE.",
        }
    },
    # Slide 14: Three Column - Strategy RTBs
    {
        'template_index': 6,
        'replacements': {
            '{{three_col_text.title}}': "THE STRATEGY: 'NATURAL' IS NEVER A COMPROMISE",
            '{{three_col_text.heading_1}}': 'RTB 1',
            '{{three_col_text.heading_2}}': 'RTB 2',
            '{{three_col_text.heading_3}}': 'RTB 3',
            '{{three_col_text.body_1}}': 'Based upon Natural active enzymes that contain no bleach and no ammonia or harsh fumes.',
            '{{three_col_text.body_2}}': 'Safe for skin and lungs. Does not irritate eyes, throat, or pets.',
            '{{three_col_text.body_3}}': 'Eliminates grease and mould and is available in spray and concentrate.',
        }
    },
    # Slide 15: Statement Dark - Ruthless
    {
        'template_index': 4,
        'replacements': {
            '{{statement_dark.text}}': "DURING OUR CREATIVE CONCEPTING, WE REALLY ATTACHED OURSELVES TO ONE PARTICULARLY PIECE: 'RUTHLESS'",
        }
    },
    # Slide 16: Text + Image - Website screenshot
    {
        'template_index': 15,
        'replacements': {
            '{{text_image.heading}}': "DON'T LET DIRTY NO GOOD FILTH INVADE YOUR HOME!",
            '{{text_image.body}}': '[IMAGE E: Screenshot of Pure Home / Grime-X website product page]',
        }
    },
    # Slide 17: Two Panel Compare - Creative anchor
    {
        'template_index': 14,
        'replacements': {
            '{{compare.preheader_left}}': 'STRATEGIC PROPOSITION',
            '{{compare.heading_left}}': 'NATURAL IS NEVER A COMPROMISE',
            '{{compare.subheading_left}}': "A declarative stake in the ground that Grime-X Natural's range isn't a lesser option.",
            '{{compare.bubble_left_1}}': ' ',
            '{{compare.body_left_1}}': ' ',
            '{{compare.bubble_left_2}}': ' ',
            '{{compare.body_left_2}}': ' ',
            '{{compare.preheader_right}}': 'CREATIVE ANCHOR',
            '{{compare.heading_right}}': 'BAD FOR GRIME. NOT BAD FOR YOU.',
            '{{compare.subheading_right}}': "It's an effective solution that keeps your whole family safe when you need it most.",
            '{{compare.bubble_right_1}}': ' ',
            '{{compare.body_right_1}}': ' ',
            '{{compare.bubble_right_2}}': ' ',
            '{{compare.body_right_2}}': ' ',
        }
    },
    # Slide 18: Section Divider - Creative
    {
        'template_index': 2,
        'replacements': {
            '{{section.number}}': '02',
            '{{section.title}}': 'CREATIVE',
        }
    },
    # Slide 19: Statement Light - Five Ideas
    {
        'template_index': 5,
        'replacements': {
            '{{statement_light.text}}': 'WE HAVE FIVE IDEAS TO SHARE TODAY',
        }
    },
    # Slide 20: Text + Image - Five pillars
    {
        'template_index': 15,
        'replacements': {
            '{{text_image.heading}}': 'EACH WITH A UNIQUE WAY IN TO OUR STRATEGY',
            '{{text_image.body}}': '[IMAGE F: Diagram with 5 pillars - ONE: Full volume approach, TWO: Focus on byproduct of effectiveness, THREE: Solution as big as the problem, FOUR: Behavioural shift to a reflex, FIVE: Partnership - part celebration, part intervention]',
        }
    },
    # Slide 21: Text + Image - Provocation + logos
    {
        'template_index': 15,
        'replacements': {
            '{{text_image.heading}}': "FOR EACH, WE'VE FOCUSED ON PROVOCATION. THIS IS WHAT WILL DRIVE OUTSIZED IMPACT FOR OUR CAMPAIGN. BUT WE'RE NOT BEING PROVOCATIVE TOWARDS THEM. THIS IS ABOUT DIRT.",
            '{{text_image.body}}': '[IMAGE G: Earth Alliance and National Health Board logos]',
        }
    },
    # Slide 22: Statement Dark - If not provocative
    {
        'template_index': 4,
        'replacements': {
            '{{statement_dark.text}}': "IF WE'RE NOT PROVOCATIVE NO ONE WILL GIVE A DAMN",
        }
    },
    # Slide 23: Statement Light - For people who love clean
    {
        'template_index': 5,
        'replacements': {
            '{{statement_light.text}}': "SO IT'S FOR PEOPLE WHO LOVE CLEAN BUT HATE FUMES.",
        }
    },
    # Slide 24: Section Divider - 01 only
    {
        'template_index': 2,
        'replacements': {
            '{{section.number}}': '01',
            '{{section.title}}': ' ',
        }
    },
    # Slide 25: Thank You
    {
        'template_index': 23,
        'replacements': {}  # No replacements needed - static slide
    },
]


def main():
    """Generate the GRIME-X presentation."""
    print("Generating GRIME-X Creative Concepts Presentation...")
    print(f"Template: {TEMPLATE}")
    print(f"Output: {OUTPUT}")
    print("-" * 50)

    if not os.path.exists(TEMPLATE):
        print(f"ERROR: Template not found: {TEMPLATE}")
        sys.exit(1)

    # PHASE 1: Duplicate slides
    print("\nPhase 1: Duplicating slides...")
    prs = Presentation(TEMPLATE)
    original_count = len(prs.slides)
    print(f"  Template has {original_count} slides")

    for i, spec in enumerate(SLIDE_SPECS, 1):
        template_idx = spec['template_index']
        print(f"  Creating slide {i} from template index {template_idx}")
        duplicate_slide(prs, template_idx)

    # Remove original template slides
    print(f"\n  Removing {original_count} original template slides...")
    for i in range(original_count - 1, -1, -1):
        rId = prs.slides._sldIdLst[i].rId
        prs.part.drop_rel(rId)
        del prs.slides._sldIdLst[i]

    # Save intermediate file
    prs.save(OUTPUT)
    print(f"  Saved intermediate file with {len(prs.slides)} slides")

    # PHASE 2: Apply text replacements
    print("\nPhase 2: Applying text replacements...")
    prs = Presentation(OUTPUT)

    for slide_idx, spec in enumerate(SLIDE_SPECS):
        replacements = spec.get('replacements', {})
        if not replacements:
            continue

        slide = prs.slides[slide_idx]
        for placeholder, text in replacements.items():
            replaced = replace_placeholder(slide, placeholder, text)
            if not replaced:
                print(f"  WARNING: Slide {slide_idx + 1} - '{placeholder}' not found")

    # Save final file
    prs.save(OUTPUT)
    print(f"\nGenerated: {OUTPUT}")
    print(f"Total slides: {len(prs.slides)}")

    return OUTPUT


if __name__ == "__main__":
    main()
