class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if len(nums)%2==1:
            return sum(nums)-min(nums)
        else:
            return sum(nums)-min(map(sum, pairwise(nums)))