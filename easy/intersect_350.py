'''
@Project ：Python 
@File    ：intersect_350.py
@Author  ：Master
@Date    ：2024/5/15 11:06 
'''
import collections
from typing import List

class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        hash表做法,需要额外的存储空间
        :param nums1:
        :param nums2:
        :return:
        '''
        ans={}
        res=[]
        for i in nums1:
            if  not ans.get(i):
                ans[i]=1
            else:
                ans[i]+=1
        for i in nums2:
            if ans.get(i):
                res.append(i)
                ans[i]-=1
        return res
    def intersect2(self, nums1: List[int],nums2: List[int]) -> List[int]:
        '''
        高级做法，Counter  返回结果 &交集
        :param nums1:
        :param nums2:
        :return:
        '''
        n1=collections.Counter(nums1)
        n2=collections.Counter(nums2)
        res=n1 & n2
        return list(res.elements())