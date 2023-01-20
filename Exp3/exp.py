#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 8月 26, 2022, at 17:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'exp'  # from the Builder filename that created this script
expInfo = {'name': '', 'participant': '001', 'date': '2022/', 'sex': 'female/male/I don`t want to talk about it', 'age': '', 'dominant hand': 'right / left / both', 'tempareature': '℃', 'disinfection': 'done / not yet', 'note': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\AjustSize\\exp.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "inst"
instClock = core.Clock()
win.mouseVisible = False
text = visual.TextStim(win=win, name='text',
    text='Practice\n\nadjust same size using mouse\npress space',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color=[0, 0, 0], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "pra"
praClock = core.Clock()
win.mouseVisible = False
import random
import numpy as np
import math
blank_pra = visual.TextStim(win=win, name='blank_pra',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fix_pra = visual.ShapeStim(
    win=win, name='fix_pra', vertices='cross',units='deg', 
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-2.0, interpolate=True)
stanTriangle_pra = visual.ShapeStim(
    win=win, name='stanTriangle_pra',units='deg', 
    size=[1.0, 1.0], vertices='triangle',
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-3.0, interpolate=True)
stanSquare_pra = visual.Rect(
    win=win, name='stanSquare_pra',units='deg', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-4.0, interpolate=True)
stanCir_pra = visual.ShapeStim(
    win=win, name='stanCir_pra', vertices=40,units='deg', 
    size=[1.0, 1.0],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-5.0, interpolate=True)
fix_pra2 = visual.ShapeStim(
    win=win, name='fix_pra2', vertices='cross',units='deg', 
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-6.0, interpolate=True)
AjustSquare_pra = visual.Rect(
    win=win, name='AjustSquare_pra',units='deg', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-7.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "main"
mainClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='main\n\nadjust same size using mouse\npress space',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color=[0,0,0], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
win.mouseVisible = False
import random
import numpy as np
import math
from PIL import Image
import matplotlib as plt
import matplotlib.pyplot

trialCounter = 0
nRestTrial = 20
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fix_main = visual.ShapeStim(
    win=win, name='fix_main',units='deg', 
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-2.0, interpolate=True)
stanTriangle_main = visual.ShapeStim(
    win=win, name='stanTriangle_main',units='deg', 
    size=[1.0, 1.0], vertices='triangle',
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-3.0, interpolate=True)
stanSquare_main = visual.Rect(
    win=win, name='stanSquare_main',units='deg', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-4.0, interpolate=True)
stanCircle_main = visual.ShapeStim(
    win=win, name='stanCircle_main',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-5.0, interpolate=True)
fix_main2 = visual.ShapeStim(
    win=win, name='fix_main2',units='deg', 
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-6.0, interpolate=True)
AjustSquare_main = visual.Rect(
    win=win, name='AjustSquare_main',units='deg', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=None,
    opacity=None, depth=-7.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text=None,
    font='Open Sans',
    units='norm', pos=(0.5, 0.5), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='rest !\nPress space',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color=[0,0,0], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Thank you !',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color=[0,0,0], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "inst"-------
continueRoutine = True
# update component parameters for each repeat
win.mouseVisible = False
corner = 4
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instComponents = [text, key_resp_2]
for thisComponent in instComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst"-------
while continueRoutine:
    # get current time
    t = instClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    win.mouseVisible = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst"-------
for thisComponent in instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "inst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pra.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pra"-------
    continueRoutine = True
    # update component parameters for each repeat
    intervalBlank = random.uniform(0.5, 0.8)
    win.mouseVisible = False
    
    jit = round(random.uniform(-0.5, 0.5), 2)
    prove = mouse.setPos(newPos=(dev+jit, dev+jit))
    
    if geo == "uptriangle" or geo =="downtriangle":
        xtri = round(random.uniform(1, 5), 2)
        ytri = round(random.uniform(1, 5), 2)
        xsq = 0
        ysq = 0
        xcir = 0
        ycir = 0
        
    if geo == "square":
        xtri = 0
        ytri = 0
        xsq = round(random.uniform(1, 5), 2)
        ysq = round(random.uniform(1, 5), 2)
        xcir = 0
        ycir = 0
        
    if geo == "circle":
        xtri = 0
        ytri = 0
        xsq = 0
        ysq = 0
        xcir = round(random.uniform(1, 5), 2)
        ycir = round(random.uniform(1, 5), 2)
    stanTriangle_pra.setSize((xtri, ytri))
    stanTriangle_pra.setOri(ori)
    stanSquare_pra.setSize((xsq, ysq))
    stanCir_pra.setSize((xcir, ycir))
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    praComponents = [blank_pra, fix_pra, stanTriangle_pra, stanSquare_pra, stanCir_pra, fix_pra2, AjustSquare_pra, mouse]
    for thisComponent in praComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    praClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pra"-------
    while continueRoutine:
        # get current time
        t = praClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=praClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        prove = mouse.getPos()
        x, y = mouse.getPos()
        
        if x < 0:
            prove[0] = 0
        
        if y < 0:
            prove[1] = 0
        
        if y > 0 and x < 0:
            prove[1] = 0
        
        if y < 0 and x > 0:
            prove[0] = 0
        
        # *blank_pra* updates
        if blank_pra.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_pra.frameNStart = frameN  # exact frame index
            blank_pra.tStart = t  # local t and not account for scr refresh
            blank_pra.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_pra, 'tStartRefresh')  # time at next scr refresh
            blank_pra.setAutoDraw(True)
        if blank_pra.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_pra.tStartRefresh + intervalBlank-frameTolerance:
                # keep track of stop time/frame for later
                blank_pra.tStop = t  # not accounting for scr refresh
                blank_pra.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_pra, 'tStopRefresh')  # time at next scr refresh
                blank_pra.setAutoDraw(False)
        
        # *fix_pra* updates
        if fix_pra.status == NOT_STARTED and tThisFlip >= intervalBlank-frameTolerance:
            # keep track of start time/frame for later
            fix_pra.frameNStart = frameN  # exact frame index
            fix_pra.tStart = t  # local t and not account for scr refresh
            fix_pra.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_pra, 'tStartRefresh')  # time at next scr refresh
            fix_pra.setAutoDraw(True)
        if fix_pra.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_pra.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                fix_pra.tStop = t  # not accounting for scr refresh
                fix_pra.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_pra, 'tStopRefresh')  # time at next scr refresh
                fix_pra.setAutoDraw(False)
        
        # *stanTriangle_pra* updates
        if stanTriangle_pra.status == NOT_STARTED and tThisFlip >= intervalBlank+0.25-frameTolerance:
            # keep track of start time/frame for later
            stanTriangle_pra.frameNStart = frameN  # exact frame index
            stanTriangle_pra.tStart = t  # local t and not account for scr refresh
            stanTriangle_pra.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stanTriangle_pra, 'tStartRefresh')  # time at next scr refresh
            stanTriangle_pra.setAutoDraw(True)
        
        # *stanSquare_pra* updates
        if stanSquare_pra.status == NOT_STARTED and tThisFlip >= intervalBlank+0.25-frameTolerance:
            # keep track of start time/frame for later
            stanSquare_pra.frameNStart = frameN  # exact frame index
            stanSquare_pra.tStart = t  # local t and not account for scr refresh
            stanSquare_pra.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stanSquare_pra, 'tStartRefresh')  # time at next scr refresh
            stanSquare_pra.setAutoDraw(True)
        
        # *stanCir_pra* updates
        if stanCir_pra.status == NOT_STARTED and tThisFlip >= intervalBlank+0.25-frameTolerance:
            # keep track of start time/frame for later
            stanCir_pra.frameNStart = frameN  # exact frame index
            stanCir_pra.tStart = t  # local t and not account for scr refresh
            stanCir_pra.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stanCir_pra, 'tStartRefresh')  # time at next scr refresh
            stanCir_pra.setAutoDraw(True)
        
        # *fix_pra2* updates
        if fix_pra2.status == NOT_STARTED and tThisFlip >= intervalBlank+0.5-frameTolerance:
            # keep track of start time/frame for later
            fix_pra2.frameNStart = frameN  # exact frame index
            fix_pra2.tStart = t  # local t and not account for scr refresh
            fix_pra2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_pra2, 'tStartRefresh')  # time at next scr refresh
            fix_pra2.setAutoDraw(True)
        
        # *AjustSquare_pra* updates
        if AjustSquare_pra.status == NOT_STARTED and tThisFlip >= intervalBlank+0.5-frameTolerance:
            # keep track of start time/frame for later
            AjustSquare_pra.frameNStart = frameN  # exact frame index
            AjustSquare_pra.tStart = t  # local t and not account for scr refresh
            AjustSquare_pra.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AjustSquare_pra, 'tStartRefresh')  # time at next scr refresh
            AjustSquare_pra.setAutoDraw(True)
        if AjustSquare_pra.status == STARTED:  # only update if drawing
            AjustSquare_pra.setSize(prove, log=False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= intervalBlank+1-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in praComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra"-------
    for thisComponent in praComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prove = mouse.getPos()
    x, y = mouse.getPos()
    
    estArea = x * y
    estArea = estArea/2
    thisExp.addData("estArea", estArea)
    
    if geo == "uptriangle" or "downtriangle":
        diffx_tri = abs(x) - xtri
        thisExp.addData("diffx_tri", diffx_tri)
        ratiox_tri = abs(x) / xtri
        thisExp.addData("ratiox_tri", ratiox_tri)
        diffy_tri = abs(y) - ytri
        thisExp.addData("diffy_tri", diffy_tri)
        ratioy_tri = abs(y) / ytri
        thisExp.addData("ratioy_tri", ratioy_tri)
        diffarea_tri = diffx_tri * diffy_tri/2
        thisExp.addData("diffarea_tri", diffarea_tri)
    
    if geo == "square":
        diffx_sq = abs(x) - xsq
        thisExp.addData("diffx_sq", diffx_sq)
        ratiox_sq = abs(x) / xsq
        thisExp.addData("ratiox_sq", ratiox_sq)
        diffy_sq = abs(y) - ysq
        thisExp.addData("diffy_sq", diffy_sq)
        ratioy_sq = abs(y) / ysq
        thisExp.addData("ratioy_sq", ratioy_sq)
        diffarea_sq = diffx_sq * diffy_sq/2
        thisExp.addData("diffarea_sq", diffarea_sq)
        
    if geo == "circle":
        diffx_cir = abs(x) - xcir
        thisExp.addData("diffx_cir", diffx_cir)
        ratiox_cir = abs(x) / xcir
        thisExp.addData("ratiox_cir", ratiox_cir)
        diffy_cir = abs(y) - ycir
        thisExp.addData("diffy_cir", diffy_cir)
        ratioy_cir = abs(y) / ycir
        thisExp.addData("ratioy_cir", ratioy_cir)
        diffarea_cir = diffx_cir * diffy_cir/2
        thisExp.addData("diffarea_cir", diffarea_cir)
    trials.addData('blank_pra.started', blank_pra.tStartRefresh)
    trials.addData('blank_pra.stopped', blank_pra.tStopRefresh)
    trials.addData('fix_pra.started', fix_pra.tStartRefresh)
    trials.addData('fix_pra.stopped', fix_pra.tStopRefresh)
    trials.addData('stanTriangle_pra.started', stanTriangle_pra.tStartRefresh)
    trials.addData('stanTriangle_pra.stopped', stanTriangle_pra.tStopRefresh)
    trials.addData('stanSquare_pra.started', stanSquare_pra.tStartRefresh)
    trials.addData('stanSquare_pra.stopped', stanSquare_pra.tStopRefresh)
    trials.addData('stanCir_pra.started', stanCir_pra.tStartRefresh)
    trials.addData('stanCir_pra.stopped', stanCir_pra.tStopRefresh)
    trials.addData('fix_pra2.started', fix_pra2.tStartRefresh)
    trials.addData('fix_pra2.stopped', fix_pra2.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    trials.addData('mouse.x', x)
    trials.addData('mouse.y', y)
    trials.addData('mouse.leftButton', buttons[0])
    trials.addData('mouse.midButton', buttons[1])
    trials.addData('mouse.rightButton', buttons[2])
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    # the Routine "pra" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'trials'


# ------Prepare to start Routine "main"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
mainComponents = [text_2, key_resp]
for thisComponent in mainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "main"-------
while continueRoutine:
    # get current time
    t = mainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=mainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "main"-------
for thisComponent in mainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "main" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main.csv'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    intervalBlank = random.uniform(0.5, 0.8)
    win.mouseVisible = False
    
    jit = round(random.uniform(-0.5, 0.5), 2)
    prove = mouse.setPos(newPos=(dev+jit, dev+jit))
    
    if stim == "stan" and geo == "uptriangle":
        xtri = size
        ytri = size
        xsq = 0
        ysq = 0
        xcir = 0
        ycir = 0
    
    if stim == "stan" and geo =="downtriangle":
        xtri = size
        ytri = size
        xsq = 0
        ysq = 0
        xcir = 0
        ycir = 0
    
    if stim == "filer" and geo == "uptriangle":
        xtri = round(random.uniform(1, 5), 2)
        ytri = round(random.uniform(1, 5), 2)
        xsq = 0
        ysq = 0
        xcir = 0
        ycir = 0
        
    if stim == "filer" and geo =="downtriangle":
        xtri = round(random.uniform(1, 5), 2)
        ytri = round(random.uniform(1, 5), 2)
        xsq = 0
        ysq = 0
        xcir = 0
        ycir = 0
        
    if geo == "square":
        xtri = 0
        ytri = 0
        xsq = round(random.uniform(1, 5), 2)
        ysq = round(random.uniform(1, 5), 2)
        xcir = 0
        ycir = 0
        
    if geo == "circle":
        xtri = 0
        ytri = 0
        xsq = 0
        ysq = 0
        xcir = round(random.uniform(1, 5), 2)
        ycir = round(random.uniform(1, 5), 2)
    
    img = np.random.randint(0, 255, (9, 16))
    I = np.dstack([img, img, img])
    I=I.astype(np.uint8)
    im = plt.image.imsave('name.jpg', I)
    
    trialCounter = trialCounter + 1
    if trialCounter % nRestTrial == 0:
        isRest = 1
    else:
        isRest = 0
    stanTriangle_main.setSize((xtri, ytri))
    stanTriangle_main.setOri(ori)
    stanSquare_main.setSize((xsq, ysq))
    stanCircle_main.setSize((xcir, ycir))
    # setup some python lists for storing info about the mouse_2
    gotValidClick = False  # until a click is received
    text_9.setText('')
    image.setImage(im)
    # keep track of which components have finished
    trialComponents = [text_3, fix_main, stanTriangle_main, stanSquare_main, stanCircle_main, fix_main2, AjustSquare_main, mouse_2, text_9, image]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        prove = mouse.getPos()
        x, y = mouse.getPos()
        
        if x < 0:
            prove[0] = 0
        
        if y < 0:
            prove[1] = 0
        
        if y > 0 and x < 0:
            prove[1] = 0
        
        if y < 0 and x > 0:
            prove[0] = 0
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + intervalBlank-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *fix_main* updates
        if fix_main.status == NOT_STARTED and tThisFlip >= intervalBlank-frameTolerance:
            # keep track of start time/frame for later
            fix_main.frameNStart = frameN  # exact frame index
            fix_main.tStart = t  # local t and not account for scr refresh
            fix_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_main, 'tStartRefresh')  # time at next scr refresh
            fix_main.setAutoDraw(True)
        
        # *stanTriangle_main* updates
        if stanTriangle_main.status == NOT_STARTED and tThisFlip >= intervalBlank+0.25-frameTolerance:
            # keep track of start time/frame for later
            stanTriangle_main.frameNStart = frameN  # exact frame index
            stanTriangle_main.tStart = t  # local t and not account for scr refresh
            stanTriangle_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stanTriangle_main, 'tStartRefresh')  # time at next scr refresh
            stanTriangle_main.setAutoDraw(True)
        if stanTriangle_main.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stanTriangle_main.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                stanTriangle_main.tStop = t  # not accounting for scr refresh
                stanTriangle_main.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stanTriangle_main, 'tStopRefresh')  # time at next scr refresh
                stanTriangle_main.setAutoDraw(False)
        
        # *stanSquare_main* updates
        if stanSquare_main.status == NOT_STARTED and tThisFlip >= intervalBlank+0.25-frameTolerance:
            # keep track of start time/frame for later
            stanSquare_main.frameNStart = frameN  # exact frame index
            stanSquare_main.tStart = t  # local t and not account for scr refresh
            stanSquare_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stanSquare_main, 'tStartRefresh')  # time at next scr refresh
            stanSquare_main.setAutoDraw(True)
        if stanSquare_main.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stanSquare_main.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                stanSquare_main.tStop = t  # not accounting for scr refresh
                stanSquare_main.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stanSquare_main, 'tStopRefresh')  # time at next scr refresh
                stanSquare_main.setAutoDraw(False)
        
        # *stanCircle_main* updates
        if stanCircle_main.status == NOT_STARTED and tThisFlip >= intervalBlank+0.25-frameTolerance:
            # keep track of start time/frame for later
            stanCircle_main.frameNStart = frameN  # exact frame index
            stanCircle_main.tStart = t  # local t and not account for scr refresh
            stanCircle_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stanCircle_main, 'tStartRefresh')  # time at next scr refresh
            stanCircle_main.setAutoDraw(True)
        if stanCircle_main.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stanCircle_main.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                stanCircle_main.tStop = t  # not accounting for scr refresh
                stanCircle_main.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stanCircle_main, 'tStopRefresh')  # time at next scr refresh
                stanCircle_main.setAutoDraw(False)
        
        # *fix_main2* updates
        if fix_main2.status == NOT_STARTED and tThisFlip >= intervalBlank+0.7-frameTolerance:
            # keep track of start time/frame for later
            fix_main2.frameNStart = frameN  # exact frame index
            fix_main2.tStart = t  # local t and not account for scr refresh
            fix_main2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_main2, 'tStartRefresh')  # time at next scr refresh
            fix_main2.setAutoDraw(True)
        if fix_main2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_main2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix_main2.tStop = t  # not accounting for scr refresh
                fix_main2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_main2, 'tStopRefresh')  # time at next scr refresh
                fix_main2.setAutoDraw(False)
        
        # *AjustSquare_main* updates
        if AjustSquare_main.status == NOT_STARTED and tThisFlip >= intervalBlank+0.7-frameTolerance:
            # keep track of start time/frame for later
            AjustSquare_main.frameNStart = frameN  # exact frame index
            AjustSquare_main.tStart = t  # local t and not account for scr refresh
            AjustSquare_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AjustSquare_main, 'tStartRefresh')  # time at next scr refresh
            AjustSquare_main.setAutoDraw(True)
        if AjustSquare_main.status == STARTED:  # only update if drawing
            AjustSquare_main.setSize(prove, log=False)
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= intervalBlank+0.7-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prove = mouse.getPos()
    x, y = mouse.getPos()
    
    estArea = x * y
    estArea = estArea/2
    thisExp.addData("estArea", estArea)
    
    if geo == "uptriangle" or geo =="downtriangle":
        diffx_tri = abs(x) - xtri
        thisExp.addData("diffx_tri", diffx_tri)
        ratiox_tri = abs(x) / xtri
        thisExp.addData("ratiox_tri", ratiox_tri)
        diffy_tri = abs(y) - ytri
        thisExp.addData("diffy_tri", diffy_tri)
        ratioy_tri = abs(y) / ytri
        thisExp.addData("ratioy_tri", ratioy_tri)
        diffarea_tri = diffx_tri * diffy_tri/2
        thisExp.addData("diffarea_tri", diffarea_tri)
    
    if geo == "square":
        diffx_sq = abs(x) - xsq
        thisExp.addData("diffx_sq", diffx_sq)
        ratiox_sq = abs(x) / xsq
        thisExp.addData("ratiox_sq", ratiox_sq)
        diffy_sq = abs(y) - ysq
        thisExp.addData("diffy_sq", diffy_sq)
        ratioy_sq = abs(y) / ysq
        thisExp.addData("ratioy_sq", ratioy_sq)
        diffarea_sq = diffx_sq * diffy_sq/2
        thisExp.addData("diffarea_sq", diffarea_sq)
        
    if geo == "circle":
        diffx_cir = abs(x) - xcir
        thisExp.addData("diffx_cir", diffx_cir)
        ratiox_cir = abs(x) / xcir
        thisExp.addData("ratiox_cir", ratiox_cir)
        diffy_cir = abs(y) - ycir
        thisExp.addData("diffy_cir", diffy_cir)
        ratioy_cir = abs(y) / ycir
        thisExp.addData("ratioy_cir", ratioy_cir)
        diffarea_cir = diffx_cir * diffy_cir/2
        thisExp.addData("diffarea_cir", diffarea_cir)
    trials_3.addData('text_3.started', text_3.tStartRefresh)
    trials_3.addData('text_3.stopped', text_3.tStopRefresh)
    trials_3.addData('stanTriangle_main.started', stanTriangle_main.tStartRefresh)
    trials_3.addData('stanTriangle_main.stopped', stanTriangle_main.tStopRefresh)
    trials_3.addData('stanSquare_main.started', stanSquare_main.tStartRefresh)
    trials_3.addData('stanSquare_main.stopped', stanSquare_main.tStopRefresh)
    trials_3.addData('stanCircle_main.started', stanCircle_main.tStartRefresh)
    trials_3.addData('stanCircle_main.stopped', stanCircle_main.tStopRefresh)
    trials_3.addData('fix_main2.started', fix_main2.tStartRefresh)
    trials_3.addData('fix_main2.stopped', fix_main2.tStopRefresh)
    trials_3.addData('AjustSquare_main.started', AjustSquare_main.tStartRefresh)
    trials_3.addData('AjustSquare_main.stopped', AjustSquare_main.tStopRefresh)
    # store data for trials_3 (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    trials_3.addData('mouse_2.x', x)
    trials_3.addData('mouse_2.y', y)
    trials_3.addData('mouse_2.leftButton', buttons[0])
    trials_3.addData('mouse_2.midButton', buttons[1])
    trials_3.addData('mouse_2.rightButton', buttons[2])
    trials_3.addData('mouse_2.started', mouse_2.tStart)
    trials_3.addData('mouse_2.stopped', mouse_2.tStop)
    trials_3.addData('text_9.started', text_9.tStartRefresh)
    trials_3.addData('text_9.stopped', text_9.tStopRefresh)
    trials_3.addData('image.started', image.tStartRefresh)
    trials_3.addData('image.stopped', image.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=isRest, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rest"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        restComponents = [text_4, key_resp_3]
        for thisComponent in restComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rest"-------
        while continueRoutine:
            # get current time
            t = restClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=restClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in restComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rest"-------
        for thisComponent in restComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('text_4.started', text_4.tStartRefresh)
        trials_2.addData('text_4.stopped', text_4.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials_2.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials_2.addData('key_resp_3.rt', key_resp_3.rt)
        trials_2.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        trials_2.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        # the Routine "rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed isRest repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
endComponents = [text_5, key_resp_4]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
