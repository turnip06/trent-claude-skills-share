# Multi-Image Composition Operations

Combine elements from multiple source images into single unified composition whilst maintaining physical coherence.

---

## Output Format

**COMPOSITION INSTRUCTION**
```
[Complete 60-100 word precise integration strategy for multi-image composite]
```

**SOURCE IMAGES**
- **Image A:** [What's being extracted and its characteristics]
- **Image B:** [What's being extracted and its characteristics]
- **Image C (if applicable):** [What's being extracted and its characteristics]

**INTEGRATION STRATEGY**
- **Lighting Unification:** [Which lighting dominates, how to align]
- **Shadow Generation:** [New shadows cast between elements]
- **Depth of Field:** [Which layer is focal plane, how blur progresses]
- **Scale Calibration:** [Size relationships between composited elements]
- **Colour Harmony:** [Grading approach to unify disparate sources]

**EXPECTED COMPOSITION:** [Description of final unified image]

---

## Composition Patterns

### Pattern 1: Subject + Environment Combination

Most common: person/object from Image A, environment from Image B.

**Structure:**
```
Combine the [subject] from Image A with the [environment] from Image B. Match
lighting direction [specific alignment], shadow behaviour [cast directions], and
depth of field [focal plane placement] to unify both into cohesive frame. Place
subject at [specific position] with [perspective considerations].
```

**Example:**
```
Combine the standing figure from Image A with the industrial loft interior from
Image B. Match lighting direction so Image A's soft right-side lighting aligns
with Image B's large right-facing windows—both at approximately 4500K neutral
temperature. Generate new shadow from figure cast left across floor, matching
Image B's existing shadow quality (soft edge, 60% opacity). Place figure in
mid-ground left, scale appropriately for 3-meter distance from camera. Unify
depth of field with figure as focal plane—slight background softness beyond
5 meters matching Image B's existing shallow depth.
```

---

### Pattern 2: Multi-Subject Layering

Combining multiple subjects into single environment.

**Structure:**
```
Composite [number] subjects into single environment: Subject A (depth position),
Subject B (depth position), Subject C (depth position) into the [environment]
from Image [X]. Establish [lighting approach] for all subjects. Generate [shadow
strategy]. Scale [perspective relationships]. Apply [depth of field logic].
```

**Example:**
```
Composite three subjects into single environment: Subject A (foreground left),
Subject B (mid-ground center), Subject C (background right) into the café interior
environment from Image D. Establish consistent lighting from large front windows—
all subjects receive same soft overhead illumination at 5500K. Generate shadows
for all three subjects cast backward toward rear wall, matching existing shadow
quality in Image D (soft gradient edges, 50% opacity). Scale subjects appropriately
for their depth positions—Subject A largest, C smallest following perspective
compression. Apply graduated depth of field—Subject B sharp at focal plane, A
and C with progressive blur matching their distance from focus point.
```

---

### Pattern 3: Background Replacement

Keeping subject, replacing entire environment.

**Structure:**
```
Extract the subject from Image A (including [detail considerations]) and composite
into the [environment] from Image B. Align lighting [specific alignment strategy].
Generate [shadow description]. Place subject at [position and depth]. Match [depth
of field approach]. Colour grade [unification strategy].
```

**Example:**
```
Extract the subject from Image A (sharp cutout including hair detail and soft
edges) and composite into the mountain landscape from Image B. Align lighting so
Image A's soft directional light matches Image B's overcast ambient—both at
similar exposure and colour temperature (5800K cool neutral). Generate new ground
shadow from subject cast onto grass in Image B, matching existing landscape shadow
character (extremely soft edges due to overcast diffusion, 40% density). Place
subject in foreground at 2-meter camera distance. Match Image B's existing depth
of field—subject sharp, mountains beyond 50 meters softening into atmospheric
haze. Colour grade subject to match Image B's slightly desaturated, cool palette.
```

---

### Pattern 4: Element Extraction & Recombination

Taking specific elements from multiple sources to build new unified scene.

**Example:**
```
Combine the vintage car from Image A (foreground right), the street environment
from Image B (overall setting), and the dramatic sky from Image C (background
replacement). Unify lighting to golden hour aesthetic—regrade all elements to
warm 3500K with strong side light from left. Generate new shadow from car cast
rightward across street, soft edge gradient at 55% opacity matching golden hour
characteristics. Replace Image B's original sky with Image C's dramatic clouds,
ensuring horizon line alignment and colour grading to match warm golden hour tone
(warm highlights, cool shadow complements). Scale car appropriately for stated
2-meter foreground position. Apply consistent depth of field—car sharp, street
mid-ground transitioning to soft, sky naturally distant with slight atmospheric
haze.
```

---

## Integration Technical Requirements

### Lighting Hierarchy Decision

When sources have different lighting, choose an approach:

**Option 1: Preserve Source Lighting (Diegetic)**
Maintain each element's original lighting, provide narrative motivation (subject indoors looking outside, mixed practical sources, etc.). Requires careful selection of compatible sources.

**Option 2: Unify to Dominant Source**
Choose strongest/best lighting (usually background environment) and adjust all composited elements to match. Relight subjects to align with environmental lighting direction and quality.

**Option 3: Hybrid Approach**
Primary elements keep character lighting, background provides ambient. Common in commercial compositing—hero product lit separately but integrated into environmental ambient.

**Example of Option 2:**
```
Unify all elements to match Image B's soft window light. Regrade Image A's subject
to receive soft directional light from right at 5000K neutral, eliminating Image A's
original hard spotlight character. Adjust Image C's product to also receive same
soft right-side illumination, creating consistent lighting logic across entire
composite where single large window right serves as primary source for all elements.
```

---

### Shadow Generation Requirements

New shadows must be created where composited elements interact:

**Direction:** Follow environmental lighting source identified/established
**Quality:** Match existing shadows in target environment (hard/soft edges)
**Colour:** Inherit temperature of environmental shadows (cool/warm/neutral)
**Opacity:** Scale to match existing shadow density in environment
**Placement:** Ground contact points must cast shadows onto receiving surface
**Interaction:** Shadows acknowledge environmental geometry (bending up walls, etc.)

**Example:**
```
Generate three new shadows for composited subjects: (1) Subject A shadow cast
leftward 2 meters across floor, soft gradient edge, 50% opacity, cool blue tint
matching overcast ambient. (2) Subject B shadow cast same direction but 1.5 meters
given closer light source angle, identical quality. (3) Subject C shadow minimal—
barely visible given distance and atmospheric diffusion. All shadows bend slightly
upward where floor meets far wall, acknowledging environmental geometry.
```

---

### Depth of Field Unification

Establish single focal plane for entire composition:

**Identify Focal Plane:** Determine which layer should be sharpest (usually mid-ground subject)
**Foreground Blur:** Blur objects closer to camera appropriately
**Background Blur:** Blur objects further from camera appropriately
**Blur Consistency:** Match existing blur quality from sources (smooth/bokeh/textured)
**Progressive Falloff:** Maintain consistent focus falloff throughout composition

**Example:**
```
Establish focal plane at mid-ground subject (3 meters from camera). Apply foreground
blur to elements 1-2 meters from camera—gentle circular bokeh with smooth falloff
matching Image B's existing shallow depth characteristics. Apply progressive
background blur beyond focal plane—moderate softness 5-10 meters, heavy softness
beyond 10 meters, complete atmospheric dissolution beyond 20 meters. Maintain
bokeh highlight character from Image B (smooth circular shapes, not harsh edges).
```

---

### Colour Grade Unification

Sources often have different colour character—unify them:

**Approach 1: Match to Dominant Source**
Grade all composited elements to match target environment's colour—temperature, saturation, contrast, tonal curve.

**Approach 2: Neutral Rebalance**
Bring all sources to neutral baseline, then apply unified grade across entire composition.

**Approach 3: Intentional Separation**
Maintain slight colour difference between layers for stylistic effect—but must feel intentional, not accidental.

**Example of Approach 1:**
```
Grade all elements to match Image B's cool desaturated palette: (1) Reduce Image A
subject saturation by 30% and shift colour temperature cool by +800K to match Image B's
6200K tone. (2) Apply same desaturation and cooling to Image C product. (3) Unify
contrast curve across all elements to match Image B's lifted blacks and compressed
highlights (matte film aesthetic). (4) Apply subtle teal cast to shadows across
entire composition matching Image B's existing grade.
```

---

### Perspective & Scale Calibration

Ensure all elements obey consistent perspective rules:

**Horizon Line:** All elements must share single horizon line
**Vanishing Points:** Architectural elements converge consistently
**Atmospheric Perspective:** Distant elements more desaturated, lower contrast, cooler
**Size Relationships:** Elements scaled appropriately for stated depth positions

**Example:**
```
Calibrate perspective: Align all elements to share horizon line at 1.5 meters
above ground plane. Subject A (foreground, 2m away) rendered at 180cm apparent
height. Subject B (mid-ground, 5m away) rendered at 120cm apparent height following
perspective compression. Background architecture converges toward vanishing point
on horizon line at frame center right. Apply atmospheric perspective—foreground
100% saturation and contrast, mid-ground 70%, background 40% with progressive cool
shift following natural depth haze.
```

---

## Advanced Composition Techniques

### Technique 1: Environmental Wrapping

Ensure composited subject interacts with environment:

- Reflections in windows, water, glossy surfaces
- Contact shadows where subject touches surfaces
- Environmental light bouncing onto subject from surroundings
- Atmospheric effects (fog, haze) affecting subject same as environment

### Technique 2: Edge Quality Matching

Different edge treatments for different scenarios:

- **Clean studio shots** → Hard cutout with subtle edge softening
- **Outdoor diffused light** → Soft feathered edges
- **Backlit subjects** → Rim light preservation with gentle edge glow
- **Hair/fur detail** → Semi-transparent edge complexity

### Technique 3: Depth Integration

Create believable spatial relationships:

- Establish clear foreground/mid-ground/background layers
- Apply atmospheric perspective (colour and contrast reduction with distance)
- Implement depth-appropriate blur
- Ensure scale follows perspective compression
- Align all elements to shared vanishing points

### Technique 4: Lighting Continuity

Maintain consistent light behaviour across all elements:

- Single dominant light source direction
- Consistent hard/soft quality throughout
- Unified colour temperature (or motivated temperature shifts)
- Shadow consistency (direction, length, edge, opacity)
- Appropriate fill light ratios
