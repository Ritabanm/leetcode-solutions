class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_sum=-float('inf')
        for i in range(1,n-1):
            for j in range(1,m-1):
                max_sum = max(max_sum, grid[i][j])
        
        for i in range(n):
            curr_sum = grid[i][0]
            for j in range(1,m):
                curr_sum = max(curr_sum + grid[i][j], grid[i][j] + grid[i][j-1])
                max_sum = max(max_sum, curr_sum)
        
        for j in range(m):
            curr_sum = grid[0][j]
            for i in range(1, n):
                curr_sum = max(curr_sum + grid[i][j], 
                grid[i][j]+grid[i-1][j])
                max_sum = max(max_sum, curr_sum)
        return max_sum