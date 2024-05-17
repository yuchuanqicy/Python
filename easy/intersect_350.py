'''
@Project ：Python 
@File    ：intersect_350.py
@Author  ：Master
@Date    ：2024/5/15 11:06 
'''
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
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

