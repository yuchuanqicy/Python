'''
@Project ：Python 
@File    ：isAnagram_242.py
@Author  ：Master
@Date    ：2024/4/16 10:48 
'''
from collections import Counter


class Solution:
    def isAnagram_1(self, s: str, t: str) -> bool:
        '''
        API战士，使用Counter函数统计字符串，字符个数，结果为字典，判断两个字符串统计结果是否相等，技能判断是否为异位词
        :param s:
        :param t:
        :return:
        '''
        return Counter(s)==Counter(t)

    def isAnagram_2(self,s:str,t:str) -> bool:
        '''
        对两个字符串进行排序，两个字符串长度不相等，直接返回false，在判断两个字符串是不是相等，相等即为异位词字符串否则false
        :param s:
        :param t:
        :return:
        '''
        list1=list(s)
        list2=list(t)
        list1.sort()
        list2.sort()
        if len(list1)!=len(list2):
            return False
        if list1==list2:
            return True
        return  False

    def isAnagram_3(self,s:str,t:str) -> bool:
        '''
        自己实现hash表，统计字符串的字符个数，在对比hash表，需要使用两个hash表
        :param s:
        :param t:
        :return:
        '''
        dict1={}
        dict2={}
        for s1 in s:
            if s1 in dict1:
                dict1[s1]+=1
            else:
                dict1[s1]=1
        for t1 in t:
            if t1 in dict2:
                dict2[t1]+=1
            else:
                dict2[t1]=1
        return  dict1==dict2
    def isAnagram_4(self,s:str,t:str) -> bool:
        '''
        因为字符串总为小写字母，总共26个字母，使用长度为26的列表，来统计字母个数，
        遍历s字符串，数组对应位置索引出现一次 值就+1，遍历t字符串 就-1，遍历完成后，数组存在小于0的元素，即两个字符串不为异位词
        关键点：在于降字符串每一位字符转换为数组索引，通过ACSII方式来转换
        :param s:
        :param t:
        :return:
        '''
        if len(s)!=len(t):
            return False
        # 列表推导式，初始化26位全为0的列表，或者使用 Arry=[0]*26的方式来初始化
        Arry=[0 for _ in range(26)]
        for s1 in s:
            Arry[ord(s1)-ord('a')]+=1
        for t1 in t:
            Arry[ord(t1)-ord('a')]-=1
            if Arry[ord(t1)-ord('a')]<0:
                return False
        return True



