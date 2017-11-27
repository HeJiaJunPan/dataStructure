#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
链表的基本组件是节点。
节点由数据域和指针域两部分构成。
'''

class Node(object):
    def __init__(self,initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,data):
        self.data = data

    def setNext(self,newNext):
        self.next = newNext

if __name__ == '__main__':
    temp = Node(93)
    print(temp.getData())
