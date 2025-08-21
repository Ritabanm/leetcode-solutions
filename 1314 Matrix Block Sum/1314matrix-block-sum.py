class Solution:
    def matrixBlockSum(self, matrix, K):
        m, n = len(matrix), len(matrix[0])
        
        # Crear una matriz auxiliar con valores acumulados
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + matrix[i][j]

        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                r_start, r_end = max(i - K, 0), min(i + K, m - 1)
                c_start, c_end = max(j - K, 0), min(j + K, n - 1)
                result[i][j] = dp[r_end + 1][c_end + 1] - dp[r_end + 1][c_start] - dp[r_start][c_end + 1] + dp[r_start][c_start]

        return result