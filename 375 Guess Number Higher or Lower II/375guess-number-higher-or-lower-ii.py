class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(l, r):
            if l >= r:
                return 0       
            ans = float('inf')     
            for i in range(l, r):
                ans = min(ans, max(dp(l, i - 1), dp(i + 1, r)) + i)
            return ans
        return dp(1, n)