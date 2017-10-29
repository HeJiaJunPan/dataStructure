#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
中缀表达式转前缀表达式

创建栈保存操作符，操作数保存在列表中
从右到左扫描中缀表达式
    1.如果标记是操作数，将其插入列表首部
    2.如果标记是右括号，将其压入栈中
    3.如果标记是左括号，从栈中弹出字符，依序插入列表首部，直到相应的右括号被删除
    4.如果标记是运算符，将其压入栈中。但是入栈前，须先将具有更高或相等优先级的运算符弹出，并依序插入列表首部
    5.中缀表达式扫描完后，若栈不为空，从栈中弹出字符，并依序插入列表首部
'''

from myStack import Stack

def convert(infixString):
    #运算符优先级
    prec = {
        '*':3,
        '/':3,
        '+':2,
        '-':2,
        ')':1
    }
    
    #保存操作符
    opStack = Stack()
    #保存前缀表达式
    prefixList = []
    #以空白字符分割中缀表达式
    tokenList = infixString.split()

    index = len(tokenList) - 1
    while index >= 0:
        token = tokenList[index]

        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            prefixList.insert(0,token)

        elif token == ')':
            opStack.push(token)

        elif token == '(':
            topToken = opStack.pop()
            while topToken != ')':
                prefixList.insert(0,topToken)
                topToken = opStack.pop()

        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                prefixList.insert(0,opStack.pop())
            opStack.push(token)

        index = index - 1

    while not opStack.isEmpty():
        prefixList.insert(0,opStack.pop())

    return ' '.join(prefixList)


if __name__ == '__main__':
    print(convert('( A + B ) * C - ( D - E ) * ( F + G )'))
    print(convert('A + B * C'))

