#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class HashTable(object):
    def __init__(self,tableSize=11):
        self.size = tableSize
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashFunction(self,key,size):
        return key % size

    def reHash(self,oldHash,size):
        return (oldHash + 1) % size

    def put(self,key,data):
        #计算哈希值
        hashValue = self.hashFunction(key,len(self.slots))

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                nextSlot = self.reHash(hashValue,len(self.slots))
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.reHash(nextSlot,len(self.slots))

                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data

    def get(self,key):
        startSlot = self.hashFunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startSlot

        while self.slots[position] != None and not stop and not found:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.reHash(position,len(self.slots))
                if position == startSlot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


if __name__ == '__main__':
    H = HashTable()
    H[54] = 'cat'
    H[26] = 'dog'
    H[93] = 'lion'
    H[17] = 'tiger'
    H[77] = 'bird'
    H[31] = 'cow'
    H[44] = 'goat'
    H[55] = 'pig'
    H[20] = 'chicken'

    print(H.slots)
    print(H.data)

    print(H[20])
    print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H.data)
    print(H[99])
