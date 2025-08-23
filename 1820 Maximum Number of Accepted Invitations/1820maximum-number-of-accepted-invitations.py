class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        match = [-1] * n
        
        def fn(i): 
            """Look up match for ith boy."""
            for j in range(n):
                if grid[i][j] and not seen[j]: 
                    seen[j] = True
                    if match[j] == -1 or fn(match[j]): 
                        match[j] = i
                        return True 
            return False 
        
        for i in range(m):
            seen = [False] * n
            if fn(i): ans += 1
        return ans 