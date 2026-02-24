class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 0
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j >= nums[i - 1] and dp[i - 1][j - nums[i - 1]] != -1:
                    dp[i][j] = max(1 + dp[i - 1][j - nums[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        #print(dp)
        return dp[n][target] 