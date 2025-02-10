### Main Hamen library for heck related maps.
### Use this library for heck modules
### TODO add info.dat support

import random as rand
import math
from copy import deepcopy
import json

# Map to apply scripts to
fileName = 'ExpertStandard.dat' 

# Export filename
exportName = 'ExpertPlusStandard.dat'

# unused
def export_json():
    diPlusFile = open(exportName, 'w')
    diPlusFile.write(json.dumps(exData,indent=2))
    diPlusFile.close()

# open file
exFile = open(fileName, 'r')
exData = json.loads(exFile.read())
exFile.close()
