class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i == n:
                return 0

            # pick up current passenger
            curr_ride = rides[i]
            start = curr_ride[0]
            end = curr_ride[1]
            tip = curr_ride[2]
            # binary search on next passenger
            lo, hi = i + 1, n - 1
            while lo < hi:
                mid = lo + ((hi - lo) >> 1)
                if rides[mid][0] >= end:
                    hi = mid
                else:
                    lo = mid + 1

            # profit: end - start + tip
            pick = end - start + tip + (
                dp(lo) 
                if lo < n and rides[lo][0] >= end 
                else 0
            )
            not_pick = dp(i + 1)
            return max(pick, not_pick)

        rides.sort()
        n = len(rides)
        return dp(0)