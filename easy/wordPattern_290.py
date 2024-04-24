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
    def wordPattern_2(self, pattern: str, s: str) -> bool:
        '''
        使用hash表来判断
        :param pattern:
        :param s:
        :return:
        '''
        hash1={}
        hash2=dict()
        list1=list(pattern)
        list2=s.split(" ")
        if len(list1)!=len(list2):
            return False
        for c,s in zip(list1,list2):
            if (c in hash1 and hash1[c]!=s)  or (s in hash2 and hash2[s]!=c):
                return False
        return True


