class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        res = float('-inf')
        mp, curr, low, curr_min = Counter(), 0, 0, 0
        for n in nums:
            curr += n
            res = max(res, curr - curr_min)
            mp[n], low = min(mp[n], low) + n, min(curr, low)
            curr_min = min(curr_min, low, mp[n])
        return res