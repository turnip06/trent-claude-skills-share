# Storyboard-to-Frames Skill

Analyze a storyboard grid image (typically 4x2, 8-9 frames) using Gemini 3 Flash with agentic vision, generate optimized cinematic prompts per frame, and produce 4K 16:9 images via the fal CLI.

## How to Run

```bash
python3 ~/.claude/skills/storyboard-to-video/scripts/storyboard-to-frames.py <image_path> [options]
```

Always run with Bash `dangerouslyDisableSandbox: true` (the script needs network access for Gemini API and delegates to fal CLI which writes to ~/Downloads).

## Basic Usage

```bash
# Analyze and generate all scene frames
python3 ~/.claude/skills/storyboard-to-video/scripts/storyboard-to-frames.py /path/to/storyboard.png

# Dry run — Gemini analysis only, no image generation
python3 ~/.claude/skills/storyboard-to-video/scripts/storyboard-to-frames.py --dry-run /path/to/storyboard.jpg
```

## Bookend Frames

Generate additional frames before the first scene and/or after the last scene for smoother video transitions:

```bash
# Start frame only (5 seconds before frame 1)
python3 ~/.claude/skills/storyboard-to-video/scripts/storyboard-to-frames.py --start-frame /path/to/storyboard.png

# End frame only (5 seconds after last scene)
python3 ~/.claude/skills/storyboard-to-video/scripts/storyboard-to-frames.py --end-frame /path/to/storyboard.png

# Both bookend frames
python3 ~/.claude/skills/storyboard-to-video/scripts/storyboard-to-frames.py --start-frame --end-frame /path/to/storyboard.png
```

## Options

| Flag | Description |
|---|---|
| `--dry-run` | Gemini analysis only — print JSON, skip image generation |
| `--start-frame` | Generate a bookend frame before frame 1 |
| `--end-frame` | Generate a bookend frame after the last scene |

## Pipeline

1. **Gemini 3 Flash** analyzes the storyboard with agentic vision (code execution enabled) — autonomously crops/zooms frames via Python
2. Returns structured JSON: grid layout, frame classifications (scene vs endcard), cinematic prompts optimized for Nano Banana Pro
3. **fal CLI** generates 4K 16:9 images for each scene frame (endcards are skipped)
4. If bookend flags set, generates before/after frames using gemini-edit with the scene images as reference

## After Generation

Images are saved to `~/Downloads/fal/images/`. After the script finishes:

1. Read the output to find saved file paths
2. Use the Read tool to display the generated image(s) to the user
3. Report the frame-to-path mapping
4. Note which frames were skipped (endcards)
5. Report bookend frame paths separately if generated

## Important

- Requires `GEMINI_API_KEY` in `~/Cursor/storyboard-to-video/.dev.vars`
- Requires the fal CLI skill to be installed at `~/.claude/skills/fal/scripts/run-fal.sh`
- Gemini handles all image cropping/zooming autonomously via code execution — no local image processing needed
- Endcard frames (logos, legal text) are detected and skipped automatically
- Prompts are optimized for Nano Banana Pro (Gemini 3 Pro Image): natural language, editorial photography style, no tag spam
