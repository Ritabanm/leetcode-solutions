class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for index in range(n):
            ans = max(ans, nums[index]+nums[n-index-1])
        return ans
        