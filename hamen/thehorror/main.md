# `hamen.main` — Core Module

The core of Hamen. Every other module imports from this one, so it needs to be the first thing set up in any script. It handles loading your source map, writing the output, and managing `Info.dat`.

```python
from hamen.main import *
```

---

## Setup

Before running any scripts, set these two variables at the top of your working file to point at your source and export filenames:

```python
fileName   = 'ExpertStandard.dat'      # The map you're reading from
exportName = 'ExpertPlusStandard.dat'  # The map you're writing to
```

On import, `main.py` immediately opens both `fileName` and `Info.dat` and loads them into memory as `exData` and `infDat` respectively. All functions in Hamen operate by mutating these two dicts in-place, and the export functions write them back to disk.

### Global State

| Variable | Type | Description |
|----------|------|-------------|
| `exData` | `dict` | The loaded beatmap JSON. All note/event/customData edits go here. |
| `infDat` | `dict` | The loaded `Info.dat` JSON. Requirement/suggestion edits go here. |

Before using `chroma.py` or your own scripts, you'll also need to pre-initialize the `customData` arrays you plan to use. These are **not** created automatically on import:

```python
exData['customData']['fakeColorNotes']  = []
exData['customData']['fakeBombNotes']   = []
exData['customData']['fakeObstacles']   = []
exData['customData']['fakeBurstSliders'] = []
exData['customData']['customEvents']    = []  # already created on import
```

---

## Export Functions

### `export_diff()`

Writes the modified `exData` to disk as `exportName`.

Before writing, it sorts the following arrays by beat (`b`) automatically:

- `colorNotes`, `basicBeatmapEvents`, `bombNotes`, `obstacles`, `burstSliders`
- `fakeColorNotes`, `fakeBombNotes`, `customEvents`, `fakeBurstSliders`, `fakeObstacles` (if present)

A `.bak` backup of the previous `exportName` is created before overwriting. Call this at the very end of your script.

```python
export_diff()
```

---

### `export_infoDat()`

Writes the modified `infDat` back to `Info.dat`. Creates a `.bak` backup first.

Call this alongside `export_diff()` whenever you've made changes to requirements, suggestions, or settings.

```python
export_infoDat()
```

---

## Info.dat Functions

### `infoDat_addRequirement(requirement)`

Adds mod requirements to the export difficulty entry in `Info.dat`. Requirements force the player to have those mods installed to play the map.

| Parameter | Type | Description |
|-----------|------|-------------|
| `requirement` | `str[]` | List of mod names to require. Pass `[]` to clear existing requirements. |

```python
infoDat_addRequirement(["Noodle Extensions", "Chroma"])

# Clear all requirements
infoDat_addRequirement([])
```

The function automatically finds the correct difficulty entry by matching `exportName` against `_beatmapFilename` in `Info.dat`.

---

### `infoDat_addSuggestion(suggestion)`

Adds mod suggestions to the export difficulty. Suggestions are shown to the player but not enforced.

| Parameter | Type | Description |
|-----------|------|-------------|
| `suggestion` | `str[]` | List of mod names to suggest. Pass `[]` to clear existing suggestions. |

```python
infoDat_addSuggestion(["Vivify"])
```

---

### `infoDat_removeBaseMap()`

Removes the `fileName` difficulty entry from `Info.dat`. Use this when you've finished base-mapping and don't want the source difficulty to ship with the map.

```python
infoDat_removeBaseMap()
```

---

### `infoDat_settingsSetter(...)`

Injects a `_settings` block into the export difficulty's `customData`, which lets you recommend specific game settings to the player via [Heck's settings system](https://heck.aeroluna.dev/).

All parameters are optional. Pass only the categories you want to configure.

| Parameter | Type | Description |
|-----------|------|-------------|
| `player` | `dict` | `_playerOptions` block |
| `modifiers` | `dict` | `_modifiers` block |
| `chroma` | `dict` | `_chroma` block |
| `cPlus` | `dict` | `_countersPlus` block |
| `uiTweaks` | `dict` | `_uiTweaks` block |
| `nTweaks` | `dict` | `_noteTweaks` block |
| `graphics` | `dict` | `_graphics` block |

```python
infoDat_settingsSetter(
    modifiers={'_noFailOn0Energy': True},
    graphics={'_mainEffectGraphicsPreset': 1}
)
```

Refer to the [Heck documentation](https://heck.aeroluna.dev/) for the full list of valid keys inside each block.

---

### `infoDat_setEditedVersion()`

Stamps the `Info.dat` `_editors` field with Hamen's product ID and version. Mostly for bookkeeping.

```python
infoDat_setEditedVersion()
```

---

## Utility

### `countUp()`

Increments a `count.txt` run counter and prints it to the console. Useful for sanity-checking how many times you've run a script during a session. Creates `count.txt` if it doesn't exist.

```python
countUp()
```

Output:
```
GIVE IT UP FOR RUN 7!!!!
```

---

### `beat(e)`

Internal sort key used by `export_diff()`. Returns `e['b']`. You generally won't need to call this directly, but it's available if you want to sort custom arrays the same way.

```python
my_list.sort(key=beat)
```
