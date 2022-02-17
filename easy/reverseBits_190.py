class Solution:

    def reverseBits1(self, n: int) -> int:
        str1=str(n).zfill(32)[::-1]
        print(str1)
        num=int(str1,2)
        print(num)
        # str1=str(bin(n))[2:].zfill(32)[::-1]
        # print(int(str1,2))
    def reverseBits2(self,n):
        res=0
        for i in range(32):
            res=(res<<1)+(n&1)
            n=n>>1
        print(res)



S=Solution()
print(dir(S))
S.reverseBits1(10100101000001111010011100)
S.reverseBits2(11)