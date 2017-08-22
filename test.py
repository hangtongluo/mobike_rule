# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:49:58 2017

@author: Administrator
"""
import gc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#nrows = 10
nrows = None
merge_data = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/data_process/merge_data.csv', nrows=nrows)
print(merge_data)

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






















