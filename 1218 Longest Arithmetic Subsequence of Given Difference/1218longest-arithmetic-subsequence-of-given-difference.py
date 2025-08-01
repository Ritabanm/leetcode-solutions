class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        for a in arr:
            b_a = dp.get(a-difference,0)
            dp[a]=b_a+1
            ans = max(ans, dp[a])
        return ans