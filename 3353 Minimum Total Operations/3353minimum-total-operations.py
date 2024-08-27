class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                cnt+=1
        return cnt