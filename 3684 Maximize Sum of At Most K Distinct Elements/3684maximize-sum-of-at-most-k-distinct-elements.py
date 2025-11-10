class Solution:
    def maxKDistinct(self, nums: list[int], k: int) -> list[int]:
        nums = list(set(nums))
        nums.sort(reverse = True)
        return nums[:k]