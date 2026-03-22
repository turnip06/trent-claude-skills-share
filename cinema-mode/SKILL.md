---
name: cinema-mode
description: Rewrite any image prompt or scene description into a cinematic film still prompt for Nano Banana Pro. Use when the user asks for a cinematic prompt, cinematic still, film still, movie still, cinema mode, or wants to make a prompt look like a real film frame. Also triggers when the user says "cinema mode", "make it cinematic", "film look", "movie frame", or asks for a photorealistic cinematic rewrite of an existing prompt.
---

# Cinema Mode

Take the user's prompt or scene description and rewrite it as a cinematic film still prompt for Nano Banana Pro. Direct the shot like a cinematographer. Pick the camera package, translate vague intent into physical film language, output a structured prompt.

---

## Non-Negotiables

1. **No empty adjectives.** Never use hyperrealistic, cinematic masterpiece, ultra detailed, photoreal 8k. They push NBP towards glossy digital art.
2. **Every prompt describes a physical shot.** Real scene, real subject, real framing, real lighting, real camera package.
3. **One camera, one lens.** Do not stack cameras or lenses.
4. **Anti-digital texture is mandatory.** Gentle optical diffusion, slight grain, subtle halation, soft highlight rolloff, natural skin texture, minimal sharpening, no digital harshness.
5. **Human imperfection is mandatory.** Pores, fine lines, blemishes, peach fuzz, flyaway hairs, lived-in fabric, dust, condensation where appropriate.
6. **Stills archive is optional flavour, not foundation.** See rules below.

---

## Output Format

Single line prompt, all prompts enclosed in a single code block. This exact field order:

```
SUBJECT: ... | ACTION: ... | SETTING: ... | COMPOSITION: ... | CAMERA: ... | LENS: ... | EXPOSURE: ... | LIGHTING: ... | COLOUR_GRADE: ... | TEXTURE: ... | ATMOSPHERE: ... | REALISM_CONSTRAINTS: ... | STYLE_ANCHOR: ...
```

No commentary. No explanation.

### Field Rules

**SUBJECT** — Who or what is in frame. Age range, visual identity, clothing, materials, distinguishing traits.

**ACTION** — What is happening right now. Visual and specific. "Fidgeting with a cigarette" not "standing around".

**SETTING** — Physical environment. Surfaces, props, weather, architecture, period cues.

**COMPOSITION** — Call the shot. Medium close up, wide environmental portrait, low angle medium shot. Include framing position, negative space, eye line.

**CAMERA** — One locked camera body from the package library.

**LENS** — One locked lens and focal length with aperture or T-stop.

**EXPOSURE** — Optical behaviour: depth of field, focus falloff, underexposure, handheld feeling.

**LIGHTING** — Source, direction, softness, contrast, time of day. Motivated light beats vague mood language.

**COLOUR_GRADE** — Film stock or grading language. "Muted teal shadows, warm Kodak skin tones" not "cinematic colours".

**TEXTURE** — Always include `gentle optical diffusion`. Then add tactile reality: pores, fabric weave, dust in light, halation, grain, bloom, wood grain, scratched metal, damp asphalt.

**ATMOSPHERE** — Only what helps. Mist, cigarette smoke, sea haze, rain particles, low fog, subtle steam.

**REALISM_CONSTRAINTS** — Mandatory. Default: `single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture`

**STYLE_ANCHOR** — One or two tokens max, or none. Allowed: `stills archive` | `stills archive, warner bros .com` | `documentary grade realism` | `photojournalistic realism` | `1980s colour film, slightly grainy`

---

## Camera Packages

Pick the package based on the scene. Do not ask the user unless they explicitly want to choose.

### A — Grounded Narrative (default)

Use for: drama, realistic ads, editorial portraits, relationship moments, intimate interiors, most human storytelling.
Camera: ARRI Alexa 35
Lenses: Cooke S4/i 40mm T2.0 (medium/environmental) or Cooke S4/i 75mm T2.0 (close portrait)
Tokens: famous Cooke Look, silky warm skin tones, organic and poetic rendering, subtle halation in highlights

### B — Premium Beauty / Intimate Close Portrait

Use for: beauty campaigns, skincare, luxury close-ups, intimate faces, polished portraiture that still feels photographic.
Camera: Leica SL2
Lenses: APO Summicron 90mm f/2 (extreme facial detail) or Leica Summilux C 50mm T1.4 (creamy beauty)
Tokens: high micro contrast, creamy skin rendering, no digital harshness, subtle highlight rolloff, natural skin texture with pores, fine lines, tiny blemishes, peach fuzz, realistic hydration shine
Hard rule: must include `minimal sharpening` and `no beautification` unless user explicitly wants retouched gloss.

### C — Classic Anamorphic Cinema

Use for: noir, smoky interiors, jazz club mood, moody fashion, prestige drama, widescreen energy.
Camera: Panavision Panaflex
Lens: Panavision C Series 40mm T2.3
Tokens: classic Hollywood anamorphic, heavy edge fall off, centre focus weight, organic film-like character
Hard rule: keep restrained. Overdone flares look like AI cosplay.

### D — Warm Nostalgic Lifestyle

Use for: golden hour, family scenes, countryside, memory feeling, summer warmth, backlit lifestyle.
Camera: Sony Venice
Lens: Canon K 35 85mm T1.4
Tokens: glowing highlights, warm vintage flares, soft skin rendering, 1970s film aesthetic, backlit halo
Hard rule: works with backlight, sun haze, warm colour. Fails in cold interiors.

### E — Raw Documentary / Street

Use for: reportage, street, travel, historical feeling, youth culture, raw interiors, anything observed not staged.
Camera: ARRIFLEX 16SR
Lens: Leitz M 0.8 35mm f/1.4
Tokens: classic 16mm film, documentary grade realism, photojournalistic realism, legendary Leica 3D pop, vintage street photography soul, slightly grainy
Hard rule: natural or practical lighting only. Dies with glossy studio light.

### F — Neon Night Exterior

Use for: wet city streets, cyberpunk-adjacent realism, nightlife, rain-soaked pavements, nocturnal wides.
Camera: ARRI Alexa 35
Lens: JDC Xtal Xpress 50mm T2.3
Tokens: dreamy cinematic widescreen look, heavy horizontal blue flares, rain-slicked street reflections, restrained contrast
Hard rule: needs grounded detail (wet asphalt, sodium spill, mist, smoke, glass reflections). Without it, becomes fake.

### G — Tactile Macro

Use for: products, insects, food details, beauty macro, watch parts, liquids, textures, material studies.
Camera: Panavision Millennium DXL2
Lens: Laowa Macro 50mm
Tokens: extreme macro, tactile surface detail, shallow macro depth, realistic material texture, controlled falloff
Hard rule: obsess over surfaces. Condensation, scratches, powder, fibres, droplets.

---

## Package Selection

1. Grounded human portrait or narrative → A
2. Face-led, beauty-led, luxury close detail → B
3. Prestige cinema, noir, smoky glamour, anamorphic → C
4. Nostalgic, sun-drenched, sentimental, memory → D
5. Observed, messy, documentary, youthful, archival → E
6. Urban night, wet, neon, sci-fi adjacent but photoreal → F
7. Extreme close detail or material study → G

---

## Anti-Digital Stack

Unless user explicitly asks for a cleaner commercial look:

- **Prefer** character lenses (Cooke, Panavision, Leica, Canon K 35, Leitz M, Laowa) over clinically sharp modern optics.
- **Always add** (where appropriate): gentle optical diffusion, subtle halation, slight grain, no sharpening, soft film sill low res feel, restrained contrast, soft highlight rolloff, natural shadow gradients, no digital harshness.
- **Prefer** warm/neutral/restrained grades over heavy teal-orange.
- **Prefer** practical light, overcast, window light, sodium vapour, tungsten practicals, golden hour backlight over generic "cinematic lighting".
- **Strip** if present in user input: hyperrealistic, ultra sharp, HDR, crisp 8k, Unreal Engine, Octane render, ray traced, trending on ArtStation, perfect skin, flawless face, studio beauty retouch, glossy CGI, masterpiece, award winning, insane detail.

---

## Workflow

Every time:

1. Read user input. Identify dominant scene type.
2. Pick camera package before writing anything.
3. Translate vague adjectives into physical film language. "Moody" = low-key tungsten practicals and smoke. "Cinematic" = wide anamorphic framing and motivated backlight. "Realistic" = natural proportions, pores, texture, restrained grade.
4. Fill every field in order.
5. Add anti-digital realism constraints.
6. Compress into one line.
7. Wrap all prompts in a code block, separated by line breaks.

If the user gives a vague prompt, do not echo the vagueness. Infer the missing film grammar: expand subject details, setting specifics, composition, lighting source, camera package, and texture.

If the user gives a bloated prompt full of junk tokens, strip them out and replace with actual cinematography.

---

## Examples

### Grounded Drama

User: "A tired chef standing outside the back door of a restaurant at night"

```
SUBJECT: a tired chef in his late thirties wearing a stained white jacket, apron half untied, slight under-eye shadows, damp hair, nicotine-stained fingers | ACTION: standing just outside the restaurant back door, exhaling slowly, one hand on the metal door handle, looking past camera | SETTING: narrow service alley, wet concrete, dented bins, stainless steel prep table visible inside, faint steam from kitchen, scattered cigarette butts, sodium streetlight spill | COMPOSITION: medium close up, eye level, slightly off centre, shallow depth of field, background falling softly out of focus, negative space on the right | CAMERA: ARRI Alexa 35 | LENS: Cooke S4/i 75mm T2.0 | EXPOSURE: shallow depth of field, gentle falloff into shadow, natural compression | LIGHTING: motivated sodium vapour from above and behind, soft warm spill from kitchen practicals through doorway, low key contrast, subtle highlight rolloff on skin | COLOUR_GRADE: restrained cinematic grade, warm skin tones, slightly dirty shadows, subtle filmic contrast | TEXTURE: gentle optical diffusion, natural skin texture with pores, fine lines, slight sweat sheen, fabric creases, grease marks, damp concrete, light grain, minimal sharpening, subtle halation | ATMOSPHERE: faint steam, alley humidity, late-night service fatigue, quiet urban grit | REALISM_CONSTRAINTS: single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture | STYLE_ANCHOR: documentary grade realism
```

### Documentary Street

User: "Teenagers outside a convenience store in the rain"

```
SUBJECT: three teenagers in oversized hoodies and school trousers, one with a half-zipped rain jacket, one with chipped nail polish, one carrying a plastic bag of snacks, damp hair and tired posture | ACTION: loitering under the awning, laughing between cigarettes, one glancing toward camera as if caught accidentally | SETTING: suburban convenience store frontage at night, fluorescent interior spilling onto wet pavement, lottery posters in the window, puddles, bike chained to a pole, passing headlights | COMPOSITION: medium wide documentary frame, slightly handheld feeling, off-centre group, wide environmental context | CAMERA: ARRIFLEX 16SR | LENS: Leitz M 0.8 35mm f/1.4 | EXPOSURE: slightly underexposed with practical light rolloff, natural depth | LIGHTING: fluorescent shop spill mixed with cool street rain ambience, practical top light from awning, natural shadow gradients, no stylised key light | COLOUR_GRADE: documentary grade realism, cool wet night palette, restrained saturation, slightly grainy | TEXTURE: gentle optical diffusion, wet fabric, pores, flyaway hairs stuck to skin, damp asphalt, sticker residue on window, light grain, minimal sharpening, vintage street photography soul | ATMOSPHERE: candid, rain-soaked, youthful, observational | REALISM_CONSTRAINTS: single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture, not a contact sheet | STYLE_ANCHOR: stills archive
```

### Nostalgic Lifestyle

User: "A father carrying his daughter through a field at sunset"

```
SUBJECT: a father in his mid-thirties carrying his young daughter on one arm, worn denim jacket, sun-faded cotton dress on the child, loose hair blowing | ACTION: walking through tall dry grass while the child laughs and leans back into the light, both mid-stride | SETTING: open rural field, warm summer grass, distant tree line, low sun near horizon, dust catching in the air | COMPOSITION: medium wide, side angle, subjects moving left to right, horizon low, generous negative space | CAMERA: Sony Venice | LENS: Canon K 35 85mm T1.4 | EXPOSURE: gentle compression, backlit halo, soft focus falloff, slight flare from sun angle | LIGHTING: golden hour backlight, warm edge light on hair and shoulders, soft ambient fill, low contrast memory feeling | COLOUR_GRADE: warm nostalgic grade, 1970s film aesthetic, slightly faded warmth, subtle grain | TEXTURE: gentle optical diffusion, glowing highlights, warm vintage flares, fabric movement, believable skin texture, dust in light, minimal sharpening | ATMOSPHERE: memory-coded, tender, sun-drenched, lived-in | REALISM_CONSTRAINTS: single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture | STYLE_ANCHOR: 1980s colour film, grainy
```

### Tactile Macro

User: "Macro shot of a perfume bottle with condensation"

```
SUBJECT: extreme macro study of a luxury perfume bottle, frosted glass body, serif label, fine scratches on the cap, tiny beads of condensation | ACTION: static product still, droplets collecting and streaking down the glass | SETTING: dark reflective surface, soft blurred background, condensation pooling around base | COMPOSITION: tight macro close up, angled three-quarter view, label partially visible, shallow macro depth of field | CAMERA: Panavision Millennium DXL2 | LENS: Laowa Macro 50mm | EXPOSURE: extreme macro depth falloff, precise focal plane across label and front droplets, rich shadow detail | LIGHTING: controlled soft side light with narrow rim from behind, subtle specular control on glass, gentle diffusion | COLOUR_GRADE: restrained luxury grade, neutral blacks, elegant muted highlights, filmic contrast | TEXTURE: gentle optical diffusion, tactile glass texture, condensation droplets, micro scratches, fingerprint smudges, slight grain, minimal sharpening, realistic material behaviour | ATMOSPHERE: expensive, tactile, quiet, product fetish without CGI gloss | REALISM_CONSTRAINTS: single photographic frame, realistic optics, natural proportions, no beautification, no plastic skin, no CGI sheen, no over sharpening, no HDR glow, no game engine look, no synthetic symmetry, no waxy texture
```
