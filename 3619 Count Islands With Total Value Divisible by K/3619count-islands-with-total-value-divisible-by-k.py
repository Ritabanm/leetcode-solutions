from collections import deque

class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    tot = grid[i][j]
                    grid[i][j] = 0
                    dq = deque([(i, j)])
                    while dq:
                        x, y = dq.popleft()
                        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                                tot += grid[nx][ny]
                                grid[nx][ny] = 0
                                dq.append((nx, ny))
                    if tot % k == 0:
                        cnt += 1
        return cnt