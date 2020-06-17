#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

#%% THE POSSIBLE TRICKS
# #  Name             Number
# 0  nothing          1,302,540
# 1  one pair         1,098,240
# 2  two pair         123,552
# 3  three of a kind  54,912
# 4  straight         10,200
# 5  flush            5,108
# 6  full house       3,744
# 7  four of a kind   624
# 8  straight flush   40

# We specify for each type of trick, 
# how many we'll use for training, 
# and how many we'll use for testing.

train_size = [ 400, 100,  50,  50, 100, 400,  50,  50,  8]
test__size = [ 800, 100, 100, 100, 800, 800, 100, 100, 20]

#%% IMPORTS
import json
import numpy as np
from hw6 import preprocess
from sklearn.svm import SVC
from itertools import combinations as choose

#%% GENERATING ALL HANDS
cards = range(52)
hands = np.array(list(choose(cards, 5)), dtype = np.int8)

with open('trick.json') as f:
    trick = np.array(json.load(f), dtype = np.int8)

hands = [hands[trick == i] for i in range(9)]

#%% PARTITION HANDS INTO TRAINING AND TESTING SETS AND CREATE TARGETS
def partition(h, train, test):
    l = len(h)
    p = np.random.permutation(l)
    h = h[p]

    assert train > 0 and test > 0 and train + test <= l
    return h[:train], h[-test:]

N = len(hands)
samples = [partition(hands[i], train_size[i], test__size[i]) for i in range(N)]

train_samples = np.concatenate( [samples[i][0] for i in range(N)] )
test__samples = np.concatenate( [samples[i][1] for i in range(N)] )

train_targets = np.array([i for i in range(N) 
                            for _ in range(train_size[i])], dtype = np.int8)
test__targets = np.array([i for i in range(N) 
                            for _ in range(test__size[i])], dtype = np.int8)

#%% TRAIN THE SVC AND TEST ITS ACCURACY
clf = SVC(kernel = 'linear')
clf.fit(preprocess(train_samples), train_targets)

predict = clf.predict(preprocess(test__samples))
correct = test__targets

print('accuracy ==')
print(100 * np.count_nonzero(predict == correct) / len(correct))

# SHOW INFO ABOUT WRONG PREDICTIONS
print(test__samples[predict != correct])
print(correct[predict != correct], predict[predict != correct])