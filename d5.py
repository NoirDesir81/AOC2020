# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 06:11:52 2020

@author: Notebook
"""

def getSeatParameters(seat):
    row = seat[:7].replace('F', '0').replace('B', '1')
    row = int(row, base=2)    
    col = seat[7:].replace('L','0').replace('R', '1')
    col = int(col, base=2)
    return row, col, row*8+col

with open('C:/Users/Notebook/Documents/AOC/2020/input_d5.txt') as f:
    seats = f.readlines()
    
N = [getSeatParameters(seat)[2] for seat in seats]
print(max(N))

N = sorted(N)
for i in range(1, len(N)-1):
    if N[i]-N[i-1] == 2:
        print(N[i]-1)
        break