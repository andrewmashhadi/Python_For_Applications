#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Andrew Mashhadi
"""

import numpy as np
import matplotlib.image as mpimg

#%% PART A

jb = mpimg.imread('jb.jpg')
jb_barrel_A = mpimg.imread('barrel.jpg').copy()

top_y = (jb_barrel_A.shape[0] - jb.shape[0]) // 2
bottom_y = (jb_barrel_A.shape[0] + jb.shape[0]) // 2

left_x = (jb_barrel_A.shape[1] - jb.shape[1]) // 2
right_x = (jb_barrel_A.shape[1] + jb.shape[1]) // 2

jb_barrel_A[top_y:bottom_y, left_x:right_x, :] = jb

mpimg.imsave('jb_barrel_A.jpg', jb_barrel_A)


#%% PART B

jb = mpimg.imread('jb.jpg')
jb_barrel_B = mpimg.imread('barrel.jpg').copy()

jb_small = jb[:400, :, :]

left_x = (jb_barrel_B.shape[1] - jb.shape[1]) // 2
right_x = (jb_barrel_B.shape[1] + jb.shape[1]) // 2

jb_barrel_B[165:(165 + jb_small.shape[0]), left_x:right_x, :] = jb_small

mpimg.imsave('jb_barrel_B.jpg', jb_barrel_B)


#%% PART C

jb = mpimg.imread('jb.jpg')
jb_barrel_C = mpimg.imread('barrel.jpg').copy()

left_x = (jb_barrel_C.shape[1] - jb.shape[1]) // 2
right_x = (jb_barrel_C.shape[1] + jb.shape[1]) // 2

jb_small = jb[:400, :, :]
sub_barrel = jb_barrel_C[165:(165 + jb_small.shape[0]), left_x:right_x, :]

L =  sub_barrel > 150
L = L.all(axis = 2)
sub_barrel[L] = jb_small[L]

mpimg.imsave('jb_barrel_C.jpg', jb_barrel_C)







