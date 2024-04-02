'''
@Project ：Python 
@File    ：missingNumber_268.py
@Author  ：YCQ
@Date    ：2024/4/2 23:14 
'''
from typing import List


class Solution:
    def missingNumber_1(self, nums: List[int]) -> int:
        '''
        给定一个数n，找出 [0, n] 这个范围内没有出现在数组中的那个数。
        因为给定n，数组肯定要包含n个元素，并且元素是在【0，n】之间的数字，但是又要缺少部分数，所以只能缺少一个数，因此可以简单做法
        先排序，在根据下标遍历数组，下标与元素值不相等的，即为缺失的数字，返回下标即可
        :param nums:
        :return:
        '''
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
    def missingNumber_2(self, nums: List[int]) -> int:
        '''
        方法二、使用哈希实现
        :param nums:
        :return:
        '''
        res=set(nums)
        for i in  range(0,len(nums)+1):
            if i not in res:
                return i
    def missingNumber_3(self, nums: List[int]) -> int:
        '''
        方法三、使用位运算
        :param nums:
        :return:
        '''
        n=len(nums)
        xor=0
        for i in range(n):
            xor=xor^nums[i]
        for j  in range(n+1):
            xor^=j
        return xor
