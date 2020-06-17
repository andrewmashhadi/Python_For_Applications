#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Andrew Mashhadi
"""

#%% THE POSSIBLE TRICKS
# #  Name             Number
# -  nothing          1,302,540  # we will not include these
# -  one pair         1,098,240  # we will not include these
# -  two pair         123,552    # we will not include these
# -  three of a kind  54,912     # we will not include these
# -  straight         10,200     # we will not include these
# -  flush            5,108      # we will not include these
# 0  full house       3,744
# 1  four of a kind   624
# 2  straight flush   40

# We specify for each type of trick, 
# how many we'll use for training, 
# and how many we'll use for testing.

#train_size = [500, 100, 20]  # larger training sets
train_size = [ 28,  28,  8]
test__size = [ 50,  50, 20]

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

hands = [hands[trick == i] for i in range(6,9)] 

# You do not need to worry about how I created hands.
# But you should understand how the data in hands is stored.
# This should help you...
print('hands has type ', type(hands))
print('hands[0] has type ', type(hands[0]), '\n')

# hands[0] consists of full houses
# hands[1] consists of four of a kinds
# hands[2] consists of straight flushes

print('    full house:', hands[0][888])
print('four of a kind:', hands[1][ 88])
print('straight flush:', hands[2][ 28])
print('')

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
# print(test__samples[predict != correct])
# print(correct[predict != correct], predict[predict != correct])