class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def to_the_end(a, b, i):
            nonlocal n, num
            c, c_str = a + b, str(a + b)  # sort of do-while loop
            c_l = len(c_str)
            while i + c_l <= n and num[i:i + c_l] == c_str:
                a, b = b, c
                c, c_str = a + b, str(a + b)
                i, c_l = i + c_l, len(c_str)
            return i == n  # when index reach to the end

        for i in range(1, n):  # try out all first value possibilities
            if i > 1 and num[0] == '0': break  # leading zero non-zero number, like '02'
            first = int(num[:i])
            print(first)
            for j in range(i + 1, n):  # try out all second value possibilities
                print(j)
                if j > i + 1 and num[i] == '0': break  # leading zero non-zero number, like '02'
                second = int(num[i:j])
                print(second)
                if to_the_end(first, second, j):  # given first & second str, see if it can reach to the end
                    return "OK"
        return False
S=Solution()
print(S.isAdditiveNumber("11235820"))