class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:        
        if nums.count(1) == 0:
            return 0

        n = len(nums)
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i = 0, hasOne = False):
            if i == n:
                return int(hasOne)
            
            ans = 0
            if nums[i] == 0:
                ans += dp(i + 1, hasOne) # Continue Subarray As It is
                if hasOne:
                    ans += dp(i + 1, False) # Discontinue Subarray
            else:
                # Continue or Discontinue Subarray
                ans = dp(i + 1, True) 

            return ans % MOD

        return dp()