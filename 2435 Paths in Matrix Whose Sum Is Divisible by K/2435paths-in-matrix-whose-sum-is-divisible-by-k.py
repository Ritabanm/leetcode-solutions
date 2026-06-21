class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod=10**9+7
        n = len(grid)
        m = len(grid[0])
        memo = {}
        

        def solve(i, j, curr_sum):
            if i == n - 1 and j == m - 1:
                if (grid[i][j] + curr_sum) % k == 0:
                    return 1
                else:
                    return 0

            if i >= n or j >= m:
                return 0

            if (i, j, curr_sum) in memo:
                return memo[(i, j, curr_sum)]

            down = solve(i + 1, j, (curr_sum + grid[i][j]) % k)

            right = solve(i, j + 1, (curr_sum + grid[i][j]) % k)
            memo[(i, j, curr_sum)] = (down + right) % mod

            return memo[(i, j, curr_sum)]

        return solve(0, 0, 0)