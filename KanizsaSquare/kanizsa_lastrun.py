#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 11月 06, 2021, at 14:46
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
expName = 'kanizsa'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\ak221\\OneDrive\\デスクトップ\\kanizsa_lastrun.py',
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
x = 0
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
circle_s_1 = visual.ShapeStim(
    win=win, name='circle_s_1', vertices=40,units='deg', 
    size=(2, 2),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=-2.0, interpolate=True)
circle_s_2 = visual.ShapeStim(
    win=win, name='circle_s_2', vertices=40,units='deg', 
    size=(2, 2),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
circle_s_3 = visual.ShapeStim(
    win=win, name='circle_s_3', vertices=40,units='deg', 
    size=(2, 2),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
circle_s_4 = visual.ShapeStim(
    win=win, name='circle_s_4', vertices=40,units='deg', 
    size=(2, 2),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)
square = visual.Rect(
    win=win, name='square',units='deg', 
    width=(4, 4)[0], height=(4, 4)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-6.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
circle_s_1.setPos((x+2, 2))
circle_s_2.setPos((x-2, 2))
circle_s_3.setPos((x+2, -2))
circle_s_4.setPos((x-2, -2))
square.setPos((x, 0))
# keep track of which components have finished
trialComponents = [fix, circle_s_1, circle_s_2, circle_s_3, circle_s_4, square]
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
    
    # *fix* updates
    if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix.frameNStart = frameN  # exact frame index
        fix.tStart = t  # local t and not account for scr refresh
        fix.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
        fix.setAutoDraw(True)
    
    # *circle_s_1* updates
    if circle_s_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_s_1.frameNStart = frameN  # exact frame index
        circle_s_1.tStart = t  # local t and not account for scr refresh
        circle_s_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_s_1, 'tStartRefresh')  # time at next scr refresh
        circle_s_1.setAutoDraw(True)
    
    # *circle_s_2* updates
    if circle_s_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_s_2.frameNStart = frameN  # exact frame index
        circle_s_2.tStart = t  # local t and not account for scr refresh
        circle_s_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_s_2, 'tStartRefresh')  # time at next scr refresh
        circle_s_2.setAutoDraw(True)
    
    # *circle_s_3* updates
    if circle_s_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_s_3.frameNStart = frameN  # exact frame index
        circle_s_3.tStart = t  # local t and not account for scr refresh
        circle_s_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_s_3, 'tStartRefresh')  # time at next scr refresh
        circle_s_3.setAutoDraw(True)
    
    # *circle_s_4* updates
    if circle_s_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_s_4.frameNStart = frameN  # exact frame index
        circle_s_4.tStart = t  # local t and not account for scr refresh
        circle_s_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_s_4, 'tStartRefresh')  # time at next scr refresh
        circle_s_4.setAutoDraw(True)
    
    # *square* updates
    if square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        square.frameNStart = frameN  # exact frame index
        square.tStart = t  # local t and not account for scr refresh
        square.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square, 'tStartRefresh')  # time at next scr refresh
        square.setAutoDraw(True)
    
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
thisExp.addData('circle_s_1.started', circle_s_1.tStartRefresh)
thisExp.addData('circle_s_1.stopped', circle_s_1.tStopRefresh)
thisExp.addData('circle_s_2.started', circle_s_2.tStartRefresh)
thisExp.addData('circle_s_2.stopped', circle_s_2.tStopRefresh)
thisExp.addData('circle_s_3.started', circle_s_3.tStartRefresh)
thisExp.addData('circle_s_3.stopped', circle_s_3.tStopRefresh)
thisExp.addData('circle_s_4.started', circle_s_4.tStartRefresh)
thisExp.addData('circle_s_4.stopped', circle_s_4.tStopRefresh)
thisExp.addData('square.started', square.tStartRefresh)
thisExp.addData('square.stopped', square.tStopRefresh)
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
