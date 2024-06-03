'''
@Project ：Python 
@File    ：firstUniqChar_387.py
@Author  ：Master
@Date    ：2024/6/1 10:53 
'''
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        通过字符串内置方法find()、rfind()分别从左遍历字符串，从右边遍历字符串，当找的字符的下标一致，就证明字符是字符串唯一的字符
        idnex()、rindex()也可以
        :param s:
        :return:
        '''
        for c in s:
            if s.find(c)==s.rfind(c):
                return s.find(c)
        return -1

    def firstUniqChar2(self, s: str) -> int:

        '''
        hash表做法，hash统计字符出现的个数，在遍历hash表，找到统计次数为1的字符，返回其在字符串的下标
        '''
        hashson=collections.Counter(s)
        for k,v in enumerate(s):
            print(k,v)
            if hashson[v]==1:
                return s.index(v)
        return -1
    def firstUniqChar3(self, s: str) -> int:
        '''
        使用队列
        :param s:
        :return:
        '''
        pass
