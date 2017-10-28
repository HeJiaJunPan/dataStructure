#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
多符号平衡检测
与单符号平衡检测相比，只需加入弹出字符是否符号匹配
'''

from myStack import Stack
def checker(symbol):
    s = Stack()
    index = 0
    balance = True

    while index < len(symbol) and balance:
        sym = symbol[index]
        if sym in '([{':
            s.push(sym)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not matches(top,sym):
                    balance = False

        index = index + 1

    return balance and s.isEmpty()

def matches(open,close):
    opens = '([{'
    closes = ')]}'

    return opens.index(open) == closes.index(close)


if __name__ == '__main__':
    print(checker('([{}])'))
    print(checker('([{}]'))
