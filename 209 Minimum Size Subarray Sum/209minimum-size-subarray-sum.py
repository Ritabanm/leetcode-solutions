class Solution:
    def minSubArrayLen(self, target, nums):
        l = 0
        r = 0 
        sumOfCurrentWindow = 0
        res = float('inf')
        for r in range(0, len(nums)):
            sumOfCurrentWindow += nums[r]
            while sumOfCurrentWindow>=target:
                res = min(res, r-l+1)
                sumOfCurrentWindow -= nums[l]
                l+=1
        return res if res!=float('inf') else 0
        #T: O(N), S: O(1)