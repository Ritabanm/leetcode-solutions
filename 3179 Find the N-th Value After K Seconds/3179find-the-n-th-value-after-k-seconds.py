class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
    
        dp = [1] * n
        
        for _ in range(k):
            new_dp = dp[:]
            for i in range(1, n):
                new_dp[i] = (new_dp[i - 1] + dp[i]) % MOD
            dp = new_dp
        
        return dp[-1]