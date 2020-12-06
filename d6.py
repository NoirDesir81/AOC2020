# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 07:37:04 2020

@author: Notebook
"""
def compareStrings(strings):
    compare = ''
    for char in strings[0]:
        if all([char in string for string in strings]):
            compare += char
    return compare

with open('C:/Users/Notebook/Documents/AOC/2020/input_d6.txt') as f:
    groups = f.read().split('\n\n')
    
Nany = 0
Nall = 0

for g in groups:
    Nany += len(set(''.join(g.split())))
    Nall += len(compareStrings(g.split()))

print(Nany)
print(Nall)