# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 05:52:12 2020

@author: Notebook
"""
import numpy as np

with open('C:/Users/Notebook/Documents/AOC/2020/input_d12.txt') as f:
    inst = [r.strip() for r in f.readlines()]
    
directions = ['N', 'E', 'S', 'W']
pos = [0, 0]
direct = 1

move={'N': [-1, 0], 'E': [0, 1], 'S': [1, 0], 'W':[0, -1]}

for i in inst:
    letter=i[0]
    num=int(i[1:])
    if letter in move:
        pos = np.add(np.multiply(num, move[letter]), pos)
    elif letter == 'F':
        pos = np.add(np.multiply(num, move[directions[direct]]), pos)
    elif letter == 'R':
        direct = (direct + int(num/90)) % 4
    elif letter == 'L':
        direct = (direct - int(num/90)) % 4
    print(pos)

print(abs(pos[0])+abs(pos[1]))

turns=[1, -1] # rotation matrix
rdir = {'R': 1, 'L': -1}
       
wp = [-1, 10]
pos = [0, 0]
for i in inst:
    letter=i[0]
    num=int(i[1:])
    if letter in move:
        wp = np.add(np.multiply(num, move[letter]), wp)
    elif letter in rdir:
        steps = int(num/90)
        for t in range(steps):
            oldwp=wp.copy()
            wp[0]=oldwp[1]*turns[0]*rdir[letter]
            wp[1]=oldwp[0]*turns[1]*rdir[letter]
    elif letter == 'F':
        pos = np.add(np.multiply(num, wp), pos)

print(abs(pos[0])+abs(pos[1]))



















