'''
@Project ：Python 
@File    ：278_firstBadVersion.py
@Author  ：YCQ
@Date    ：2024/4/18 23:41 
'''


class Solution:
    def isBadVersion(self, version):
        pass

    def firstBadVersion(self, n: int) -> int:
        '''
        给顶一个n 找到第一个错误的版本，找到的次数最少，使用二分法
        :param n:
        :return:
        '''
        left, right = 1, n-1
        while left<=right:
            mid = (left+right)//2

            if self.isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1
        return left