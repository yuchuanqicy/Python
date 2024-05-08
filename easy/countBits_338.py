'''
@Project ：Python 
@File    ：countBits_338.py
@Author  ：YCQ
@Date    ：2024/5/7 21:05 
'''
from typing import List


class Solution:
    def count(self,x: int) -> int:
        one=0
        while x>0:
            x&=(x-1)
            one+=1
        return one
    def countBits1(self, n: int) -> List[int]:
        '''
        使用一比特数实现，统计每个整数二进制 1的个数
        :param n:
        :return:
        '''
        res=[]
        for i in range(n+1):
           res.append(self.count(n))
        return res

    def countBits2(self, n: int) -> List[int]:
        '''
        大佬骚操作`
        :param n:
        :return:
        '''
        res = [0]
        for i in range(1, n + 1):
            if i & 1 == 0:
                res.append(res[i // 2])
            else:
                res.append(res[i - 1] + 1)
        return res
    def countBits3(self, n: int) -> List[int]:
        '''
        位运算解决
        :param n:
        :return:
        '''
        count=0
        res=[]
        for i in range(n+1):
            while i:
                count+=i& 1
                i=i>>1
            res.append(count)
            count=0
    def countBits4(self, n: int) -> List[int]:
        '''
        API战士
        :param n:
        :return:
        '''
        def cout(x):
            cout=0
            for i in range(x+1):
                count=bin(i).count("1")
            return count

        # 使用推导式生成列表
        return  [cout(i) for i in range(n+1)]
    def countBits5(self, n: int) -> List[int]:
        '''
        使用动态规划解决
        :param n:
        :return:
        '''
        count=[0]*(n+1)
        for i  in range(1,n+1):
            count[i]=count[i>>1]+(i&1)
        return count
