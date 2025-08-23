class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diffs = [0]*n
        for i in range(n):
            diffs[i] = len(set(nums[:i+1])) - len(set(nums[i+1:]))
        return diffs