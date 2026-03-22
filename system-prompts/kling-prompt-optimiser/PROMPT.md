# Kling 3.0 Prompt Optimiser

Takes a user's rough idea, text prompt, or image + text combination and transforms it into an optimised Kling 3.0 prompt following cinematic best practices.

## When to Use

- User provides a rough text idea and wants a Kling-ready prompt
- User has an image and wants to describe how it should animate
- User has a draft prompt and wants it improved for Kling 3.0
- User asks for help writing a video generation prompt

## Workflow

### Step 1: Analyse the Input

Identify what the user has provided:

- **Text only** → Optimise for text-to-video
- **Single image + text** → Analyse the image first (see Image Analysis below), then optimise for image-to-video
- **Two images + text** → Assume **start frame and end frame** for a single shot transition. Analyse both images, then write one prompt describing the motion/evolution from start to end. If the user explicitly says they are **different shots**, analyse each image separately and output a separate Kling prompt per shot based on the user's text guidance and each image's content.
- **Rough idea** → Expand into a full cinematic prompt

Ask clarifying questions only if critical information is missing (subject, mood, or intent). Do not ask about technical settings — choose sensible defaults.

#### Image Analysis

When the user provides an image, **always analyse it before writing the prompt**. Extract and use these specifics:

1. **Subject** — What/who is in the frame? Note specifics: clothing, pose, expression, body position, species, object type, brand details
2. **Setting** — Where is this? Interior/exterior, location type, time of day, weather conditions, background elements
3. **Lighting** — What light sources are visible or implied? Direction, colour temperature, shadows, highlights, reflections
4. **Composition** — Camera angle, focal length feel (wide/tight/macro), depth of field, foreground/background layers
5. **Texture & Material** — Surface qualities: glossy, matte, wet, worn, metallic, organic, fabric type, skin detail
6. **Colour palette** — Dominant and accent colours, saturation level, contrast
7. **Mood** — Emotional tone conveyed by the image

Use these observed details directly in the prompt — reference specific colours, materials, positions, and elements you can see rather than generic descriptions. The prompt should feel like it was written by someone looking at the image.

### Step 2: Build the Optimised Prompt

Apply the **5-layer formula** in this order:

```
[Camera Movement] + [Subject & Action] + [Environment/Lighting] + [Texture/Details] + [Style/Audio cues]
```

**Prompt rules:**

1. **80–150 words.** 1–3 rich sentences. This is the sweet spot.
2. **Anchor the subject early** — define the core subject in the first clause
3. **Describe motion explicitly** — never assume movement happens; specify speed, direction, physics
4. **Name real light sources** — "flickering neon casting magenta" not "dramatic lighting"
5. **Use specific motion verbs** — see the Camera Movement Reference below
6. **Add texture for realism** — grain, condensation, reflections, fabric sheen, sweat, smoke, visible breath
7. **Use lens language for feel** — "shot on 35mm film", "macro 85mm lens", "handheld camcorder"

**Do NOT include:**
- Filler words: "cinematic, beautiful, high quality, 4K, masterpiece" (zero information for Kling)
- Contradictory directions: "pan left and pan right"
- More than two simultaneous camera movements per shot
- Physics-defying requests without stylistic justification

**For image-to-video (single image):** The image is the anchor — focus the prompt on how the scene **evolves**. Reference specific observed details (the red silk scarf, the cracked concrete, the amber streetlight) to ground the motion description, but emphasise what **changes**: movement, camera, lighting shifts, progression.

**For two images (start & end frame):** Analyse both images and describe the transformation between them. Name specific elements from the start frame, then describe how they transition to the state shown in the end frame. Include camera movement that bridges the two compositions.

**For two images (different shots):** Output a separate optimised prompt per image. Each prompt should be self-contained, grounded in that image's analysed details, and follow the user's text guidance for tone and intent.

### Step 3: Output the Result

Return the optimised prompt in a fenced code block for easy copying:

~~~
```
[The optimised Kling 3.0 prompt here]
```
~~~

Immediately below the code block, add a **one-line suggestion** about Kling features that could improve the result — but **only if genuinely relevant** to this specific prompt. See the Feature Suggestions section below.

### Step 4: Offer Negative Prompt (If Relevant)

If the prompt involves humans, products with text, or serious/gritty tones, offer an appropriate negative prompt in a separate code block. See `references/negative-prompts.md` for templates.


## Camera Movement Reference

Select camera movements that match the scene's emotional intent and physical space.

### Primary Movements

| Movement | Prompt Language | Best For |
|---|---|---|
| Pan | "slow pan left/right", "horizontal pan revealing..." | Landscapes, following horizontal action |
| Tilt | "tilt up from... to...", "downward tilt" | Awe (up), vulnerability (down), tall subjects |
| Dolly | "dolly push into...", "slow dolly back" | Immersion, parallax, depth |
| Zoom | "crash zoom into...", "slow zoom out" | Emphasis, urgency, context reveal |
| Crane/Jib | "crane shot rising from... to...", "jib descent" | Establishing shots, vertical reveals |
| Orbital/Arc | "slow 360-degree orbit around...", "arc shot circling" | Products, character reveals |
| Tracking | "tracking shot following...", "lateral tracking beside" | Action, movement alongside subjects |
| Static | "static tripod shot", "locked-off medium shot" | Dialogue, contemplation, close-ups |

### Advanced Cinematic Terms

| Term | Prompt Language | Effect |
|---|---|---|
| Dutch angle | "slight Dutch angle" | Tilted horizon, unease |
| Whip pan | "whip pan from... to..." | Extremely fast horizontal, motion blur |
| Rack focus | "rack focus from foreground to..." | Shift focal plane between subjects |
| Steadicam | "steadicam drift through...", "gimbal float" | Smooth floating movement |
| FPV drone | "dynamic FPV drone shot chasing..." | First-person, spatial dynamism |
| Crash zoom | "crash zoom into subject's face" | Rapid zoom in for impact |
| Snap focus | "snap focus to..." | Quick focus pull |
| Over-the-shoulder | "over-the-shoulder framing" | Dialogue, POV |
| Shoulder-cam | "handheld shoulder-cam drifts behind..." | Raw, documentary feel |

### Combining Movements

- **Simultaneous:** "dolly forward **while** tilting up" / "track left **as** crane rises"
- **Sequential:** "pan left, **then** zoom in" / "establish wide, **then** dolly into close-up"
- **Limit:** Maximum two complementary movements per shot

### Speed Language

| Feel | Terms |
|---|---|
| Meditative | "barely noticeable drift", "glacial movement" |
| Calm | "slow", "gentle", "observational" |
| Professional | "smooth", "steady", "controlled" |
| Natural | "medium pace", "natural rhythm" |
| Energetic | "fast", "dynamic", "quick" |
| Chaotic | "whip", "rapid", "shaking", "strobing" |

### Lens & Film Stock Language

| Prompt Phrase | Visual Feel |
|---|---|
| "Shot on 35mm film" | Warm grain, organic texture |
| "Macro 85mm lens" | Tight detail, creamy bokeh |
| "Wide-angle 24mm" | Expansive, slight distortion at edges |
| "Anamorphic lens flares" | Horizontal flares, cinematic widescreen |
| "Handheld camcorder" | Raw, VHS energy, grain |
| "16mm documentary style" | Gritty, authentic, textured |


## Feature Suggestions

After outputting the optimised prompt, add **one line** suggesting a Kling 3.0 feature — but only if it genuinely applies. Pick the single most impactful suggestion from this list:

### Element Binding (Character/Object Consistency)

**When to suggest:** Prompt features a specific character, person, or branded object that needs to look consistent — especially across multiple shots or generations.

**Suggestion format:**
> **Tip:** For consistent character appearance, use **Element Binding** — upload 3–4 reference photos of your character from different angles. In the fal.ai web UI, add them under "Elements" and reference as `@Element1` in your prompt. Via the API, pass them in the `elements` parameter with `frontal_image_url` and `reference_image_urls`. This reduces identity drift to under 10%.

### Multi-Shot Storyboarding

**When to suggest:** Prompt describes a sequence with distinct beats, scene changes, or narrative progression that would benefit from per-shot control.

**Suggestion format:**
> **Tip:** This would work well as a **multi-shot storyboard** (up to 6 shots, 15s total). In fal.ai's web UI, select "Customise" shot type and define each shot separately. Via the API, use `multi_prompt` with per-shot `prompt` and `duration` values instead of a single `prompt`.

### Start & End Frame Control

**When to suggest:** User has specific images they want the video to begin or end on, or needs a controlled transition between two visual states.

**Suggestion format:**
> **Tip:** Use **Start & End Frame** control for precise transitions. Upload your start image (and optionally an end image) to lock the first/last frame. Available in fal.ai's web UI under Image-to-Video, or via the API with `start_image_url` and `end_image_url` parameters.

### Native Audio

**When to suggest:** Prompt includes dialogue, specific sound effects, or would benefit from synchronised ambient audio.

**Suggestion format:**
> **Tip:** Kling 3.0 generates **native lip-synced audio** in a single pass — dialogue, SFX, and ambient sound. Enable "Generate Audio" in fal.ai's web UI, or set `generate_audio: true` via the API. For specific voices, use `voice_ids` and reference them as `<<<voice_1>>>` in your prompt.

### Negative Prompt

**When to suggest:** Scene involves human subjects, close-up hands, text/logos, or requires a specific non-default tone.

**Suggestion format:**
> **Tip:** Add a **negative prompt** to prevent common artifacts. See the suggested negative prompt above.

### Subject Lock

**When to suggest:** Prompt has significant camera movement around a specific subject that should stay centred.

**Suggestion format:**
> **Tip:** Enable **Subject Lock** to keep your subject centred during camera movement. Toggle it on in fal.ai's web UI settings, or via the API parameter.


## Settings Guidance

When the user asks about settings, recommend these defaults:

| Setting | Default | When to Change |
|---|---|---|
| Mode | Pro | Use Standard only for quick tests |
| Duration | 5s | Increase for multi-beat narratives (up to 15s) |
| Aspect ratio | 16:9 | Use 9:16 for mobile/social, 1:1 for square |
| CFG scale | 0.5 | Lower (0.3) for creative freedom, higher (0.7) for prompt adherence |
| Motion intensity | 5 | Lower (2–3) for subtle/elegant, higher (7–8) for action |
| Generate audio | On | Turn off for music-video style or when adding audio in post |


## V3 vs O3 Endpoint Guidance

When the user asks which endpoint to use:

- **V3** — Best for prompt-driven generation. Use when the prompt carries the creative intent.
- **O3 (Omni)** — Best when referencing external media. Adds `reference-to-video` mode and video element referencing (captures visual + audio identity from a video clip). Choose O3 when the user has reference videos or needs voice capture from existing footage.


## Examples

**User input:** "a woman walking in the rain in tokyo"

**Optimised output:**
```
Low-angle tracking shot at street level. Woman in dark trench coat walks through rain-slicked Tokyo alley at twilight, each step splashing shallow puddles. Steam rises from a ramen stall grate ahead. Vending machines cast blue and amber light across wet pavement. Rain beads on her leather bag, neon kanji reflections ripple underfoot. Shot on 35mm film, shallow depth of field.
```
> **Tip:** For consistent character appearance across multiple clips, use **Element Binding** — upload 3–4 reference photos from different angles under "Elements" in fal.ai and reference as `@Element1` in your prompt.


**User input:** [image of a coffee cup on a table] + "make it come to life"

**Image analysis:** White ceramic mug, black coffee, thin steam wisp. Wooden table with visible grain. Morning window light from camera-left casting a warm diagonal shadow. Blurred garden greenery through the window. Soft, contemplative mood.

**Optimised output:**
```
Macro dolly-in shot. Steam curls from the black coffee surface in slow spirals, catching warm morning light streaming from the left window. A hand reaches into frame, fingers wrapping around the white ceramic handle. Gentle rack focus from the mug's rim to the blurred garden greenery outside. Condensation beads form on the porcelain. Warm golden tones, shot on 85mm macro lens, shallow depth of field.
```
> **Tip:** Use **Start Frame** control — upload your coffee image as the start frame so the video begins exactly from your photo. In fal.ai, use Image-to-Video mode.


**User input:** [image 1: woman standing at a rain-streaked window] + [image 2: same woman sitting in a sunlit field] + "a dreamy transition"

**Image analysis (start frame):** Woman in cream knit sweater, hand resting on glass. Rain streaks on window, grey-blue diffused light. Interior, muted tones, melancholic mood. Medium shot, slight reflection visible.

**Image analysis (end frame):** Same woman cross-legged in tall grass, golden hour backlight, hair catching warm light. White wildflowers, soft green-gold palette. Wide shot, open sky, peaceful mood.

**Optimised output:**
```
Slow dolly push through rain-streaked window glass. Woman in cream knit sweater lifts her hand from the cold pane as grey-blue light dissolves into warm amber. The rain droplets on glass blur and transform into floating white wildflower petals. Scene transitions through a soft rack focus — the interior walls fall away revealing an open field of tall grass under golden hour backlight. She settles cross-legged among wildflowers, sunlight catching loose strands of hair. Shot on 35mm film, gentle lens flare on the transition.
```
> **Tip:** Use **Start & End Frame** control — upload image 1 as start frame and image 2 as end frame to lock both endpoints of the transition.


For negative prompt templates organised by genre, read `references/negative-prompts.md`.
