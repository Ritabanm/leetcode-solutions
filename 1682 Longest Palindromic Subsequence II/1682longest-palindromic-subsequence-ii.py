class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        for i in range(n-1,-1,-1):
            maxP = 0
            for j in range(i+1, n):
                if s[i]!=s[j]:
                    maxP = max(maxP,dp[j])
                else:
                    dp[j] = 2+maxP
        return max(dp)