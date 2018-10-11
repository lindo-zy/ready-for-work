#!/usr/bin/python3
# -*- coding:utf-8 -*-

a = 1
b = 1
print(id(a))
print(id(b))
print(a is b)
print(a == b)
'''
1693932592
1693932592
True
True

'''
a = 'a'
b = 'a'
print(id(a))
print(id(b))
print(a is b)
print(a == b)
'''
1441961844552
1441961844552
True
True
'''
a = [1]
b = [1]
print(id(a))
print(id(b))
print(a is b)
print(a == b)
'''
2300001792840
2300001893192
False
True

'''

a = (1, 2)
b = (1, 2)
print(id(a))
print(id(b))
print(a is b)
print(a == b)
'''
2300001891656
2300001892040
False
True

'''
a = {'a': 1}
b = {'a': 1}
print(id(a))
print(id(b))
print(a is b)
print(a == b)
'''
2299982059560
2299982059632
False
True

'''
