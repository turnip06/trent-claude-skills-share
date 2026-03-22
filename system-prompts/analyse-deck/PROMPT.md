# Analyse Deck

Analyse a creative brief deck and produce a structured breakdown.

Input: $ARGUMENTS

## Instructions

### Step 1 - Parse input

Parse `$ARGUMENTS` to extract:
- **Path**: The file or folder path (required). Could be a folder of exported PNG/JPG slide images or a single PDF file.
- **Brand/project hint**: Any additional context included after the path (optional). Used to search for related context.

If no path is provided, ask the user for one and stop.

### Step 2 - Detect input type

- If the path is a directory, glob for `*.png`, `*.jpg`, `*.jpeg` files inside it. These are the slides.
- If the path is a file ending in `.pdf`, this is the deck PDF. Read it using the Read tool with page ranges.
- If neither, tell the user the path must be a folder of images or a PDF file, and stop.

### Step 3 - Search for existing context

Before analysing slides, explore the input folder (and its parent) for related documentation. Run these searches in parallel:

1. **Sibling files**: Glob for `*.md`, `*.pdf`, `*.txt`, `*.docx` files alongside the input (briefs, guidelines, notes).
2. **Subfolders**: Check for any `reference/`, `brand/`, `brief/`, or similarly named subdirectories.
3. **Parent folder**: Check one level up for related brand or project context.

Read any relevant documents found. Store this context for later use. If nothing is found, proceed without — the slides themselves are sufficient.

### Step 4 - Read all slides

- **Image folder**: Read every image file using the Read tool (Claude's vision will process them).
- **PDF**: Read the PDF using the Read tool with `pages` parameter. Process in batches of 10-15 pages if the PDF is large.

### Step 5 - Analyse each slide

For each slide, determine its type and describe accordingly:

- **Simple slides** (text on solid background, title cards, section dividers): Write a brief one-line description of the content. If the slide contains roughly 500 words or less of readable text, include the exact text verbatim after the description.
- **Visual slides** (imagery, layouts, mockups, references, photography, illustrations): Write a detailed description covering:
  - What the image shows (subject, setting, composition)
  - Visual style (colour palette, mood, lighting, texture, diagram, illustration, infographic, cinematic style, overall vibe)
  - How it relates to the brief (if provided)
  - Content type tag: `visual reference` | `inspiration` | `previous work` | `wireframe` | `mockup` | `OOH` | `headline` | `photography description` | `character/scene/environment description` | `sketch/rough` | `layout`

### Step 6 - Identify routes

Group the slides by creative route if multiple routes exist in the deck. If there's only one route, still give it a descriptive name. Look for:
- Section divider slides
- Shifts in visual direction or concept
- Explicit route labels in the deck

### Step 7 - Cross-reference with found context

If Step 3 found any briefs, guidelines, or reference docs, compare the slide content against them:
- Note where slides align with existing briefs or brand guidelines
- Flag any gaps (things in the brief not addressed in the deck, or vice versa)
- Flag any contradictions with brand guidelines

If no context was found in Step 3, skip this step.

### Step 8 - Infer the brief

Read between the lines. Articulate the actual ask/task for the designer, informed by both:
- What the slides show and imply
- Any existing documentation found nearby

The inferred brief should answer:
- What is the designer being asked to create?
- What are the constraints (format, size, channel)?
- What is the creative territory or mood?
- What must be avoided?

### Step 9 - Confirm with user

Present to Trent:
1. The inferred brief (clear, concise)
2. A summary of the routes found
3. How many slides were analysed
4. Any relevant context found nearby
5. Any gaps or contradictions noted

Ask Trent to confirm or correct the brief before writing the analysis. **Stop and wait for confirmation.**

### Step 10 - Write analysis

After Trent confirms, derive a short project name from the brief (lowercase, hyphens).

**Output location**: Write the analysis alongside the input:
- If input is a folder: `{folder}/ideate-analysis-{project-name}.md`
- If input is a PDF: write as a sibling file in the same directory, e.g. `{pdf-dir}/ideate-analysis-{project-name}.md`

Use this format:

```markdown
type: reference
tags:
  - reference
  - ideation
  - active
brand: "[[brand-name]]"
project: "[[project-name]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD

# Ideation Analysis: [Brief/Project Name]

## The Brief
[The confirmed brief from Step 9]

## Deck Analysis

### Route 1: [Route Name]
#### Slide 1: [Title/Description]
[Description - brief for simple slides, detailed for visual slides]
...

### Route 2: [Route Name]
...

## Found Context
[Summary of relevant brand guidelines, briefs, or reference docs found, or "None found"]

## Gaps and Contradictions
[Any issues noted in Step 7, or "None identified"]
```

Use today's date for `created` and `updated`.
