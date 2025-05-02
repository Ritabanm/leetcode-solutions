class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m,n = len(grid), len(grid[0])
        compatible_set = set()

        for i in range(n):
            for j in range(i+1,n):
                if all(abs(grid[r][i]-grid[r][j])<= limit for r in range(m)):
                    compatible_set.add((i,j))
        
        dp = [1]*n
        for j in range(1,n):
            for i in range(j):
                if (i,j) in compatible_set:
                    dp[j]=max(dp[j], dp[i]+1)
        return max(dp)