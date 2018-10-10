#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 迭代器
mylist = [x for x in range(3)]
for i in mylist:
    print(i)

# 生成器

mylist = (x for x in range(3))
for i in mylist:
    print(i)


# yield
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i  # 返回一个迭代对象


mygenrator = createGenerator()
print(mygenrator)  # <generator object createGenerator at 0x0000020F4998FAF0>
for i in mygenrator:
    print(i)

# 生成器相当节约内存
# import sys  sys.getsizeof()方法可以查看内存
