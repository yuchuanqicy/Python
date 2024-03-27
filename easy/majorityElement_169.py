'''
@Project ：Python 
@File    ：majorityElement_169.py
@Author  ：YCQ
@Date    ：2024/3/27 23:16
'''
from typing import List
from   collections import Counter


class Solution:
    def majorityElement_1(self, nums: List[int]) -> int:
        '''
        求一个数组中数字出现的次数，大于数组长度len/2，返回计数最大的数,使用coolections的Counter来统计
        :param nums:
        :return:
        '''
        res=Counter(nums)
        return max(res.keys(), key=res.get)
