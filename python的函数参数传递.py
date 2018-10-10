#!/usr/bin/python3
# -*- coding:utf-8 -*-

a = 1


def fun(a):
    print(a, id(a))
    a = 3
    print(a, id(a))


print(a, id(a))
fun(a)
print(a, id(a))
'''
1 1622367280
1 1622367280
3 1622367344
1 1622367280

'''
b = []


def func(b):
    print(b, id(b))
    b.append(3)
    print(b, id(b))


print(b, id(b))
func(b)
print(b, id(b))

'''
[] 2352533549576
[] 2352533549576
[3] 2352533549576
[3] 2352533549576
'''
