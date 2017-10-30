#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
队列是一种在尾部添加项，首部删除项的线性数据结构,具有先进先出的特点
队列的操作包括：
    1.创建新队列
    2.在队首删除项，并返回项
    3.在队尾添加项
    4.检测队列是否为空
    5.返回队列大小

利用Python原生数据类型list作为底层实现，将列表首部作为队尾，列表尾部作为对首
'''

class Queue(object):
    def __init__(self):
        self.items = []

    def dequeue(self):
        return self.items.pop()

    def enqueue(self,item):
        self.items.insert(0,item)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue('dog')
    q.enqueue(6.00)
    print(q.size())
    print(q.dequeue())
    print(q.isEmpty())
