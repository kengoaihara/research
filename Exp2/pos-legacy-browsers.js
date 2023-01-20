/************ 
 * Pos Test *
 ************/


// store info about the experiment session:
let expName = 'pos';  // from the Builder filename that created this script
let expInfo = {
    'name': '',
    'participant': '',
    'date': '2021/',
    'sex': 'female / male / I don`t want to talk about it',
    'age': '',
    'dominant hand': 'right / left / both',
    'temparature': '℃',
    'disinfection': 'done / not yet',
    'note': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color((-1.0000, -1.0000, -1.0000)),
  units: 'deg',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const repLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(repLoopBegin(repLoopScheduler));
flowScheduler.add(repLoopScheduler);
flowScheduler.add(repLoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'comb_b.csv', 'path': 'comb_b.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var pra_instClock;
var inst;
var resp;
var praClock;
var fix;
var st_pra;
var pr_pra;
var resp_pra;
var noise_3Clock;
var main_instClock;
var instr2;
var m_resp;
var mainClock;
var fix2;
var st_main;
var pr_main;
var resp2;
var restClock;
var text2;
var key_resp;
var endClock;
var ending;
var resp3;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "pra_inst"
  pra_instClock = new util.Clock();
  inst = new visual.ImageStim({
    win : psychoJS.window,
    name : 'inst', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1920, 1080],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pra"
  praClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  win.mouseVisible = false;
  
  fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix',
    text: '+',
    font: 'Open Sans',
    units: 'deg', 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((0.0000, 0.0000, 0.0000)),  opacity: undefined,
    depth: -1.0 
  });
  
  st_pra = new visual.ShapeStim ({
    win: psychoJS.window, name: 'st_pra', units : 'height', 
    vertices: [[-[4, 4][0]/2.0, -[4, 4][1]/2.0], [+[4, 4][0]/2.0, -[4, 4][1]/2.0], [0, [4, 4][1]/2.0]],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color((0.0000, 0.0000, 0.0000)),
    fillColor: new util.Color((0.0000, 0.0000, 0.0000)),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  pr_pra = new visual.Polygon ({
    win: psychoJS.window, name: 'pr_pra', units : 'height', 
    edges: 40, size:[1.0, 1.0],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color((0.0000, 0.0000, 0.0000)),
    fillColor: new util.Color((0.0000, 0.0000, 0.0000)),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  resp_pra = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "noise_3"
  noise_3Clock = new util.Clock();
  // Initialize components for Routine "main_inst"
  main_instClock = new util.Clock();
  instr2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instr2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1920, 1080],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  m_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "main"
  mainClock = new util.Clock();
  fix2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix2',
    text: '+',
    font: 'Open Sans',
    units: 'deg', 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((0.0000, 0.0000, 0.0000)),  opacity: undefined,
    depth: -1.0 
  });
  
  st_main = new visual.ShapeStim ({
    win: psychoJS.window, name: 'st_main', units : 'height', 
    vertices: [[-[4, 4][0]/2.0, -[4, 4][1]/2.0], [+[4, 4][0]/2.0, -[4, 4][1]/2.0], [0, [4, 4][1]/2.0]],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color((0.0000, 0.0000, 0.0000)),
    fillColor: new util.Color((0.0000, 0.0000, 0.0000)),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  pr_main = new visual.ShapeStim ({
    win: psychoJS.window, name: 'pr_main', units : 'height', 
    vertices: [[-[1.0, 1.0][0]/2.0, 0], [+[1.0, 1.0][0]/2.0, 0]],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color((0.0000, 0.0000, 0.0000)),
    fillColor: new util.Color((0.0000, 0.0000, 0.0000)),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  resp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rest"
  restClock = new util.Clock();
  text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text2',
    text: 'Rest !\nPress space',
    font: 'Open Sans',
    units: 'deg', 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((0.0000, 0.0000, 0.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  ending = new visual.TextStim({
    win: psychoJS.window,
    name: 'ending',
    text: 'Exp is ended.\nThank you!',
    font: 'Open Sans',
    units: 'deg', 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((0.0000, 0.0000, 0.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  resp3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var rep;
function repLoopBegin(repLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    rep = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'comb_b.csv',
      seed: undefined, name: 'rep'
    });
    psychoJS.experiment.addLoop(rep); // add the loop to the experiment
    currentLoop = rep;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    rep.forEach(function() {
      snapshot = rep.getSnapshot();
    
      repLoopScheduler.add(importConditions(snapshot));
      repLoopScheduler.add(pra_instRoutineBegin(snapshot));
      repLoopScheduler.add(pra_instRoutineEachFrame());
      repLoopScheduler.add(pra_instRoutineEnd(snapshot));
      const rep1LoopScheduler = new Scheduler(psychoJS);
      repLoopScheduler.add(rep1LoopBegin(rep1LoopScheduler, snapshot));
      repLoopScheduler.add(rep1LoopScheduler);
      repLoopScheduler.add(rep1LoopEnd);
      repLoopScheduler.add(main_instRoutineBegin(snapshot));
      repLoopScheduler.add(main_instRoutineEachFrame());
      repLoopScheduler.add(main_instRoutineEnd(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      repLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      repLoopScheduler.add(trialsLoopScheduler);
      repLoopScheduler.add(trialsLoopEnd);
      repLoopScheduler.add(repLoopEndIteration(repLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var rep1;
function rep1LoopBegin(rep1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    rep1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: pra,
      seed: undefined, name: 'rep1'
    });
    psychoJS.experiment.addLoop(rep1); // add the loop to the experiment
    currentLoop = rep1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    rep1.forEach(function() {
      snapshot = rep1.getSnapshot();
    
      rep1LoopScheduler.add(importConditions(snapshot));
      rep1LoopScheduler.add(praRoutineBegin(snapshot));
      rep1LoopScheduler.add(praRoutineEachFrame());
      rep1LoopScheduler.add(praRoutineEnd(snapshot));
      rep1LoopScheduler.add(noise_3RoutineBegin(snapshot));
      rep1LoopScheduler.add(noise_3RoutineEachFrame());
      rep1LoopScheduler.add(noise_3RoutineEnd(snapshot));
      rep1LoopScheduler.add(rep1LoopEndIteration(rep1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function rep1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(rep1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function rep1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 8, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: main,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(mainRoutineBegin(snapshot));
      trialsLoopScheduler.add(mainRoutineEachFrame());
      trialsLoopScheduler.add(mainRoutineEnd(snapshot));
      trialsLoopScheduler.add(noise_3RoutineBegin(snapshot));
      trialsLoopScheduler.add(noise_3RoutineEachFrame());
      trialsLoopScheduler.add(noise_3RoutineEnd(snapshot));
      const restOrNotLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(restOrNotLoopBegin(restOrNotLoopScheduler, snapshot));
      trialsLoopScheduler.add(restOrNotLoopScheduler);
      trialsLoopScheduler.add(restOrNotLoopEnd);
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var restOrNot;
function restOrNotLoopBegin(restOrNotLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    restOrNot = new TrialHandler({
      psychoJS: psychoJS,
      nReps: isRest, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'restOrNot'
    });
    psychoJS.experiment.addLoop(restOrNot); // add the loop to the experiment
    currentLoop = restOrNot;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    restOrNot.forEach(function() {
      snapshot = restOrNot.getSnapshot();
    
      restOrNotLoopScheduler.add(importConditions(snapshot));
      restOrNotLoopScheduler.add(restRoutineBegin(snapshot));
      restOrNotLoopScheduler.add(restRoutineEachFrame());
      restOrNotLoopScheduler.add(restRoutineEnd(snapshot));
      restOrNotLoopScheduler.add(restOrNotLoopEndIteration(restOrNotLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function restOrNotLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(restOrNot);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function restOrNotLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function repLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(rep);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function repLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var _resp_allKeys;
var pra_instComponents;
function pra_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pra_inst' ---
    t = 0;
    pra_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    inst.setImage(inst1);
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    // keep track of which components have finished
    pra_instComponents = [];
    pra_instComponents.push(inst);
    pra_instComponents.push(resp);
    
    pra_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function pra_instRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pra_inst' ---
    // get current time
    t = pra_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *inst* updates
    if (t >= 0.0 && inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst.tStart = t;  // (not accounting for frame time here)
      inst.frameNStart = frameN;  // exact frame index
      
      inst.setAutoDraw(true);
    }

    
    // *resp* updates
    if (t >= 0.0 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
    }

    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['space'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[_resp_allKeys.length - 1].name;  // just the last key pressed
        resp.rt = _resp_allKeys[_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pra_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pra_instRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pra_inst' ---
    pra_instComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp.corr, level);
    }
    psychoJS.experiment.addData('resp.keys', resp.keys);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        routineTimer.reset();
        }
    
    resp.stop();
    // the Routine "pra_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp_pra_allKeys;
var praComponents;
function praRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pra' ---
    t = 0;
    praClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    st_pra.setPos([xpos_st, jit]);
    st_pra.setOri(ori_st);
    pr_pra.setPos([xpos_pr, ((ypos_pr * size) + jit)]);
    pr_pra.setSize([w, 0]);
    resp_pra.keys = undefined;
    resp_pra.rt = undefined;
    _resp_pra_allKeys = [];
    // keep track of which components have finished
    praComponents = [];
    praComponents.push(fix);
    praComponents.push(st_pra);
    praComponents.push(pr_pra);
    praComponents.push(resp_pra);
    
    praComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function praRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pra' ---
    // get current time
    t = praClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix* updates
    if (t >= 0.5 && fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix.tStart = t;  // (not accounting for frame time here)
      fix.frameNStart = frameN;  // exact frame index
      
      fix.setAutoDraw(true);
    }

    
    // *st_pra* updates
    if (t >= 1.0 && st_pra.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      st_pra.tStart = t;  // (not accounting for frame time here)
      st_pra.frameNStart = frameN;  // exact frame index
      
      st_pra.setAutoDraw(true);
    }

    
    // *pr_pra* updates
    if (t >= 1.0 && pr_pra.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pr_pra.tStart = t;  // (not accounting for frame time here)
      pr_pra.frameNStart = frameN;  // exact frame index
      
      pr_pra.setAutoDraw(true);
    }

    
    // *resp_pra* updates
    if (t >= 1.0 && resp_pra.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_pra.tStart = t;  // (not accounting for frame time here)
      resp_pra.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_pra.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_pra.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_pra.clearEvents(); });
    }

    if (resp_pra.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_pra.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _resp_pra_allKeys = _resp_pra_allKeys.concat(theseKeys);
      if (_resp_pra_allKeys.length > 0) {
        resp_pra.keys = _resp_pra_allKeys[_resp_pra_allKeys.length - 1].name;  // just the last key pressed
        resp_pra.rt = _resp_pra_allKeys[_resp_pra_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    praComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function praRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pra' ---
    praComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_pra.corr, level);
    }
    psychoJS.experiment.addData('resp_pra.keys', resp_pra.keys);
    if (typeof resp_pra.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_pra.rt', resp_pra.rt);
        routineTimer.reset();
        }
    
    resp_pra.stop();
    // the Routine "pra" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var noise_3Components;
function noise_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'noise_3' ---
    t = 0;
    noise_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    noise_3Components = [];
    
    noise_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function noise_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'noise_3' ---
    // get current time
    t = noise_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    noise_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function noise_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'noise_3' ---
    noise_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "noise_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _m_resp_allKeys;
var main_instComponents;
function main_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'main_inst' ---
    t = 0;
    main_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instr2.setImage(inst2);
    m_resp.keys = undefined;
    m_resp.rt = undefined;
    _m_resp_allKeys = [];
    // keep track of which components have finished
    main_instComponents = [];
    main_instComponents.push(instr2);
    main_instComponents.push(m_resp);
    
    main_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function main_instRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'main_inst' ---
    // get current time
    t = main_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr2* updates
    if (t >= 0.0 && instr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr2.tStart = t;  // (not accounting for frame time here)
      instr2.frameNStart = frameN;  // exact frame index
      
      instr2.setAutoDraw(true);
    }

    
    // *m_resp* updates
    if (t >= 0.0 && m_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      m_resp.tStart = t;  // (not accounting for frame time here)
      m_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { m_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { m_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { m_resp.clearEvents(); });
    }

    if (m_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = m_resp.getKeys({keyList: ['space'], waitRelease: false});
      _m_resp_allKeys = _m_resp_allKeys.concat(theseKeys);
      if (_m_resp_allKeys.length > 0) {
        m_resp.keys = _m_resp_allKeys[_m_resp_allKeys.length - 1].name;  // just the last key pressed
        m_resp.rt = _m_resp_allKeys[_m_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    main_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function main_instRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'main_inst' ---
    main_instComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(m_resp.corr, level);
    }
    psychoJS.experiment.addData('m_resp.keys', m_resp.keys);
    if (typeof m_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('m_resp.rt', m_resp.rt);
        routineTimer.reset();
        }
    
    m_resp.stop();
    // the Routine "main_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp2_allKeys;
var mainComponents;
function mainRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'main' ---
    t = 0;
    mainClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    st_main.setPos([xpos_st, jit]);
    st_main.setOri(ori_st);
    pr_main.setPos([xpos_pr, ((ypos_pr * size) + jit)]);
    pr_main.setSize([w, 0]);
    pr_main.setOri(ori_st);
    resp2.keys = undefined;
    resp2.rt = undefined;
    _resp2_allKeys = [];
    // keep track of which components have finished
    mainComponents = [];
    mainComponents.push(fix2);
    mainComponents.push(st_main);
    mainComponents.push(pr_main);
    mainComponents.push(resp2);
    
    mainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function mainRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'main' ---
    // get current time
    t = mainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix2* updates
    if (t >= 0.5 && fix2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix2.tStart = t;  // (not accounting for frame time here)
      fix2.frameNStart = frameN;  // exact frame index
      
      fix2.setAutoDraw(true);
    }

    
    // *st_main* updates
    if (t >= 1.0 && st_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      st_main.tStart = t;  // (not accounting for frame time here)
      st_main.frameNStart = frameN;  // exact frame index
      
      st_main.setAutoDraw(true);
    }

    
    // *pr_main* updates
    if (t >= 1.0 && pr_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pr_main.tStart = t;  // (not accounting for frame time here)
      pr_main.frameNStart = frameN;  // exact frame index
      
      pr_main.setAutoDraw(true);
    }

    
    // *resp2* updates
    if (t >= 1.0 && resp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp2.tStart = t;  // (not accounting for frame time here)
      resp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp2.clearEvents(); });
    }

    if (resp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp2.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _resp2_allKeys = _resp2_allKeys.concat(theseKeys);
      if (_resp2_allKeys.length > 0) {
        resp2.keys = _resp2_allKeys[_resp2_allKeys.length - 1].name;  // just the last key pressed
        resp2.rt = _resp2_allKeys[_resp2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    mainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mainRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'main' ---
    mainComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp2.corr, level);
    }
    psychoJS.experiment.addData('resp2.keys', resp2.keys);
    if (typeof resp2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp2.rt', resp2.rt);
        routineTimer.reset();
        }
    
    resp2.stop();
    // the Routine "main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var restComponents;
function restRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rest' ---
    t = 0;
    restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    restComponents = [];
    restComponents.push(text2);
    restComponents.push(key_resp);
    
    restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function restRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rest' ---
    // get current time
    t = restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text2* updates
    if (t >= 0.0 && text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text2.tStart = t;  // (not accounting for frame time here)
      text2.frameNStart = frameN;  // exact frame index
      
      text2.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rest' ---
    restComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp3_allKeys;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    resp3.keys = undefined;
    resp3.rt = undefined;
    _resp3_allKeys = [];
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(ending);
    endComponents.push(resp3);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ending* updates
    if (t >= 0.0 && ending.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ending.tStart = t;  // (not accounting for frame time here)
      ending.frameNStart = frameN;  // exact frame index
      
      ending.setAutoDraw(true);
    }

    
    // *resp3* updates
    if (t >= 0.0 && resp3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp3.tStart = t;  // (not accounting for frame time here)
      resp3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp3.clearEvents(); });
    }

    if (resp3.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp3.getKeys({keyList: ['space'], waitRelease: false});
      _resp3_allKeys = _resp3_allKeys.concat(theseKeys);
      if (_resp3_allKeys.length > 0) {
        resp3.keys = _resp3_allKeys[_resp3_allKeys.length - 1].name;  // just the last key pressed
        resp3.rt = _resp3_allKeys[_resp3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp3.corr, level);
    }
    psychoJS.experiment.addData('resp3.keys', resp3.keys);
    if (typeof resp3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp3.rt', resp3.rt);
        routineTimer.reset();
        }
    
    resp3.stop();
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
