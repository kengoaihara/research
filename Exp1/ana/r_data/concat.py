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
import itertools

# パスで指定したファイルの一覧をリスト形式で取得. （ここでは一階層下のtestファイル以下）

csv_files = glob.glob("*.csv")

#読み込むファイルのリストを表示
for a in csv_files:
    print(a)

#csvファイルの中身を追加していくリストを用意
data_list = []

#読み込むファイルのリストを走査
for file in csv_files:
    data_list.append(pd.read_csv(file))

#リストを全て行方向に結合
#axis=0:行方向に結合, sort
compact = pd.concat(data_list, axis=0, sort=True)

compact.to_csv("all.csv",index=False)
