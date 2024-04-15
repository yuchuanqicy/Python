'''
@Project ：Python 
@File    ：MyQueue_232.py
@Author  ：Master
@Date    ：2024/4/15 18:25 
'''


class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack1.insert(x)


    def pop(self) -> int:
        self.stack.reverse()
        return self.stack.pop()

    def peek(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0
