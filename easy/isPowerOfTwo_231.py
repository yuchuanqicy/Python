'''
@Project ：Python 
@File    ：isPowerOfTwo_231.py
@Author  ：Master
@Date    ：2024/4/17 10:46 
'''
class Solution:
    def isPowerOfTwo1(self, n: int) -> bool:
        '''
        一个整数，判断其是否是2的幂次，普通做法
        :param n:
        :return:
        '''
        while n%2==0 and n>0:
            n/=2
        return  n==1
    def isPowerOfTwo2(self, n: int) -> bool:
        '''
        使用位运算来做 如果n是2的幂次， 1 ，2，4，8...... 对应二进制 0001 0010 0100 1000 那么n-1就是 0000 0001 0011 0111
        那么n&（n-1）==0
        :param n:
        :return:
        '''

        return n>0 and n&(n-1)==0
