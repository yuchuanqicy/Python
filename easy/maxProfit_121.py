'''
@Project ：Python 
@File    ：maxProfit_121.py
@Author  ：YCQ
@Date    ：2024/3/26 23:05 
'''
from math import inf
from typing import List


class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        '''
        方法一：循环遍历数组，找出最大值即可
        :param prices: List类型
        :return: int类型
        '''
        maxprofit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                maxprofit = max(prices[j] - prices[i], maxprofit)
        return maxprofit

    def maxProfit_2(self, prices: List[int]) -> int:
        '''
        方法二、使用DP去做，
        1、明确 dp(i)dp(i)dp(i) 应该表示什么（二维情况：dp(i)(j)）；
        2、根据 dp(i)和dp(i-1)的关系得出状态转移方程；
        3、确定初始条件，如 dp(0).
         所以dp[i]为最大利润
        :param prices:
        :return:
        '''
        maxprofit = 0
        minprice = prices[0]
        for price in prices:
            minprice = min(minprice, price)
            maxprofit =max(maxprofit, price - minprice)
        return maxprofit



