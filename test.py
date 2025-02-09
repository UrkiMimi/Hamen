### Basic preperation stuff
import json
from heckNoodle import *
from heckChroma import *
from heckVivify import *
from copy import deepcopy

'''
exFile = open("ExpertStandard.dat", "r")
exData = json.loads(exFile.read())
exFile.close()
'''
exportName = 'ExpertPlusStandard.dat'


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
diPlusFile = open(exportName, 'w')
diPlusFile.write(json.dumps(exData,indent=2))
diPlusFile.close()