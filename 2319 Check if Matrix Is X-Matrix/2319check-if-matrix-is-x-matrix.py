class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        size = len(grid)
        last = size - 1

        for i in range(size):
            if grid[i][i] == 0 or grid[i][last - i] == 0:
                return False

            grid[i][i] = 0
            grid[i][last - i] = 0

        return sum(map(sum, grid)) == 0