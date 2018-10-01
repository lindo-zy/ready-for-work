#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 快速排序

def quicksort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)

    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    array = [5, 8, 7, 9, 6, 4, 1, 2, 3]
    print(quicksort(array))
