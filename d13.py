# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 07:15:47 2020

@author: Notebook
"""

def Bezout(a, b):    
    r = [a, b]
    q = []
    s = [1, 0]
    t = [0, 1]
    
    i = 0
    rem = 1
    while rem != 0:
        rem = r[i] % r[i+1]
        quot = (r[i]-rem) / r[i+1]
        r.append(rem)
        q.append(quot)
        s.append(s[i] - quot*s[i+1])
        t.append(t[i] - quot*t[i+1])
        if rem != 0:
            i+=1
    
    return int(t[-2]), int(s[-2])

with open('C:/Users/Notebook/Documents/AOC/2020/input_d13.txt') as f:
    for i, line in enumerate(f):
        if i == 0:
            timestamp = int(line)
        else:
            buses = [int(b) for b in line.split(',') if b != 'x']
            busd = [[N, int(b)] for N, b in enumerate(line.split(',')) if b != 'x']
    
Found=False
sortedbus = list(sorted(busd, key=lambda x: x[1]))
sortedbus = sortedbus[-1::-1]

i = 0
k = 0

a = [sb[1]-sb[0] if sb[0]!= 0 else 0 for sb in sortedbus ]
n = [sb[1] for sb in sortedbus]

test1 = a[0]
test2 = a[1]
n2 = n[1]
n1 = n[0]

res = []
k = 1
while k < len(n):
    m2, m1 = Bezout(n1, n2)
    x = test1*m2*n2 + test2*m1*n1
    res.append(x)
    test1 = x % (n1*n2)
    if k == len(n)-1:
        break
    k+=1
    n1 *= n2
    n2 = n[k]
    test2 = a[k]

print(test1)
