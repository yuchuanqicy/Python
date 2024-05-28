'''
@Project ：Python 
@File    ：guessNumber_374.py
@Author  ：Master
@Date    ：2024/5/20 9:26 
'''
class Solution:
    def guess(self,n):
        num=100
        if n<num:
            return  -1
        elif n>num:
            return  1
        else: return 0
    def guessNumber(self, n: int) -> int:
        left=0
        right=n
        while left<=right:
            mid=(left+right)//2
            if -1==self.guess(mid):
                right=mid-1
            elif 1==self.guess(mid):
                left=mid+1
            elif 0==self.guess(mid):
                return mid