'''
@Project ：Python 
@File    ：fizzBuzz_412.py
@Author  ：Master
@Date    ：2024/8/26 21:11 
'''
from typing import List


class Solution:
    def fizzBuzz_1(self, n: int) -> List[str]:
        StrRes = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                StrRes.append('FizzBuzz')
            elif i % 3 == 0 :
                StrRes.append('Fizz')
            elif i%5==0:
                StrRes.append('Buzz')
            else:
                StrRes.append(f"{i}")
        return StrRes
    def fizzBuzz_1(self, n: int) -> List[str]:
        ans=[]
        for i in range(1,n+1):
            flag1,flag2= i%3==0,i%5==0
            if flag1 or flag2:
                ans.append('Fizz'*flag1+'Buzz'*flag2)
            else:
                ans.append(str(i))
        return ans