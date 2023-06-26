
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=1
        y=0
        while(n!=0):
            x=x*(n%10)
            y = y + (n % 10)

            n=n//10

        return x-y