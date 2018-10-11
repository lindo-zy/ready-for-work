#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 使用__new__方法
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    a = 1


# 共享属性
class Borg:
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1


# 使用装饰器
def singleton(cls):
    instance = {}

    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton
class Myclass:
    a = 1


# import方法

class My_Singleton:
    def foo(self):
        pass


my_singleton = My_Singleton()

# 从其他地方导入这个包
# from mysingleton import my_singleton
# my_singleton.foo()
