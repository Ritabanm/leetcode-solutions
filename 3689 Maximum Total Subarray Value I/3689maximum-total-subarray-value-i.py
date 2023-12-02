class Solution:
    def maxTotalValue(self, nums, k):
        m1 = min(nums)
        m2 = max(nums)
        return (m2-m1)*k