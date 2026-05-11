### Basic preperation stuff
from hamen.main import *
setup('ExpertStandard.dat', 'ExpertPlusStandard.dat')

# import optionals
from hamen.vivify import *


# load bundles
bundle = loadBundleInfo('bundleinfo.json')
infoDat_injectCRCs()

# infodat
infoDat_addRequirement([
    "Noodle Extensions",
    "Chroma",
    "Vivify"
])


#region ### do note scripts here
InstantiatePrefab(8, bundle['prefabs']['cube'],'cube') # example code, remove this before doing mod effects

# increment run
countUp()

### Save edited json and info dat
export_infoDat()
export_diff()