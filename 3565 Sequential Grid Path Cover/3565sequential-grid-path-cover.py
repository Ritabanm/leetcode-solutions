class Solution:
    def findPath(self, grid: List[List[int]], k: int) -> List[List[int]]:

        def backtrack(row: int, col: int, num: int)-> bool:

            cell = grid[row][col]
            if  cell == -1 or (cell != 0 and cell != num): return False
        
            path.append([row, col])
            if len(path) == m * n: return True
            if cell == num: num+= 1
            grid[row][col] = -1
            
            for dr, dc in dir:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and backtrack(r, c, num):
                    return True
                    
            grid[row][col] = cell
            path.pop()
            return False


        dir = ((0, -1), (-1, 0), (0, 1), (1, 0))
        m, n, path = len(grid), len(grid[0]), []

        for row in range(m):
            for col in range(n):
                if grid[row][col] > 1: continue
                if backtrack(row, col, 1): break

        return path