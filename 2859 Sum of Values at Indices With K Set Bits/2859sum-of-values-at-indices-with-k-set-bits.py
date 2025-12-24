class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        total = 0
        for i, val in enumerate(nums):
            if bin(i).count('1') == k:
                total += val
        return total