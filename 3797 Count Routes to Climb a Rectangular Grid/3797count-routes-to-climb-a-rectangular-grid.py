import math

class Solution:
    def numberOfRoutes(self, grid: list[str], d: int) -> int:
        n = len(grid)
        m = len(grid[0])
        MOD = 10**9 + 7

        def get_presum(arr):
            presum = [0] * (m + 1)
            for k in range(m):
                presum[k+1] = (presum[k] + arr[k]) % MOD
            return presum

        def query_sum(ps, l, r):
            l, r = max(0, l), min(m - 1, r)
            if l > r: return 0
            return (ps[r+1] - ps[l] + MOD) % MOD

        initial_dp = [1 if grid[n-1][j] == '.' else 0 for j in range(m)]
        ps_initial = get_presum(initial_dp)
        
        dp = [0] * m
        for j in range(m):
            if grid[n-1][j] == '.':
                dp[j] = query_sum(ps_initial, j - d, j + d)

        r_vert = int(math.isqrt(max(0, d*d - 1)))

        for i in range(n - 2, -1, -1):
            prev_ps = get_presum(dp)
            
            vert_dp = [0] * m
            for j in range(m):
                if grid[i][j] == '.':
                    vert_dp[j] = query_sum(prev_ps, j - r_vert, j + r_vert)
            
            v_ps = get_presum(vert_dp)
            
            new_dp = [0] * m
            for j in range(m):
                if grid[i][j] == '.':
                    ways_v = vert_dp[j]
                    ways_h = (query_sum(v_ps, j - d, j + d) - vert_dp[j] + MOD) % MOD
                    new_dp[j] = (ways_v + ways_h) % MOD
            
            dp = new_dp

        return sum(dp) % MOD