class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        ans, m, n = -inf, len(grid), len(grid[0])
        grid = [[inf]*n] + grid
        grid = [[inf]+row for row in grid]
        # for row in grid: print(row)
        
        for row, col in product(range(m), range(n)):
            mn = min(grid[row][col+1], grid[row+1][col])
            ans = max(ans, grid[row+1][col+1] - mn)
            grid[row+1][col+1] = min(grid[row+1][col+1], mn)
         # for row in grid: print(row)
        
        return ans