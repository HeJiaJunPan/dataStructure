#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
简单的符号平衡检测
如：“（（（）））”，检测括号是否匹配对称

从左到右读入开始字符到栈中，碰见关闭字符，将字符弹出栈
'''

from myStack import Stack
def checker(symbol):
    s = Stack()
    index = 0
    balance = True

    while index < len(symbol) and balance:
        if symbol[index] == '(':
            s.push(symbol[index])
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()

        index = index + 1

    return balance and s.isEmpty()



if __name__ == '__main__':
    print(checker('()'))
    print(checker('((((())))'))
