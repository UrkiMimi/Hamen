# ![Hamen](https://raw.githubusercontent.com/UrkiMimi/Hamen/refs/heads/main/resources/HamenBanner.png)

## Overview
A Python framework to aid in creation of Beat Saber modcharts. This has support for Heck libaries Noodle, Chroma, and Vivify.

## Usage
Edit the `fileName` and `exportName` variables in `Hamen.py` depending on what file you're injecting functions into. Use the provided `example.py` file as a foundation for scripting.

## Example 
## TODO: Replace this segment with the reorganized library setup pls kthnx ;^)
```python
# example.py
### Basic preperation stuff
import json
from hamen.main import *
from hamen.noodle import *
from hamen.chroma import *
from hamen.vivify import *


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
InstantiatePrefab(8,'assets/cube.prefab','cube')

# increment run
countUp()

### Save edited json and info dat
export_infoDat()
export_diff()
```
