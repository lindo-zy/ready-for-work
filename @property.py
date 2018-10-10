#!/usr/bin/python3
# -*- coding:utf-8 -*-

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(10)
print(c.radius)
print(c.area)
print(c.perimeter)


class Foo:
    def __init__(self, val):
        self.__NAME = val

    @property
    def name(self):
        return self.__NAME

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('{0} must be str'.format(value))
        self.__NAME = value

    @name.deleter
    def name(self):
        raise TypeError('can not delete')


f = Foo('egon')
print(f.name)


# f.name = 10
# del f.name


class Foo:
    @property
    def name(self):
        print('get的时候运行我')

    @name.setter
    def name(self, value):
        print('set的时候运行我')

    @name.deleter
    def name(self):
        print('delete的时候运行我')


f = Foo()
f.name
f.name = 'a'
del f.name
