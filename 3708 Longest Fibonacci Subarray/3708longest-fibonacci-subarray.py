class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        maxl = 2
        for r in range(2, len(nums)):
            if nums[r]!=nums[r-1]+nums[r-2]:
                while r-l+1>2:
                    l+=1
            maxl = max(maxl,r-l+1)
        return maxl