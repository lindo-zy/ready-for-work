#!/usr/bin/python3
# -*- coding:utf-8 -*-

class A:
    def __init__(self):
        self.__x = 3
        self._y = 4
        self.z = 5


a = A()

# print(a.__x)  #报错
print(a._A__x)  # 3
print(a._y)  # 4
print(a.z)  # 5
