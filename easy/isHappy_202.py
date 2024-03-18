class Solution:
   # 判断一个数是不是快乐数
   def isHappy_1(self,n):

       def getNext(n):
           totalSum = 0
           while n>0:
               n,m=divmod(n,10)
               totalSum+=m**2
           return totalSum

       seen=set()
       while n!=1 and n not in seen:
            self.add = seen.add(n)
            n=getNext(n)

       return n==1

   def isHappy_2(self,n):
        pass



