'''
@Project ：Python 
@File    ：MyStack_225.py
@Author  ：YCQ
@Date    ：2024/4/7 21:54 
'''
import collections


class MyStack:
    '''
    使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
    '''
    def __init__(self):
        self.queue1=collections.deque()
        self.queue2=collections.deque()
    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1,self.queue2=self.queue2,self.queue1
        return   self.queue1

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return  not self.queue1
