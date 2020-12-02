# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 06:08:11 2020

@author: Notebook
"""

import re

passwords = []
matching = []
rules = []

def getOccurences(string, pattern):
    pos = 0
    i = 0
    while pos > -1:
        pos = string.find(pattern)
        string = string[pos+1:]
        if pos > -1: 
            i+=1
    return i

valid = []
valid2 = []
with open('C:/Users/Notebook/Documents/AOC/2020/input_d2.txt') as f:
    for line in f:
        rules.append(line.split(':')[0].strip())
        passwords.append(line.split(':')[1].strip())
        
for i, rule in enumerate(rules):
    Nlow = int(rule.split('-')[0])
    Nhigh = int(rule.split('-')[1].split()[0])
    letter = rule.split('-')[1].split()[1]
    if Nlow <= getOccurences(passwords[i], letter) <= Nhigh:
        valid.append(passwords[i])
    if (passwords[i][Nlow-1] == letter) != (passwords[i][Nhigh-1] == letter):
        valid2.append(passwords[i])

print(len(valid))
print(len(valid2))




    #print(regex)
    