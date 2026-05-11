# `hamen.noodle` — Noodle Extensions Module

Wraps Noodle Extensions and Heck's animation/track system. Handles assigning notes and obstacles to tracks, spawning fake notes, path and track animation events, and note visibility utilities.

```python
from hamen.noodle import *
```

> Importing this module also imports everything from `hamen.main` and automatically initializes `fakeColorNotes` and `fakeBombNotes` inside `customData`. If `customData` doesn't already exist in the loaded map, a `TypeError` is raised.

This file is intended to be edited directly. Most megascript logic lives here — the functions documented below are the stable, reusable utilities extracted from that. For a full reference on Noodle Extensions and Heck animation, see [heck.aeroluna.dev](https://heck.aeroluna.dev/).

---

## Track Assignment

### `assignNotesToTrack(startTime, endTime, trackName, colorCheck=False)`

Assigns all notes in a time range to a track. If a note already has a track assigned, it prints a warning for the first conflict and silently overwrites the rest.

| Parameter | Type | Description |
|-----------|------|-------------|
| `startTime` | `float` | Range start in beats (inclusive) |
| `endTime` | `float` | Range end in beats (inclusive) |
| `trackName` | `str` | Track name to assign |
| `colorCheck` | `bool` | If `True`, left (red) notes get `trackName + '1'` and right (blue) notes get `trackName + '2'`. Defaults to `False` |

```python
# Assign all notes in bars 1–4 to a single track
assignNotesToTrack(0, 16, 'intro')

# Split by hand color
assignNotesToTrack(0, 16, 'hand', colorCheck=True)
# Red notes → 'hand1', Blue notes → 'hand2'
```

---

### `assignObstaclesToTrack(startTime, endTime, trackName)`

Assigns all walls in a time range to a track.

| Parameter | Type | Description |
|-----------|------|-------------|
| `startTime` | `float` | Range start in beats (inclusive) |
| `endTime` | `float` | Range end in beats (inclusive) |
| `trackName` | `str` | Track name to assign |

```python
assignObstaclesToTrack(32, 64, 'walls')
```

---

### `assignNoteLaneToTrack(startTime, endTime, trackName, lane)`

Assigns notes in a time range to a track, filtered by horizontal lane (the `x` column value).

| Parameter | Type | Description |
|-----------|------|-------------|
| `startTime` | `float` | Range start in beats |
| `endTime` | `float` | Range end in beats |
| `trackName` | `str` | Track name |
| `lane` | `int` | Horizontal lane index (`0`–`3` in standard mapping) |

```python
assignNoteLaneToTrack(0, 32, 'leftLane', 0)
assignNoteLaneToTrack(0, 32, 'rightLane', 3)
```

---

### `assignNoteColumnToTrack(startTime, endTime, trackName, column)`

Same as `assignNoteLaneToTrack` but filters by vertical row (the `y` value).

| Parameter | Type | Description |
|-----------|------|-------------|
| `column` | `int` | Vertical row index (`0` = bottom, `2` = top in standard mapping) |

```python
assignNoteColumnToTrack(0, 32, 'topRow', 2)
```

---

### `assignPlayerToTrack(nTime, trackName, target=None)`

Emits an `AssignPlayerToTrack` custom event, putting the player (or a specific player target) on a named track for animation.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat |
| `trackName` | `str` | Track to assign the player to |
| `target` | `str` | Optional specific player target (refer to Heck docs for valid values) |

```python
assignPlayerToTrack(0.0, 'player')
assignPlayerToTrack(0.0, 'playerHead', target='Head')
```

---

### `childrenTracks(nTime, trackName, childrens)`

Emits an `AssignTrackParent` event, parenting a list of child tracks under a parent track. Useful for grouping objects so you can transform them all together.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat |
| `trackName` | `str` | Parent track |
| `childrens` | `str[]` | List of child track names |

```python
childrenTracks(0.0, 'group', ['hand1', 'hand2', 'walls'])
```

---

## Fake Notes

Fake notes are visual-only copies of real notes — they don't count toward score or trigger miss events, making them safe to use for purely visual effects.

### `spawnFakeNotesWithTrackAt(startTime, endTime, disableGravity, timeOffset, track='', disableDebris=False, uninteractable=False)`

Deep-copies all real notes in a time range into `fakeColorNotes`, offsetting their beat by `timeOffset`. Spawn effects are always disabled on fake notes.

| Parameter | Type | Description |
|-----------|------|-------------|
| `startTime` | `float` | Range start in beats |
| `endTime` | `float` | Range end in beats |
| `disableGravity` | `bool` | Disables note gravity (the flip-in animation) on the fakes |
| `timeOffset` | `float` | Beat offset applied to each fake note's spawn time |
| `track` | `str` | Track to assign the fake notes to. Omitted if empty string |
| `disableDebris` | `bool` | Disables debris on cut. Defaults to `False` |
| `uninteractable` | `bool` | Makes fakes physically uninteractable. Defaults to `False` |

```python
# Spawn shadow copies of notes from beats 0–16, half a beat early, on a separate track
spawnFakeNotesWithTrackAt(0, 16, True, -0.5, track='shadows', disableDebris=True)
```

---

## Note Gravity

### `removeGravity(startTime, endTime, fakeNotes=False)`

Disables note gravity (the arc flip-in animation) on all notes in a time range. Can target either real notes or fake notes.

| Parameter | Type | Description |
|-----------|------|-------------|
| `startTime` | `float` | Range start in beats |
| `endTime` | `float` | Range end in beats |
| `fakeNotes` | `bool` | If `True`, operates on `fakeColorNotes` instead of `colorNotes`. Defaults to `False` |

```python
removeGravity(0, 64)
removeGravity(0, 64, fakeNotes=True)
```

---

## Note Visibility

### `invisibleNotes(startTime, endTime)`

Makes all notes in a time range invisible by setting their `dissolve` and `dissolveArrow` animation to `0` at beat `0`. Useful for sections where fake notes are carrying the visual and you don't want the real notes interfering.

```python
invisibleNotes(32, 48)
```

---

### `wipeCustomNoteData(startTime, endTime)`

Removes the entire `customData` block from all notes in a time range. Use with caution — this will strip any track assignments, animation, or other custom properties already applied to those notes.

```python
wipeCustomNoteData(0, 16)
```

---

## Animation Events

### `animateTrack(nTime, trackName, duration, easings='easeLinear', pos=None, worldRotation=None, localRotation=None, scale=None, dissolve=None, dissolveArrow=None, interactable=None, time=None)`

Emits an `AnimateTrack` custom event. All animation properties are optional — only the ones you pass will be written to the event.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat |
| `trackName` | `str` | Target track |
| `duration` | `float` | Animation duration in beats |
| `easings` | `str` | Default easing for the event. Defaults to `'easeLinear'` |
| `pos` | point def | `offsetPosition` animation |
| `worldRotation` | point def | `offsetWorldRotation` animation |
| `localRotation` | point def | `localRotation` animation |
| `scale` | point def | `scale` animation |
| `dissolve` | point def | `dissolve` animation |
| `dissolveArrow` | point def | `dissolveArrow` animation |
| `interactable` | point def | `interactable` animation |
| `time` | point def | `time` animation (controls note approach speed) |

Point definitions follow the [Heck animation spec](https://heck.aeroluna.dev/) — each is a nested array of keyframes, e.g. `[[x, y, z, beat, easing], ...]`.

```python
# Spin a track over 8 beats
animateTrack(16.0, 'rings', 8.0, worldRotation=[[0,0,0,0],[0,360,0,1,'easeInOutQuad']])

# Fade notes out over 4 beats
animateTrack(32.0, 'intro', 4.0, dissolve=[[1,0],[0,1]])
```

---

### `assignPathAnimation(nTime, trackName, duration, easings='easeLinear', pos=None, worldRotation=None, localRotation=None, scale=None, dissolve=None, dissolveArrow=None, definitePos=None, interactable=None)`

Emits an `AssignPathAnimation` event. Path animations play out along each object's individual approach path rather than as a fixed-time track animation — the keyframe time axis maps to the note's approach progress (`0` = spawn, `1` = reach the player).

Accepts the same animation properties as `animateTrack`, with the addition of `definitePos` and without `time`.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Beat |
| `trackName` | `str` | Target track |
| `duration` | `float` | How long the path assignment persists |
| `easings` | `str` | Default easing. Defaults to `'easeLinear'` |
| `definitePos` | point def | `definitePosition` — overrides the note's lane position entirely |
| *(rest)* | point def | Same properties as `animateTrack` |

```python
# Notes on 'swoopTrack' arc downward as they approach
assignPathAnimation(0.0, 'swoopTrack', 32.0,
    pos=[[0,4,0,0],[0,0,0,1,'easeInQuad']]
)
```

---

## Utilities

### `findNoteAt(nTime)`

Returns a list of indices into `exData['colorNotes']` for all notes that land exactly on `nTime`. Useful when you need to inspect or directly modify specific notes.

| Parameter | Type | Description |
|-----------|------|-------------|
| `nTime` | `float` | Exact beat to search |

**Returns:** `int[]`

```python
hits = findNoteAt(8.0)
for i in hits:
    print(exData['colorNotes'][i])
```
