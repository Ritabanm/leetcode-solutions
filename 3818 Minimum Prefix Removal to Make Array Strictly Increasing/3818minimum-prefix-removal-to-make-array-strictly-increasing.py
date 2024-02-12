class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        i = n-1
        while i>0 and nums[i-1]<nums[i]:
            i-=1
        count = i
        return count