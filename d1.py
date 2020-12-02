# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 06:41:44 2020

@author: Notebook
"""

numbers = []
with open('C:/Users/Notebook/Documents/AOC/2020/input_d1.txt') as f:
    for line in f:
        numbers.append(int(line.strip()))

found = False
for i in numbers:
    for j in numbers:
        if i+j == 2020:
            print(i*j)
            found=True
            break
    if found: 
        break

found = False
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i+j+k == 2020:
                print(i*j*k)
                found = True
                break
        if found:
            break
    if found: 
        break
