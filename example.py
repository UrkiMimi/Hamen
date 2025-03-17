### Basic preperation stuff
import json
from Hamen import *
from hamenNoodle import *
from hamenChroma import *
from hamenVivify import *
from copy import deepcopy


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