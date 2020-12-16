# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 06:08:48 2020

@author: Notebook
"""

from collections import defaultdict

with open('C:/Users/Notebook/Documents/AOC/2020/input_d16.txt') as f:
    data = f.read()
    
rules = data.split('\n\n')[0]
myticket = data.split('\n\n')[1].strip()
tickets = data.split('\n\n')[2].strip()

rulesDict = {}
for line in rules.split('\n'):
    items = line.split(':')
    rule = items[0]
    ranges = items[1].split('or')
    rstart = [r.split('-')[0].strip() for r in ranges]
    rstop = [r.split('-')[1].strip() for r in ranges]
    rulesDict[rule] = [[int(rstart[0]), int(rstop[0])], [int(rstart[1]), int(rstop[1])]]

tickets = tickets.split('\n')
tickets.pop(0)
invalidTickets = []

# p1
invalid = 0
for i, ticket in enumerate(tickets):
    numbers = [int(n) for n in ticket.strip().split(',')]
    for n in numbers:
        valid = False
        for v in rulesDict.values():
            for rang in v:
                if rang[0] <= n <= rang[1]:
                    valid = True
            if valid:
                break
        if not valid:
            invalid += n
            invalidTickets.append(ticket)
            break
print(invalid)

#p2
for iT in invalidTickets:
    tickets.remove(iT)            

valDicts = []
for ticket in tickets:
    numbers = [int(n) for n in ticket.strip().split(',')]
    validDict = defaultdict(list)
    for i, n in enumerate(numbers):
        for k, v in rulesDict.items():
            for rang in v:
                if rang[0] <= n <= rang[1]:
                    validDict[k].append(i)
    valDicts.append(validDict)

availableDict = {}
for rule in rulesDict.keys():
    available = list(range(0, len(rulesDict)))
    for vD in valDicts:
        for a in available:
            if a not in vD[rule]:
                available.remove(a)
    availableDict[rule] = available.copy()
                
avSorted = list(sorted(availableDict.items(), key = lambda item: len(item[1]) ))
match = {}
ignore = []
for i, a in enumerate(avSorted):
    for ig in ignore:
        a[1].remove(ig)
    match[a[0]] = a[1]
    ignore.extend(a[1])

myticketVals = [int(v) for v in myticket.split('\n')[1].strip().split(',')]

result = 1
for m, v in match.items():
    if 'departure' in m:
        result *= myticketVals[v[0]]
print(result)
