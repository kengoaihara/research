import pandas as pd
from psychopy import prefs
import numpy as np
import glob
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import openpyxl
import itertools

#data1015a.csv
#data1015c.csv
#data1018b.csv
#data1019b.csv
#data1022a.csv
#data1029b.csv
#data1030a.csv
#data1015b.csv

lists = ["data1015a.csv", "data1015c.csv", "data1015c.csv","data1018b.csv","data1019b.csv",
        "data1022a.csv", "data1029b.csv", "data1030a.csv"]
        
names = ["data1015a",  "data1015c", "data1015c","data1018b","data1019b",
        "data1022a", "data1029b", "data1030a"]

num = 0

for i in lists:
  dat = pd.read_csv("/cloud/project/raw/" + i)

  dat2 = dat.loc[:, [
  'ori_st', 'ypos_pr', 'size', 
  'resp2.keys', 'resp2.rt',]]

  #replace figure as icon
  dat3 = dat2.replace(0, 'U').replace(180, 'I')
  dat4 = dat3.replace(2, 'T').replace(-2, 'D')
  dat5 = dat4.replace('resp2.rt', 'rt')

  dat5['cond'] = dat5['ori_st'] + dat5['ypos_pr']
  dat6 = dat5.replace('UT', 'UV').replace('UD', 'UB').replace('ID', 'IV').replace('IT', 'IB')

  #practice trial is removed.
  dat7 = dat6.dropna(how='any')

  #disalignment from baseline
  dat7['x'] = dat7['cond'] + dat7['size'].astype(str)
  dat8 = dat7.replace('UV1.4', '+0.8').replace('UV1.2', '+0.4').replace('UV1.1', '+0.2').replace('UV1.0', 0).replace('UV0.9', '-0.2').replace('UV0.8', '-0.4').replace('UV0.6', '-0.8')
  dat9 = dat8.replace('IB1.4', '+0.8').replace('IB1.2', '+0.4').replace('IB1.1', '+0.2').replace('IB1.0', 0).replace('IB0.9', '-0.2').replace('IB0.8', '-0.4').replace('IB0.6', '-0.8')
  dat10 = dat9.replace('UB1.4', '-0.8').replace('UB1.2', '-0.4').replace('UB1.1', '-0.2').replace('UB1.0', 0).replace('UB0.9', '+0.2').replace('UB0.8', '+0.4').replace('UB0.6', '+0.8')
  dat11 = dat10.replace('IV1.4', '-0.8').replace('IV1.2', '-0.4').replace('IV1.1', '-0.2').replace('IV1.0', 0).replace('IV0.9', '+0.2').replace('IV0.8', '+0.4').replace('IV0.6', '+0.8')

  #resp
  dat12 = dat11.replace('j', 1).replace('f', 0)
  dat12["y"] = dat12["resp2.keys"]
  dat12["rt"] = dat12["resp2.rt"]
  dat12["sub"] = dat["participant"]
  
  dat12 = dat12.dropna(how='any')

  dat12 = dat12.loc[:, ['sub','cond', 'x', 'y','rt']]

  dat12.to_csv("/cloud/project/r_data/"+ names[num] + "_r.csv")
  num = num +1
