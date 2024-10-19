class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        return sum(n>0 for n in accumulate(nums))