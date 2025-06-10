class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m: return 1
        depth = [0]*m
        
        def fn(x): 
            """Explore tiling rectangle area via backtracking."""
            nonlocal ans 
            if x < ans: 
                if min(depth) == n: ans = x # all tiled
                else: 
                    i = min(depth)
                    j = jj = depth.index(i) # (i, j)
                    while jj < m and depth[jj] == depth[j]: jj += 1
                    k = min(n - i, jj - j)
                    for kk in reversed(range(1, k+1)): 
                        for jj in range(j, j+kk): depth[jj] += kk
                        fn(x+1)
                        for jj in range(j, j+kk): depth[jj] -= kk
                            
        ans = max(n, m)
        fn(0)
        return ans 