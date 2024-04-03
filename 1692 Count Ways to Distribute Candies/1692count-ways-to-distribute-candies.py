class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        d = [[0]*(k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, min(i+1,k+1)):
                if i == j or j == 1:
                    d[i][j] = 1
                    continue
                d[i][j] = (d[i-1][j-1] + j*d[i-1][j])%MOD
        return d[-1][-1]