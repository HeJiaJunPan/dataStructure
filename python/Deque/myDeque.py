#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
双端队列是一种能够从首部或尾部的任一端添加或删除项的线性数据结构
双端队列包含的操作：
    1.创建新的双端队列
    2.从首部添加项
    3.从尾部添加项
    4.从首部删除项，并返回
    5.从尾部删除项，并返回
    6.检测双端队列是否为空
    7.返回双端队列的大小

利用Python原生数据类型list作为底部实现，把列表尾部视为双端队列的首部
'''

class Deque(object):
    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    d = Deque()
    print(d.size())
    d.addFront(0)
    d.addRear(10)
    print(d.isEmpty())
    d.addFront(6)
    print(d.removeFront())
    print(d.removeRear())
    print(d.size())
    print(d.removeFront())
    print(d.isEmpty())
