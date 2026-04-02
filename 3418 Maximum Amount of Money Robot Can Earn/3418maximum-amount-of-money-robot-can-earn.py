class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:

        dp = lambda v, x: (max(v + x[0], x[1]), max(v + x[1], x[2]), v + x[2])

        m, n = len(coins), len(coins[0])
        coins[0][0] = (0, 0, coins[0][0])                       # <-- 1)

        for col in range(1,n):                                  # <-- 2)
            coins[0][col] = dp(coins[0][col], coins[0][col-1])

        for row in range(1,m):                                  # <-- 3)
            coins[row][0] = dp(coins[row][0], coins[row-1][0])

            for col in range(1,n):
                uppr0, uppr1, uppr2 = coins[row-1][col]
                left0, left1, left2 = coins[row][col-1]
                best = (max(uppr0, left0), max(uppr1, left1), max(uppr2, left2))

                coins[row][col] = dp(coins[row][col], best)
        
        return max(coins[-1][-1])                               # <-- 4)