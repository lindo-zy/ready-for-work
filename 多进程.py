#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 多进程
from multiprocessing import Process, Pool, Queue, Event, Lock
import os
import time


def run_proc(name):
    print('子进程', name, os.getpid())


# 进程间通信,使用Queue
def work_1(q):
    try:
        n = 1
        while n < 5:
            print('work_1,{0}'.format(n))
            q.put(n)
            time.sleep(1)
            n += 1
    except BaseException as e:
        print('work_1 error:', e)
    finally:
        print('work_1 end')


def work_2(q):
    try:
        n = 1
        while n < 5:
            print('work_2,{0}'.format(q.get()))
            time.sleep(1)
            n += 1
    except BaseException as e:
        print('work_2 error:', e)
    finally:
        print('work_2 end')


# 使用Event

def wait_for_event(e):
    print('等待event事件')
    e.wait()
    print(str(e.is_set()))


def wait_for_event_timeout(e, t):
    print('等待event事件，带有超时事件')
    e.wait(t)
    print(str(e.is_set()))


# 进程加锁
def worker_1(lock, file_name):
    lock.acquire()
    try:
        f = open(file_name, 'a+')
        f.write('hehe\n')
        f.close()
    finally:
        lock.release()
        print('work_1')


def worker_2(lock, file_name):
    lock.acquire()
    try:
        f = open(file_name, 'a+')
        f.write('haha\n')
        f.close()
    finally:
        lock.release()
        print('work_2')


if __name__ == '__main__':
    # print('父进程', os.getpid())
    # p = Process(target=run_proc, args=('test',))
    # p.start()
    # p.join()
    # print('子进程结束！')

    # 使用进程池
    # pool = Pool(processes=3)
    # for i in range(4):
    #     message = 'hello world {0}'.format(i)
    #     pool.apply_async(func=run_proc, args=(message,))
    # pool.close()
    # pool.join()
    # print('进程池结束!')

    # q = Queue()
    # p1 = Process(target=work_1, args=(q,))
    # p2 = Process(target=work_2, args=(q,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # print('end!')

    # e = Event()
    # p1 = Process(target=wait_for_event, args=(e,))
    # p2 = Process(target=wait_for_event_timeout, args=(e, 2,))
    # p1.start()
    # p2.start()
    # time.sleep(3)
    # e.set()
    # print('设置event')

    lock = Lock()
    f = '1.txt'
    p1 = Process(target=worker_1, args=(lock, f,))
    p2 = Process(target=worker_2, args=(lock, f,))
    p1.start()
    p2.start()
    print('end')
    '''
    end
    work_2
    work_1
    文本内容:haha hehe
    '''
