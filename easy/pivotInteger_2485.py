class pivotInteger_2485:
    # 普通方法,利用等差数列来求解
    def pivotInteger(self, n: int) -> int:
        for  x in  range(1,n+1):
            if (1+x)*x==(x+n)*(n-x+1):
                return x
        return -1
    # 方法二、使用二分法计算
    def pivotInteger_2(self, n: int) -> int:
        pass