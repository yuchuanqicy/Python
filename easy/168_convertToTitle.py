'''
@Project ：Python 
@File    ：168_convertToTitle.py
@Author  ：YCQ
@Date    ：2024/4/6 23:13 
'''


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        26进制转换，特殊地方，需要重1开始，【1-26】正常进制是从0开始 例如十进制【0-9】
        :param columnNumber:
        :return:
        '''
        res = list()
        while columnNumber > 0:
            columnNumber=columnNumber-1
            num = columnNumber % 26
            str = chr(num+ord('A'))
            res.append(str)
            columnNumber = columnNumber// 26
        return ''.join(res[::-1])
