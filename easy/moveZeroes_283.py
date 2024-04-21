'''
@Project ：Python 
@File    ：moveZeroes_283.py
@Author  ：YCQ
@Date    ：2024/4/21 22:40 
'''
from typing import List


class Solution:
    def moveZeroes_1(self, nums: List[int]) -> None:
        """
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        快慢指针，两次遍历，快指针找出数组非0元素，最后，将后半部全部置为零
        """
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for i in range(j,len(nums)):
            nums[i]=0
        return nums
    def moveZeroes_2(self, nums: List[int]) -> None:
        '''
        一次遍历方法，将非0值交换到左边，0全部交换到右边
        :param nums:
        :return:
        '''
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        return nums