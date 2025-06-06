class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[0 for j in range(len(w2)+1)] for i in range(len(w1)+1)]
        for i in range(len(w1)-1,-1,-1):
            for j in range(len(w2)-1,-1,-1):
                if w1[i] == w2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return len(w1)-dp[0][0] + len(w2)-dp[0][0]