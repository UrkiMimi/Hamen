### Main Hamen library for heck related maps.
### Use this library for heck modules
### TODO add info.dat support

import random as rand
import math
from copy import deepcopy
import json, os

# initial stuffs
infDat = {}

# Map to apply scripts to
fileName = 'ExpertStandard.dat' 

# Export filename
exportName = 'ExpertPlusStandard.dat'

# version constant and stuff
VERSION = 'v0.2.4'
PRODID = 'Hamen <3'

# open files
exFile = open(fileName, 'r')
exData = json.loads(exFile.read())
exFile.close()

infFile = open('Info.dat', 'r')
infDat = json.loads(infFile.read())
infFile.close()

# required arrays
exData['customData'] = {}
exData['customData']['customEvents'] = []



#region functions
# for final exporting
def export_diff():
    """Exports map
    """

    ## data cleanup 
    # sort basic beatmap events
    for basic in ['colorNotes', 'basicBeatmapEvents', 'bombNotes', 'obstacles', 'burstSliders']:
        exData[basic].sort(key=beat)

    # sort custom events
    for adv in ['fakeColorNotes', 'fakeBombNotes', 'customEvents', 'fakeBurstSliders', 'fakeObstacles']:
        if adv in exData['customData']:
            exData['customData'][adv].sort(key=beat)


    # remove old backup
    if os.path.exists(exportName + '.bak'):
        os.remove(exportName + '.bak')
        
    
    # rename old diff file incase accidental overwrites
    os.rename(exportName, exportName + '.bak')

    diPlusFile = open(exportName, 'w')
    diPlusFile.write(json.dumps(exData,indent=2))
    diPlusFile.close()

#region info.dat part

def export_infoDat():
    """Exports info.dat and backs it up
    """
    # remove old backup
    if os.path.exists('Info.dat.bak'):
        os.remove('Info.dat.bak')

    # rename old info.dat
    os.rename('Info.dat', 'Info.dat.bak')

    # export info
    infFile = open('Info.dat', 'w')
    infFile.write(json.dumps(infDat,indent=2))
    infFile.close()

# inject requirements
def infoDat_addRequirement(requirement):
    """Adds a mod requirement to exported difficulty

    Args:
        requirement (string[]): Map requirements
    """
    indexes = []
    # find correct diff
    for index in range(len(infDat['_difficultyBeatmapSets'])):
        for index2 in range(len(infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'])):
            if infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]['_beatmapFilename'] == exportName:
                indexes = [index, index2]

    # customData check
    if not('_customData' in infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]):
        infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData'] = {}
    
    # set requirements to array argument
    # blank out requirements if empty
    if requirement == []:
        if ('_requirements' in infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]):
            infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData'].pop('_requirements')
    else:
        infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData']['_requirements'] = requirement
    
# inject requirements
def infoDat_addSuggestion(suggestion):
    """Adds a mod suggestion to exported difficulty

    Args:
        suggestion (string[]): Map suggestions
    """
    indexes = []
    # find correct diff
    for index in range(len(infDat['_difficultyBeatmapSets'])):
        for index2 in range(len(infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'])):
            if infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]['_beatmapFilename'] == exportName:
                indexes = [index, index2]

    # customData check
    if not('_customData' in infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]):
        infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData'] = {}
    
    # set requirements to array argument
    # blank out suggestions if empty
    if suggestion == []:
        if ('_suggestions' in infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]):
            infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData'].pop('_suggestions')
    else:
        infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData']['_suggestion'] = suggestion

def infoDat_removeBaseMap():
    """Removes base map from Info.dat
    Use this if you've finished mapping your base difficulty!
    """
    indexes = []
    # find correct diff
    for index in range(len(infDat['_difficultyBeatmapSets'])):
        for index2 in range(len(infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'])):
            if infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]['_beatmapFilename'] == fileName:
                indexes = [index, index2]
    
    #pops base map
    infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'].pop(indexes[1])

def countUp():
    """So I don't lose my sanity
    Add this at the end of a modfile
    """
    # make new counter if it doesnt exist
    if not(os.path.exists('count.txt')):
        with open('count.txt', 'w') as f:
            f.write('0')
            f.close()
    
    # get number from counter
    with open('count.txt', 'r') as f:
        counter = int(f.read())
        f.close()

    # count up
    counter += 1
    print(f'GIVE IT UP FOR RUN {counter}!!!!')

    # save result
    with open('count.txt', 'w') as f:
        f.write(str(counter))
        f.close()

def infoDat_settingsSetter(player = None, modifiers = None, chroma = None, cPlus = None, uiTweaks = None, nTweaks = None, graphics = None):
    # cjd
    dat = {}
    
    if player != None:
        dat['_playerOptions'] = player
    if modifiers != None:
        dat['_modifiers'] = modifiers
    if chroma != None:
        dat['_chroma'] = chroma
    if cPlus != None:
        dat['_countersPlus'] = cPlus
    if uiTweaks != None:
        dat['_uiTweaks'] = uiTweaks
    if nTweaks != None:
        dat['_noteTweaks'] = nTweaks
    if graphics != None:
        dat['_graphics'] = graphics


    indexes = []
    # find export diff
    for index in range(len(infDat['_difficultyBeatmapSets'])):
        for index2 in range(len(infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'])):
            if infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]['_beatmapFilename'] == exportName:
                indexes = [index, index2]

    if not('_customData' in infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]):
        infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData'] = {}
    
    # generate settings
    infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData']['_settings'] = dat

# last edited by thing
def infoDat_setEditedVersion():
    infDat['_customData']['_editors'][PRODID] = {}
    infDat['_customData']['_editors'][PRODID]['version'] = VERSION
    infDat['_customData']['_editors']['_lastEditedBy'] = PRODID

# this is for file saving so please dont remove this (even though it looks stupid)
def beat(e):
    return e['b']