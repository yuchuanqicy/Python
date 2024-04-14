'''
@Project ：Python 
@File    ：MyStack_225_2.py
@Author  ：YCQ
@Date    ：2024/4/14 20:13 
'''
import collections

class MyStack:
    '''
    使用单队列实现栈的操作，队列添加一个元素后，将队列首部的元素重新添加到队列尾部，构造栈先入先出的形式
    '''
    def __init__(self):
        self.deque1=collections.deque()
    def push(self, x: int) -> None:
        #  这步很关键，需要获取，添加元素前的队列的长度，不然会在队列尾部多添加一次
        n=len(self.deque1)
        self.deque1.append(x)
        for  _  in range(n):
            self.deque1.append(self.deque1.popleft())
    def pop(self) -> int:
        return self.deque1.popleft()
    def top(self) -> int:
        return self.deque1[0]
    def empty(self) -> bool:
        return  not self.deque1