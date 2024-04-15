'''
@Project ：Python 
@File    ：MyQueue_232_2.py
@Author  ：YCQ
@Date    ：2024/4/15 23:43 
'''


class MyQueue:
    '''
    使用单栈方式模拟队列
    '''
    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.insert(0, x)

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        if len(self.stack1) == 0:
            return None
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0
