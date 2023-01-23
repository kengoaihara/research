import pandas as pd
from psychopy import prefs
import numpy as np
import glob
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import openpyxl
import itertools

lists = ["data0630a.csv", "data0630b.csv", "data0701a.csv","data0701c.csv","data0702a.csv",
        "data0702b.csv", "data0704a.csv", "data0705a.csv", "data0705b.csv", "data0706a.csv",
        "data0707a.csv","data0707b.csv", "data0708a.csv", "data0708b.csv", "data0708c.csv",
        "data0708d.csv", "data0710a.csv","data0710b.csv", "data0712a.csv", "data0713a.csv"]
        
names = ["data0630a", "data0630b", "data0701a","data0701c","data0702a",
        "data0702b", "data0704a", "data0705a", "data0705b", "data0706a",
        "data0707a","data0707b", "data0708a", "data0708b", "data0708c",
        "data0708d", "data0710a","data0710b", "data0712a", "data0713a"]

num = 0 
i  = "data0630a.csv"

for i in lists:
  dat = pd.read_csv("C:/Users/User/Desktop/exp1/raw/" +i)

  dat2 = dat.loc[:, ['ori_st', 'ori_pr', 'xpos_st','xpos_pr','resp.keys', 'resp.rt', 'size']]
  dat1 = dat.loc[:, ['participant']]

  #replace figure as icon
  dat3 = dat2.replace(180, 'I').replace(0, 'U')
  dat3['cond'] = dat3['ori_st'] + dat3['ori_pr']

  #practice trial is removed.
  
  dat5 = dat3.replace(-4, 'left')
  dat6 = dat5.replace(4, 'right')
  dat7 = dat6.replace("f", 'left')
  dat8 = dat7.replace("j", 'right')
  
  dat8['y'] = dat8['xpos_st'] + dat8['resp.keys']
  
  dat9 = dat8.replace('leftleft', 0).replace('rightright', 0).replace('rightleft', 1).replace('leftright', 1)

  #resp
  dat9["x"] = dat9["size"]
  dat9["rt"] = dat9["resp.rt"]
  dat9["sub"] = dat1["participant"]
  
  dat12 = dat9.dropna(how='any')

  dat13 = dat12.loc[:, ['sub','cond', 'x', 'y','rt']]

  dat13.to_csv("C:/Users/User/Desktop/exp1/r_data/"+ names[num] + "_r.csv")
  
  num = num + 1

d = pd.read_csv("data0708a_r.csv")
d2 = d.replace("m", "g")
d3 = d2.loc[:, ['sub','cond', 'x', 'y','rt']]
d3.to_csv("C:/Users/User/Desktop/exp1/r_data/data0708a_r.csv")

f = pd.read_csv("data0710a_r.csv")
f2 = f.replace("q", "l")
f3 = f2.loc[:, ['sub','cond', 'x', 'y','rt']]
f3.to_csv("C:/Users/User/Desktop/exp1/r_data/data0710a_r.csv")
