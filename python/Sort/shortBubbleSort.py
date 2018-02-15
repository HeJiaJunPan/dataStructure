#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def shortBubbleSort(alist):
    exchange = True

    passnum = len(alist) - 1

    while passnum > 0 and exchange:
        exchange = False

        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i],alist[i + 1] = alist[i + 1],alist[i]

        passnum = passnum - 1
    # print(passnum)

if __name__ == '__main__':
    alist = [20,30,40,50,60,70,80,100,110]
    shortBubbleSort(alist)
    print(alist)
