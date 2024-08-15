'''
@Project ：Python 
@File    ：longestPalindrome_409.py
@Author  ：Master
@Date    ：2024/8/9 10:36 
'''
import collections


class Solution:
    #API战士
    def longestPalindrome(self, s: str) -> int:
        ctn=collections.Counter(s)
        res=0
        odd=0
        listctn=list(ctn.values())
        for i in listctn:
            if i %2==0:
                res+=i
            else:
                res+=(i-1)
                odd=1
        if odd==1:
            return res+1
        else:
            return res

