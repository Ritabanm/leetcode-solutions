"""class Solution:
    def moveZeroes(self, nums):
        idx = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                t = nums[idx]
                nums[idx]=nums[i]
                nums[i]=t
                idx+=1
"""

class Solution:
    def moveZeroes(self,nums):
        idx = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                t = nums[idx]
                nums[idx]=nums[i]
                nums[i]=t
                idx+=1
                