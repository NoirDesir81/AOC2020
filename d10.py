# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 06:27:10 2020

@author: Notebook
"""
import numpy as np

with open('C:/Users/Notebook/Documents/AOC/2020/input_d10.txt') as f:
    adapters=sorted([int(a.strip()) for a in f.readlines()])
    
adapters.insert(0, 0)
adapters.append(max(adapters)+3)
diffs = np.diff(adapters)

d1 = sum(d==1 for d in diffs)
d3 = sum(d==3 for d in diffs)
print(d1*d3)

groups = []
i = 0
c = 0
while i < len(diffs)-1:
    if diffs[i] == 1:
        c+=1
    else:
        groups.append(c)
        c = 0
    i += 1
    
combos = {'0': 1, '1': 1, '2': 2, '3': 4, '4': 7} # found by pen+paper method
total = 1
for g in groups:
    total *= combos[str(g)]
    
print(total)
