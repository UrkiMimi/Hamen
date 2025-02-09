# Reck (Ramen + Heck)
### Someone please give me a better name for this

These scripts help make Beat Saber maps that take advantage of the Heck mod. Chroma and Noodle are mostly supported with primitive Vivify support (untested)



## Usage
Change the `fileName` variable in `heckNoodle.py` to the diff name you're editing. Then edit the `exportName` variable to the diff name you're exporting it to. Lastly, import these scripts like you would with any other library. You must have them in the same folder as your `.py` file. 

## Example
```python
### example.py
import json
from heckNoodle import *
from heckChroma import *
from heckVivify import *

exportName = 'ExpertPlusStandard.dat' #file export name

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
```
