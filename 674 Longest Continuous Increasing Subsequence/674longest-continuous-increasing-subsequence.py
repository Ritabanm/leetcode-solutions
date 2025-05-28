class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        long = 1
        currLen = 1
        for i in range(1, n):
            if nums[i]>nums[i-1]:
                currLen+=1
                long = max(long, currLen)
            else:
                currLen=1
        return long