class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            nonlocal m, n, grid
            if not grid[x][y]:
                return False
            if x == m-1 and y == n-1:
                return True
            grid[x][y] = 0    
            if x + 1 < m and dfs(x + 1, y):
                return True
            if y + 1 < n and dfs(x, y + 1):
                return True
            return False
        dfs(0, 0)            # destroy one path
        grid[0][0] = 1       # reset origin
        return not dfs(0, 0) # try to find another path, if not possible, then such a point exists
                            