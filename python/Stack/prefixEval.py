#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
前缀表达式计算

创建栈保存操作数
从右到左扫描前缀表达式：
    1.如果标记是操作数，将其压入栈中
    2.如果标记是操作符，从栈中弹出两次，并进行计算，结果压入栈中
    3.前缀表达式扫描结束后，将结果从栈中弹出
'''

from myStack import Stack

def prefixEval(prefixString):
    operateStack = Stack()
    tokenList = prefixString.split()
    index = len(tokenList) - 1

    while index >= 0:
        token = tokenList[index]

        if token in '0123456789':
            operateStack.push(int(token))

        else:
            operate1 = operateStack.pop()
            operate2 = operateStack.pop()
            result = doMath(token,operate1,operate2)
            operateStack.push(result)

        index = index - 1

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
    print(prefixEval('- * 6 5 5'))
