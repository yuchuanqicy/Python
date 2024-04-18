'''
@Project ：Python 
@File    ：219_containsNearbyDuplicate.py
@Author  ：YCQ
@Date    ：2024/4/4 23:28 
'''
from typing import List


class Solution:
    def containsNearbyDuplicate_1(self, nums: List[int], k: int) -> bool:
        '''
        给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
        :param nums:
        :param k:
        :return:
        '''
        res={}
        for i,num in enumerate(nums):
            if num in res and i-res[num]<=k:
                return True
            res[num]=i
        return False

    def containsNearbyDuplicate_2(self, nums: List[int], k: int) -> bool:
        '''
        方法二、暴力解法，超时
        :param nums:
        :param k:
        :return:
        '''
        length = len(nums)
        i=0
        while i <length :
            for j in  range(i+1,length):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
                if abs(j-i)>k:
                    continue
            i+=1
        return False
    def containsNearbyDuplicate_3(self,nums: List[int], k: int) -> bool:

        '''
        方法三、滑动窗口与数组结合
        :param nums:
        :param k:
        :return:
        '''
        res=set()
        for i,num in enumerate(nums):
            if i>k:
                res.remove(nums[i-k-1])
            if num in res:return True
            res.add(num)
        return  False
