#!/usr/bin/python3
# -*- coding:utf-8 -*-


class A:
    x = 1

    @classmethod
    def test(cls):
        print(cls, cls.x)


class B(A):
    x = 3


B.test()
