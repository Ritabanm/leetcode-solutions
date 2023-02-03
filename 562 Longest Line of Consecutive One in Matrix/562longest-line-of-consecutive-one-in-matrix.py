class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # maximum line of len [0..n] in direction (horizonal, vertical, diagonal, antidiagonal)
        dp = [[(0, 0, 0, 0)] * (n + 2) for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if mat[i-1][j-1] == 1:
                    dp[i][j] = (dp[i][j-1][0] + 1, dp[i-1][j][1] + 1, dp[i-1][j-1][2] + 1, dp[i-1][j+1][3] + 1)
                    ans = max(max(dp[i][j]), ans)
        return ans