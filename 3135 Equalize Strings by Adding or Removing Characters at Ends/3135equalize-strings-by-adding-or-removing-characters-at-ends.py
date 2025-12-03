class Solution:
    def minOperations(self, initial, target):
        m, n = len(initial), len(target)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if initial[i-1] == target[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

        max_val = max([max(i) for i in dp])

        return m+n-2*max_val