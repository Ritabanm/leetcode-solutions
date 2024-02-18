class Solution:
    def maxWeight(self, weights: List[int], w1: int, w2: int) -> int:
        dp = [[0 for _ in range(w2+1)] for _ in range(w1+1)]

        for w in weights:
            for i in range(w1+1):
                for j in range(w2+1):
                    take1 = take2 = 0
                    if i+w <= w1:
                        take1 = dp[i+w][j] + w
                    if j+w <= w2:
                        take2 = dp[i][j+w] + w
                    dp[i][j] = max(dp[i][j], take1, take2)

        return dp[0][0]

