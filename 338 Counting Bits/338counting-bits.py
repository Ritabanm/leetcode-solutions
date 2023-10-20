class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize an array to store the number of 1s for each number
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # Use the formula: dp[i] = dp[i >> 1] + (i & 1)
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp
