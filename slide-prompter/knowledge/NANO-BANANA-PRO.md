# Nano Banana Pro Prompting Reference

Nano Banana Pro (Gemini 3 Pro Image via fal.ai) uses semantic reasoning, not keyword matching. It understands intent, physics, and composition.

## Table of Contents

- [Prompt Architecture](#prompt-architecture)
  - [Text-to-Image Formula](#text-to-image-formula)
  - [Core Principles](#core-principles)
- [Lighting Vocabulary](#lighting-vocabulary)
- [Camera References](#camera-references)
- [Colour Grading Terms](#colour-grading-terms)
- [Film Stocks](#film-stocks)
- [Aspect Ratios](#aspect-ratios)
- [Negative Constraint Templates](#negative-constraint-templates)
- [Example Prompt Styles](#example-prompt-styles)
  - [Cinematic Portrait](#cinematic-portrait)
  - [Product Photography](#product-photography)
  - [Illustration (Non-Photorealistic)](#illustration-non-photorealistic)
- [Key Tips](#key-tips)

## Prompt Architecture

### Text-to-Image Formula

```
Subject + Action + Setting + Composition + Style + Technical Details
```

Adapt or abandon elements based on the style (illustration, abstract, graphic design won't need camera specs).

### Core Principles

1. **Describe the cause, not the effect** - Specify light source positions and types, not "moody lighting". Describe the physical setup that creates the look.

2. **Write sentences, not tags** - "A young woman in a flowing red dress stands on a rain-slicked Parisian street at night" beats "woman, red dress, rain, Paris, 4k, realistic".

3. **Specify camera gear for photorealism** - Camera body, lens, and film stock trigger specific rendering behaviours:
   - "Shot on Arri Alexa" = cinematic colour science, subtle grain
   - "85mm f/1.8" = portrait compression, creamy bokeh
   - "35mm anamorphic" = horizontal flares, oval bokeh
   - "Kodak Portra 400" = natural skin, subtle grain

4. **Include negative constraints** - Define what to exclude to avoid common failures.

5. **Use spatial language** - "bottom-left corner", "behind the main subject", "through the window on the right".

## Lighting Vocabulary

| Term | Use Case |
|------|----------|
| Key light | Main illumination, specify angle and type |
| Fill light | Softens shadows, reduce contrast |
| Rim/Hair light | Backlight for subject separation |
| Rembrandt lighting | Triangle on shadow cheek, dramatic portraits |
| Chiaroscuro | High contrast, moody/artistic |
| High-key | Bright, even, minimal shadows, commercial |
| Low-key | Dark, selective light, dramatic |
| Softbox | Diffused, even, beauty/product |
| Fresnel | Hard, focusable, dramatic spots |

## Camera References

**Cinema**: Arri Alexa Mini LF, Arri Alexa 35, RED V-Raptor, Sony Venice
**Stills**: Phase One IQ4, Hasselblad X2D, Leica M11, Sony A1
**Lenses**: Cooke S4 (warm), Zeiss Master Primes (clinical), Leica Summilux (character), Petzval (swirly bokeh)

## Colour Grading Terms

| Term | Effect |
|------|--------|
| Orange and teal | Complementary, cinematic standard |
| Crushed blacks | Deep shadows, minimal detail |
| Lifted blacks | Faded, matte shadows |
| Desaturated | Muted, documentary feel |
| Bleach bypass | Low saturation, high contrast |
| Split toning | Different hues in shadows/highlights |

## Film Stocks

| Stock | Character |
|-------|-----------|
| Kodak Portra 400 | Natural skin, subtle grain |
| Kodak Ektar 100 | Saturated, fine grain |
| Cinestill 800T | Halation, neon glow |
| Kodak Tri-X | Contrasty black and white |
| Ilford HP5 | Classic black and white |
| Kodak Vision3 500T | Cinematic warmth |

## Aspect Ratios

| Ratio | Use |
|-------|-----|
| 1:1 | Social, profile |
| 16:9 | Cinematic, banners |
| 9:16 | Vertical video, stories |
| 4:3 | Traditional photography |
| 3:2 | Standard photography |
| 4:5 | Instagram portrait |
| 2.39:1 | Anamorphic widescreen |

## Negative Constraint Templates

**Portraits**: No distorted features, no extra fingers, no plastic skin, no unnatural smoothing
**Landscapes**: No blur, no watermarks, no power lines, no chromatic aberration
**Products**: No warped labels, no distorted typography, no photographer reflection
**General**: No compression artefacts, no inconsistent lighting, no amateur composition

## Example Prompt Styles

### Cinematic Portrait
```
Dramatic cinematic portrait of a woman in her 30s with natural skin texture and visible pores. She gazes directly at camera with an intense, contemplative expression.

Lit by a single key light positioned 45 degrees above and to the left, creating a gentle Rembrandt triangle on her right cheek. Subtle hair light from behind adds separation from the dark gradient background.

Shot on Arri Alexa Mini LF with a 50mm Cooke S4 lens at f/2. Shallow depth of field. Fine film grain texture. Colour graded with desaturated tones and lifted blacks.

No smoothed skin, no beauty filter effect, no artificial perfection.
```

### Product Photography
```
Professional photograph of a premium glass perfume bottle on polished marble. Clean, minimalist composition, bottle centred and slightly angled to show label.

Three-point lighting: large softbox key from camera-left, silver reflector fill from camera-right, subtle backlight creating rim highlights on glass edges.

Shot on Phase One IQ4 with 80mm lens at f/11. Pure white background with soft shadow. High-key, crisp focus throughout.

No warped reflections, no distorted label text.
```

### Illustration (Non-Photorealistic)
```
Gouache illustration of a lonely lighthouse on a storm-battered cliff. Thick, visible brushstrokes in slate grey, deep teal, and weathered white. The sea churns in abstracted waves.

Influenced by Ravilious and Bawden, with Japanese woodblock simplicity. Strong graphic shapes, limited tonal range, atmospheric without being photographic.

Slightly textured paper visible through the paint. No photorealism, no digital perfection.
```

## Key Tips

- Up to 14 reference images supported - assign clear roles to each
- For character consistency, generate a character sheet first and reference it
- When editing, explicitly state what should remain unchanged
- Place exact text in quotation marks with font style specified
- If standard formula doesn't fit, write a clear descriptive paragraph instead
- Generate at highest resolution; upscaling introduces artefacts
