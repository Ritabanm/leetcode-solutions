class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
    
        return sum(max(row[i] for row in grid) for i in range(len(grid[0])))
