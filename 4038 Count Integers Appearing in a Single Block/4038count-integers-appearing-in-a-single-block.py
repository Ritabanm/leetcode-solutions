class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:

        once, twce = 1 << nums[0], 0

        for lft, rgt in pairwise(nums):
            if lft == rgt: continue
            twce|= (1 << rgt) & once
            once|= (1 << rgt)

        return (once & ~ twce).bit_count()