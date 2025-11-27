class Solution:
    def minDays(self, n: int) -> int:
        # dp[score] will store the minimum days to reach a specific score.
        # Initialize with infinity, and dp[0] = 0 (0 days for 0 points).
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Precompute possible streak lengths L
        # Points earned: pts = L * (L + 1) // 2
        # Total days incurred: days = L + 1 (streak days + 1 skipped day)
        streaks = []
        L = 1
        while True:
            pts = L * (L + 1) // 2
            if pts > n:
                break
            days = L + 1
            streaks.append((pts, days))
            L += 1
            
        # Unbounded knapsack / DP transition
        for score in range(1, n + 1):
            for pts, days in streaks:
                if score >= pts:
                    dp[score] = min(dp[score], dp[score - pts] + days)
                    
        # Subtract 1 because the final streak does not need a trailing skip day
        return dp[n] - 1