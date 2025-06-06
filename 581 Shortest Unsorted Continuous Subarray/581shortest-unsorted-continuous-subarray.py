class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortNums  = sorted(nums)
        if sortNums == nums:
            return 0
        
        for i in range(len(nums)):
            if nums[i]!=sortNums[i]:
                firstMismatchidx = i
                break
        
        for j in range(len(nums)-1, -1, -1):
            if nums[j]!=sortNums[j]:
                lastMismatchidx = j
                break
        return lastMismatchidx - firstMismatchidx+1