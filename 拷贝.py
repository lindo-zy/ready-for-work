#!/usr/bin/python3
# -*- coding:utf-8 -*-

import copy

a = ['a', 1, ['zy', 2]]

b = a

c = copy.copy(a)
# c = a[:]

d = copy.deepcopy(a)

print(a, id(a))
print(b, id(b))

print(c, id(c))
print(d, id(d))
'''
['a', 1, ['zy', 2]] 2666045422344
['a', 1, ['zy', 2]] 2666045422344

['a', 1, ['zy', 2]] 2141879102088
['a', 1, ['zy', 2]] 2246737346184
'''

a.append(3)
a[2].append('csy')

print(a, id(a))
print(b, id(b))

print(c, id(c))
print(d, id(d))
'''
['a', 1, ['zy', 2, 'csy'], 3] 2330088160072
['a', 1, ['zy', 2, 'csy'], 3] 2330088160072

['a', 1, ['zy', 2, 'csy']] 2141879102088

['a', 1, ['zy', 2]] 2246737346184
'''
