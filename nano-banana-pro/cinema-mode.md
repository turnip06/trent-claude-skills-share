# Cinema Mode

Cinematic film still pipeline for Nano Banana Pro. Use this when the user wants photorealistic or cinematic stills that feel like real frames from a film archive, not glossy AI renders.

The job is to direct the shot like a cinematographer. Pick the camera package, translate vague intent into physical film language, and output a structured prompt.

## Table of Contents

- [Non-Negotiables](#non-negotiables)
- [Output Format](#output-format)
  - [Field Rules](#field-rules)
- [Camera Package Library](#camera-package-library)
  - [Package A — Grounded Narrative](#package-a--grounded-narrative)
  - [Package B — Premium Beauty / Intimate Close Portrait](#package-b--premium-beauty--intimate-close-portrait)
  - [Package C — Classic Anamorphic Cinema](#package-c--classic-anamorphic-cinema)
  - [Package D — Warm Nostalgic Lifestyle](#package-d--warm-nostalgic-lifestyle)
  - [Package E — Raw Documentary / Street](#package-e--raw-documentary--street)
  - [Package F — Neon Night Exterior](#package-f--neon-night-exterior)
  - [Package G — Tactile Macro](#package-g--tactile-macro)
- [Package Selection Logic](#package-selection-logic)
- [Anti-Digital Stack](#anti-digital-stack)
- [Stills Archive Rules](#stills-archive-rules)
- [Creative Camera Techniques](#creative-camera-techniques)
- [Prompt Construction Workflow](#prompt-construction-workflow)
- [Handling Vague Prompts](#handling-vague-prompts)
- [Handling Overcooked Prompts](#handling-overcooked-prompts)

---

## Non-Negotiables

1. **No empty adjectives.** Never lead with hyperrealistic, cinematic masterpiece, ultra detailed, photoreal 8k. They push NBP towards glossy digital art.
2. **Every prompt describes a physical shot.** Real scene, real subject, real framing, real lighting, real camera package.
3. **One camera, one lens.** Do not stack cameras or lenses. That is prompt pollution.
4. **Anti-digital texture is mandatory.** Include filmic texture language: slight grain, subtle halation, soft highlight rolloff, natural skin texture, minimal sharpening, no digital harshness.
5. **Human imperfection is mandatory.** Pores, fine lines, blemishes, peach fuzz, flyaway hairs, lived-in fabric, dust, condensation, atmospheric haze where appropriate.
6. **Stills archive is optional flavour, not foundation.** See stills archive rules below.

---

## Output Format

Single line prompt in a code block using this exact field order:

```
SUBJECT: ... | ACTION: ... | SETTING: ... | COMPOSITION: ... | CAMERA: ... | LENS: ... | EXPOSURE: ... | LIGHTING: ... | COLOUR_GRADE: ... | TEXTURE: ... | ATMOSPHERE: ... | REALISM_CONSTRAINTS: ... | OPTIONAL_META: ...
```

### Field Rules

**SUBJECT** — Who or what is in frame. Age range, visual identity, clothing, materials, distinguishing traits.

**ACTION** — What is happening right now. Keep it visual and specific. "Fidgeting with a cigarette" not "standing around".

**SETTING** — Physical environment with surfaces, props, weather, architecture, period cues.

**COMPOSITION** — Call the shot. Medium close up, wide environmental portrait, low angle medium shot, tight profile. Include framing position, negative space, eye line.

**CAMERA** — One locked camera body from the package library.

**LENS** — One locked lens and focal length with aperture or T-stop.

**EXPOSURE** — Optical behaviour: depth of field, focus falloff, underexposure, handheld feeling.

**LIGHTING** — Source, direction, softness, contrast, time of day. Motivated light beats vague mood language.

**COLOUR_GRADE** — Film stock or grading language. "Muted teal shadows, warm Kodak skin tones" not "cinematic colours".

**TEXTURE** — Tactile reality. Pores, fabric weave, dust in light, halation, grain, bloom, wood grain, scratched metal, damp asphalt.

**ATMOSPHERE** — Only what helps. Mist, cigarette smoke, sea haze, rain particles, low fog, subtle steam. Do not flood with effects.

**REALISM_CONSTRAINTS** — Mandatory. Default: `single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture`

**OPTIONAL_META** — One or two tokens maximum, or none. Allowed: `stills archive` | `stills archive, warner bros .com` | `documentary grade realism` | `photojournalistic realism` | `1980s colour film, slightly grainy`

---

## Camera Package Library

Pick the package based on the scene. Do not ask the user unless they explicitly want to choose.

### Package A — Grounded Narrative

**Use for:** Grounded drama, realistic ad scenes, editorial portraits, relationship moments, intimate interiors, most human-centred storytelling.

Camera: ARRI Alexa 35
Lenses: Cooke S4/i 40mm T2.0 (medium/environmental) or Cooke S4/i 75mm T2.0 (close portrait)
Tokens: famous Cooke Look, silky warm skin tones, organic and poetic rendering, subtle halation in highlights

This is the default. Use it unless another package clearly fits better.

### Package B — Premium Beauty / Intimate Close Portrait

**Use for:** Beauty campaigns, premium skincare, luxury close-ups, intimate faces, polished portraiture that still feels photographic.

Camera: Leica SL2
Lenses: APO Summicron 90mm f/2 (extreme facial detail) or Leica Summilux C 50mm T1.4 (creamy beauty close-ups)
Tokens: high micro contrast, extreme micro contrast, creamy skin rendering, no digital harshness, subtle highlight rolloff, natural skin texture with pores, fine lines, tiny blemishes, peach fuzz, realistic hydration shine
Hard rule: Must include `minimal sharpening` and `no beautification` unless the user explicitly wants retouched advertising gloss.

### Package C — Classic Anamorphic Cinema

**Use for:** Noir, smoky interiors, jazz club mood, moody fashion, prestige drama, widescreen film energy.

Camera: Panavision Panaflex
Lens: Panavision C Series 40mm T2.3
Tokens: classic Hollywood anamorphic, heavy edge fall off, centre focus weight, organic film-like character
Hard rule: Keep restrained. Do not overdo flares or it looks like AI cosplay of cinema.

### Package D — Warm Nostalgic Lifestyle

**Use for:** Golden hour, family scenes, countryside, memory feeling, summer warmth, soft backlit lifestyle.

Camera: Sony Venice
Lens: Canon K 35 85mm T1.4
Tokens: glowing highlights, warm vintage flares, soft skin rendering, 1970s film aesthetic, backlit halo
Hard rule: Works best with backlight, sun haze, warm practical colour. Fails in cold interiors.

### Package E — Raw Documentary / Street

**Use for:** Reportage, street scenes, travel, historical feeling, youth culture, raw interiors, anything that should feel observed rather than staged.

Camera: ARRIFLEX 16SR
Lens: Leitz M 0.8 35mm f/1.4
Tokens: classic 16mm film, documentary grade realism, photojournalistic realism, legendary Leica 3D pop, vintage street photography soul, slightly grainy
Hard rule: Keep lighting natural or practical. This package dies when paired with glossy studio lighting.

### Package F — Neon Night Exterior

**Use for:** Wet city streets, cyberpunk-adjacent realism, nightlife, rain-soaked pavements, moody nocturnal wides.

Camera: ARRI Alexa 35
Lens: JDC Xtal Xpress 50mm T2.3
Tokens: dreamy cinematic widescreen look, heavy horizontal blue flares, rain-slicked street reflections, restrained contrast
Hard rule: Needs grounded physical detail: wet asphalt, sodium spill, mist, smoke, glass reflections, dirty light. Without those it becomes fake and gamey.

### Package G — Tactile Macro

**Use for:** Products, insects, food details, beauty macro, watch parts, liquids, textures, material fetish shots.

Camera: Panavision Millennium DXL2
Lens: Laowa Macro 50mm
Tokens: extreme macro, tactile surface detail, shallow macro depth, realistic material texture, controlled falloff
Hard rule: Macro prompts must obsess over surfaces. Condensation, scratches, powder, skin texture, fibres, tiny droplets.

---

## Package Selection Logic

1. Grounded human portrait or narrative frame → Package A
2. Face-led, beauty-led, or luxury close detail → Package B
3. Prestige cinema, noir, smoky glamour, anamorphic drama → Package C
4. Nostalgic, sun-drenched, sentimental, memory-coded → Package D
5. Observed, messy, documentary, youthful, archival → Package E
6. Urban night, wet, neon, sci-fi adjacent but photoreal → Package F
7. Extreme close detail or material study → Package G

---

## Anti-Digital Stack

Unless the user explicitly asks for a cleaner commercial look, bias towards the least digital stack:

**Prefer** vintage or character lenses (Cooke, Panavision, Leica, Canon K 35, Leitz M, Laowa) over clinically sharp modern digital optics.

**Always add** (where appropriate): subtle halation in highlights, slight grain, minimal sharpening, restrained contrast, soft highlight rolloff, natural shadow gradients, no digital harshness.

**Prefer** warm, neutral, or restrained grades over heavy teal-orange clichés.

**Prefer** practical light, overcast, window light, sodium vapour, tungsten practicals, golden hour backlight over generic "cinematic lighting".

**Avoid** (unless explicitly requested): hyperrealistic, ultra sharp, HDR, crisp 8k, Unreal Engine, Octane render, ray traced, trending on ArtStation, perfect skin, flawless face, studio beauty retouch, glossy CGI.

---

## Stills Archive Rules

1. Use only for production still, press still, behind the scenes, archival movie frame, or studio publicity still aesthetics.
2. Do not use for product photography, macro, food, or clean commercial work.
3. Place at the end in OPTIONAL_META.
4. Keep it to one or two tokens.
5. When using it, add `single photographic frame, not a contact sheet` to REALISM_CONSTRAINTS. NBP can take the archive wording literally and produce a multi-image sheet.

---

## Creative Camera Techniques

Apply to stills, campaign key visuals, editorial, documentary, social content, and storyboard frames. These techniques add depth and visual interest — use your judgement on when they serve the shot.

**Depth layering**: Strong compositions have at least three depth planes. Describe foreground (often soft, obstructing), midground (sharp, where the subject lives), and background (falling into bokeh or haze).

**Foreground obstruction**: Place something between the camera and subject — rain-streaked glass, foliage, a silhouetted shoulder, chain-link fence. Creates depth and intimacy.

**Reflections as composition**: Puddle reflections, shop window overlays, sunglasses, chrome surfaces. Doubles visual information and creates natural layering.

**Deliberate exclusion**: Extreme close-ups cropping half the face, subjects shown only from the waist down, hands only, edge-of-frame placement.

**Colour restraint**: A single red element in an otherwise desaturated frame. Monochromatic scene with only skin tones retaining colour. Restriction beats broad grading.

**The "wrong" focus**: Sharp focus on hands while the face goes soft, background in focus with foreground blurred, rack focus frozen mid-pull.

**In-camera physics**: Describe as physical setups — lens fog from temperature change, water droplets on the lens, prism refractions at frame edges, practical flare from direct sun, dust catching backlight.

---

## Prompt Construction Workflow

Follow this sequence every time:

1. Read the user input and identify the dominant scene type.
2. Pick the camera package before writing anything else.
3. Translate vague adjectives into physical film language. "Moody" becomes low-key tungsten practicals and smoke. "Cinematic" becomes wide anamorphic framing and motivated backlight. "Realistic" becomes natural proportions, pores, texture, restrained grade.
4. Fill every labelled field in order.
5. Add anti-digital realism constraints.
6. Add at most one meta token, or none.
7. Compress into one clean line.
8. Wrap in a code block and stop.

---

## Handling Vague Prompts

If the user gives a weak prompt like "a woman in a cafe looking cinematic", do not echo the vagueness. Infer the missing film grammar.

Internally expand it: subject (age, clothing, props, expression), setting (specific surfaces, architecture, weather), composition (shot size, angle, framing), lighting (source, direction, quality), camera package (based on scene type), texture (tactile detail).

Then output the structured prompt only.

## Handling Overcooked Prompts

If the user gives a bloated AI prompt full of junk tokens, strip them out. Delete: masterpiece, award winning, ultra detailed, highly detailed, 8k, insane detail, trending on artstation, octane render, unreal engine, perfect composition, perfect face, hyperrealistic cinematic. Replace with actual cinematography.

---

## Example: Grounded Dramatic Portrait

User: "A tired chef standing outside the back door of a restaurant at night, cinematic and realistic"

```
SUBJECT: a tired chef in his late thirties wearing a stained white jacket, apron half untied, slight under-eye shadows, damp hair, nicotine-stained fingers | ACTION: standing just outside the restaurant back door, exhaling slowly, one hand on the metal door handle, looking past camera | SETTING: narrow service alley, wet concrete, dented bins, stainless steel prep table visible inside, faint steam from kitchen, scattered cigarette butts, sodium streetlight spill | COMPOSITION: medium close up, eye level, slightly off centre, shallow depth of field, background falling softly out of focus, negative space on the right | CAMERA: ARRI Alexa 35 | LENS: Cooke S4/i 75mm T2.0 | EXPOSURE: shallow depth of field, gentle falloff into shadow, natural compression | LIGHTING: motivated sodium vapour from above and behind, soft warm spill from kitchen practicals through doorway, low key contrast, subtle highlight rolloff on skin | COLOUR_GRADE: restrained cinematic grade, warm skin tones, slightly dirty shadows, subtle filmic contrast | TEXTURE: natural skin texture with pores, fine lines, slight sweat sheen, fabric creases, grease marks, damp concrete, light grain, minimal sharpening, subtle halation | ATMOSPHERE: faint steam, alley humidity, late-night service fatigue, quiet urban grit | REALISM_CONSTRAINTS: single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture | OPTIONAL_META: documentary grade realism
```

## Example: Raw Documentary Street

User: "Teenagers outside a convenience store in the rain, feels candid and real"

```
SUBJECT: three teenagers in oversized hoodies and school trousers, one with a half-zipped rain jacket, one with chipped nail polish, one carrying a plastic bag of snacks, damp hair and tired posture | ACTION: loitering under the awning, laughing between cigarettes, one glancing toward camera as if caught accidentally | SETTING: suburban convenience store frontage at night, fluorescent interior spilling onto wet pavement, lottery posters in the window, puddles, bike chained to a pole, passing headlights | COMPOSITION: medium wide documentary frame, slightly handheld feeling, off-centre group, wide environmental context | CAMERA: ARRIFLEX 16SR | LENS: Leitz M 0.8 35mm f/1.4 | EXPOSURE: slightly underexposed with practical light rolloff, natural depth | LIGHTING: fluorescent shop spill mixed with cool street rain ambience, practical top light from awning, natural shadow gradients, no stylised key light | COLOUR_GRADE: documentary grade realism, cool wet night palette, restrained saturation, slightly grainy | TEXTURE: wet fabric, pores, flyaway hairs stuck to skin, damp asphalt, sticker residue on window, light grain, minimal sharpening, vintage street photography soul | ATMOSPHERE: candid, rain-soaked, youthful, observational | REALISM_CONSTRAINTS: single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture, not a contact sheet | OPTIONAL_META: stills archive
```

## Example: Warm Nostalgic Lifestyle

User: "A father carrying his daughter through a field at sunset, feels like a memory"

```
SUBJECT: a father in his mid-thirties carrying his young daughter on one arm, worn denim jacket, sun-faded cotton dress on the child, loose hair blowing | ACTION: walking through tall dry grass while the child laughs and leans back into the light, both mid-stride | SETTING: open rural field, warm summer grass, distant tree line, low sun near horizon, dust catching in the air | COMPOSITION: medium wide, side angle, subjects moving left to right, horizon low, generous negative space, shallow but not extreme depth | CAMERA: Sony Venice | LENS: Canon K 35 85mm T1.4 | EXPOSURE: gentle compression, backlit halo, soft focus falloff, slight flare from sun angle | LIGHTING: golden hour backlight, warm edge light on hair and shoulders, soft ambient fill, low contrast memory feeling | COLOUR_GRADE: warm nostalgic grade, 1970s film aesthetic, slightly faded warmth, subtle grain | TEXTURE: glowing highlights, warm vintage flares, fabric movement, believable skin texture, dust in light, minimal sharpening | ATMOSPHERE: memory-coded, tender, sun-drenched, lived-in | REALISM_CONSTRAINTS: single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture | OPTIONAL_META: 1980s colour film, slightly grainy
```

## Example: Tactile Macro

User: "Macro shot of a perfume bottle with condensation and scratches, expensive but real"

```
SUBJECT: extreme macro study of a luxury perfume bottle, frosted glass body, serif label, fine scratches on the cap, tiny beads of condensation | ACTION: static product still, droplets slowly collecting and streaking down the glass | SETTING: dark reflective surface, soft blurred background, condensation pooling around base | COMPOSITION: tight macro close up, angled three-quarter view, label partially visible, shallow macro depth of field | CAMERA: Panavision Millennium DXL2 | LENS: Laowa Macro 50mm | EXPOSURE: extreme macro depth falloff, precise focal plane across label and front droplets, rich shadow detail | LIGHTING: controlled soft side light with narrow rim from behind, subtle specular control on glass, gentle diffusion | COLOUR_GRADE: restrained luxury grade, neutral blacks, elegant muted highlights, filmic contrast | TEXTURE: tactile glass texture, condensation droplets, micro scratches, fingerprint smudges, slight grain, minimal sharpening, realistic material behaviour | ATMOSPHERE: expensive, tactile, quiet, product fetish without CGI gloss | REALISM_CONSTRAINTS: single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture | OPTIONAL_META: none
```
