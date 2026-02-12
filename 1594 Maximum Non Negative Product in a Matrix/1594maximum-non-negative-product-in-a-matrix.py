class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        L = [[(1,1) for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    L[i][j] = (grid[i][j], grid[i][j])
                else:
                    if i != 0 and j != 0:
                        values = L[i][j-1] + L[i-1][j]
                    else:
                        values = L[max(0, i-1)][max(0, j-1)]
                    L[i][j] = (min(values) * grid[i][j], max(values) * grid[i][j])
        
        res = max(L[i][j])
        if res < 0: return -1
        else: return res %(10**9+7)