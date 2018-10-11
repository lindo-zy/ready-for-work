#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random
import threading
import time


def thread_student(name):
    print(name, threading.current_thread().name)


def thread_process(name):
    thread_student(name)


# 生产者消费者模型,条件锁
queue = []
con = threading.Condition()


class Producer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue) > 5:
                    con.wait()
                else:
                    elem = random.randrange(5)
                    queue.append(elem)
                    print('生成元素{0},队列大小为{1}'.format(elem, len(queue)))
                    time.sleep(3)
                    con.notify()
                con.release()


class Consumer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue) < 0:
                    con.wait()
                else:
                    elem = queue.pop()
                    print('消费元素{0},队列大小为{1}'.format(elem, len(queue)))
                    time.sleep(3)
                    con.notify()
                con.release()


def main():
    for i in range(3):
        Producer().start()
    for i in range(2):
        Consumer().start()


# 多线程
def music(func):
    for i in range(2):
        print(func, time.ctime())
        time.sleep(1)


def movie(func):
    for i in range(2):
        print(func, time.ctime())
        time.sleep(4)


if __name__ == '__main__':
    # t1 = threading.Thread(target=thread_process, args=('thread_a',))
    # t2 = threading.Thread(target=thread_process, args=('thread_b',))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print('end!')

    # main()

    threads = []
    t1 = threading.Thread(target=music, args=('告白气球',))
    threads.append(t1)
    t2 = threading.Thread(target=movie, args=('肖申克的救赎',))
    threads.append(t2)
    for i in threads:
        i.setDaemon(True)
        i.start()
    i.join()
    print('end', time.ctime())
