# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:42:39 2017

@author: Administrator
"""

import gc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from dateutil.parser import parse


train = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/train_process.csv', nrows=None)
test = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/test_process.csv', nrows=None)

print(train.starttime.max(), train.starttime.min())
print(test.starttime.max(), test.starttime.min())

print(Counter(train.starttime.apply(lambda x: x[8:10])))
print(Counter(test.starttime.apply(lambda x: x[8:10])))

#通过观察数据将训练数据分为（两周：10-16/18-24(五17天)）、测试集
train['starttime'] = pd.to_datetime(train['starttime'])
test['starttime'] = pd.to_datetime(test['starttime'])

train_train = train[train.starttime < parse('2017-05-18')]
train_test = train[train.starttime >= parse('2017-05-18')]

train_train.to_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/train_train.csv', index=False)
train_test.to_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/train_test.csv', index=False)
test.to_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/test_test.csv', index=False)





































