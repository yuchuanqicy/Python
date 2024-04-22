'''
@Project ：Python 
@File    ：wordPattern_290.py
@Author  ：Master
@Date    ：2024/4/22 18:26 
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        给定两个字符串，判定两个字符串 模式是不是相同
        :param pattern:
        :param s:
        :return:
        '''
        list1=list(pattern)
        list2=str.split(str)
        if len(list1)!=len(list2):
            return False
