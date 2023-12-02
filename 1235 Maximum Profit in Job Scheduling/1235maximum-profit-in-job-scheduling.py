from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        # Step 1: Sort jobs based on endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        start, end, profit = zip(*jobs)  # Unzip sorted jobs

        # Step 2: DP array with binary search
        dp = [(0, 0)]  # (endTime, maxProfit)

        for i in range(len(start)):
            # Step 3: Find the latest job that doesn't overlap
            idx = bisect_right(dp, (start[i], float('inf'))) - 1
            new_profit = dp[idx][1] + profit[i]

            # Step 4: Update DP if this job gives more profit
            if new_profit > dp[-1][1]:
                dp.append((end[i], new_profit))

        return dp[-1][1]
