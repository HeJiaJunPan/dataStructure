#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
游戏：
    烫手山芋——狡猾的背叛者

规则：
    众人围成一圈，尽可能快的将一个山芋递给旁边的孩子。
    某时刻结束，有山芋的孩子从圈中移除。游戏继续开始，直到剩下最后一个孩子

模拟：
    我们通过出队后入队形成循环队列，并指定第N个被传递到山芋的人永久退出队列
'''

from myQueue import Queue

def hotPotato(nameList,num=6):
    simQueue = Queue()

    for name in nameList:
        simQueue.enqueue(name)

    while simQueue.size() > 1:
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())

        simQueue.dequeue()

    return simQueue.dequeue()

if __name__ == '__main__':
    print(hotPotato(['Bill','David','Susan','Jane','Kent','Brad']))
    print(hotPotato(['Bill','David','Susan','Jane','Kent','Brad'],7))
