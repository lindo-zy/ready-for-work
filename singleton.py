#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 单例模式
class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


a = Singleton(18, 'dg')
b = Singleton(8, 'ac')
a.age = 19
print(b.age)
