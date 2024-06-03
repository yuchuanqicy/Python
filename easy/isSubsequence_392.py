'''
@Project ：Python 
@File    ：isSubsequence_392.py
@Author  ：Master
@Date    ：2024/6/3 11:44 
'''
class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:
        '''
        双指针，沾边贪心
        :param s:
        :param t:
        :return:
        '''
        n,m=len(s),len(t)
        i,j=0,0
        while i<n and j<m:
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==n
    def isSubsequence2(self, s: str, t: str) -> bool:
        '''
        动态规划
        :param s:
        :param t:
        :return:
        '''
    def isSubsequence3(self, s: str, t: str) -> bool:
        '''
        取巧办法，通过python迭代器，生成t可迭代对象，迭代对象，只能往前遍历，不能往后遍历，使用此特性，来解决问题
        :param s:
        :param t:
        :return:
        '''
        newIter=iter(t)
        return all(c in newIter for c in s)
    def isSubsequence4(self, s: str, t: str) -> bool:
        '''
        find()函数使用
        '''
        i=0
        for c in s:
            j=t.find(c,i)
            if j==-1:
                return False
            i=j+1
        return True
    def isSubsequence5(self, s: str, t: str) -> bool:
        '''
        使用切片方式
        :param s:
        :param t:
        :return:
        '''
        for i in s:
            if i in t:
                t = t[t.index(i) + 1:]
            else:
                return False
        return True