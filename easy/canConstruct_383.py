'''
@Project ：Python 
@File    ：canConstruct_383.py
@Author  ：Master
@Date    ：2024/5/30 20:17 
'''
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if  len(ransomNote)>len(magazine):
            return False
        list1=list(ransomNote)
        hash2=collections.Counter(magazine)
        print(list1,hash2)
        for i in list1:
            if i in hash2:
                hash2[i]-=1
            if hash2[i]<0:
                return False
            if i not in hash2:
                return False
        return True