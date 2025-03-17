# [Header](./resources/HamenBanner.png)

## Overview
A Python framework to aid in creation of Beat Saber modcharts. This has support for Heck libaries Noodle, Chroma, and Vivify.

## Usage
Edit the `fileName` and `exportName` variables in `Hamen.py` depending on what file you're injecting functions into. Use the provided `example.py` file as a foundation for scripting.

## Example
```python
### example.py
import json
from Hamen import *
from hamenNoodle import *
from hamenChroma import *
from hamenVivify import *


# load bundles
bundle = loadBundleInfo('bundleinfo.json')

# infodat
infoDat_addRequirement([
    "Noodle Extensions",
    "Chroma",
    "Vivify"
])

# add arrays for important stuff
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}
exData['customData']['environment'] = []


#region ### do note scripts here
InstantiatePrefab(8,'assets/cube.prefab','cube') # example code, remove this before doing mod effects

### Save edited json and info dat
export_infoDat()
export_diff()
```
