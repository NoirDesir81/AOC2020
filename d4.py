# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:49:08 2020

@author: Notebook
"""

from functools import partial
import re

with open('C:/Users/Notebook/Documents/AOC/2020/input_d4.txt') as f:
    lines=f.readlines()
    
datasets = []
newdict = {}
for line in lines:
    if line=='\n':
        datasets.append(newdict.copy())
        newdict={}
    else:
        for item in line.strip().split():
            key, value = item.split(':')[0:2]
            newdict[key] = value
datasets.append(newdict.copy())


def checkYear(string, low, high):
    try:
        return low<=int(string)<=high
    except:
        return False

def checkHeight(string):
    try:
        cm = string.find('cm')
        inch = string.find('in')
        if cm > -1:
            if 150<=int(string[0:3])<=193:
                return True
        elif inch > -1:
            if 59<=int(string[0:2])<=76:
                return True
        else:
            return False
    except:
        return False

def checkExpression(string, pattern):
    return re.search(pattern, string) is not None

necessary = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
functions = [partial(checkYear, low=1920, high=2002),
             partial(checkYear, low=2010, high=2020),
             partial(checkYear, low=2020, high=2030),
             partial(checkHeight),
             partial(checkExpression, pattern='^#{1}[0-9,a-f]{6}$'),
             partial(checkExpression, pattern='(^amb$)|(^blu$)|(^brn$)|(^gry$)|(^grn$)|(^hzl$)|(^oth$)'),
             partial(checkExpression, pattern='^[0-9]{9}$')]
    
checkDict = dict(zip(necessary, functions))
    
present = 0
valid = 0

for data in datasets:
    if all([n in data for n in necessary]):
        present += 1
        if all([f(data[n]) for n, f in checkDict.items()]):
            valid += 1

print(present)
print(valid)

    