'''
@Project ：Python 
@File    ：217_containsDuplicate.py
@Author  ：YCQ
@Date    ：2024/4/3 23:17 
'''
from typing import List


class Solution:
    def containsDuplicate_1(self, nums: List[int]) -> bool:
        '''
        给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false
        方法一、使用hash表的方法来做
        :param nums:
        :return:
        '''
        ret=set()
        for num in nums:
            if num in ret:
                return  True
            else:
                ret.add(num)
        return False

    def containsDuplicate_2(self,nums: List[int]) -> bool:
        '''
        方法二、先排序，比较前后两位元素是否相等，相等返回true 否则遍历数组，直至结束，然后返回false
        :param nums:
        :return:
        '''
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False