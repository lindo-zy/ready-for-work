#!/usr/bin/python3
# -*- coding:utf-8 -*-
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # 包装器接受所有参数
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Do I have args?:")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")


function_with_no_argument()


# 输出
# Do I have args?:
# ()
# {}
# Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)


# 输出
# Do I have args?:
# (1, 2, 3)
# {}
# 1 2 3

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print("Do %s, %s and %s like platypus? %s" % \
          (a, b, c, platypus))


function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")


# 输出
# Do I have args ? :
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Indeed!'}
# Do Bill, Linus and Steve like platypus? Indeed!

class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):  # 可以加入一个默认值
        print("I am %s, what did you think ?" % (self.age + lie))


m = Mary()
m.sayYourAge()


# 输出
# Do I have args?:
# (<__main__.Mary object at 0xb7d303ac>,)
# {}
# I am 28, what did you think?


def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print('我创建了一个装饰器，获取的参数是:', decorator_arg1, decorator_arg2)

    def my_decorator(func):
        print('我是装饰器，传递来的参数是：', decorator_arg1, decorator_arg2)

        def wrapped(function_arg1, function_arg2):
            print('我是装饰器函数，装饰器传递来的参数是：', decorator_arg1, decorator_arg2,
                  '被装饰函数传递来的参数是：', function_arg1, function_arg2, '之后我将传递给被装饰器装饰的函数')

            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments('A', 'B')
def decorated_function_with_arguments(function_arg1, function_arg2):
    print('我是被装饰器装饰的函数，我的参数是：', function_arg1, function_arg2)


decorated_function_with_arguments('C', 'D')
'''
我创建了一个装饰器，获取的参数是: A B
我是装饰器，传递来的参数是： A B
我是装饰器函数，装饰器传递来的参数是： A B 被装饰函数传递来的参数是： C D 之后我将传递给被装饰器装饰的函数
我是被装饰器装饰的函数，我的参数是： C D
'''

c1 = 'zy'
c2 = 'csy'


@decorator_maker_with_arguments('pig', c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print('我是被装饰的函数，我的参数是：', function_arg1, function_arg2)


decorated_function_with_arguments(c2, 'love')
'''
我创建了一个装饰器，获取的参数是: pig zy
我是装饰器，传递来的参数是： pig zy
我是装饰器函数，装饰器传递来的参数是： pig zy 被装饰函数传递来的参数是： csy love 之后我将传递给被装饰器装饰的函数
我是被装饰的函数，我的参数是： csy love

'''


def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res

    return wrapper


def logging(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res

    return wrapper


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print(func.__name__, wrapper.count)
        return res

    wrapper.count = 0
    return wrapper


# 装饰器顺序从下往上执行
@counter
@benchmark
@logging
def reverse_string(string):
    return list(reversed(string))


print(reverse_string('abc'))
print(reverse_string('def'))
