from typing import List


class singleNumber(object):
    #解法一，统计每个数字的个数，个数为一的，即为所求数字
    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            count=nums.count(i)
            if count==1:
                return i
    # 方法二，
    def singleNumber2(self, nums: List[int]) -> int:
        pass