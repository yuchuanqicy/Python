'''
@Project ：Python 
@File    ：thirdMax_414.py
@Author  ：Master
@Date    ：2024/8/29 17:05 
'''
from typing import List


class Solution:
    def thirdMax_2(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        dif=1
        for i  in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                dif+=1
                if dif==3:
                    return nums[i]
        return nums[0]

