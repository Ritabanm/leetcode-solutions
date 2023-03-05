class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        n = len(points)
        mask = defaultdict(int)
        for i in range(n): 
            for j in range(i+1, n): 
                mask[i, j] ^= 1<<i ^ 1<<j 
                for k in range(j+1, n): 
                    if (points[i][0]-points[j][0]) * (points[i][1]-points[k][1]) == (points[i][1]-points[j][1]) * (points[i][0]-points[k][0]): mask[i, j] ^= 1<<k 
        
        dp = [inf]*(1<<n)
        dp[0] = 0 
        for m in range(1, 1<<n): 
            if  bin(m).count('1') <= 2: dp[m] = 1
            else: 
                for i in range(n): 
                    if m & 1<<i: break 
                for j in range(i+1, n): 
                    if m & 1<<j: dp[m] = min(dp[m], 1 + dp[m ^ mask[i, j]])
        return dp[-1]