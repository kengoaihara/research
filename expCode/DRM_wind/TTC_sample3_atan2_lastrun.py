#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on 7月 13, 2021, at 12:49
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
expName = 'TTC_sample3'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\mnaga\\Desktop\\RA\\TTC_sample3_atan2_lastrun.py',
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
    size=[1536, 864], fullscr=True, screen=0, 
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

# Initialize components for Routine "inst"
instClock = core.Clock()
same = visual.TextStim(win=win, name='same',
    text='same = F\ndifferent = J\n\n',
    font='Open Sans',
    units='deg', pos=(0, 1), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
space = visual.TextStim(win=win, name='space',
    text='press SPACE to start',
    font='Open Sans',
    units='deg', pos=(0, -2), height=1.5, wrapWidth=None, ori=0.0, 
    color=(-1.0000, 0.0039, -1.0000), colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
win.mouseVisible = False

far = 130
near = 60
s = 10
diff = far - near
distance = diff/2
v = distance/0.75

#V = VARIABLE
#distance = 0.75*v
#diff = distance*2
obeject = visual.Polygon(
    win=win, name='obeject',units='deg', 
    edges=40, size=[1.0, 1.0],
    ori=0.0, pos=(0,0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-1.0, interpolate=True)
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.5, wrapWidth=None, ori=0.0, 
    color=(0.0000, 0.0000, 0.0000), colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.5, wrapWidth=None, ori=0.0, 
    color=(0.0000, 0.0000, 0.0000), colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "resp"
respClock = core.Clock()
#import random
prove = visual.Polygon(
    win=win, name='prove',units='deg', 
    edges=40, size=[1.0, 1.0],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-1.0, interpolate=True)
resp1 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "inst"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instComponents = [same, key_resp, space]
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
    
    # *same* updates
    if same.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        same.frameNStart = frameN  # exact frame index
        same.tStart = t  # local t and not account for scr refresh
        same.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(same, 'tStartRefresh')  # time at next scr refresh
        same.setAutoDraw(True)
    
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
    
    # *space* updates
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space.frameNStart = frameN  # exact frame index
        space.tStart = t  # local t and not account for scr refresh
        space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
        space.setAutoDraw(True)
    
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
thisExp.addData('same.started', same.tStartRefresh)
thisExp.addData('same.stopped', same.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space.started', space.tStartRefresh)
thisExp.addData('space.stopped', space.tStopRefresh)
# the Routine "inst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
rep = data.TrialHandler(nReps=10.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='rep')
thisExp.addLoop(rep)  # add the loop to the experiment
thisRep = rep.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRep.rgb)
if thisRep != None:
    for paramName in thisRep:
        exec('{} = thisRep[paramName]'.format(paramName))

for thisRep in rep:
    currentLoop = rep
    # abbreviate parameter names if possible (e.g. rgb = thisRep.rgb)
    if thisRep != None:
        for paramName in thisRep:
            exec('{} = thisRep[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TTC_sample3copycopy.csv'),
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
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(2.250000)
        # update component parameters for each repeat
        import random
        import math
        # keep track of which components have finished
        trialComponents = [obeject, fix]
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
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if d == 60:
               size = 360/pi*math.atan(s/(d+v*(t-1.5))/2)
            else:
               size = 360/pi*math.atan(s/(d-v*(t-1.5))/2)
            
            
            #= 360/PI()*ATAN(I2/H2/2)
            #= 57+344*J3
            #atan
            #function = (360/pi*math.atan(s/d-v*(t-1.5)/2))*(t-1.5)
            #function2 = (360/pi*math.atan(s/d+v*(t-1.5)/2))*(t-1.5)
            
            #function = 9.71**(t-1.5)
            #jit = random.uniform(-1,1)
            
            #if d == 573:
            #    size = function+start_size
            
            #else:
            #    size = function2+start_size2
            
            # *obeject* updates
            if obeject.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                obeject.frameNStart = frameN  # exact frame index
                obeject.tStart = t  # local t and not account for scr refresh
                obeject.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(obeject, 'tStartRefresh')  # time at next scr refresh
                obeject.setAutoDraw(True)
            if obeject.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > obeject.tStartRefresh + 0.75-frameTolerance:
                    # keep track of stop time/frame for later
                    obeject.tStop = t  # not accounting for scr refresh
                    obeject.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(obeject, 'tStopRefresh')  # time at next scr refresh
                    obeject.setAutoDraw(False)
            if obeject.status == STARTED:  # only update if drawing
                obeject.setSize((size,size))
            
            # *fix* updates
            if fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                fix.setAutoDraw(True)
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                    fix.setAutoDraw(False)
            
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
        trials.addData('obeject.started', obeject.tStartRefresh)
        trials.addData('obeject.stopped', obeject.tStopRefresh)
        trials.addData('fix.started', fix.tStartRefresh)
        trials.addData('fix.stopped', fix.tStopRefresh)
        
        # ------Prepare to start Routine "ISI"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [text]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI"-------
        while continueRoutine:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + asarray(isi)-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('text.started', text.tStartRefresh)
        trials.addData('text.stopped', text.tStopRefresh)
        # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "resp"-------
        continueRoutine = True
        # update component parameters for each repeat
        #probe = probe
        #jit = random.uniform(-1,1)
        prove.setSize((probe,probe))
        resp1.keys = []
        resp1.rt = []
        _resp1_allKeys = []
        # keep track of which components have finished
        respComponents = [prove, resp1]
        for thisComponent in respComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "resp"-------
        while continueRoutine:
            # get current time
            t = respClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=respClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prove* updates
            if prove.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prove.frameNStart = frameN  # exact frame index
                prove.tStart = t  # local t and not account for scr refresh
                prove.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prove, 'tStartRefresh')  # time at next scr refresh
                prove.setAutoDraw(True)
            
            # *resp1* updates
            waitOnFlip = False
            if resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp1.frameNStart = frameN  # exact frame index
                resp1.tStart = t  # local t and not account for scr refresh
                resp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp1, 'tStartRefresh')  # time at next scr refresh
                resp1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp1.status == STARTED and not waitOnFlip:
                theseKeys = resp1.getKeys(keyList=['f', 'j'], waitRelease=False)
                _resp1_allKeys.extend(theseKeys)
                if len(_resp1_allKeys):
                    resp1.keys = _resp1_allKeys[-1].name  # just the last key pressed
                    resp1.rt = _resp1_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in respComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "resp"-------
        for thisComponent in respComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('prove.started', prove.tStartRefresh)
        trials.addData('prove.stopped', prove.tStopRefresh)
        # check responses
        if resp1.keys in ['', [], None]:  # No response was made
            resp1.keys = None
        trials.addData('resp1.keys',resp1.keys)
        if resp1.keys != None:  # we had a response
            trials.addData('resp1.rt', resp1.rt)
        trials.addData('resp1.started', resp1.tStartRefresh)
        trials.addData('resp1.stopped', resp1.tStopRefresh)
        # the Routine "resp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'rep'


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
