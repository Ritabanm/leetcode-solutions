class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        while nums:
            res += nums[:2][::-1]
            nums = nums[2:]
        return res