# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:48:06 2020

@author: Notebook
"""
from treelib import Tree
from copy import deepcopy

class Rule():
    def __init__(self, name, children, data):
        self.name = name
        self.children = children
        self.data = data
        self.discovered = False
        self.value = 1
        
Rules = {}

with open('C:/Users/Notebook/Documents/AOC/2020/input_d7.txt') as f:
    rules = f.readlines()
    tree = Tree()
    tree.create_node('root', 'root')
    
for r in rules:
    name = r.split('bags')[0].strip().replace(' ','')
    children_raw = r.split('contain')[1].split(',')
    if 'no' in children_raw [0]:
        children=[]
    else:
        data =[]
        children=[]
        for cr in children_raw:
            data.append(int(cr.split()[0]))
            children.append((cr.split()[1]+cr.split()[2]).strip())
    Rules[name] = Rule(name, children, data)

stack = []
for rule in Rules.values():
    if 'shinygold' in rule.children:
        stack.append(rule)

while stack:
    v = stack.pop()
    if not Rules[v.name].discovered:
        Rules[v.name].discovered = True
        for rule in Rules.values():
            if v.name in rule.children:
                stack.append(rule)
i=0
for rule in Rules.values():
    i += rule.discovered
print(i)

stack = []
stack.append(Rules['shinygold'])
bags=0
while stack:
    v = stack.pop()
    bags += v.value
    for i, c in enumerate(v.children):
        toappend = deepcopy(Rules[c])
        toappend.value=v.value*v.data[i]
        stack.append(toappend)
print(bags-1) # do not count shiny gold bag
