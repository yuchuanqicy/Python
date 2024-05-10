'''
@Project ：Python 
@File    ：reverseString_344.py
@Author  ：YCQ
@Date    ：2024/5/9 22:52 
'''
from typing import List


class Solution:
    def reverseString1(self, s: List[str]) -> None:
        """
        API战士
        """
        s.reverse()

    def reverseString2(self, s: List[str]) -> None:
        '''
        原地切片做法
        :param s:
        :return:
        '''
        print(s)
        print(id(s))
        print(id(s[:]))
        s[:]=s[::-1]

        print(s)
        print(id(s))

    def reverseString3(self, s: List[str]) -> None:
        '''
        双指针做法
        :param s:
        :return:
        '''
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1