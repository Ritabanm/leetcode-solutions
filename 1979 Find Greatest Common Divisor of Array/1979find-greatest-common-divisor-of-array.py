class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        divisor = min_num
        dividend = max_num

        remainder = dividend%divisor
        while remainder:
            dividend = divisor
            divisor = remainder
            remainder = dividend%divisor
        return divisor