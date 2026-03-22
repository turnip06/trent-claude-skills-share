---
name: nano-banana-pro
description: Writes production-ready image generation prompts for Nano Banana Pro (Gemini 3 Pro Image). Use when the user mentions "NBP", "Nano Banana Pro", or asks for cinematic stills, photorealistic portraits, product shots, character sheets, edit prompts, campaign prompt suites, or style extraction from reference images. Also triggers when enhancing rough prompt ideas or reverse-engineering prompts from uploaded images.
---

# Nano Banana Pro Prompt Engineer

Transform user requests into production-ready prompts for Nano Banana Pro (Gemini 3 Pro Image).

**For cinematic or photorealistic stills**, read [cinema-mode.md](cinema-mode.md) and follow its pipeline. That file contains camera packages, the structured field format, anti-digital texture rules, and worked examples.

**For everything else** (edit prompts, character sheets, product shots, reference image workflows), use the principles and formulas below.

---

## Core Model Behaviour

NBP is built on Gemini 3 Pro multimodal architecture. It understands intent, physics, and composition through semantic reasoning rather than keyword matching.

- Processes prompts conversationally, not as weighted tokens
- Describing physical causes (light source position, lens choice) outperforms describing effects ("dramatic shadows")
- Natural sentences beat keyword lists
- Spatial composition instructions placed early in the prompt carry more weight
- Supports up to 14 reference images for style and character consistency
- Handles text rendering, reflections, and physical light behaviour well

---

## Prompt Writing Principles

Apply to every prompt regardless of type.

### Describe the cause, not the effect

Weak: "A moody portrait with dramatic shadows"
Strong: "Portrait lit by a single 2000W Fresnel spotlight, 90 degrees camera-right, aimed down at 45 degrees. No fill light. Background is absolute darkness."

### Write sentences, not tag soup

Weak: "woman, red dress, rain, Paris, 4k, realistic, cinematic"
Strong: "A young woman in a flowing red dress stands on a rain-slicked Parisian street at night. She holds a clear umbrella, neon signs reflecting in the puddles at her feet. Shot on an 85mm lens at f/1.8, shallow depth of field, teal shadows and warm highlights."

### Capture the micro-moment

Describe the exact fraction of a second, not a generic pose. "The exact instant espresso hits milk, a barista's wrist mid-twist on the pitcher" beats "A barista making coffee."

### Place spatial composition early

Recommended element order:
1. Camera position and lens choice
2. Subject and action
3. Setting and environment
4. Depth layers (foreground, midground, background)
5. Lighting setup
6. Style, colour grade, film stock
7. Negative constraints

### Use negative constraints

End prompts with explicit exclusions:
- Portraits: "No distorted features, no extra fingers, no plastic skin, no unnatural smoothing"
- Landscapes: "No blur, no watermarks, no power lines"
- Products: "No warped labels, no photographer reflection"

---

## Text-to-Image Prompt Formula

For non-cinematic work (product shots, character sheets, illustrations, graphic design):

```
Subject + Action + Setting + Composition + Style + Technical Details
```

| Element | Purpose | Example |
|---------|---------|---------|
| Subject | Main focus | "a weathered fisherman in his 60s with deep-set wrinkles" |
| Action | What they're doing | "mending a fishing net with calloused hands" |
| Setting | Environment | "on a wooden pier at dawn, mist rising off the harbour" |
| Composition | Framing and angle | "medium close-up, low angle, rule of thirds" |
| Style | Artistic treatment | "documentary photography, desaturated colour palette" |
| Technical | Camera, lens, lighting | "shot on Arri Alexa Mini LF, 50mm Cooke S4, soft key light camera-left" |

For **cinematic or photorealistic stills**, switch to the structured field format in [cinema-mode.md](cinema-mode.md). It produces significantly better results for that use case.

---

## Edit Prompts

```
Action Verb + Specific Element + Desired Change + Preservation Instructions
```

Five essential action verbs: Add, Change, Make, Remove, Replace.

Keep edit prompts concise and direct. The existing image provides context. State what to change, where it is, and what to preserve.

**Example:** "Replace the background with a rain-soaked Tokyo alley at night with neon signs in pink and cyan reflecting off wet pavement. Blur the background into soft bokeh. Match the colour temperature to the subject. Keep the person exactly as they are."

Use spatial language for precision: "bottom-left corner", "behind the main subject", "visible through the window on the right".

Always include preservation instructions: "Keep the person's face exactly as is", "Preserve the lighting and shadows", "Maintain the original composition".

---

## Reference Image Usage

NBP supports up to 14 reference images. Assign clear functions to each:

```
Use the uploaded images as follows:
- [Image 1]: Character reference, maintain this exact face and features
- [Image 2]: Pose reference, place the character in this body position
- [Image 3]: Style reference, apply this colour palette and lighting
- [Image 4]: Environment reference, use this location as the setting
```

For character consistency across multiple generations:
1. Generate a character sheet first (face close-up + full body)
2. Use this sheet as reference for all subsequent generations
3. Include: "Maintain exact facial features, hair style, and body proportions from the reference image"
4. If drift occurs, upload both the problematic output and the original reference, then prompt: "Replace the face with the correct character from the reference sheet"

When the user uploads reference images, use the notation `[image 1-N]` as style and likeness anchors within prompts.

---

## Output Format

- Deliver prompts in a single markdown code block
- Write each prompt as a single continuous line with no line breaks
- When returning multiple prompts, place them all in the same code block separated by one blank line
- No prompt titles, numbering, or labels inside the code block
- Write clean prose blocks, not numbered sections or labelled parts
- Expression and mood language should read as animated and full of attitude, not fierce or angry

---

## Examples: Non-Cinematic Prompts

### Product Shot

User: "A luxury watch on a dark surface, premium feel"

```
A luxury diver's watch with brushed titanium case and dark blue dial rests on a slab of raw black slate. The crown is at the 3 o'clock position, bezel slightly rotated. A single soft light source from above and camera-left creates a clean highlight running along the case edge and a controlled reflection on the dial. Background is absolute black. The slate surface shows natural texture — fine scratches, mineral veins, a few particles of dust. Shot on a medium format digital back at 80mm, f/8, precise focus across the dial face. No warped reflections, no photographer visible, no floating product, no gradient background.
```

### Character Sheet

User: "Character sheet for a cyberpunk hacker girl, consistent across scenes"

```
Character reference sheet showing a woman in her mid-twenties with an undercut hairstyle, dark roots fading to electric violet tips, angular jawline, small scar across the left eyebrow, three silver ear piercings on the right ear, pale skin with visible freckles across the nose. She wears a cropped black tactical vest over a faded grey t-shirt, cargo pants with knee patches, and fingerless gloves. Top row: front-facing headshot, three-quarter profile, side profile. Bottom row: full body front, full body back, full body three-quarter. Neutral pose, arms relaxed at sides. Plain light grey background, even studio lighting from two softboxes at 45 degrees, no dramatic shadows. Clean linework between views. No extra limbs, no inconsistent features between views.
```

---

## Examples: Edit Prompts

### Remove

User: "Get rid of the power lines in this landscape"

```
Remove the power lines and utility poles from the sky. Reconstruct the sky with matching cloud texture and colour gradients where the lines were. Preserve the horizon, mountains, and all foreground elements exactly as they are.
```

### Add

User: "Add rain to this street scene"

```
Add steady rainfall throughout the scene. Include rain streaks visible against dark backgrounds, wet reflections on the road surface and pavement, small puddles forming in uneven ground, and water droplets on the car windshield in the foreground. Darken the overall exposure slightly to match overcast rain conditions. Keep all people, vehicles, and buildings exactly as they are.
```
