'''
@Project ：Python 
@File    ：summaryRanges_228.py
@Author  ：Master
@Date    ：2024/4/17 11:21 
'''
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        双指针方式，遍历区间
        :param nums:
        :return:
        '''
        i=0
        n=len(nums)
        res=list()
        while i<n:
            j=i
            while j+1<n and nums[j+1]==nums[j]+1:
                j+=1
            if  i==j:
                res.append(str(nums[i]))
            else:
                res.append(f"{nums[i]}->{nums[j]}")
            i=j+1
        return res
