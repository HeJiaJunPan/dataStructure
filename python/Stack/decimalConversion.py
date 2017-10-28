#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
十进制转换，默认转换为二进制
'''

from myStack import Stack

def convert(decNumber,base=2):
    remStack = Stack()
    #进制字符替换
    digits = '0123456789ABCDEF'

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    result = ''
    while not remStack.isEmpty():
        result = result + digits[remStack.pop()]

    return result



if __name__ == '__main__':
    print(convert(3))
    print(convert(9,8))
    print(convert(12,16))
