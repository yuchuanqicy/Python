'''
@Project ：Python 
@File    ：isPowerOfFour_342.py
@Author  ：YCQ
@Date    ：2024/5/8 22:42 
'''
import math


class Solution:
    def isPowerOfFour1(self, n: int) -> bool:
        '''
        简单做法
        :param n:
        :return:
        '''
        while n%4==0 and n>0:
            n/=4
        return n==1
    def isPowerOfFour2(self, n: int) -> bool:
        '''
        递归普通做法
        :param n:
        :return:
        '''
        if n==1 or n==0 :
            return n==1
        else:
            return self.isPowerOfFour2(n/4)
    def isPowerOfFour3(self, n: int) -> bool:
        '''
        二进制做法
        :param n:
        :return:
        '''
