class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0, len(nums)):
            for j in range(i, bisect_right(nums, 2*nums[i])):
                ans = max(ans, nums[i]^nums[j])
        return ans