#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 11月 08, 2021, at 18:59
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
expName = 'circleMove'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\mnaga\\Desktop\\circleMove_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
win.mouseVisible = False
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp = keyboard.Keyboard()
inverse = visual.Rect(
    win=win, name='inverse',units='deg', 
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
top = visual.Rect(
    win=win, name='top',units='deg', 
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 10),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
bottom = visual.Rect(
    win=win, name='bottom',units='deg', 
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, -10),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
right = visual.Rect(
    win=win, name='right',units='deg', 
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(10, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
left = visual.Rect(
    win=win, name='left',units='deg', 
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(-10, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
resp.keys = []
resp.rt = []
_resp_allKeys = []
# keep track of which components have finished
trialComponents = [fix, resp, inverse, top, bottom, right, left]
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
    radius = 5 # deg
    radius_top = 10 # deg
    radius_bottom = 12 # deg
    radius_right = 13 # deg
    radius_left = 14 # deg
    
    angle_deg_sec = 100# deg/sec
    current_deg = angle_deg_sec * t
    
    inverse.pos = (radius * cos(deg2rad(current_deg)), radius * sin(deg2rad(current_deg)))
    top.pos = (radius_top * cos(deg2rad(current_deg)), radius_top * sin(deg2rad(current_deg)))
    bottom.pos = (radius_bottom * cos(deg2rad(current_deg)), radius_bottom * sin(deg2rad(current_deg)))
    right.pos = (radius_right * cos(deg2rad(current_deg)), radius_right * sin(deg2rad(current_deg)))
    left.pos = (radius_left * cos(deg2rad(current_deg)), radius_left * sin(deg2rad(current_deg)))
    
    # *fix* updates
    if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix.frameNStart = frameN  # exact frame index
        fix.tStart = t  # local t and not account for scr refresh
        fix.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
        fix.setAutoDraw(True)
    
    # *resp* updates
    waitOnFlip = False
    if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp.frameNStart = frameN  # exact frame index
        resp.tStart = t  # local t and not account for scr refresh
        resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
        resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp.status == STARTED and not waitOnFlip:
        theseKeys = resp.getKeys(keyList=['space'], waitRelease=False)
        _resp_allKeys.extend(theseKeys)
        if len(_resp_allKeys):
            resp.keys = _resp_allKeys[-1].name  # just the last key pressed
            resp.rt = _resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *inverse* updates
    if inverse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inverse.frameNStart = frameN  # exact frame index
        inverse.tStart = t  # local t and not account for scr refresh
        inverse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inverse, 'tStartRefresh')  # time at next scr refresh
        inverse.setAutoDraw(True)
    
    # *top* updates
    if top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top.frameNStart = frameN  # exact frame index
        top.tStart = t  # local t and not account for scr refresh
        top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top, 'tStartRefresh')  # time at next scr refresh
        top.setAutoDraw(True)
    
    # *bottom* updates
    if bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bottom.frameNStart = frameN  # exact frame index
        bottom.tStart = t  # local t and not account for scr refresh
        bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bottom, 'tStartRefresh')  # time at next scr refresh
        bottom.setAutoDraw(True)
    
    # *right* updates
    if right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right.frameNStart = frameN  # exact frame index
        right.tStart = t  # local t and not account for scr refresh
        right.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right, 'tStartRefresh')  # time at next scr refresh
        right.setAutoDraw(True)
    
    # *left* updates
    if left.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        left.frameNStart = frameN  # exact frame index
        left.tStart = t  # local t and not account for scr refresh
        left.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left, 'tStartRefresh')  # time at next scr refresh
        left.setAutoDraw(True)
    
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
thisExp.addData('fix.started', fix.tStartRefresh)
thisExp.addData('fix.stopped', fix.tStopRefresh)
# check responses
if resp.keys in ['', [], None]:  # No response was made
    resp.keys = None
thisExp.addData('resp.keys',resp.keys)
if resp.keys != None:  # we had a response
    thisExp.addData('resp.rt', resp.rt)
thisExp.addData('resp.started', resp.tStartRefresh)
thisExp.addData('resp.stopped', resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('inverse.started', inverse.tStartRefresh)
thisExp.addData('inverse.stopped', inverse.tStopRefresh)
thisExp.addData('top.started', top.tStartRefresh)
thisExp.addData('top.stopped', top.tStopRefresh)
thisExp.addData('bottom.started', bottom.tStartRefresh)
thisExp.addData('bottom.stopped', bottom.tStopRefresh)
thisExp.addData('right.started', right.tStartRefresh)
thisExp.addData('right.stopped', right.tStopRefresh)
thisExp.addData('left.started', left.tStartRefresh)
thisExp.addData('left.stopped', left.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
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
