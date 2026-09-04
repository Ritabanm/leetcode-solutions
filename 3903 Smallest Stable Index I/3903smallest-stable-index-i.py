"""class Solution:
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            m = max(nums[:i+1])
            m1 = min(nums[i:])
            if m-m1<=k:
                return i
        return -1"""

class Solution:
    def firstStableIndex(self,nums, k):
        for i in range(len(nums)):
            m = max(nums[:i+1])
            m1 = min(nums[i:])
            if m-m1<=k:
                return i
        return -1