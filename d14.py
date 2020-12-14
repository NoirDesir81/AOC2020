# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 07:57:16 2020

@author: Notebook
"""

with open('C:/Users/Notebook/Documents/AOC/2020/input_d14.txt') as f:
    file = f.readlines()

def pad(string, N):
    for i in range(N-len(string)):
        string = '0'+string
    return string

def getAddresses(bitmask):
    space = []
    out = []
    space.append(bitmask)
    while space:
        bm = space.pop()
        pos = bm.find('X')
        if pos >= 0:
            bm1 = bm[:pos]+'1'+bm[pos+1:]
            bm2 = bm[:pos]+'0'+bm[pos+1:]
            space.extend([bm1, bm2])
        else:
            out.append(bm)
    return out

# p2
memory = {}
for line in file:
    if line.split('=')[0].strip() == 'mask':
        memory['mask'] = line.split('=')[1].strip()
    else:
        address = line.split('=')[0].strip()[line.split('=')[0].strip().find('[')+1:line.split('=')[0].strip().find(']')]
        address = pad(bin(int(address))[2:], 36)
        value=int(line.split('=')[1].strip())
        add = ''
        for i, char in enumerate(memory['mask']):
            if char == 'X' or char == '1':
                add += char
            else:
                add += address[i]
        for address in getAddresses(add):
            memory[address] = value

# p1
memory1 = {}
for line in file:
    if line.split('=')[0].strip() == 'mask':
        memory1['mask'] = line.split('=')[1].strip()
    else:
        address = line.split('=')[0].strip()[line.split('=')[0].strip().find('[')+1:line.split('=')[0].strip().find(']')]
        bitfield = bin(int(line.split('=')[1].strip()))[2:]
        bitfield = pad(bitfield, 36)
        for i, char in enumerate(memory1['mask']):
            if char != 'X':
                bitfield = bitfield[0:i]+char+bitfield[i+1:]
        memory1[address] = int(bitfield, base=2)

for m in [memory1, memory]:
    s = 0
    for key, value in m.items():
         if key != 'mask':
             s += value
    print(s)