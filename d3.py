# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 06:37:05 2020

@author: Notebook
"""
grid = []
import numpy as np

with open('C:/Users/Notebook/Documents/AOC/2020/input_d3.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
        
gridarray = np.array(grid)
depth, width = gridarray.shape

vect = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
totaltrees=1
for v in vect:
    row=0
    col=0
    trees = 0
    while row <= depth:
        row += v[0]
        col += v[1]
        col %= width
        try:
            if gridarray[row, col] == '#':
                trees += 1
        except:
            break
    totaltrees*=trees
    if v == [1, 3]:
        print (trees)

print (totaltrees)