from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        # Step 1: Sort envelopes
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # Sort by width asc, height desc

        # Step 2: Extract heights and find LIS
        heights = [h for _, h in envelopes]  # Extract heights after sorting
        dp = []

        for h in heights:
            idx = bisect_left(dp, h)  # Find insertion position
            if idx == len(dp):
                dp.append(h)  # Extend LIS
            else:
                dp[idx] = h  # Replace element

        return len(dp)  # Length of LIS in heights
