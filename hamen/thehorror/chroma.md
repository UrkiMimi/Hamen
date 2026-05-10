# `hamen.chroma` — Chroma & Environment Module

Wraps Chroma and Heck's environment enhancement system. Handles geometry, materials, environment object manipulation, lighting, and color animation events.

```python
from hamen.chroma import *
```

> Importing this module also imports everything from `hamen.main` and automatically initializes `exData['customData']['materials']` and `exData['customData']['environment']` as empty collections if they don't exist.

For a full reference on what Chroma supports at the JSON level, see [heck.aeroluna.dev](https://heck.aeroluna.dev/).

---

## Materials

Materials are named resources referenced by geometry objects. They must be defined before any geometry that uses them.

### `addMaterial(shader, color, unlit, matName)`

Registers a new named material into `customData.materials`.

| Parameter | Type | Description |
|-----------|------|-------------|
| `shader` | `str` | Shader name (e.g. `"Standard"`, `"OpaqueLight"`, `"TransparentLight"`) |
| `color` | `float[4]` | RGBA color as `[r, g, b, a]` |
| `unlit` | `bool` | If `True`, sets `shaderKeywords` to `[]` for an unlit look. **Note:** unlit materials do not work on Beat Saber 1.39+. |
| `matName` | `str` | The key used to reference this material in geometry |

```python
addMaterial('Standard', [1, 0, 0, 1], False, 'RedMat')
addMaterial('OpaqueLight', [0, 1, 1, 1], True, 'CyanGlow')  # unlit, may break on 1.39+
```

---

## Geometry

Primitive geometry objects are rendered in-world by Heck. They're positioned in Beat Saber world-space and can optionally be assigned to a track for animation.

### `addPrimitiveModel(type, material, position, localRotation, scale)`

Spawns a primitive geometry object with no track assignment.

| Parameter | Type | Description |
|-----------|------|-------------|
| `type` | `str` | Primitive type: `"Cube"`, `"Sphere"`, `"Cylinder"`, `"Plane"`, `"Quad"`, `"Triangle"` |
| `material` | `str` | Name of a material defined via `addMaterial()` |
| `position` | `float[3]` | World position `[x, y, z]` |
| `localRotation` | `float[3]` | Local Euler rotation `[x, y, z]` |
| `scale` | `float[3]` | Object scale `[x, y, z]` |

```python
addMaterial('Standard', [1, 1, 1, 1], False, 'White')
addPrimitiveModel('Cube', 'White', [0, 4, 20], [0, 45, 0], [2, 2, 2])
```

---

### `addPrimitiveModelTrack(type, material, position, localRotation, scale, track)`

Same as `addPrimitiveModel` but assigns the geometry to a named track, allowing it to be animated via `AnimateTrack` events.

| Parameter | Type | Description |
|-----------|------|-------------|
| `type` | `str` | Primitive type |
| `material` | `str` | Material name |
| `position` | `float[3]` | World position |
| `localRotation` | `float[3]` | Local Euler rotation |
| `scale` | `float[3]` | Object scale |
| `track` | `str` | Track name to assign this geometry to |

```python
addPrimitiveModelTrack('Sphere', 'CyanGlow', [0, 2, 10], [0, 0, 0], [1, 1, 1], 'orb')
```

---

### `fridgeTrack(pix, trackName, distanceFromPlayer=12, color=[1,1,1,0])`

Converts a black-and-white "fridge image" (a 2D array of `'x'` and `' '` characters) into a grid of cubes and assigns them all to a track. Each `'x'` cell becomes a `0.5×0.5×0.5` cube placed in world-space.

| Parameter | Type | Description |
|-----------|------|-------------|
| `pix` | `str[][]` | 2D array where `'x'` = filled cell and anything else = empty |
| `trackName` | `str` | Track to assign all spawned cubes to |
| `distanceFromPlayer` | `float` | Z depth the grid sits at. Defaults to `12` |
| `color` | `float[4]` | RGBA color for the auto-generated material. Defaults to `[1,1,1,0]` |

The material is generated automatically with a random name and uses an unlit `Standard` shader.

```python
img = [
    ['x', ' ', 'x'],
    [' ', 'x', ' '],
    ['x', ' ', 'x'],
]
fridgeTrack(img, 'pixelArt', distanceFromPlayer=15, color=[0, 1, 1, 1])
```

---

## Environment Object Manipulation

These functions operate on existing environment objects by ID, and append entries to `customData.environment`. The `lookupMethod` parameter controls how the ID is matched against environment object names.

**Valid lookup methods:** `"Regex"`, `"Exact"`, `"Contains"`, `"StartsWith"`, `"EndsWith"`

---

### `assignEnvironmentToTrack(envName, trackName, lkMethod)`

Assigns an existing environment object to a track so it can be animated.

| Parameter | Type | Description |
|-----------|------|-------------|
| `envName` | `str` | Environment object ID |
| `trackName` | `str` | Track name to assign |
| `lkMethod` | `str` | Lookup method |

```python
assignEnvironmentToTrack('RingLight', 'rings', 'Contains')
```

---

### `disableObject(envId, lookupMe)`

Hides an environment object entirely (`active: false`).

```python
disableObject('Spectrograms', 'Contains')
```

---

### `dupe(envId, lookupMe, dupe)`

Duplicates an environment object a given number of times. Note that the original is also set to `active: false` — the duplicates are what get shown.

| Parameter | Type | Description |
|-----------|------|-------------|
| `dupe` | `int` | Number of duplicates to create |

```python
dupe('RingLight', 'Exact', 8)
```

---

### `editer(envId, lookupMe, pos, sc, rotation, enabled)`

General-purpose environment object editor. Repositions, rescales, rotates, and enables or disables an object.

| Parameter | Type | Description |
|-----------|------|-------------|
| `pos` | `float[3]` | Local position |
| `sc` | `float[3]` | Scale |
| `rotation` | `float[3]` | Local rotation |
| `enabled` | `bool` | Whether the object is active |

```python
editer('Logo', 'Contains', [0, 10, 0], [1, 1, 1], [0, 0, 0], False)
```

---

### `tubeEditer(envId, lookupMe, pos, sc, rotation, enabled, id, multi, fogMulti)`

Extended version of `editer` for tube lights. Exposes `ILightWithId` and `TubeBloomPrePassLight` component fields for fine-grained control of light IDs and bloom multipliers.

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | `int` | Light ID for `ILightWithId` |
| `multi` | `float` | `colorAlphaMultiplier` on `TubeBloomPrePassLight` |
| `fogMulti` | `float` | `bloomFogIntensityMultiplier` on `TubeBloomPrePassLight` |

```python
tubeEditer('NeonTube', 'Exact', [2, 0, 0], [1, 1, 1], [0, 0, 0], True, 5, 1.5, 0.8)
```

---

### `fogging(envId, lookupMe, atten, offset, startY, height)`

Adjusts the `BloomFogEnvironment` component on an environment object, letting you tweak fog parameters per-object.

| Parameter | Type | Description |
|-----------|------|-------------|
| `atten` | `float` | Fog attenuation |
| `offset` | `float` | Fog offset along Z |
| `startY` | `float` | Y value where fog begins |
| `height` | `float` | Height falloff distance |

```python
fogging('FogRing', 'Contains', 0.1, 0.0, -2.0, 10.0)
```

---

## V2 Ring Events

These only apply to V2 environments that have ring objects (e.g. the classic Triangle or Origins environment). They emit `basicBeatmapEvents` with Chroma `customData`.

### `customRingRotation(time, rotation, step=15, prop=None, speed=1, namefilter=None, direction=None)`

Fires a ring rotation event.

| Parameter | Type | Description |
|-----------|------|-------------|
| `time` | `float` | Beat |
| `rotation` | `float` | Target rotation value |
| `step` | `float` | Angular step between rings. Defaults to `15` |
| `prop` | `float` | Propagation speed (optional) |
| `speed` | `float` | Rotation speed. Defaults to `1` |
| `namefilter` | `str` | Filter by ring name (optional) |
| `direction` | `int` | `0` = CCW, `1` = CW (optional) |

```python
customRingRotation(16.0, 90.0, step=20, speed=2)
```

---

### `customRingStep(time, step=15, speed=1)`

Fires a ring zoom/step event.

| Parameter | Type | Description |
|-----------|------|-------------|
| `time` | `float` | Beat |
| `step` | `float` | Ring step. Defaults to `15` |
| `speed` | `float` | Animation speed. Defaults to `1` |

```python
customRingStep(32.0, step=5, speed=3)
```

---

## Color Animation Events

These append `AnimateTrack` custom events that animate the `color` property on a track. Both target tracks that are already assigned to notes, walls, or geometry.

### `clrTween(nTime, trackName, duration, clr0, clr1, easing='easeLinear')`

Simple two-keyframe color tween. Animates from `clr0` to `clr1` over `duration` beats.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Event beat |
| `trackName` | `str` | Target track |
| `duration` | `float` | Tween duration in beats |
| `clr0` | `float[4]` | Start color `[r, g, b, a]` |
| `clr1` | `float[4]` | End color `[r, g, b, a]` (easing appended automatically) |
| `easing` | `str` | Easing function name. Defaults to `'easeLinear'` |

> **Note:** `clr1` is mutated in-place — `easing` is appended to the array before it's inserted into the event. Avoid reusing the same list object across multiple calls.

```python
clrTween(8.0, 'rings', 4.0, [1, 0, 0, 1], [0, 0, 1, 1], easing='easeInOutQuad')
```

---

### `clrPointDef(nTime, trackName, duration, clr)`

Full point definition color animation. Use this when you need more than two keyframes.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Event beat |
| `trackName` | `str` | Target track |
| `duration` | `float` | Animation duration in beats |
| `clr` | `float[5][]` | Array of keyframes, each formatted as `[r, g, b, a, time]` or `[r, g, b, a, time, easing]` |

```python
clrPointDef(16.0, 'orb', 8.0, [
    [1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0.5, 'easeInQuad'],
    [0, 0, 1, 1, 1],
])
```

The point definition format follows the [Heck animation spec](https://heck.aeroluna.dev/). Time values are normalized `0.0`–`1.0` across the duration.
