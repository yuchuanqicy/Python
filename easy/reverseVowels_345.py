'''
@Project ：Python 
@File    ：reverseVowels_345.py
@Author  ：Master
@Date    ：2024/5/13 20:18 
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        codeList=['a','e','i','o','u','A','E','I','O','U']
        strList=list(s)
        left=0
        right=len(strList)-1
        while left<right:
            if strList[left] in codeList and strList[right] in codeList:
                strList[left],strList[right]=strList[right],strList[left]
                left+=1
                right-=1
            elif strList[left] not in codeList and strList[right] in codeList :
                left+=1
            elif strList[left]  in codeList and strList[right] not in codeList:
                right-=1
            else:
                left+=1
                right-=1
        return ''.join(strList)