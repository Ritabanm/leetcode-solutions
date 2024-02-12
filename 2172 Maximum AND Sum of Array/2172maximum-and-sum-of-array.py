class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        
        @lru_cache(None)
        def dp(i, m1, m2):
            if i == len(nums):
                return 0

            ans = float('-inf')
            for j in range(numSlots):
                if m1 & (1 << j):
                    ans = max(ans, (nums[i] & (j + 1)) + dp(i + 1, m1 ^ (1 << j), m2))
                elif m2 & (1 << j):
                    ans = max(ans, (nums[i] & (j + 1)) + dp(i + 1, m1, m2 ^ (1 << j)))
            return ans

        return dp(0, (1<<numSlots)-1, (1<<numSlots)-1)