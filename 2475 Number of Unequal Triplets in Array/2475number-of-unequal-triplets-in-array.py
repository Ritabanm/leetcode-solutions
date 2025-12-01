class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        freq = Counter(nums)
        left = 0
        right = len(nums)
        res = 0
        for i in freq.values():
            right -= i
            res += left * i * right
            left += i
        return res

