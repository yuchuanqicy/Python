'''
@Project ：Python 
@File    ：intersection_349.py
@Author  ：YCQ
@Date    ：2024/5/13 22:19 
'''
from typing import List


class Solution:
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        暴力方法优化，时间复杂度优化为2n
        :param nums1:
        :param nums2:
        :return:
        '''
        len1, len2 = len(nums1), len(nums2)
        res = []
        if len1 > len2:
            for i in range(len2):
                if nums2[i] in nums1 and nums2[i] not in res:
                    res.append(nums2[i])
            return res

        else:
            for i in range(len1):
                if nums1[i] in nums2 and nums1[i] not in res:
                    res.append(nums1[i])
            return res
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        集合操作
        :param nums1:
        :return:
        '''
        return list(set(nums1) & set(nums2))

