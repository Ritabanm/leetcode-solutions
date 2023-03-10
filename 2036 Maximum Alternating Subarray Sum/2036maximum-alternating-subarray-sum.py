class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        dance1 = dance2 = res = -inf
        for i in range(len(nums)):
            if i%2==0:
                dance1 = max(nums[i], dance1 + nums[i])
                dance2 -= nums[i]
            else:
                dance2 = max(dance2 + nums[i], nums[i])
                dance1 -= nums[i]
            res = max(dance1, dance2, res)
        return res