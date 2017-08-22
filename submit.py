# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 17:32:06 2017

@author: Administrator
"""
import gc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#nrows = 10
nrows = None
#==============================================================================
# submission_fillna = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/submit/submission_fillna.csv', nrows=nrows, header=None)
# 
# #print(submission_fillna)
# 
# #submission_fillna[submission_fillna[3] == 'missing'] = np.nan
# submission_fillna[submission_fillna[3] == 'missing'][[1,2,3]] = 'missing'
# print(submission_fillna)
# submission_fillna.to_csv(r'F:\data\biendata\MOBIKE_CUP_2017\submit\submission_rule1.csv', index=False, header=None)
#==============================================================================


submission_rule1 = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/submit/submission_rule1.csv', nrows=nrows, header=None)
#submission_rule1
submission_rule1[2] = 'missing'
submission_rule1.to_csv(r'F:\data\biendata\MOBIKE_CUP_2017\submit\submission_rule1-1.csv', index=False, header=None)

submission_rule1 = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/submit/submission_rule1.csv', nrows=nrows, header=None)
submission_rule1[3] = 'missing'
submission_rule1.to_csv(r'F:\data\biendata\MOBIKE_CUP_2017\submit\submission_rule1-2.csv', index=False, header=None)

submission_rule1 = pd.read_csv(r'F:/data/biendata/MOBIKE_CUP_2017/submit/submission_rule1.csv', nrows=nrows, header=None)
submission_rule1[2] = 'missing'
submission_rule1[3] = 'missing'
submission_rule1.to_csv(r'F:\data\biendata\MOBIKE_CUP_2017\submit\submission_rule1-3.csv', index=False, header=None)




#0.02172096199892601
#0.006548190810165999
#0.028269152809092007












