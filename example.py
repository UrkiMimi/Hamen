### Basic preperation stuff
import json
from hamenNoodle import *
from hamenChroma import *
from hamenVivify import *
from copy import deepcopy

# requirement shit
infoDat_addRequirement([
    "Noodle Extensions",
    "Chroma",
    "Vivify"
])
infoDat_addSuggestion([])
infoDat_removeBaseMap()

# Add arrays
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}
exData['customData']['environment'] = []

#region ### do note scripts here

#scale notes across X axis
assignNotesToTrack(1,8,'notes')
scaleTween(4,'notes',2,'easeOutQuad',[1,1,1,0],[2,1,1,1])


### Save json to Ex+ file
export_infoDat()
export_diff()