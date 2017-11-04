#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
背景：
    在实验室中，平均每天大约10名学生在任何给定时间在实验室工作。
这些学生通常在此期间打印两次，这些任务的长度范围从1到20页。实验
室中的打印机较旧，每分钟以草稿质量可以处理10页。打印机可以切换以
提供更好的质量，但是它将每分钟只能处理五页。较慢的打印速度可能会
使学生等太久。应使用什么页面速率？

建模：
    上述问题，通过研究学生等待他们论文打印的平均时间，也就是任务
在队列中等待的平均时间量解决。

    任务长度：学生打印长度在1到20页间，且可能性相同。通过使用1到
20间的随机数来模拟每个任务提交时应打印的页数。

    任务创建：如果实验室中有10个学生，每人打印两次，则平均每小时
有20个打印任务，即平均每180秒创建一个任务。通过生成1到180之间的随
机数来模拟打印任务发生的机会。如果随机数是180，我们认为任务创建。

模拟：
    1.创建打印任务队列，每个任务都有个时间戳。
    2.模拟每秒发生的状况：
        a.是否创建新的打印任务？如果是，添加时间戳并入队
        b.如果打印机空闲且任务队列不为空：
            1）从任务队列删除一个任务并分配给打印机
            2）从当前时间减去任务的时间戳，计算任务的等待时间
            3）将该任务的等待时间添加到列表中稍后处理
            4）根据打印任务的页数，确定打印机打印文件需要多少时间
        c.打印机内部定时器，初始值为打印文件所需时间
        d.如果任务已经完成，换句话说，所需的时间已经达到零，打印机空闲
    3.模拟完成后，从生成的等待时间列表中计算平均等待时间
'''

import time
import random
from myQueue import Queue

class Printer(object):
    '''
    打印机类
    '''

    def __init__(self,ppm):
        self.pageRate = ppm #每分钟打印页数
        self.currentTask = None
        self.timeRemaining = 0 #内部定时器,单位秒

    def tick(self):
        '''
        打印机内部状态模拟，模拟打印机打印文件
        '''
        if self.currentTask:
            self.timeRemaining = self.timeRemaining - 1
            
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask:
            return True
        else:
            return False

    def startNext(self,newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pageRate

class Task(object):
    def __init__(self,time):
        #时间戳
        self.timeStamp = time
        #任务长度
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pages

    def waitTime(self,currentTime):
        return currentTime - self.timeStamp

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds,pagesPerMinute):
    '''
    numSeconds,模拟时间，我们将每次模拟视为1秒
    pagesPerMinute,页面速率，以分钟计
    '''

    #create Printer object
    labPrinter = Printer(pagesPerMinute)
    #create task queue
    taskQueue = Queue()
    #save time that task wait
    waitingTimes = []

    #模拟时间
    for currentSecond in range(numSeconds):
        if newPrintTask():
            #create Task object
            task = Task(currentSecond)
            #push task queue
            taskQueue.enqueue(task)

        #add task to printer
        if not labPrinter.busy() and not taskQueue.isEmpty():
            nextTask = taskQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)

        #printer deal task
        labPrinter.tick()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print('Average wait %6.2f seconds and %3d tasks remaining' % (averageWait,taskQueue.size()))

if __name__ == '__main__':
    #共进行10次实验，每次实验模拟时间3600秒，页面速率5页每分钟
    for i in range(10):
        simulation(3600,5)
