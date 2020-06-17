#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Andrew Mashhadi
"""

import numpy as np

#%% PREPROCESSING
def preprocess(data):
    
    cols = data.shape[1]
    rank = data % 13
    
    diff_by_1 = rank[:, :cols-1] - rank[:, 1:]
    diff_by_2 = rank[:, :cols-2] - rank[:, 2:]
    diff_by_3 = rank[:, :cols-3] - rank[:, 3:]
    diff_by_4 = rank[:, :cols-4] - rank[:, 4:]
    
    diff = (diff_by_1, diff_by_2, diff_by_3, diff_by_4)
    feat = np.abs(np.concatenate(diff, axis = 1))
    
    # Helps with straights containing kings and aces
    feat[feat == 12] = 1
    
    feat.sort(axis = 1)
    
    return feat
                
    