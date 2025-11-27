class Solution:
    def minCost(self, nums: List[int]) -> int:

        @lru_cache(3_000)
        def dp(i, num):
            
            if i >= n:
                return num
            if i >= n - 1:
                return max(nums[i], num)

            lo, md, hi = sorted([num, nums[i], nums[i+1]])

            return min(hi + dp(i+2,lo), hi + dp(i+2,md), md + dp(i+2, hi))

        n = len(nums)
        return dp(1, nums[0])