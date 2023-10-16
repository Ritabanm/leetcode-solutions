class Solution:
    def containsDuplicate(self, nums):
        if not nums or len(nums)==0:
            return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False