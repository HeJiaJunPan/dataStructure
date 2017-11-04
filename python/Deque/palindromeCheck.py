#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
回文检测
'''

from myDeque import Deque

def check(palString):
    charQueue = Deque()
    stillEqual = True

    for ch in palString:
        charQueue.addRear(ch)

    while charQueue.size() > 1 and stillEqual:
        first = charQueue.removeFront()
        last = charQueue.removeRear()

        if first != last:
            stillEqual = False

    return stillEqual

if __name__ == '__main__':
    print(check('lsdkjfskf'))
    print(check('radar'))
