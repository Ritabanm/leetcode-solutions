class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        total = 1
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        if len(negative) % 2 != 0:
            negative.sort()
            negative.pop()
        if not positive and not negative:
            return max(nums)
        for num in positive:
            total *= num
        for num in negative:
            total *= num
        return total