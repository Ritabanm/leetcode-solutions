class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        s = nums[0] + nums[1]
        cnt, idx = 1, 2
        while idx + 1 < len(nums) and nums[idx] + nums[idx + 1] == s:
            cnt += 1
            idx += 2
        return cnt