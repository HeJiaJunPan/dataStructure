#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
无序链表。
关键在于，创建表头来。
'''

from Node import Node

class unorderedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        '''
        首插法
        '''

        newNode = Node(item)
        temp = self.head
        self.head = newNode
        newNode.setNext(temp)

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData == item:
                found = True

            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while current != None and not  found:
            if current.getdata == item:
                found = True

                if previous is None:
                    self.head = None
                else:
                    previous.setNext(current.getNext())

            else:
                previous = current
                current = current.getNext()

    def printList(self):
        current = self.head

        while current != None:
            print(current.getData())
            current = current.getNext()

if __name__ == '__main__':
    l = unorderedList()
    l.add(0)
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)
    l.printList()
