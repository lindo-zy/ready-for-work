#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 顺序单线程

from threading import Thread
import time


def my_counter():
    count = 0
    for i in range(1000000000):
        count += 1
    return True


def main1():
    thread_array = {}
    start_time = time.time()
    for i in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print('总共用时间:{0}'.format(end_time - start_time))


def main2():
    thread_array = {}
    start_time = time.time()
    for i in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_array[i] = t
    for j in range(2):
        thread_array[j].join()
    end_time = time.time()
    print('总共用时：{0}'.format(end_time - start_time))


if __name__ == '__main__':
    main1()  # 62.33681297302246
    # main2()  # 62.62918210029602
