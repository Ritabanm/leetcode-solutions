class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        if n%2:
            dp = 0
            for i in range(1,n-1,2):
                dp+=max(max(nums[i-1], nums[i+1])-nums[i]+1,0)
            return dp
        dp1, dp2 = 0,0
        for i in range(1, n-2,2):
            dp1+= max(max(nums[i-1], nums[i+1])-nums[i]+1,0)
            dp2+= max(max(nums[i], nums[i+2])-nums[i+1]+1,0)
            dp2 = min(dp1, dp2)
        return dp2