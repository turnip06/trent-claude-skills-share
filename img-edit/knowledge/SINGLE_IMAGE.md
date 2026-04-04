# Single Image Editing Operations

Detailed techniques for modifying specific elements within an existing image whilst maintaining physical coherence and photorealistic integration.

---

## Output Format

**EDIT INSTRUCTION**
```
[Complete 40-80 word precise edit prompt describing the modification]
```

**TARGET ELEMENT:** [What's being changed]
**MODIFICATION TYPE:** [Add/Remove/Replace/Adjust]
**INTEGRATION REQUIREMENTS:**
- **Lighting Match:** [How to align with existing image lighting]
- **Shadow Adjustment:** [New or modified shadows needed]
- **Colour Harmony:** [Colour adjustments to unify]
- **Depth Positioning:** [Where in the depth plane this sits]
- **Edge Treatment:** [How to blend into existing image]

**EXPECTED RESULT:** [Description of final integrated image]

---

## Edit Types

### Type 1: Element Removal

Remove objects, people, or details from the scene cleanly.

**Structure:**
```
Remove [specific element] from [location in frame]. Fill the vacated area with
[appropriate background continuation] matching existing [texture/pattern/lighting].
Ensure seamless integration by [specific blending approach] and [shadow/lighting
considerations].
```

**Example:**
```
Remove the blue car from the right side of the frame. Fill the vacated area with
continuation of the asphalt road texture and painted parking lines visible in
adjacent areas. Match the existing harsh noon sun lighting creating minimal
shadows, with slight heat distortion maintaining atmospheric consistency. Extend
the distant building façade visible behind the car's previous position, preserving
perspective convergence toward existing vanishing point.
```

---

### Type 2: Element Addition

Add new objects, people, or details that weren't in the original.

**Structure:**
```
Add [new element] at [specific position]. Match lighting by [alignment strategy],
generate [shadow description], scale appropriately for [depth consideration], and
integrate colour by [grading approach].
```

**Example:**
```
Add a wooden park bench in the mid-ground left, approximately 3 meters from
camera. Match the existing soft overcast lighting at 5500K neutral, casting
minimal shadow directly beneath bench with soft gradient edges at 40% opacity.
Scale bench appropriately for mid-ground placement—approximately 1.2 meters
visible width. Grade wood tones to match the slightly desaturated, cool palette
of existing image. Position on grass texture visible in adjacent area, with
bench legs creating subtle compression in grass surface.
```

---

### Type 3: Element Replacement

Swap one element for another whilst maintaining scene coherence.

**Structure:**
```
Replace [existing element] with [new element]. Maintain same [spatial position/
scale/lighting direction]. Adjust [shadows/reflections/interactions] to match
new element's form whilst preserving original scene's lighting character.
```

**Example:**
```
Replace the vintage sedan in the foreground with a modern electric SUV. Maintain
same spatial position in right third of frame, same scale (approximately 2 meters
from camera), and same orientation (3/4 front view facing left). Match existing
golden hour lighting—warm 3500K from left creating strong side light with specular
highlights on glossy paint. Modify ground shadow to match new vehicle's higher
profile—shadow cast right with soft edge gradient, 50% opacity, extending 2.5
meters. Update reflections in vehicle's windows to match existing sky and
surrounding environment visible in original image.
```

---

### Type 4: Lighting Adjustment

Modify the lighting conditions within the scene.

**Structure:**
```
Adjust lighting from [current state] to [new state]. Modify [shadows/highlights/
colour temperature/direction] whilst maintaining [what should remain consistent].
Update [environmental indicators] to support new lighting logic.
```

**Example:**
```
Adjust lighting from harsh noon overhead sun to soft golden hour side light.
Rotate light source from top-down to low left at 15-degree angle, changing colour
temperature from neutral 5500K to warm 3500K. Soften all shadow edges from hard
crisp to gentle gradients. Extend all shadows significantly longer (4-5x current
length) cast rightward. Add warm golden colour cast to all highlight areas whilst
deepening shadows to cooler blue tones. Maintain existing composition and all
elements' positions—only lighting behaviour changes.
```

---

### Type 5: Atmospheric Modification

Change weather, environmental effects, or atmospheric conditions.

**Structure:**
```
Modify atmosphere from [current condition] to [new condition]. Add/adjust
[volumetric effects], modify [visibility/contrast], update [colour relationships],
and ensure [physical plausibility].
```

**Example:**
```
Modify atmosphere from clear day to heavy fog. Reduce visibility beyond 10 meters
to graduated obscurity—mid-ground elements visible but muted, background almost
completely obscured. Lower overall contrast by 40%, creating soft diffused quality.
Add volumetric fog density visible in light beams from existing street lamps,
creating dimensional atmospheric perspective. Desaturate colour progressively with
distance—foreground retains 80% original saturation, mid-ground 50%, background
20%. Maintain existing lighting sources but add visible glow/halo effect where
light interacts with fog particles.
```

---

## Integration Techniques

### Lighting Match Detail

When adding or replacing elements:

1. **Analyze existing lighting**
   - Identify primary light source direction
   - Determine hard vs soft quality
   - Note colour temperature
   - Observe shadow characteristics

2. **Apply matching illumination**
   - Light new element from same direction
   - Match shadow edge quality
   - Align colour temperature
   - Calibrate exposure level

3. **Generate appropriate shadows**
   - Cast shadows in same direction as existing
   - Match edge softness/hardness
   - Align shadow colour and opacity
   - Ensure shadows interact with geometry

### Scale Calibration Detail

Ensure added elements appear at correct size:

1. **Determine depth position**
   - Foreground (0-2m from camera)
   - Mid-ground (2-10m from camera)
   - Background (10m+ from camera)

2. **Apply perspective compression**
   - Closer objects appear larger
   - Distant objects appear smaller
   - Follow existing perspective cues
   - Match convergence to vanishing points

3. **Verify against reference elements**
   - Compare to similar objects in scene
   - Check horizon line alignment
   - Ensure realistic proportions

### Colour Grading Integration

Unify new elements with existing palette:

1. **Match temperature**
   - Warm scenes: add warm colour cast
   - Cool scenes: add cool colour cast
   - Neutral scenes: maintain balance

2. **Align saturation**
   - Vibrant scenes: maintain high saturation
   - Muted scenes: desaturate new elements
   - Match overall colour intensity

3. **Apply consistent contrast**
   - High contrast scenes: deepen shadows, brighten highlights
   - Low contrast scenes: compress tonal range
   - Maintain existing tonal curve

### Edge Treatment Strategies

**Hard Cutout:**
- Use when lighting is clean and contrasty
- Appropriate for studio or controlled environments
- Creates precise, defined separation

**Soft Transition:**
- Use when lighting is diffused
- Appropriate for outdoor or atmospheric scenes
- Creates natural, blended integration

**Feathered Edge:**
- Use for hair, fur, semi-transparent materials
- Gradual transparency at boundaries
- Most realistic for organic subjects

**Motion Blur Edge:**
- Use when adding moving elements
- Directional blur indicating movement
- Maintains photorealistic action

---

## Common Edit Patterns

### Pattern 1: Time of Day Transformation

Change the apparent time when photo was taken:

1. Analyze existing lighting
2. Specify new time characteristics
3. Modify shadows (direction, length, quality)
4. Adjust colour temperature
5. Update sky if visible
6. Modify ambient light levels

### Pattern 2: Weather Transformation

Change atmospheric conditions:

1. Identify current weather state
2. Specify new weather conditions
3. Add/remove weather effects (rain, fog, snow)
4. Modify visibility and contrast
5. Update reflections if surfaces are wet
6. Adjust lighting diffusion

### Pattern 3: Object Removal & Fill

Remove unwanted elements cleanly:

1. Identify element to remove
2. Determine what should replace it
3. Analyze adjacent textures/patterns
4. Specify fill strategy
5. Ensure lighting consistency
6. Maintain perspective

### Pattern 4: Subject Insertion

Add new subject to existing environment:

1. Specify subject and position
2. Match environmental lighting
3. Generate appropriate shadows
4. Scale for depth position
5. Integrate colour grading
6. Blend edges appropriately
