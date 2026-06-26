# ![Hamen](https://raw.githubusercontent.com/UrkiMimi/Hamen/refs/heads/main/resources/HamenBanner.png)

## Overview
A Python framework to aid in creation of Beat Saber modcharts. This has support for Heck libaries Noodle, Chroma, and Vivify.

## Usage
Edit the `fileName` and `exportName` variables in `Hamen.py` depending on what file you're injecting functions into. Use the provided `example.py` file as a foundation for scripting.

## Example 
## TODO: Replace this segment with the reorganized library setup pls kthnx ;^)
```python
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
```
