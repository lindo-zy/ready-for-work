#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 列表推导式

m = [i for i in range(10) if i % 3 is 0]
print(m)  # [0, 3, 6, 9]


def add(x):
    return x + 1


m = [add(i) for i in range(10) if i % 3 == 0]
print(m)  # [1, 4, 7, 10]

# 得到生成器
m = (i for i in range(10) if i % 3 == 0)
print(list(m))

# 字典推导式
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# 快速变换k-v
mcase_f = {v: k for k, v in mcase.items()}
print(mcase_f)

# 集合推导式
squared = {x ** 2 for x in [1, 1, 3]}
print(squared)  # {1, 9}
