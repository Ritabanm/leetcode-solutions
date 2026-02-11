class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        if stampHeight > m or stampWidth > n:
            return all(cell == 1 for row in grid for cell in row)
        
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                prefix[i + 1][j + 1] = prefix[i][j + 1] + row_sum
        
        def is_empty(x1, y1, x2, y2):
            return prefix[x2 + 1][y2 + 1] - prefix[x1][y2 + 1] - prefix[x2 + 1][y1] + prefix[x1][y1] == 0
        
        diff = [[0] * (n + 2) for _ in range(m + 2)]
        
        for x1 in range(m - stampHeight + 1):
            for y1 in range(n - stampWidth + 1):
                x2 = x1 + stampHeight - 1
                y2 = y1 + stampWidth - 1
                if is_empty(x1, y1, x2, y2):
                    diff[x1][y1] += 1
                    diff[x1][y2 + 1] -= 1
                    diff[x2 + 1][y1] -= 1
                    diff[x2 + 1][y2 + 1] += 1
        
        coverage = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                coverage[i + 1][j + 1] = diff[i][j] + coverage[i][j + 1] + coverage[i + 1][j] - coverage[i][j]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and coverage[i + 1][j + 1] == 0:
                    return False
        return True