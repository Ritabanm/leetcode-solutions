class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        
        self.full = 2 ** n - 1
        @lru_cache(None)
        def dfs(idx, mask):
            if idx == n:
                if mask == self.full:
                    return 1
                return 0
            
            ans = 0
            for i in range(n):
                if (1 << i & mask) == 0 and math.gcd(i + 1, idx + 1) == 1:
                    ans += dfs(idx + 1, 1 << i | mask)
            return ans
        
        return dfs(0, 0)