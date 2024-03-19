class Solution:
    # 给定整数N，判断其是不是丑数，包含2，3，5的因子的数才是丑数，即能整除2,3,5的数为丑数
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        while n % 2 == 0: n = n / 2
        while n % 3 == 0: n = n / 3
        while n % 5 == 0: n = n / 5
        return n==1
