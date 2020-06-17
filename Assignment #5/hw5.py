#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Andrew Mashhadi
"""

#%%
import numpy as np
import matplotlib.image as mpimg

#%% Q1
a = mpimg.imread('a.jpg')
b = mpimg.imread('b.jpg')

from_y = (a.shape[0] - b.shape[0]) // 2
to_y = (a.shape[0] + b.shape[0]) // 2

from_x = (a.shape[1] - b.shape[1]) // 2
to_x = (a.shape[1] + b.shape[1]) // 2

c = a.copy()
c[from_y:to_y, from_x:to_x, :] = b

mpimg.imsave('c.jpg', c)

#%% Q2
d = mpimg.imread('d.jpg')
e = mpimg.imread('e.jpg')

abs_diff = np.abs(d.astype(np.int32) - e.astype(np.int32))
f = abs_diff.astype(np.uint8)

mpimg.imsave('f.jpg', f)

#%% Q3
minion = mpimg.imread('g.jpg')
shugga = mpimg.imread('h.jpg')

i = shugga.copy()
top_m = i.shape[0] - minion.shape[0]
left_m = (i.shape[1] - minion.shape[1]) // 2
right_m = (i.shape[1] + minion.shape[1]) // 2
sub_i = i[top_m:, left_m:right_m, :]

L1 = minion[:,:,0] <= 80
L2 = 180 <= minion[:,:,1]
L3 = minion[:,:,2] <= 60
bgPxls = L1 & L2 & L3

sub_i[~bgPxls] = minion[~bgPxls]

mpimg.imsave('i.jpg', i)