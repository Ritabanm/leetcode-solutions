class Solution:
    def getSum(self, nums: List[int]) -> int:
        ans = nums[0]
        MOD = 10**9 + 7
        
        curr = nums[0]
        left = 0
        prior = 0
        for right in range(1, len(nums)):
            diff = nums[right] - nums[right-1]
            
            if abs(diff) != 1:
                prior = 0
                left = right
                curr = 0
            elif prior != diff:
                    curr = nums[right-1]
                    left = right-1
                    prior = diff
            curr += nums[right] * (right-left+1)
            ans = (ans + curr)  % MOD
        return ans