class Solution:
    def deleteString(self, S):
        N = len(S)
        if S.count(S[0]) == N: return N
        P = [0] * (N + 1)
        dp = [1] * N
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                P[j] = P[j + 1] + 1 if S[i] == S[j] else 0
                if P[j] >= j - i:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[0]