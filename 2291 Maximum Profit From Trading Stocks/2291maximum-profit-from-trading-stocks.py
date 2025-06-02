class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        total_cost = sum(present)
        dp = [[0] * (budget + 1) for _ in range(n + 1)]

        curr_cost = 0
        for i in range(n - 1, -1, -1):
            for curr_cost in range(budget, -1, -1):
                buy = 0
    
                if curr_cost + present[i] <= budget:
                    buy = future[i] - present[i] + dp[i + 1][curr_cost + present[i]]
                not_buy = dp[i + 1][curr_cost]
                dp[i][curr_cost] = max(buy, not_buy)

        return dp[0][0]