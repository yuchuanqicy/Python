'''
@Project ：Python 
@File    ：wordPattern_290.py
@Author  ：Master
@Date    ：2024/4/22 18:26 
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        给定两个字符串，判定两个字符串 模式是不是相同,即要求集合的双射
        :param pattern:
        :param s:
        :return:
        '''
        hash1={}
        hash2={}
        list1=list(pattern)
        list2=str.split(str)
        if len(list1)!=len(list2):
            return False
        for c,s in zip(list1,list2):
            if (c in hash1 and hash1[c]!=s) or (s in hash2 and hash2[s]!=c):
                return False
            hash1[c]=s
            hash2[s]=c
        return True
