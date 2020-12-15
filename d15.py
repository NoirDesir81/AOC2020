# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 06:33:59 2020

@author: Notebook
"""
from collections import deque

with open('C:/Users/Notebook/Documents/AOC/2020/input_d15.txt') as f:
    stack = [int(i) for i in f.read().split(',')]

read = {}
start = len(stack)
seen = []

stack = deque(stack)
for j in range(0,30000000):
    check = stack.popleft()
    if str(check) not in read:
        read[str(check)] = j
        if j >= start-1:
            stack.appendleft(0)
    else:
        stack.appendleft(j-read[str(check)])
        read[str(check)] = j
