#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import islice


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(list(islice(fib(), 5)))
