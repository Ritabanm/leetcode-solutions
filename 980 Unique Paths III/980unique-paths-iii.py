class Solution:
    def uniquePathsIII(self, grid):
        rows, cols = len(grid), len(grid[0])
        start_x = start_y = 0
        empty_cells = 0

        # Count the number of empty cells (including start and end)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_x, start_y = r, c
                if grid[r][c] != -1:  # Count all walkable cells (0, 1, 2)
                    empty_cells += 1

        def dfs(x, y, remaining):
            # Base case: If we reach the ending cell (2)
            if grid[x][y] == 2:
                return 1 if remaining == 0 else 0

            # Mark the current cell as visited
            grid[x][y] = -1  
            paths = 0

            # Explore all 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
                    paths += dfs(nx, ny, remaining - 1)

            # Backtrack: Restore the grid cell
            grid[x][y] = 0  

            return paths

        # Start DFS from the starting position
        return dfs(start_x, start_y, empty_cells - 1)
