### Noodle Extensions functions and thingies
### Refer to https://heck.aeroluna.dev/ when using this 
from hamen.main import *

# lmfao
if 'customData' in exData:
    exData['customData']['fakeColorNotes'] = []
    exData['customData']['fakeBombNotes'] = []
else:
    raise TypeError('Unable to find customData in map JSON.')

# region FUCK MATH
def noteAngleToRadians(angle):
    """Converts a note cut direction angle into radians. Useful for complex note effects

    Args:
        angle (int): Note cut direciton

    Returns:
        float: Direction (in radians)
    """
    #init
    direc = 0

    # case
    if angle == 0:
        direc = 0
    if angle == 1:
        direc = 180
    if angle == 2: 
        direc = -90
    if angle == 3: 
        direc = 90
    if angle == 4:
        direc = -45
    if angle == 5:
        direc = 45
    if angle == 6:
        direc = -135
    if angle == 7:
        direc = 135
    
    direc *= math.pi/180
    return direc

# Assigns notes to a track
def assignNotesToTrack(startTime, endTime, trackName, colorCheck=False):
    # omitting messages
    noOmit = True

    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            # if note has no customData
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            # overwriting messages
            elif ('track' in exData['colorNotes'][index]['customData']) and noOmit:
                mainTrack = exData['colorNotes'][index]['customData']['track']
                print(f'Existing track {mainTrack} in note {index}. Overwriting.')

                #omit future messages
                noOmit = False
            if colorCheck:
                if (exData['colorNotes'][index]['c'] == 0):
                    exData['colorNotes'][index]['customData']['track'] = trackName + '1'
                else:
                    exData['colorNotes'][index]['customData']['track'] = trackName + '2'
            else:
                exData['colorNotes'][index]['customData']['track'] = trackName

# Assigns notes to a track
def assignNoteDirectionToTrack(startTime, endTime, trackName):
    # omitting messages
    noOmit = True

    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            # direction
            direction = exData['colorNotes'][index]['d'] 

            # if note has no customData
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            # overwriting messages
            elif ('track' in exData['colorNotes'][index]['customData']) and noOmit:
                mainTrack = exData['colorNotes'][index]['customData']['track']
                print(f'Existing track {mainTrack} in note {index}. Overwriting.')

                #omit future messages
                noOmit = False
            else:
                exData['colorNotes'][index]['customData']['track'] = trackName + str(direction)

# Assigns notes to a track
def assignObstaclesToTrack(startTime, endTime, trackName):
    for index in range(len(exData['obstacles'])):
        if (startTime <= exData['obstacles'][index]['b']) and (endTime >= exData['obstacles'][index]['b']):
            if not('customData' in exData['obstacles'][index]):
                exData['obstacles'][index]['customData'] = {}
            exData['obstacles'][index]['customData']['track'] = trackName


# Returns an array for all notes at a specified time
def findNoteAt(nTime):
    timeList = []
    for index in range(len(exData['colorNotes'])):
        if (nTime == exData['colorNotes'][index]['b']):
            timeList.append(index)
    return(timeList)

# forces offset on specified range of notes
def forceOffset(startTime, endTime, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
    for index in range(len(exData['customData']['fakeColorNotes'])):
        if (startTime <= exData['customData']['fakeColorNotes'][index]['b']) and (endTime >= exData['customData']['fakeColorNotes'][index]['b']):
            if not('customData' in exData['customData']['fakeColorNotes'][index]):
                exData['customData']['fakeColorNotes'][index]['customData'] = {}
            exData['customData']['fakeColorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            exData['customData']['fakeColorNotes'][index]['customData']['disableNoteGravity'] = True 

# forces njs on specified range of notes
def forceNJS(startTime, endTime, jumpspeed, realNotes = False):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['noteJumpMovementSpeed'] = jumpspeed
    if not(realNotes):
        for index in range(len(exData['customData']['fakeColorNotes'])):
            if (startTime <= exData['customData']['fakeColorNotes'][index]['b']) and (endTime >= exData['customData']['fakeColorNotes'][index]['b']):
                if not('customData' in exData['customData']['fakeColorNotes'][index]):
                    exData['customData']['fakeColorNotes'][index]['customData'] = {}
                exData['customData']['fakeColorNotes'][index]['customData']['noteJumpMovementSpeed'] = jumpspeed


def spawnFakeNotesWithTrackAt(startTime, endTime, disableGravity, timeOffset, track='', disableDebris=False, uninteractable=False):
    # loop through notes
    for index in range(len(exData['colorNotes'])):

        # create fake notes at time
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            # make a complete copy of the note
            fakeLen = len(exData['customData']['fakeColorNotes']) # for indexing so python doesnt die
            exData['customData']['fakeColorNotes'].append(dict(deepcopy(exData['colorNotes'][index])))

            # offset
            exData['customData']['fakeColorNotes'][fakeLen]['b'] = exData['customData']['fakeColorNotes'][fakeLen]['b'] + timeOffset

            # customdata
            if not('customData' in exData['customData']['fakeColorNotes'][fakeLen]):
                exData['customData']['fakeColorNotes'][fakeLen]['customData'] = {}
            if not(track == ''):
                exData['customData']['fakeColorNotes'][fakeLen]['customData']['track'] = track

            # gravity and debris
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['spawnEffect'] = False

            # yep
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['disableDebris'] = disableDebris
            if disableGravity:
                exData['customData']['fakeColorNotes'][fakeLen]['customData']['disableNoteGravity'] = True
            if uninteractable:
                exData['customData']['fakeColorNotes'][fakeLen]['customData']['uninteractable'] = True


def removeGravity(startTime, endTime, fakeNotes=False):
    if fakeNotes:
        for index in range(len(exData['customData']['fakeColorNotes'])):
            if (startTime <= exData['customData']['fakeColorNotes'][index]['b']) and (endTime >= exData['customData']['fakeColorNotes'][index]['b']):
                exData['customData']['fakeColorNotes'][index]['customData']['disableNoteGravity'] = True
    else:
        for index in range(len(exData['colorNotes'])):
            if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
                if not('customData' in exData['colorNotes'][index]):
                    exData['colorNotes'][index]['customData'] = {}
                exData['colorNotes'][index]['customData']['disableNoteGravity'] = True


def assignPlayerToTrack(nTime, trackName, target=None):
    # for targets
    cData = {}
    cData['track'] = trackName

    if (target != None):
        cData['target'] = target

    
    exData['customData']['customEvents'].append(dict(b=nTime, t='AssignPlayerToTrack', d=cData))

def childrenTracks(nTime, trackName, childrens):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AssignTrackParent', d={'childrenTracks':childrens, 'parentTrack':trackName}))
    
def assignPathAnimation(nTime, trackName, duration, easings='easeLinear', pos=None, worldRotation=None, localRotation=None, scale=None, dissolve=None, dissolveArrow=None, definitePos=None, interactable=None):
    dat = {}
    # add essential stuff
    dat['track'] = trackName
    dat['duration'] = duration
    dat['easing'] = easings
    
    #if statement hell
    if (pos != None):
        dat['offsetPosition'] = pos
    if (worldRotation != None):
        dat['offsetWorldRotation'] = worldRotation
    if (localRotation != None):
        dat['localRotation'] = localRotation
    if (scale != None):
        dat['scale'] = scale
    if (dissolve != None):
        dat['dissolve'] = dissolve
    if (dissolveArrow != None):
        dat['dissolveArrow'] = dissolveArrow
    if (definitePos != None):
        dat['definitePosition'] = definitePos
    if (interactable != None):
        dat['interactable'] = interactable

    
    exData['customData']['customEvents'].append(dict(b=nTime, t='AssignPathAnimation', d=dat))


def assignNoteLaneToTrack(startTime, endTime, trackName, lane):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']) and (exData['colorNotes'][index]['x'] == lane):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['track'] = trackName

def assignNoteColumnToTrack(startTime, endTime, trackName, column):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']) and (exData['colorNotes'][index]['y'] == column):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['track'] = trackName


def wipeCustomNoteData(startTime, endTime, fakeNotes = False):
    """Wipes customData from a note. Somewhat dangerous

    Args:
        startTime (_type_): Start time (in beats)
        endTime (_type_): End time (in beats)
    """
    for index in range(len(exData['colorNotes'])):
        if (exData['colorNotes'][index]['b'] >= startTime) and (exData['colorNotes'][index]['b'] <= endTime):
            if ('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index].pop('customData')

    # fake notes
    for index in range(len(exData['customData']['fakeColorNotes'])):
        if (exData['customData']['fakeColorNotes'][index]['b'] >= startTime) and (exData['customData']['fakeColorNotes'][index]['b'] <= endTime):
            if ('customData' in exData['customData']['fakeColorNotes'][index]):
                exData['customData']['fakeColorNotes'][index].pop('customData')


def animateTrack(nTime, trackName, duration, easings='easeLinear', pos=None, worldRotation=None, localRotation=None, scale=None, dissolve=None, dissolveArrow=None, interactable=None, time=None):
    dat = {}
    # add essential stuff
    dat['track'] = trackName
    dat['duration'] = duration
    dat['easing'] = easings
    
    #if statement hell
    if (pos != None):
        dat['offsetPosition'] = pos
    if (worldRotation != None):
        dat['offsetWorldRotation'] = worldRotation
    if (localRotation != None):
        dat['localRotation'] = localRotation
    if (scale != None):
        dat['scale'] = scale
    if (dissolve != None):
        dat['dissolve'] = dissolve
    if (dissolveArrow != None):
        dat['dissolveArrow'] = dissolveArrow
    if (interactable != None):
        dat['interactable'] = interactable
    if (time != None):
        dat['time'] = time

    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d=dat))


# hijacks a note to add custom data
def forceCustomData(startTime, endTime, customData):
    """Forces a custom data on a note. Somewhat dangerous

    Args:
        startTime (float): Start time (in beats)
        endTime (float): End time (in beats)
        customData (dict): Custom JSON Data
    """

    for index in range(len(exData['colorNotes'])):
        if (exData['colorNotes'][index]['b'] >= startTime) and (exData['colorNotes'][index]['b'] <= endTime):
            exData['colorNotes'][index]['customData'] = customData

# adds to an existing custom data dict
def appendCustomData(startTime, endTime, customData):
    """Appends custom data to notes. Will create a customData key if none exists.

    Args:
        startTime (float): Start time (in beats)
        endTime (float): End time (in beats)
        customData (dict): Custom JSON Data
    """

    for index in range(len(exData['colorNotes'])):
        if (exData['colorNotes'][index]['b'] >= startTime) and (exData['colorNotes'][index]['b'] <= endTime):
            if ('customData' in exData['colorNotes'][index]):
                # make an absolute clone of custom data and append
                cData = deepcopy(exData['colorNotes'][index]['customData'])
                cData |= customData

                exData['colorNotes'][index]['customData'] = cData
            else:
                exData['colorNotes'][index]['customData'] = customData

