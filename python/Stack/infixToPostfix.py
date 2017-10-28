#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
中缀表达式转后缀表达式

创建栈保存操作符，操作数保存在列表中
从左到右扫描中缀表达式：
    1.如果标记是操作数，将其插到列表尾部
    2.如果标记是左括号，将其压入栈中
    3.如果标记是右括号，则将栈中字符弹出，直到删除相应的左括号。弹出的字符依序插入列表尾部
    4.如果标记是运算符，将其压入栈中。但入栈前应先将具有更高或相等优先级的运算符弹出，并插入列表weibu
    5.中缀表达式扫描完后，若栈不为空，则将栈中字符弹出并依序插入列表尾部
'''

from myStack import Stack

def infixToPostfix(infixString):
    #运算符优先级
    prec = {
        '*':3,
        '/':3,
        '+':2,
        '-':2,
        '(':1
    }

    #存放操作符
    opStack = Stack()
    #存放后缀表达式
    postfixList = []
    #以空白字符分割中缀表达式
    tokenList = infixString.split()

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)

        elif token == '(':
            opStack.push(token)

        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())

            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return ' '.join(postfixList)


if __name__ == '__main__':
    print(infixToPostfix('A * B + C * D'))
    print(infixToPostfix('( A + B ) * C'))
    print(infixToPostfix('( A + B ) * C - ( D - E ) * ( F + G )'))
