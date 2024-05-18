'''
@Project ：Python 
@File    ：isPerfectSquare_367.py
@Author  ：Master
@Date    ：2024/5/18 10:50 
'''
import math


class Solution:
    def isPerfectSquare1(self, num: int) -> bool:
        '''
        判断一个数是否为平方数，使用库函数解决
        :param num:
        :return:
        '''
        return float.is_integer(pow(num,0.5))
    def isPerfectSquare2(self, num: int) -> bool:

        n=math.sqrt(num)
        return n*n==num
    def isPerfectSquare3(self, num: int) -> bool:
        '''
        从1开始遍历，遍历到num，判断每个数平方是否等于num，如果有，num即为完全平方数,暴力解法，超时
        :param num:
        :return:
        '''
        if num==1:
            return True
        for i in range(1,num):
            if i*i==num:
                return True
        return False
    def isPerfectSquare4(self, num: int) -> bool:
        '''
        改进暴力解法，能通过
        '''
        i=1
        while i*i<=num:
            if i*i==num:
                return True
            i+=1
        return False

    def isPerfectSquare5(self, num: int) -> bool:
        '''
        二分法，解决
        :param num:
        :return:
        '''
        left=1
        right=num
        while left<=right:
            mid = (right + left) // 2
            if mid*mid==num:
                return True
            if mid*mid>num:
                right=mid-1
            if mid*mid<num:
                left=mid+1
        return False