# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 22:18:39 2017

@author: Administrator
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

nrows = 10000 #测试代码
#nrows = None

print('loading data starting...')
train = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/train_process.csv', nrows=nrows)
test = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/test_process.csv', nrows=nrows)
print('loading data finishing...')

#做一个基于密度的聚类
print('cluster data starting...')
db = DBSCAN(eps=0.3, min_samples=10).fit(train[['start_loc_lats','start_loc_lons']])
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)






















