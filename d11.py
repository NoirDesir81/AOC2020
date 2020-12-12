# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:40:51 2020

@author: Notebook
"""
import numpy as np

def getNeighbours_p2(seat, grid):
    occ = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if not j == i == 0:
                c = 0
                d = 0
                val = '.'
                while val == '.':
                    if seat[0]+i+c in range(grid.shape[0]) and seat[1]+j+d in range(grid.shape[1]):
                        val = grid[seat[0]+i+c, seat[1]+j+d]
                        occ += (val=='#')
                    else:
                        val = 'o'
                    c += i
                    d += j
    return occ

def getNeighbours_p1(seat, grid):
    occ = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if not j == i == 0:
                if seat[0]+i in range(grid.shape[0]) and seat[1]+j in range(grid.shape[1]):
                    val = grid[seat[0]+i, seat[1]+j]
                    occ += (val=='#')
    return occ

def step(grid_in, getNeighbours, occlim):
    grid=grid_in.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            seat = (i,j)
            if grid_in[seat] == 'L' and getNeighbours(seat, grid_in) == 0:
                grid[seat] = '#'
            elif grid_in[seat] == '#' and getNeighbours(seat, grid_in) >= occlim:
                grid[seat] = 'L'
    return grid

def run(grid, getNeighbours, occlim):
    state = grid.copy()
    while True:
        newstate = step(state, getNeighbours, occlim)
        if (newstate==state).all():
            break
        else:
            state = newstate.copy()
    print(len(np.where(newstate=='#')[0]))


with open('C:/Users/Notebook/Documents/AOC/2020/input_d11.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]
    grid = np.array(grid)
    
occlim = [4, 5]    

for i, func in enumerate([getNeighbours_p1, getNeighbours_p2]):
    run(grid, func, occlim[i])


