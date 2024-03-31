'''
@Project ：Python 
@File    ：generate_118.py
@Author  ：YCQ
@Date    ：2024/3/31 23:59 
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        输出杨辉三角前n行，
        :param numRows:
        :return:
        '''
        ret=list()
        for i in  range(numRows):

            raw=list()
            for j in range(0,i+1):
                if j==0 or j==i:
                    raw.append(1)
                else:
                    raw.append(ret[i-1][j-1]+ret[i-1][j])
            ret.append(raw)
        return ret