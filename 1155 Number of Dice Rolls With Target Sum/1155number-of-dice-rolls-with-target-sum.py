MOD = 10**9 + 7

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Initialize a DP array with (n+1) rows and (target+1) columns
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Base case: 1 way to get sum 0 with 0 dice
        dp[0][0] = 1

        # Fill the DP table
        for i in range(1, n + 1):  # Loop over the number of dice
            for j in range(1, target + 1):  # Loop over the possible sums
                for face in range(1, k + 1):  # Loop over the face values of the dice
                    if j - face >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MOD

        # The result is the number of ways to get the sum 'target' with 'n' dice
        return dp[n][target]