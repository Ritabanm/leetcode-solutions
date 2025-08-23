class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        dp = [[0]*(1 + numCarpets) for _ in range(len(floor)+1)]
        for i in range(len(floor)-1, -1, -1): 
            for j in range(0, numCarpets+1): 
                if floor[i] == '1': 
                    dp[i][j] = 1 + dp[i+1][j] 
                    if j: 
                        if i+carpetLen >= len(floor): dp[i][j] = 0 
                        else: dp[i][j] = min(dp[i+carpetLen][j-1], dp[i][j])
                else: dp[i][j] = dp[i+1][j]
        return dp[0][numCarpets]