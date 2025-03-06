class Solution:
    def maxValidPairSum(self,nums, k):
        max_i = nums[0]
        res = 0
        for i in range(k, len(nums)):
            max_i = max(max_i, nums[i-k])
            res = max(res, max_i+nums[i])
        return res