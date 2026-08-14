class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        val = [1] + nums + [1]
        dp = [[0]*(n+2) for _ in range(n+2)]

        for length in range(2, n+2):
            for left in range(0, n+2-length):
                right = left + length
                for k in range(left+1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k] + dp[k][right] 
                        + val[left]*val[k]*val[right])
        return dp[0][n+1]