class Solution:
    def maxVacationDays(self, flights, days):
        if not flights or not days:
            return 0
        
        n, k = len(flights), len(days[0])  # n = cities, k = weeks
        dp = [-float('inf')] * n  # Stores max vacation days per city for the current week
        dp[0] = 0  # Start in city 0

        # DP Iteration over weeks
        for week in range(k):
            new_dp = [-float('inf')] * n  # Temp storage for current week results

            for city in range(n):  # Destination city
                for prev_city in range(n):  # Source city
                    if prev_city == city or flights[prev_city][city] == 1:
                        new_dp[city] = max(new_dp[city], dp[prev_city] + days[city][week])

            dp = new_dp  # Move to next week
        
        return max(dp)  # Maximum vacation days across all cities
