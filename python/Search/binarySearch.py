#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
二分查找
二分查找的前提是数据有序
'''

def binarySearch(alist,item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True

        elif alist[midpoint] > item:
            last = midpoint - 1

        else:
            first = midpoint + 1

    return found

if __name__ == '__main__':
    testList = [0,1,2,8,13,17,19,32,42]
    print(binarySearch(testList,3))
    print(binarySearch(testList,13))
