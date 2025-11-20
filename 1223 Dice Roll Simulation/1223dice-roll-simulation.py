class Solution:
    def dieSimulator(self, n, A):
        dp = [[0] * 6 + [1]]
        for i in range(n):
            dp.append([dp[i][-1] - (dp[i - A[j]][-1] - dp[i - A[j]][j] if i >= A[j] else 0) for j in range(6)])
            dp[-1].append(sum(dp[-1]) % (10 ** 9 + 7))
        return dp[-1][-1]