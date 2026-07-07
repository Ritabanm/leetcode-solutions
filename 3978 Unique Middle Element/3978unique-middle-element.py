class Solution:
    def isMiddleElementUnique(self,nums):
        mid_idx = len(nums)//2
        mid_val = nums[mid_idx]
        return nums.count(mid_val)==1