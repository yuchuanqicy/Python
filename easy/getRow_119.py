'''
@Project ：Python 
@File    ：getRow_119.py
@Author  ：YCQ
@Date    ：2024/4/1 23:14 
'''
from typing import List


class Solution:
    def getRow_1(self, rowIndex: int) -> List[int]:
        '''
        根据rowIndex 求出杨辉三角的第N行
        方法一、sb方法，求出整个杨辉三角，返回最后一行，即所求的第N行
        :param rowIndex:
        :return:
        '''
        if rowIndex == 0:
            return [1]
        ret = list()
        for i in range(rowIndex+1):
            raw = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    raw.append(1)
                else:
                    raw.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(raw)
        return ret[-1]
    def getRow_2(self, rowIndex: int) -> List[int]:
        '''
        方法二、方法一进阶版本
        :param rowIndex:
        :return:
        '''
        ret = list()
        for i in range(rowIndex+1):
            raw = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    raw.append(1)
                else:
                    raw.append(ret[i - 1][j] + ret[i - 1][j - 1])
            if i==rowIndex:
                return  raw
            ret.append(raw)
    def getRow_3(self, rowIndex: int) -> List[int]:
        '''
        方法三、滚动数组方法
        :param rowIndex:
        :return:
        '''
        pre=list()
        for i in range(rowIndex+1):
            cur=list()
            for j in range(0,i+1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(pre[j - 1] + pre[j])
            pre=cur
        return pre