class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        t=0
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            t+=sum(nums[start:i+1])
        return t

