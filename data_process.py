# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:08:02 2017

@author: Administrator
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from geohash import decode, decode_exactly

train = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/train.csv', nrows=None)
test = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/test.csv', nrows=None)

#通过geohash解码出具体的经纬度信息
#train['start_loc_lats'] = train['geohashed_start_loc'].apply(lambda x: decode(x)[0])
#train['start_loc_lons'] = train['geohashed_start_loc'].apply(lambda x: decode(x)[1])
#
#train['end_loc_lats'] = train['geohashed_end_loc'].apply(lambda x: decode(x)[0])
#train['end_loc_lons'] = train['geohashed_end_loc'].apply(lambda x: decode(x)[1])
#
#test['start_loc_lats'] = test['geohashed_start_loc'].apply(lambda x: decode(x)[0])
#test['start_loc_lons'] = test['geohashed_start_loc'].apply(lambda x: decode(x)[1])

train['start_loc_lats'] = train['geohashed_start_loc'].apply(lambda x: decode_exactly(x)[0])
train['start_loc_lons'] = train['geohashed_start_loc'].apply(lambda x: decode_exactly(x)[1])

train['end_loc_lats'] = train['geohashed_end_loc'].apply(lambda x: decode_exactly(x)[0])
train['end_loc_lons'] = train['geohashed_end_loc'].apply(lambda x: decode_exactly(x)[1])

test['start_loc_lats'] = test['geohashed_start_loc'].apply(lambda x: decode_exactly(x)[0])
test['start_loc_lons'] = test['geohashed_start_loc'].apply(lambda x: decode_exactly(x)[1])


train.to_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/train_process.csv', index=False)
test.to_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/test_process.csv', index=False)




































