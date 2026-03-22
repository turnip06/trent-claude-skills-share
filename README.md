# Trent's Shared Claude Skills

Curated skills for the team. Each skill can be used as a Claude skill or as a system prompt on any platform.

## How to Use

### Claude (claude.ai)

Each skill folder contains a `SKILL.md` with frontmatter. Package with `./package-skills.sh` from the repo root and upload the ZIP to **Settings > Skills**.

### H+Co / ChatGPT / Other Platforms

Use the `system-prompts/` folder. Each subfolder contains:

- **PROMPT.md** — The system prompt (paste a folder as custom instructions)
- **README.md** — Brief usage guide
- **Reference files** — Upload as knowledge files alongside the prompt (where available)

## Skills

### Presentations & Design

| Skill             | What it does                                          |
| ----------------- | ----------------------------------------------------- |
| create-hco-ppt    | H+Co branded PowerPoint decks from markdown           |
| create-hco-slides | H+Co branded Google Slides from markdown              |
| hco-html-deck     | H+Co HTML presentations                               |
| hco-pptx-deck     | PowerPoint matching H+Co brand template               |
| hco-design-system | H+Co visual language reference                        |
| hco-pdf           | H+Co styled HTML documents / PDFs                     |
| slide-designer    | Design slides as HTML, screenshot, evaluate, iterate  |
| slide-prompter ⭐    | Analyse slides and write image generation prompts     |
| analyse-deck ⭐      | Structured breakdown and review of presentation decks |

### Image Generation

| Skill                  | What it does                                         |
| ---------------------- | ---------------------------------------------------- |
| img-generate           | Three distinct image prompt variations per concept   |
| img-edit               | Edit or combine images into compositions             |
| img-compose            | Photorealistic visual vocabulary reference library   |
| img-analyse            | Reverse-engineer prompts from images (Style DNA)     |
| campaign-image-prompts | Cohesive image prompt suites for campaigns           |
| nano-banana-pro ⭐        | Production-ready Nano Banana Pro image prompts       |
| social-grid            | Nano Banana Pro prompts for social media phone grids |

### Video & Storyboarding

| Skill                  | What it does                                        |
| ---------------------- | --------------------------------------------------- |
| cinema-mode ⭐            | Rewrite prompts into cinematic film still style     |
| kling-prompt-optimiser ⭐ | Optimise prompts for Kling 3.0 video generation     |
| script-to-storyboard ⭐   | Extract 9 key beats from a script into a storyboard |
| storyboard-to-video ⭐    | Process storyboard images into 4K cinematic frames  |

### Research & Utilities

| Skill              | What it does                                           |
| ------------------ | ------------------------------------------------------ |
| 30-day-search      | Deep research on latest AI tools and techniques        |
| clean-doc          | Apply clean, unbranded design to documents             |
| youtube-summarizer | YouTube transcript extraction and actionable summaries |