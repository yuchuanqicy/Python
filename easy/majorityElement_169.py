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


    def majorityElement_2(self, nums: List[int]) -> int:
        '''
        方法二、使用自己构造Counter函数来统计为数组元素出现的次数,大于数组长度len/2，返回计数最大的数
        :param nums:
        :return:
        '''
        countdic={}
        for num in nums:
            if num in countdic:
                countdic[num]+=1
            else:
                countdic[num]=1
        ans = max(countdic.values())
        if ans > len(nums) // 2:
            for k,v in countdic.items():
                if v==ans:
                    return k
        else:
            return None
    def majorityElement_3(self, nums: List[int]) -> int:
        '''
        方法三、使用Boyer-Moore 算法来找出众数
        :param nums:
        :return:
        '''
        count=0
        candate=0
        for num in nums:
            if count==0:
                candate=num
            count+=(1 if num==candate else -1)
        return candate


