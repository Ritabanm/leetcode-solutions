class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == n == 1:
            return grid[0][0]

        entry = [[inf] * n for _ in range(m)]
        entry[0][0] = grid[0][0]  # no direction yet, no turns spent

        for _ in range(k + 1):
            nxt = [[inf] * n for _ in range(m)]
            for i in range(m):  # right
                run = inf
                for j in range(1, n):
                    run = min(run, entry[i][j - 1]) + grid[i][j]
                    nxt[i][j] = min(nxt[i][j], run)
            for i in range(m):  # left
                run = inf
                for j in range(n - 2, -1, -1):
                    run = min(run, entry[i][j + 1]) + grid[i][j]
                    nxt[i][j] = min(nxt[i][j], run)
            for j in range(n):  # down
                run = inf
                for i in range(1, m):
                    run = min(run, entry[i - 1][j]) + grid[i][j]
                    nxt[i][j] = min(nxt[i][j], run)
            for j in range(n):  # up
                run = inf
                for i in range(m - 2, -1, -1):
                    run = min(run, entry[i + 1][j]) + grid[i][j]
                    nxt[i][j] = min(nxt[i][j], run)
            entry = nxt

        return -1 if entry[-1][-1] == inf else entry[-1][-1]