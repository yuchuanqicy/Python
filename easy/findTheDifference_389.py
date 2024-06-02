'''
@Project ：Python 
@File    ：findTheDifference_389.py
@Author  ：YCQ
@Date    ：2024/6/2 16:33 
'''
import collections


class Solution:
    def findTheDifference1(self, s: str, t: str) -> str:
        '''
        普通做法
        :param s:
        :param t:
        :return:
        '''
        if s==None:
            return t
        slist=list(s)
        tlist=list(t)
        slist.sort()
        tlist.sort()
        for i in range(len(slist)):
            if tlist[i]!=slist[i]:
                return tlist[i]
        return tlist[-1]
    def findTheDifference2(self,s:str,t:str)->str:
        '''
        hash表做法
        :param s:
        :param t:
        :return:
        '''
        s1=collections.Counter(s)
        t1=collections.Counter(t)
        for i  in s1:
            if s1[i]!=t1[i]:
                return i
        return str(list((t1-s1).keys())[0])
    def findTheDifference3(self,s:str,t:str):
        '''
        统计字符方法
        :param s:
        :param t:
        :return:
        '''
        list=[0]*26
        for c in s:
            list[ord(c)-ord('a')]+=1
        for i in t:
            list[ord(i)-ord('a')]-=1
            if list[ord(i)-ord('a')]<0:
                return i

    def findTheDifference4(self,s:str,t:str):
        '''
        首先将两个字符串合并为a,在a中遍历，如果出现奇数次的字符即为不同的字符
        :param s:
        :param t:
        :return:
        '''
        '''
        合并字符串：
        方法1：combined_str=''.join([s1,s2])
        方法2：combined_str=s1+s2
        方法3：combined_str = "{}{}".format(str1, str2)
        方法4：combined_str = f"{str1}{str2}"
        '''
        newStr=s+t
        for c in t:
            if newStr.count(c)%2==1:
                return c
    def findTheDifference5(self,s:str,t:str):
        '''
        hash表统计做法
        :param s:
        :param t:
        :return:
        '''
        res={}
        for c in  t:
            if c not in res:
                res[c]=1
            else:
                res[c]+=1
        for c in s:
            if c in res:
                res[c]-=1
        for c in res:
            if res[c]==1:
                return c
    def findTheDifference6(self,s:str,t:str):
        '''
        将字符串转变为列表，排序后，拼接列表，保存元素个数与t元素个数一致，使用zip函数打包两个列表，比较结果每个元组的元素是否相等，不相等即为答案
        :param s:
        :param t:
        :return:
        '''
        s1=sorted(s)+ " "
        t1=sorted(t)
        for i,j in zip(s1,t1):
            if i!=j:
                return j
    def findTheDifference7(self,s:str,t:str):
        '''
        位运算
        :param s:
        :param t:
        :return:
        '''
        res=0
        for c in s:
            res=res^ord(c)
        for c in t:
            res=res^ord(c)
        return chr(res)