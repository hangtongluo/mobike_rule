# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 00:45:24 2017

@author: Administrator
"""
#对于有过去有记录的用户将预测他们过去的记录为现在的
import gc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

'''['orderid', 'userid', 'bikeid', 'biketype', 'starttime',
       'geohashed_start_loc', 'geohashed_end_loc', 'start_loc_lats',
       'start_loc_lons', 'end_loc_lats', 'end_loc_lons']'''

train_col = ['userid','geohashed_start_loc', 'geohashed_end_loc', 'start_loc_lats', 'start_loc_lons']
test_col = ['orderid', 'userid','geohashed_start_loc', 'start_loc_lats', 'start_loc_lons']

train = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/train_process.csv', nrows=None, usecols=train_col)
test = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/test_process.csv', nrows=None, usecols=test_col)
print(train.shape)
print(test.shape)
print('load data finishing...')

#对train进行处理
train = train.drop_duplicates(['userid','geohashed_start_loc','geohashed_end_loc'])
print(train.shape)

merge_data = pd.merge(test, train, on='userid', how='left')
merge_data['start_distance'] = (merge_data['start_loc_lats_x'] - merge_data['start_loc_lats_y'])**2 \
                            + (merge_data['start_loc_lons_x'] - merge_data['start_loc_lons_y'])**2
print('merge_data finishing...')

del train, test
gc.collect()
def drop_df(df):
    df = df.drop_duplicates('geohashed_end_loc')\
        .sort_values('start_distance', ascending=True)
    return df
merge_data = merge_data[['orderid','geohashed_end_loc','start_distance']][:100]
merge_data = merge_data.groupby('orderid').apply(drop_df)
merge_data.to_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/merge_data.csv', index=False)
print(merge_data[merge_data['orderid'] == 86458])
print('drop_df finishing...')

print('========================作出预测===============================')
def df_sub(df):
    if df.shape[0] >= 3:
        df['end_loc1'] = df['geohashed_end_loc'].values[0]
        df['end_loc2'] = df['geohashed_end_loc'].values[1]
        df['end_loc3'] = df['geohashed_end_loc'].values[2]
    if df.shape[0] == 2:
        df['end_loc1'] = df['geohashed_end_loc'].values[0]
        df['end_loc2'] = df['geohashed_end_loc'].values[1]
        df['end_loc3'] = 'missing'
    if df.shape[0] == 1:
        df['end_loc1'] = df['geohashed_end_loc'].values[0]
        df['end_loc2'] = 'missing'
        df['end_loc3'] = 'missing'
    if df.shape[0] == 0:
        df['end_loc1'] = 'missing'
        df['end_loc2'] = 'missing'
        df['end_loc3'] = 'missing'
    return df[['end_loc1','end_loc2','end_loc3']].drop_duplicates()

submit = merge_data.groupby('orderid').apply(df_sub).reset_index()[['orderid','end_loc1','end_loc2','end_loc3']]
print(submit)

submit.to_csv(r'F:\data\biendata\MOBIKE_CUP_2017\submit\submission.csv', index=False, header=None)



































