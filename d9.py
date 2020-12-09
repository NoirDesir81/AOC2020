# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 06:25:29 2020

@author: Notebook
"""
from collections import deque

with open('C:/Users/Notebook/Documents/AOC/2020/input_d9.txt') as f:
    numbers=f.readlines()
    
check = []
store = numbers.copy()

for i in range(25):
    num = numbers.pop(0)
    check.append(int(num.strip()))

while numbers:
    num = int(numbers.pop(0).strip())
    valid = False
    for i in check:
        for j in check:
            if i+j == num and i != j:
                valid=True
    if not valid:
        print(num)
        break
    else:
        check.pop(0)
        check.append(num)

store = [int(s.strip()) for s in store]

found=False
for i in range(len(store)):
    for j in range(i+1, len(store)):
        test = sum(store[i:j])
        if test == num:
            found=True
            break
        elif test > num:
            break
    if found:
        weakness = min(store[i:j])+max(store[i:j])
        print(f'{i},{j}')
        print(f'{weakness}')
        break