#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 11月 01, 2021, at 10:34
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
expName = 'pos'  # from the Builder filename that created this script
expInfo = {'name': '', 'participant': '', 'date': '2021/', 'sex': 'female / male / I don`t want to talk about it', 'age': '', 'dominant hand': 'right / left / both', 'temparature': '℃', 'disinfection': 'done / not yet', 'note': ''}
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
    originPath='G:\\exp\\pos_lastrun.py',
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
    monitor='testMonitor', color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb',
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

# Initialize components for Routine "pra_inst"
pra_instClock = core.Clock()
inst = visual.ImageStim(
    win=win,
    name='inst', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
resp = keyboard.Keyboard()

# Initialize components for Routine "pra"
praClock = core.Clock()
import random
win.mouseVisible=False
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color=(0.0000, 0.0000, 0.0000), colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
st_pra = visual.ShapeStim(
    win=win, name='st_pra',units='deg', 
    size=(4, 4), vertices='triangle',
    ori=1.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-2.0, interpolate=True)
pr_pra = visual.ShapeStim(
    win=win, name='pr_pra', vertices=40,units='deg', 
    size=[1.0, 1.0],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-3.0, interpolate=True)
resp_pra = keyboard.Keyboard()

# Initialize components for Routine "noise_3"
noise_3Clock = core.Clock()
noise = visual.NoiseStim(
    win=win, name='noise',units='pix', 
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, 0), size=(400, 200), sf=None,
    phase=0.0,
    color=[-1,-1,-1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Uniform', noiseElementSize=[15], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=0.0)
noise.buildNoise()

# Initialize components for Routine "main_inst"
main_instClock = core.Clock()
instr2 = visual.ImageStim(
    win=win,
    name='instr2', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
m_resp = keyboard.Keyboard()

# Initialize components for Routine "main"
mainClock = core.Clock()
win.mouseVisible=False
import random

trialCounter = 0
nRestTrial = 56

fix2 = visual.TextStim(win=win, name='fix2',
    text='+',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color=(0.0000, 0.0000, 0.0000), colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
st_main = visual.ShapeStim(
    win=win, name='st_main',units='deg', 
    size=(4, 4), vertices='triangle',
    ori=1.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-2.0, interpolate=True)
pr_main = visual.Line(
    win=win, name='pr_main',units='deg', 
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=1.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.0000, 0.0000, 0.0000), fillColor=(0.0000, 0.0000, 0.0000),
    opacity=None, depth=-3.0, interpolate=True)
resp2 = keyboard.Keyboard()

# Initialize components for Routine "noise_3"
noise_3Clock = core.Clock()
noise = visual.NoiseStim(
    win=win, name='noise',units='pix', 
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, 0), size=(400, 200), sf=None,
    phase=0.0,
    color=[-1,-1,-1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Uniform', noiseElementSize=[15], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=0.0)
noise.buildNoise()

# Initialize components for Routine "rest"
restClock = core.Clock()
text2 = visual.TextStim(win=win, name='text2',
    text='Rest !\nPress space',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color=(0.0000, 0.0000, 0.0000), colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
ending = visual.TextStim(win=win, name='ending',
    text='Exp is ended.\nThank you!',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color=(0.0000, 0.0000, 0.0000), colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
rep = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('comb_b.csv'),
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
    
    # ------Prepare to start Routine "pra_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    inst.setImage(inst1)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    pra_instComponents = [inst, resp]
    for thisComponent in pra_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pra_inst"-------
    while continueRoutine:
        # get current time
        t = pra_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst* updates
        if inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst.frameNStart = frameN  # exact frame index
            inst.tStart = t  # local t and not account for scr refresh
            inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst, 'tStartRefresh')  # time at next scr refresh
            inst.setAutoDraw(True)
        
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra_inst"-------
    for thisComponent in pra_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rep.addData('inst.started', inst.tStartRefresh)
    rep.addData('inst.stopped', inst.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
    rep.addData('resp.keys',resp.keys)
    if resp.keys != None:  # we had a response
        rep.addData('resp.rt', resp.rt)
    rep.addData('resp.started', resp.tStartRefresh)
    rep.addData('resp.stopped', resp.tStopRefresh)
    # the Routine "pra_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    rep1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(pra),
        seed=None, name='rep1')
    thisExp.addLoop(rep1)  # add the loop to the experiment
    thisRep1 = rep1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRep1.rgb)
    if thisRep1 != None:
        for paramName in thisRep1:
            exec('{} = thisRep1[paramName]'.format(paramName))
    
    for thisRep1 in rep1:
        currentLoop = rep1
        # abbreviate parameter names if possible (e.g. rgb = thisRep1.rgb)
        if thisRep1 != None:
            for paramName in thisRep1:
                exec('{} = thisRep1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "pra"-------
        continueRoutine = True
        # update component parameters for each repeat
        jit = random.uniform(-0.5,0.5)
        st_pra.setPos((xpos_st, jit))
        st_pra.setOri(ori_st)
        pr_pra.setPos((xpos_pr, ypos_pr*size+jit))
        pr_pra.setSize((w,0))
        resp_pra.keys = []
        resp_pra.rt = []
        _resp_pra_allKeys = []
        # keep track of which components have finished
        praComponents = [fix, st_pra, pr_pra, resp_pra]
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
            
            # *fix* updates
            if fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                fix.setAutoDraw(True)
            
            # *st_pra* updates
            if st_pra.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                st_pra.frameNStart = frameN  # exact frame index
                st_pra.tStart = t  # local t and not account for scr refresh
                st_pra.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(st_pra, 'tStartRefresh')  # time at next scr refresh
                st_pra.setAutoDraw(True)
            
            # *pr_pra* updates
            if pr_pra.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                pr_pra.frameNStart = frameN  # exact frame index
                pr_pra.tStart = t  # local t and not account for scr refresh
                pr_pra.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pr_pra, 'tStartRefresh')  # time at next scr refresh
                pr_pra.setAutoDraw(True)
            
            # *resp_pra* updates
            waitOnFlip = False
            if resp_pra.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                resp_pra.frameNStart = frameN  # exact frame index
                resp_pra.tStart = t  # local t and not account for scr refresh
                resp_pra.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_pra, 'tStartRefresh')  # time at next scr refresh
                resp_pra.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_pra.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_pra.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_pra.status == STARTED and not waitOnFlip:
                theseKeys = resp_pra.getKeys(keyList=['f', 'j'], waitRelease=False)
                _resp_pra_allKeys.extend(theseKeys)
                if len(_resp_pra_allKeys):
                    resp_pra.keys = _resp_pra_allKeys[-1].name  # just the last key pressed
                    resp_pra.rt = _resp_pra_allKeys[-1].rt
                    # a response ends the routine
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
        rep1.addData('fix.started', fix.tStartRefresh)
        rep1.addData('fix.stopped', fix.tStopRefresh)
        rep1.addData('st_pra.started', st_pra.tStartRefresh)
        rep1.addData('st_pra.stopped', st_pra.tStopRefresh)
        rep1.addData('pr_pra.started', pr_pra.tStartRefresh)
        rep1.addData('pr_pra.stopped', pr_pra.tStopRefresh)
        # check responses
        if resp_pra.keys in ['', [], None]:  # No response was made
            resp_pra.keys = None
        rep1.addData('resp_pra.keys',resp_pra.keys)
        if resp_pra.keys != None:  # we had a response
            rep1.addData('resp_pra.rt', resp_pra.rt)
        rep1.addData('resp_pra.started', resp_pra.tStartRefresh)
        rep1.addData('resp_pra.stopped', resp_pra.tStopRefresh)
        # the Routine "pra" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "noise_3"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        if not noise._needBuild:
            noise.updateNoise()
        # keep track of which components have finished
        noise_3Components = [noise]
        for thisComponent in noise_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        noise_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "noise_3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = noise_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=noise_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *noise* updates
            if noise.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                noise.frameNStart = frameN  # exact frame index
                noise.tStart = t  # local t and not account for scr refresh
                noise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
                noise.setAutoDraw(True)
            if noise.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    noise.tStop = t  # not accounting for scr refresh
                    noise.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise, 'tStopRefresh')  # time at next scr refresh
                    noise.setAutoDraw(False)
            if noise.status == STARTED:
                if noise._needBuild:
                    noise.buildNoise()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in noise_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "noise_3"-------
        for thisComponent in noise_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rep1.addData('noise.started', noise.tStartRefresh)
        rep1.addData('noise.stopped', noise.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'rep1'
    
    
    # ------Prepare to start Routine "main_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    instr2.setImage(inst2)
    m_resp.keys = []
    m_resp.rt = []
    _m_resp_allKeys = []
    # keep track of which components have finished
    main_instComponents = [instr2, m_resp]
    for thisComponent in main_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    main_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "main_inst"-------
    while continueRoutine:
        # get current time
        t = main_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=main_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr2* updates
        if instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr2.frameNStart = frameN  # exact frame index
            instr2.tStart = t  # local t and not account for scr refresh
            instr2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
            instr2.setAutoDraw(True)
        
        # *m_resp* updates
        waitOnFlip = False
        if m_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            m_resp.frameNStart = frameN  # exact frame index
            m_resp.tStart = t  # local t and not account for scr refresh
            m_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(m_resp, 'tStartRefresh')  # time at next scr refresh
            m_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(m_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(m_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if m_resp.status == STARTED and not waitOnFlip:
            theseKeys = m_resp.getKeys(keyList=['space'], waitRelease=False)
            _m_resp_allKeys.extend(theseKeys)
            if len(_m_resp_allKeys):
                m_resp.keys = _m_resp_allKeys[-1].name  # just the last key pressed
                m_resp.rt = _m_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in main_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "main_inst"-------
    for thisComponent in main_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rep.addData('instr2.started', instr2.tStartRefresh)
    rep.addData('instr2.stopped', instr2.tStopRefresh)
    # check responses
    if m_resp.keys in ['', [], None]:  # No response was made
        m_resp.keys = None
    rep.addData('m_resp.keys',m_resp.keys)
    if m_resp.keys != None:  # we had a response
        rep.addData('m_resp.rt', m_resp.rt)
    rep.addData('m_resp.started', m_resp.tStartRefresh)
    rep.addData('m_resp.stopped', m_resp.tStopRefresh)
    # the Routine "main_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=8.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(main),
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
        
        # ------Prepare to start Routine "main"-------
        continueRoutine = True
        # update component parameters for each repeat
        jit1 = random.uniform(-0.5, 0.5)
        
        trialCounter = trialCounter + 1
        
        if trialCounter % nRestTrial == 0:
            isRest = 1
        else:
            isRest = 0
        st_main.setPos((xpos_st, jit))
        st_main.setOri(ori_st)
        pr_main.setPos((xpos_pr, ypos_pr*size+jit))
        pr_main.setSize((w, 0))
        pr_main.setOri(ori_st)
        resp2.keys = []
        resp2.rt = []
        _resp2_allKeys = []
        # keep track of which components have finished
        mainComponents = [fix2, st_main, pr_main, resp2]
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
            
            # *fix2* updates
            if fix2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                fix2.frameNStart = frameN  # exact frame index
                fix2.tStart = t  # local t and not account for scr refresh
                fix2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
                fix2.setAutoDraw(True)
            
            # *st_main* updates
            if st_main.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                st_main.frameNStart = frameN  # exact frame index
                st_main.tStart = t  # local t and not account for scr refresh
                st_main.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(st_main, 'tStartRefresh')  # time at next scr refresh
                st_main.setAutoDraw(True)
            
            # *pr_main* updates
            if pr_main.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                pr_main.frameNStart = frameN  # exact frame index
                pr_main.tStart = t  # local t and not account for scr refresh
                pr_main.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pr_main, 'tStartRefresh')  # time at next scr refresh
                pr_main.setAutoDraw(True)
            
            # *resp2* updates
            waitOnFlip = False
            if resp2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                resp2.frameNStart = frameN  # exact frame index
                resp2.tStart = t  # local t and not account for scr refresh
                resp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp2, 'tStartRefresh')  # time at next scr refresh
                resp2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp2.status == STARTED and not waitOnFlip:
                theseKeys = resp2.getKeys(keyList=['f', 'j'], waitRelease=False)
                _resp2_allKeys.extend(theseKeys)
                if len(_resp2_allKeys):
                    resp2.keys = _resp2_allKeys[-1].name  # just the last key pressed
                    resp2.rt = _resp2_allKeys[-1].rt
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
        trials.addData('fix2.started', fix2.tStartRefresh)
        trials.addData('fix2.stopped', fix2.tStopRefresh)
        trials.addData('st_main.started', st_main.tStartRefresh)
        trials.addData('st_main.stopped', st_main.tStopRefresh)
        trials.addData('pr_main.started', pr_main.tStartRefresh)
        trials.addData('pr_main.stopped', pr_main.tStopRefresh)
        # check responses
        if resp2.keys in ['', [], None]:  # No response was made
            resp2.keys = None
        trials.addData('resp2.keys',resp2.keys)
        if resp2.keys != None:  # we had a response
            trials.addData('resp2.rt', resp2.rt)
        trials.addData('resp2.started', resp2.tStartRefresh)
        trials.addData('resp2.stopped', resp2.tStopRefresh)
        # the Routine "main" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "noise_3"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        if not noise._needBuild:
            noise.updateNoise()
        # keep track of which components have finished
        noise_3Components = [noise]
        for thisComponent in noise_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        noise_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "noise_3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = noise_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=noise_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *noise* updates
            if noise.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                noise.frameNStart = frameN  # exact frame index
                noise.tStart = t  # local t and not account for scr refresh
                noise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
                noise.setAutoDraw(True)
            if noise.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    noise.tStop = t  # not accounting for scr refresh
                    noise.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise, 'tStopRefresh')  # time at next scr refresh
                    noise.setAutoDraw(False)
            if noise.status == STARTED:
                if noise._needBuild:
                    noise.buildNoise()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in noise_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "noise_3"-------
        for thisComponent in noise_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('noise.started', noise.tStartRefresh)
        trials.addData('noise.stopped', noise.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        restOrNot = data.TrialHandler(nReps=isRest, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='restOrNot')
        thisExp.addLoop(restOrNot)  # add the loop to the experiment
        thisRestOrNot = restOrNot.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRestOrNot.rgb)
        if thisRestOrNot != None:
            for paramName in thisRestOrNot:
                exec('{} = thisRestOrNot[paramName]'.format(paramName))
        
        for thisRestOrNot in restOrNot:
            currentLoop = restOrNot
            # abbreviate parameter names if possible (e.g. rgb = thisRestOrNot.rgb)
            if thisRestOrNot != None:
                for paramName in thisRestOrNot:
                    exec('{} = thisRestOrNot[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "rest"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # keep track of which components have finished
            restComponents = [text2, key_resp]
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
                
                # *text2* updates
                if text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text2.frameNStart = frameN  # exact frame index
                    text2.tStart = t  # local t and not account for scr refresh
                    text2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text2, 'tStartRefresh')  # time at next scr refresh
                    text2.setAutoDraw(True)
                
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
            restOrNot.addData('text2.started', text2.tStartRefresh)
            restOrNot.addData('text2.stopped', text2.tStopRefresh)
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            restOrNot.addData('key_resp.keys',key_resp.keys)
            if key_resp.keys != None:  # we had a response
                restOrNot.addData('key_resp.rt', key_resp.rt)
            restOrNot.addData('key_resp.started', key_resp.tStartRefresh)
            restOrNot.addData('key_resp.stopped', key_resp.tStopRefresh)
            # the Routine "rest" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed isRest repeats of 'restOrNot'
        
        thisExp.nextEntry()
        
    # completed 8.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'rep'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
resp3.keys = []
resp3.rt = []
_resp3_allKeys = []
# keep track of which components have finished
endComponents = [ending, resp3]
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
    
    # *ending* updates
    if ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ending.frameNStart = frameN  # exact frame index
        ending.tStart = t  # local t and not account for scr refresh
        ending.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ending, 'tStartRefresh')  # time at next scr refresh
        ending.setAutoDraw(True)
    
    # *resp3* updates
    waitOnFlip = False
    if resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp3.frameNStart = frameN  # exact frame index
        resp3.tStart = t  # local t and not account for scr refresh
        resp3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp3, 'tStartRefresh')  # time at next scr refresh
        resp3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp3.status == STARTED and not waitOnFlip:
        theseKeys = resp3.getKeys(keyList=['space'], waitRelease=False)
        _resp3_allKeys.extend(theseKeys)
        if len(_resp3_allKeys):
            resp3.keys = _resp3_allKeys[-1].name  # just the last key pressed
            resp3.rt = _resp3_allKeys[-1].rt
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
thisExp.addData('ending.started', ending.tStartRefresh)
thisExp.addData('ending.stopped', ending.tStopRefresh)
# check responses
if resp3.keys in ['', [], None]:  # No response was made
    resp3.keys = None
thisExp.addData('resp3.keys',resp3.keys)
if resp3.keys != None:  # we had a response
    thisExp.addData('resp3.rt', resp3.rt)
thisExp.addData('resp3.started', resp3.tStartRefresh)
thisExp.addData('resp3.stopped', resp3.tStopRefresh)
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
