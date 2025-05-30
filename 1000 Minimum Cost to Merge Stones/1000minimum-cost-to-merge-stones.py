class Solution:
    def mergeStones(self, stones: List[int], K: int):
        N = len(stones)
        if (N-1) % (K-1) != 0:
            return -1
        accum = [0] + list(itertools.accumulate(stones))

        dp = [[0]*N for _ in range(N)]
        for l in range(K, N+1):
            for i in range(N-l+1):
                j = i+l-1
                if l > K:
                    dp[i][j] = min([dp[i][t] + dp[t+1][j] for t in range(i,j,K-1)])
                if (l-1)%(K-1) == 0:
                    dp[i][j] += accum[j+1] - accum[i]

        return dp[0][N-1]