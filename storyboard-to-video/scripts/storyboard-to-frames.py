#!/usr/bin/env python3
"""
Storyboard-to-Frames Pipeline

Analyzes a storyboard grid image using Gemini 3 Flash with agentic vision,
generates optimized cinematic prompts per frame, and produces 4K images via fal CLI.
"""

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import urllib.request

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_ENDPOINT = (
    f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
)
FAL_SCRIPT = os.path.expanduser("~/.claude/skills/fal/scripts/run-fal.sh")
DEV_VARS_PATH = os.path.expanduser("~/Cursor/storyboard-to-video/.dev.vars")
PROMPTS_FILE = "/tmp/claude/storyboard-prompts.txt"

MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".gif": "image/gif",
}

# ---------------------------------------------------------------------------
# Gemini system prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are a storyboard analyst for advertising production. You will receive a storyboard image containing a grid of frames (typically 4 columns x 2 rows, 8-9 frames).

Your task:
1. Use code execution to crop and zoom into each individual frame in the grid to analyze it closely
2. Classify each frame as either "scene" (cinematic content) or "endcard" (logos, legal text, pack shots with text overlays)
3. For each scene frame, write an optimized image generation prompt

## How to Analyze

Write Python code to:
- Determine the grid layout (rows x columns) from the storyboard image
- Crop each frame individually
- Zoom in to examine details, text, composition, and lighting

## Prompt Writing Guidelines (Nano Banana Pro Optimized)

For each scene frame, write a cinematic image generation prompt following these rules:

**Structure** (in this order):
1. Subject — who/what is the main focus
2. Action — what's happening in the scene
3. Setting — where it takes place
4. Composition — camera angle and framing (wide shot, close-up, POV, low angle, etc.)
5. Lighting — specific quality (golden hour, soft diffused, rim light, key light position, etc.)
6. Atmosphere/style — mood, color grading, depth of field, texture

**Do:**
- Write full natural-language sentences, not keyword lists
- Use editorial photography language (lens type, f-stops, bokeh, depth of field)
- Specify material textures and surfaces explicitly
- Describe lighting like instructing a lighting technician (direction, quality, color temperature)
- Include emotional tone and mood
- Add context like "for a TV commercial" to imply production quality
- Describe the scene as a standalone image (the prompt must work without seeing the storyboard)

**Don't:**
- No tag soups like "4k, masterpiece, trending on artstation, ultra realistic"
- No brand names, logos, taglines, or marketing copy
- No text rendering instructions — we are generating clean visual scenes only
- No vague descriptions — be specific ("warm directional key light from camera-left at 45 degrees" not just "dramatic lighting")
- No references to other frames — each prompt must be self-contained

## Endcard Detection

Frames are endcards if they contain:
- Brand logos or wordmarks
- Legal/disclaimer text
- Call-to-action text
- URL or website addresses
- Pack shots with prominent text overlays
- Solid color backgrounds with centered text

Set endcard frames to `"type": "endcard"` with `"prompt": null`.

## Output Format

Return ONLY valid JSON (no markdown fences, no extra text) with this exact schema:

{
  "grid": { "rows": <int>, "cols": <int> },
  "title": "<storyboard title if visible, else null>",
  "frames": [
    {
      "number": <int, 1-indexed>,
      "type": "scene" | "endcard",
      "description_text": "<any text visible below/beside the frame>",
      "prompt": "<cinematic generation prompt for scene frames, null for endcards>",
      "scene_summary": "<one-sentence summary of the frame content>"
    }
  ]
}"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def load_api_key():
    """Load GEMINI_API_KEY from .dev.vars file."""
    if not os.path.exists(DEV_VARS_PATH):
        print(f"Error: {DEV_VARS_PATH} not found", file=sys.stderr)
        sys.exit(1)

    with open(DEV_VARS_PATH) as f:
        for line in f:
            line = line.strip()
            if line.startswith("GEMINI_API_KEY="):
                return line.split("=", 1)[1]

    print("Error: GEMINI_API_KEY not found in .dev.vars", file=sys.stderr)
    sys.exit(1)


def load_image(path):
    """Load image file, return (base64_data, mime_type)."""
    if not os.path.exists(path):
        print(f"Error: Image not found: {path}", file=sys.stderr)
        sys.exit(1)

    ext = os.path.splitext(path)[1].lower()
    mime_type = MIME_TYPES.get(ext)
    if not mime_type:
        print(f"Error: Unsupported image format: {ext}", file=sys.stderr)
        sys.exit(1)

    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")

    return data, mime_type


def call_gemini(api_key, image_b64, mime_type):
    """Call Gemini 3 Flash with agentic vision (code execution enabled)."""
    payload = {
        "systemInstruction": {
            "parts": [{"text": SYSTEM_PROMPT}]
        },
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "inlineData": {
                            "mimeType": mime_type,
                            "data": image_b64,
                        }
                    },
                    {
                        "text": "Analyze this storyboard. Crop and zoom into each frame using code execution, then return the structured JSON."
                    },
                ],
            }
        ],
        "tools": [{"codeExecution": {}}],
        "generationConfig": {
            "thinkingConfig": {"thinkingLevel": "high"}
        },
    }

    body = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        GEMINI_ENDPOINT,
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )

    print("Calling Gemini 3 Flash with agentic vision...")
    print("(Gemini will autonomously crop/zoom frames via code execution)")

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else "No response body"
        print(f"Gemini API error {e.code}: {error_body}", file=sys.stderr)
        sys.exit(1)


def parse_response(response):
    """Extract structured JSON from Gemini response, skipping thought/code parts."""
    candidates = response.get("candidates", [])
    if not candidates:
        print("Error: No candidates in Gemini response", file=sys.stderr)
        sys.exit(1)

    parts = candidates[0].get("content", {}).get("parts", [])

    # Collect only text parts that are NOT thoughts, code, or code results
    text_parts = []
    for part in parts:
        if part.get("thought"):
            continue
        if "executableCode" in part:
            continue
        if "codeExecutionResult" in part:
            continue
        if "text" in part:
            text_parts.append(part["text"])

    if not text_parts:
        print("Error: No text parts found in Gemini response", file=sys.stderr)
        print("Response parts types:", [list(p.keys()) for p in parts], file=sys.stderr)
        sys.exit(1)

    # Strategy 1: Combined text
    combined = "".join(text_parts).strip()
    fence_match = re.search(r"```(?:json)?\s*([\s\S]*?)```", combined)
    json_str = fence_match.group(1).strip() if fence_match else combined

    try:
        result = json.loads(json_str)
        if "frames" in result:
            return result
    except json.JSONDecodeError:
        pass

    # Strategy 2: Per-part fallback
    for text in text_parts:
        text = text.strip()
        fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
        candidate_str = fence.group(1).strip() if fence else text

        try:
            result = json.loads(candidate_str)
            if "frames" in result:
                return result
        except json.JSONDecodeError:
            continue

    print("Error: Could not parse JSON from Gemini response", file=sys.stderr)
    print("Raw text parts:", text_parts, file=sys.stderr)
    sys.exit(1)


def generate_scene_images(frames):
    """Generate 4K images for scene frames via fal CLI. Returns list of (frame_number, image_path)."""
    scene_frames = [f for f in frames if f["type"] == "scene" and f.get("prompt")]
    if not scene_frames:
        print("No scene frames to generate.")
        return []

    # Write prompts to temp file
    os.makedirs(os.path.dirname(PROMPTS_FILE), exist_ok=True)
    with open(PROMPTS_FILE, "w") as f:
        for frame in scene_frames:
            f.write(frame["prompt"] + "\n")

    print(f"\nGenerating {len(scene_frames)} scene images via fal CLI...")
    print(f"Prompts written to {PROMPTS_FILE}")

    result = subprocess.run(
        [FAL_SCRIPT, "-a", "16:9", "-r", "4K", PROMPTS_FILE],
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    if result.returncode != 0:
        print(f"Error: fal CLI exited with code {result.returncode}", file=sys.stderr)
        sys.exit(1)

    # Parse output for saved image paths
    image_paths = []
    for line in result.stdout.splitlines():
        # fal CLI prints paths like "Saved: /path/to/image.png" or just the path
        if "Saved:" in line:
            path = line.split("Saved:", 1)[1].strip()
            image_paths.append(path)
        elif line.strip().startswith(os.path.expanduser("~/Downloads/fal/")):
            image_paths.append(line.strip())

    # Map frame numbers to image paths
    results = []
    for i, frame in enumerate(scene_frames):
        if i < len(image_paths):
            results.append((frame["number"], image_paths[i]))
        else:
            results.append((frame["number"], None))

    return results


def generate_bookend(frame_data, image_path, position):
    """Generate a bookend frame using gemini-edit with a scene image as reference."""
    if not image_path or not os.path.exists(image_path):
        print(f"Warning: Cannot generate {position} frame — reference image not available")
        return None

    summary = frame_data.get("scene_summary", "the scene")

    if position == "start":
        prompt = (
            f"Generate what this scene looked like 5 seconds earlier. "
            f"Same environment, same lighting, same cinematic style. "
            f"Show the moments just before — {summary}. "
            f"Maintain identical color grading, lens characteristics, and atmosphere. [image 1]"
        )
    else:
        prompt = (
            f"Generate what this scene looks like 5 seconds later. "
            f"Same environment, same lighting, same cinematic style. "
            f"Show the moments just after — {summary}. "
            f"Maintain identical color grading, lens characteristics, and atmosphere. [image 1]"
        )

    print(f"\nGenerating {position} bookend frame via gemini-edit...")

    result = subprocess.run(
        [FAL_SCRIPT, "-m", "gemini-edit", "-a", "16:9", "-r", "4K", prompt, image_path],
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    if result.returncode != 0:
        print(f"Warning: Bookend generation failed (exit code {result.returncode})", file=sys.stderr)
        return None

    # Parse output for saved image path
    for line in result.stdout.splitlines():
        if "Saved:" in line:
            return line.split("Saved:", 1)[1].strip()
        if line.strip().startswith(os.path.expanduser("~/Downloads/fal/")):
            return line.strip()

    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a storyboard and generate 4K cinematic frames"
    )
    parser.add_argument("image_path", help="Path to the storyboard image")
    parser.add_argument(
        "--start-frame", action="store_true",
        help="Generate a bookend frame before frame 1"
    )
    parser.add_argument(
        "--end-frame", action="store_true",
        help="Generate a bookend frame after the last scene"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Gemini analysis only — print JSON, skip image generation"
    )
    args = parser.parse_args()

    # Step 1: Load image and API key
    image_path = os.path.expanduser(args.image_path)
    image_b64, mime_type = load_image(image_path)
    api_key = load_api_key()

    print(f"Storyboard: {image_path}")
    print(f"Image type: {mime_type}")
    print(f"Image size: {len(image_b64) * 3 // 4 // 1024} KB")

    # Step 2: Call Gemini
    response = call_gemini(api_key, image_b64, mime_type)

    # Step 3: Parse response
    analysis = parse_response(response)

    print(f"\n{'='*60}")
    print(f"Storyboard Analysis")
    print(f"{'='*60}")
    if analysis.get("title"):
        print(f"Title: {analysis['title']}")
    grid = analysis.get("grid", {})
    print(f"Grid: {grid.get('rows', '?')} rows x {grid.get('cols', '?')} cols")
    print(f"Total frames: {len(analysis['frames'])}")

    scene_count = sum(1 for f in analysis["frames"] if f["type"] == "scene")
    endcard_count = sum(1 for f in analysis["frames"] if f["type"] == "endcard")
    print(f"Scene frames: {scene_count}")
    print(f"Endcard frames: {endcard_count} (will be skipped)")

    print(f"\n{'='*60}")
    print("Frame Details")
    print(f"{'='*60}")
    for frame in analysis["frames"]:
        status = "SCENE" if frame["type"] == "scene" else "ENDCARD (skip)"
        print(f"\nFrame {frame['number']}: [{status}]")
        print(f"  Summary: {frame.get('scene_summary', 'N/A')}")
        if frame.get("description_text"):
            print(f"  Text: {frame['description_text']}")
        if frame.get("prompt"):
            print(f"  Prompt: {frame['prompt'][:120]}...")

    if args.dry_run:
        print(f"\n{'='*60}")
        print("DRY RUN — Full JSON output:")
        print(f"{'='*60}")
        print(json.dumps(analysis, indent=2))
        return

    # Step 4: Generate scene images
    scene_results = generate_scene_images(analysis["frames"])

    # Step 5: Generate bookend frames
    start_path = None
    end_path = None

    if args.start_frame and scene_results:
        first_frame_num = scene_results[0][0]
        first_frame_data = next(
            f for f in analysis["frames"] if f["number"] == first_frame_num
        )
        first_image_path = scene_results[0][1]
        start_path = generate_bookend(first_frame_data, first_image_path, "start")

    if args.end_frame and scene_results:
        last_frame_num = scene_results[-1][0]
        last_frame_data = next(
            f for f in analysis["frames"] if f["number"] == last_frame_num
        )
        last_image_path = scene_results[-1][1]
        end_path = generate_bookend(last_frame_data, last_image_path, "end")

    # Step 6: Report results
    print(f"\n{'='*60}")
    print("Results")
    print(f"{'='*60}")

    if start_path:
        print(f"  Start bookend: {start_path}")

    for frame_num, path in scene_results:
        status = path if path else "FAILED"
        print(f"  Frame {frame_num}: {status}")

    if end_path:
        print(f"  End bookend: {end_path}")

    skipped = [f["number"] for f in analysis["frames"] if f["type"] == "endcard"]
    if skipped:
        print(f"\n  Skipped endcard frames: {skipped}")

    failed = [num for num, path in scene_results if not path]
    if failed:
        print(f"\n  Failed frames: {failed}")


if __name__ == "__main__":
    main()
