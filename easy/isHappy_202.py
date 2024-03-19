class Solution:
   # 判断一个数是不是快乐数，遍历每位平方和，最后等于一即为快乐数
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
   # 方法二、使用快慢指针方式，当慢指针与快指针相等时，证明不是快乐数，反之永远不相等，即为快乐数,快指针需一次执行两个节点，慢节点执行一个节点，不然超时间限制
   def isHappy_2(self,n):
        def getNext(n):
            totalSum = 0
            while n>0:
                n,m=divmod(n,10)
                totalSum+=m**2


            return totalSum
        slow_Num=n
        fast_Num=getNext(n)
        while slow_Num!=fast_Num and fast_Num!=1:
            fast_Num = getNext(getNext(fast_Num))
            slow_Num=getNext(slow_Num);

        return fast_Num==1



