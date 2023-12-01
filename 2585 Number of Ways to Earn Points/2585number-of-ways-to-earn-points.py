class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [[0]*(target+1) for _ in range(len(types) + 1)]
        dp[0][0] = 1
        for i in range(len(types)):
            c, v = types[i]
            for j in range(target+1):
                for k in range(c+1):
                    if j + k*v > target: break
                    dp[i+1][j+k*v] = dp[i+1][j+k*v] + dp[i][j]
        return dp[-1][-1] % (10**9 + 7)