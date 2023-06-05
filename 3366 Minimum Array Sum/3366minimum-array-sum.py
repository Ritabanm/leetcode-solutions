class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        @cache
        def dp(i,p1,p2):
            if i == len(nums):
                return 0
            ans = nums[i] + dp(i+1,p1,p2)
            if p1:
                ans = min(ans,ceil(nums[i]/2) + dp(i+1,p1-1,p2))
            if p2 and nums[i] >= k:
                ans = min(ans,nums[i]-k+dp(i+1,p1,p2-1))
            if p1 and p2 and nums[i] >= k:
                ans = min(ans,ceil((nums[i]-k)/2)+dp(i+1,p1-1,p2-1))
            if p1 and p2 and ceil(nums[i]/2) >= k:
                ans = min(ans,ceil(nums[i]/2)-k+dp(i+1,p1-1,p2-1))
            return ans
        
        return dp(0,op1,op2)