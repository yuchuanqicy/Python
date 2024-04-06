'''
@Project ：Python 
@File    ：titleToNumber_171.py
@Author  ：YCQ
@Date    ：2024/4/6 22:08 
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        '''
        思想为26进制的思想，每26进一位
        :param columnTitle:
        :return:
        '''
        res=0
        for i   in range(len(columnTitle)):
            num= ord(columnTitle[i])-ord('A')+1
            res=res*26+num
        return  res