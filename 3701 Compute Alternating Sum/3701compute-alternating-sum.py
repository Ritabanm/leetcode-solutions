class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result+=nums[i]*(1 if i%2==0 else -1)
        return result