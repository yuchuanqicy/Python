'''
@Project ：Python 
@File    ：isPowerOfThree_326.py
@Author  ：YCQ
@Date    ：2024/5/6 21:46 
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        while n%3==0 and n>0:
            n/=3
        return n ==1
