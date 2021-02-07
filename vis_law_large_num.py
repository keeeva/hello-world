#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:48:47 2021

@author: Keegan
"""


# Just FYI for a listing of all possible colors run this code in the console:
    
#import matplotlib
#for name, hex in matplotlib.colors.cnames.items():
#    print(name, hex)


import matplotlib.pyplot as plt
import random 
import statistics
#import math
# this seed is extremely important so that 
# you can re-create the plot that I've generated
random.seed(10) 

# visualizing cumulative mean
# flipping a coin (can either be heads: 0, or tails:1)
# does it limit to the theoretical 0.5?

l = [0, 1]
m = []
val = []

for i in range(500):
    val.append(random.choice(l))
    m.append(statistics.mean(val))
    #print(val, "value")
    
hit_m = []
count = 0
for num in m:
    if 0.49 <= num <= 0.51:
        #print(num, count)
        hit_m.append(count)
    count += 1
        
y_hit_m = []
for num_two in range(len(hit_m)):
    y_hit_m.append(0.5)

    
# this is the style from R that I really like. It adds a gray background.
with plt.style.context('ggplot'): 
    plt.plot(m, color = "royalblue", alpha = 0.8)
#     plt.plot(m, color = "black", alpha = 0.2)
#     plt.ylim(0, 1)
#     plt.xlabel("nr. of trials")
#     plt.ylabel("cumulative mean")
#     plt.hlines(0.5, 0, 500, 
#                colors = "firebrick", 
#                linestyles= "solid", 
#                alpha = 0.5, 
#                linewidth = 1)
#     plt.title("Example of the Law of Large Numbers")
#     plt.plot()
# # adding some points
#     plt.scatter(hit_m, y_hit_m, c = "r")
    








