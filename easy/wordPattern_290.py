'''
@Project ：Python 
@File    ：wordPattern_290.py
@Author  ：Master
@Date    ：2024/4/22 18:26 
'''
class Solution:
    def wordPattern_1(self, pattern: str, s: str) -> bool:
        '''
        给定两个字符串，判定两个字符串 模式是不是相同
        :param pattern:
        :param s:
        :return:
        '''

        str2=s.split(" ")
        if len(pattern)!=len(str2):
            return False
        return  list(map(pattern.index,pattern))==list(map(str2.index,str2))

