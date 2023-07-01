"""class Solution:
    def removeDuplicates(self, nums):
        if not nums or len(nums)==0:
            return []
        size = len(nums)
        ii = 1
        for i in range(1, size):
            if nums[i-1]!=nums[i]:
                nums[ii]=nums[i]
                ii = ii+1
        return ii"""


class Solution:
    def removeDuplicates(self, nums):
        if not nums or len(nums)==0:
            return []
        
        size = len(nums)
        ii = 1
        for i in range(1, size):
            if nums[i-1]!=nums[i]:
                nums[ii]=nums[i]
                ii = ii+1
        return ii