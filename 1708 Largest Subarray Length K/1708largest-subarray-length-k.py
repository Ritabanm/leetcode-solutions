class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        ii = 0
        for i in range(len(nums)-k+1):
            if nums[i]>nums[ii]:ii = i
        return nums[ii:ii+k]