#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
后缀表达式计算

创建栈保存操作数
从左到右扫描后缀表达式：
    1.如果标记是操作数，将其压入栈中
    2.如果标记是操作符，从栈中弹出两次，并进行运算（注意操作数顺序），将结果压入栈中
    3.后缀表达式扫描完后，将结果从栈中弹出
'''

from myStack import Stack

def postfixEval(postfixString):
    operateStack = Stack()
    tokenList = postfixString.split()

    for token in tokenList:
        if token in '0123456789':
            operateStack.push(int(token))

        else:
            operate2 = operateStack.pop()
            operate1 = operateStack.pop()
            result = doMath(token,operate1,operate2)
            operateStack.push(result)

    return operateStack.pop()

def doMath(token,op1,op2):
    if token == '*':
        return op1 * op2

    elif token == '/':
        return op1 / op2

    elif token == '+':
        return op1 + op2
    
    elif token == '-':
        return op1 - op2

if __name__ == '__main__':
    print(postfixEval('7 8 + 3 2 + /'))
    print(postfixEval('5 6 * 5 -'))
