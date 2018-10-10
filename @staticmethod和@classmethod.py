#!/usr/bin/python3
# -*- coding:utf-8 -*-


def foo(x):  # 函数
    print('executing foo({0})'.format(x))


class A(object):
    def foo(self, x):  # 实例方法
        print('executing foo({0},{1})'.format(self, x))

    @classmethod  # 类方法
    def class_foo(cls, x):
        print('executing class_foo({0},{1})'.format(cls, x))

    @staticmethod  # 静态方法
    def static_foo(x):
        print('executing static_foo({0})'.format(x))


if __name__ == '__main__':
    x = 3
    foo(x)
    a = A()
    a.foo(x)
    print(a.foo)
    a.class_foo(x)
    print(a.class_foo)
    a.static_foo(x)
    print(type(a.static_foo))
    '''
    executing foo(3)
    executing foo(<__main__.A object at 0x000001C333249B70>,3)
    <bound method A.foo of <__main__.A object at 0x000001C333249B70>>
    executing class_foo(<class '__main__.A'>,3)
    <bound method A.class_foo of <class '__main__.A'>>
    executing static_foo(3)
    <class 'function'>
    '''
    a = 1
    # A.foo(a)  #报错
    A.class_foo(a)
    print(A.class_foo)
    A.static_foo(a)
    print(A.static_foo)
    '''
    executing class_foo(<class '__main__.A'>,1)
    <bound method A.class_foo of <class '__main__.A'>>
    executing static_foo(1)
    <function A.static_foo at 0x000001C3342B5730>
    '''
