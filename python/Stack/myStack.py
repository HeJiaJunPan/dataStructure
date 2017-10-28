#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
栈是一种只在一端添加或移除项的线性数据结构，特点是“后进先出”。
栈的操作包括：
    1.创建新栈
    2.添加新项到栈的顶部
    3.从栈中删除顶部项，并返回该项
    4.返回栈的顶部项，但不会删除顶部项
    5.测试栈是否为空栈
    6.返回栈的大小

利用Python原生数据类型list作为栈的底部实现,将列表底部视为栈的顶部
'''

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)





if __name__ == '__main__':
    s = Stack()

    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

