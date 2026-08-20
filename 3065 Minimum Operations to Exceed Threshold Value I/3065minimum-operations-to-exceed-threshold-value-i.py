class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ops, idx =0,0
        while idx<len(nums) and nums[idx]<k:
            ops+=1
            idx+=1
        return ops