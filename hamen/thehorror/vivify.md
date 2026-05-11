# `hamen.vivify` — Vivify Module

Wraps Vivify's custom event system for working with Unity AssetBundles in Beat Saber. Covers spawning prefabs, controlling post-processing via blits, managing cameras, and setting material properties at runtime.

```python
from hamen.vivify import *
```

> Importing this module also imports everything from `hamen.main`.

All functions here append entries to `exData['customData']['customEvents']`. For a full reference on what Vivify supports at the JSON level, see [heck.aeroluna.dev](https://heck.aeroluna.dev/).

---

## Background: Asset Paths

Most Vivify functions take an `asset` parameter which is the path to a Unity asset inside your compiled AssetBundle. Hamen automatically lowercases these paths to guard against case-sensitivity typos. Convention is to use forward slashes and keep paths relative to the bundle root, e.g. `"assets/models/cube.prefab"`.

---

## Prefabs

### `InstantiatePrefab(nTime, asset, id=None, track=None, position=[0,0,0], localPosition=[0,0,0], rotation=[0,0,0], localRotation=[0,0,0], scale=[1,1,1])`

Spawns a prefab from your AssetBundle into the scene. This is the primary way to bring custom 3D objects into a map.

Non-default transform values are only written to the event to keep the JSON clean.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat to spawn the prefab |
| `asset` | `str` | Asset path within the bundle |
| `id` | `str` | Optional ID used to reference or destroy the object later |
| `track` | `str` | Optional track to assign the spawned object to for animation |
| `position` | `float[3]` | World position. Omitted if `[0,0,0]` |
| `localPosition` | `float[3]` | Local position. Omitted if `[0,0,0]` |
| `rotation` | `float[3]` | World Euler rotation. Omitted if `[0,0,0]` |
| `localRotation` | `float[3]` | Local Euler rotation. Omitted if `[0,0,0]` |
| `scale` | `float[3]` | Scale. Omitted if `[1,1,1]` |

```python
InstantiatePrefab(8.0, 'assets/models/cube.prefab', id='myCube', track='cubeTrack', position=[0, 2, 10])
```

---

### `assignObjectPrefab(nTime, loadMode, objectName, contents={})`

Assigns a prefab from the AssetBundle to an existing in-game object (like a note or wall). Useful for replacing the visual of a game object with your own asset.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat |
| `loadMode` | `str` | How to load the asset (refer to Vivify docs for valid values) |
| `objectName` | `str` | Name of the target in-game object |
| `contents` | `dict` | Optional additional properties for the prefab assignment |

```python
assignObjectPrefab(0.0, 'Single', 'colorNote', {'asset': 'assets/notes/custom_note.prefab'})
```

---

### `destroyObject(nTime, id)`

Destroys a previously spawned object, camera, or texture by its ID. Can accept a single ID string or a list of IDs.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat to destroy the object |
| `id` | `str` or `str[]` | ID or list of IDs to destroy |

```python
destroyObject(32.0, 'myCube')
destroyObject(64.0, ['cam1', 'myCube', 'screenTex'])
```

---

## Material Properties

### `setUnityMaterialProperty(nTime, materialName, duration, shaderID, type, value, easing='easeLinear')`

Animates a property on a specific material asset in the bundle. The change is applied over `duration` beats.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat |
| `materialName` | `str` | Asset path of the material (auto-lowercased) |
| `duration` | `float` | Animation duration in beats |
| `shaderID` | `str` | The shader property name (e.g. `"_Color"`, `"_MainTex"`) |
| `type` | `str` | Property type: `"Texture"`, `"Float"`, `"Color"`, `"Vector"`, `"Keyword"` |
| `value` | varies | Value to set. Format depends on `type` — see Vivify docs |
| `easing` | `str` | Easing. Defaults to `'easeLinear'` |

```python
setUnityMaterialProperty(16.0, 'assets/materials/glow.mat', 2.0, '_Color', 'Color', [1, 0, 0, 1])
setUnityMaterialProperty(24.0, 'assets/materials/glow.mat', 0.0, '_Intensity', 'Float', 2.5)
```

---

### `setUnityGlobalProperty(nTime, duration, propID, type, value, easing='easeLinear')`

Same as `setUnityMaterialProperty` but sets a **global** shader property — any shader in the game that reads this property will be affected.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat |
| `duration` | `float` | Animation duration in beats |
| `propID` | `str` | Global shader property name |
| `type` | `str` | Property type |
| `value` | varies | Value to set |
| `easing` | `str` | Easing. Defaults to `'easeLinear'` |

```python
setUnityGlobalProperty(0.0, 0.0, '_GlobalFogColor', 'Color', [0, 0, 0, 1])
```

---

## Post-Processing

### `unityBlit(nTime, duration, propID, type, value, asset=None, priority=None, cPass=None, order=None, source=None, destination=None, easing='easeLinear')`

Assigns a material to the camera as a full-screen post-processing effect (a blit). The material is applied for `duration` beats. All parameters except `nTime`, `duration`, `propID`, `type`, and `value` are optional.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat |
| `duration` | `float` | How long the effect runs in beats |
| `propID` | `str` | Shader property name |
| `type` | `str` | Property type |
| `value` | varies | Property value |
| `asset` | `str` | Asset path of the blit material (auto-lowercased) |
| `priority` | `int` | Order relative to other active post-processing effects |
| `cPass` | `int` | Which shader pass to use |
| `order` | `str` | Run before or after `MainEffect` (Bloom). `"BeforeMainEffect"` or `"AfterMainEffect"` |
| `source` | `str` | Source texture key |
| `destination` | `str` | Destination texture key |
| `easing` | `str` | Easing. Defaults to `'easeLinear'` |

```python
unityBlit(
    32.0, 4.0,
    '_Intensity', 'Float', 1.0,
    asset='assets/shaders/chromatic.mat',
    order='AfterMainEffect',
    priority=0
)
```

---

## Cameras

### `createCamera(nTime, id, texture=None, depthTexture=None, prop=None)`

Creates a custom camera in the scene. The camera can render to a named texture that other shaders can then read as a global property.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat |
| `id` | `str` | Unique camera ID |
| `texture` | `str` | Key for the color render texture (optional) |
| `depthTexture` | `str` | Key for a depth-only render texture (optional) |
| `prop` | `dict` | Additional camera properties from the Vivify spec (optional) |

```python
createCamera(0.0, 'cam1', texture='_CamTex', prop={'cullingMask': {'environment': False}})
```

Refer to the [Vivify documentation](https://heck.aeroluna.dev/) for the full list of valid camera property keys.

---

## Textures

### `createScreenTexture(time, id)`

Creates a new render texture tied to the screen. The texture can be referenced by its ID in blit source/destination fields or as a global shader property.

| Parameter | Type | Description |
|-----------|------|-------------|
| `time` | `float` | Beat |
| `id` | `str` | Texture ID |

```python
createScreenTexture(0.0, '_ScreenCapture')
```

---

## Bundle Info

### `loadBundleInfo(jsn)`

Loads a `bundleinfo.json` (or equivalent) and returns the parsed contents as a dict. Used to bring in bundle CRC data for the export step.

| Parameter | Type | Description |
|-----------|------|-------------|
| `jsn` | `str` | Filename of the bundle info JSON |

**Returns:** `dict`

```python
bundle = loadBundleInfo('bundleinfo.json')
```

---

### `infoDat_injectCRCs(jsn)`

Injects bundle CRC data from a parsed `bundleinfo.json` into `infDat` under `_customData._assetBundle`. Required for Vivify maps so the mod knows what files to verify and download.

| Parameter | Type | Description |
|-----------|------|-------------|
| `jsn` | `dict` | Parsed bundle info (the return value of `loadBundleInfo`) |

```python
bundle = loadBundleInfo('bundleinfo.json')
infoDat_injectCRCs(bundle)
```
