﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on 10月 04, 2021, at 11:52
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
psychopyVersion = '2021.1.3'
expName = 'height'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\ak221\\OneDrive\\デスクトップ\\height_lastrun.py',
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
    size=[1504, 1003], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
winMouseVisible = False
line = visual.Line(
    win=win, name='line',units='deg', 
    start=(-(100, 0)[0]/2.0, 0), end=(+(100, 0)[0]/2.0, 0),
    ori=0.0, pos=(0, -5),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-1.0, interpolate=True)
building = visual.Rect(
    win=win, name='building',units='deg', 
    width=(2.5, 10)[0], height=(2.5, 10)[1],
    ori=0.0, pos=(-5, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-2.0, interpolate=True)
church = visual.Rect(
    win=win, name='church',units='deg', 
    width=(2.5, 7.5)[0], height=(2.5, 7.5)[1],
    ori=0.0, pos=(5, -1.25),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-3.0, interpolate=True)
top = visual.ShapeStim(
    win=win, name='top',units='deg', 
    vertices=[[-(2.5, 2.5)[0]/2.0,-(2.5, 2.5)[1]/2.0], [+(2.5, 2.5)[0]/2.0,-(2.5, 2.5)[1]/2.0], [0,(2.5, 2.5)[1]/2.0]],
    ori=0.0, pos=(5, 3.75),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-4.0, interpolate=True)
key_resp = keyboard.Keyboard()
rectangle2 = visual.Rect(
    win=win, name='rectangle2',units='deg', 
    width=(2.5, 7.5)[0], height=(2.5, 7.5)[1],
    ori=0.0, pos=(2, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-6.0, interpolate=True)
top2 = visual.Rect(
    win=win, name='top2',units='deg', 
    width=(2.5, 2.5)[0], height=(2.5, 2.5)[1],
    ori=0.0, pos=(2, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-7.0, interpolate=True)
top3 = visual.ShapeStim(
    win=win, name='top3',units='deg', 
    vertices=[[-(5, 5)[0]/2.0,-(5, 5)[1]/2.0], [+(5, 5)[0]/2.0,-(5, 5)[1]/2.0], [0,(5, 5)[1]/2.0]],
    ori=45.0, pos=(2, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
trialComponents = [line, building, church, top, key_resp, rectangle2, top2, top3]
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
    
    # *line* updates
    if line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        line.frameNStart = frameN  # exact frame index
        line.tStart = t  # local t and not account for scr refresh
        line.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(line, 'tStartRefresh')  # time at next scr refresh
        line.setAutoDraw(True)
    
    # *building* updates
    if building.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        building.frameNStart = frameN  # exact frame index
        building.tStart = t  # local t and not account for scr refresh
        building.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(building, 'tStartRefresh')  # time at next scr refresh
        building.setAutoDraw(True)
    
    # *church* updates
    if church.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        church.frameNStart = frameN  # exact frame index
        church.tStart = t  # local t and not account for scr refresh
        church.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(church, 'tStartRefresh')  # time at next scr refresh
        church.setAutoDraw(True)
    
    # *top* updates
    if top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top.frameNStart = frameN  # exact frame index
        top.tStart = t  # local t and not account for scr refresh
        top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top, 'tStartRefresh')  # time at next scr refresh
        top.setAutoDraw(True)
    
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
        theseKeys = key_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rectangle2* updates
    if rectangle2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rectangle2.frameNStart = frameN  # exact frame index
        rectangle2.tStart = t  # local t and not account for scr refresh
        rectangle2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rectangle2, 'tStartRefresh')  # time at next scr refresh
        rectangle2.setAutoDraw(True)
    
    # *top2* updates
    if top2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top2.frameNStart = frameN  # exact frame index
        top2.tStart = t  # local t and not account for scr refresh
        top2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top2, 'tStartRefresh')  # time at next scr refresh
        top2.setAutoDraw(True)
    
    # *top3* updates
    if top3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top3.frameNStart = frameN  # exact frame index
        top3.tStart = t  # local t and not account for scr refresh
        top3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top3, 'tStartRefresh')  # time at next scr refresh
        top3.setAutoDraw(True)
    
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
thisExp.addData('line.started', line.tStartRefresh)
thisExp.addData('line.stopped', line.tStopRefresh)
thisExp.addData('building.started', building.tStartRefresh)
thisExp.addData('building.stopped', building.tStopRefresh)
thisExp.addData('church.started', church.tStartRefresh)
thisExp.addData('church.stopped', church.tStopRefresh)
thisExp.addData('top.started', top.tStartRefresh)
thisExp.addData('top.stopped', top.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rectangle2.started', rectangle2.tStartRefresh)
thisExp.addData('rectangle2.stopped', rectangle2.tStopRefresh)
thisExp.addData('top2.started', top2.tStartRefresh)
thisExp.addData('top2.stopped', top2.tStopRefresh)
thisExp.addData('top3.started', top3.tStartRefresh)
thisExp.addData('top3.stopped', top3.tStopRefresh)
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
