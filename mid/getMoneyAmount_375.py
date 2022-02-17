from functools import lru_cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def help(l, r):
            res = float('Inf')
            if l >= r: return 0
            for i in range((l + r) // 2, r):
                res = min(res, max(help(l, i - 1), help(i + 1, r)) + i)

            return res

        return help(1, n)
s=Solution()
s.getMoneyAmount(20)