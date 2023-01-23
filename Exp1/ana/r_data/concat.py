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

# �p�X�Ŏw�肵���t�@�C���̈ꗗ�����X�g�`���Ŏ擾. �i�����ł͈�K�w����test�t�@�C���ȉ��j

csv_files = glob.glob("*.csv")

#�ǂݍ��ރt�@�C���̃��X�g��\��
for a in csv_files:
    print(a)

#csv�t�@�C���̒��g��ǉ����Ă������X�g��p��
data_list = []

#�ǂݍ��ރt�@�C���̃��X�g�𑖍�
for file in csv_files:
    data_list.append(pd.read_csv(file))

#���X�g��S�čs�����Ɍ���
#axis=0:�s�����Ɍ���, sort
compact = pd.concat(data_list, axis=0, sort=True)

compact.to_csv("all.csv",index=False)
