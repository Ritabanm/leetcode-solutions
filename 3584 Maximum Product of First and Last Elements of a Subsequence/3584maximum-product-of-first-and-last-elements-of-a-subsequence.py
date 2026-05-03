class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        ans, n = -inf, len(nums)
        small, large = inf, -inf
        for j in range(k - 1, n):
            i = j - k + 1
            small = min(small, nums[i])
            large = max(large, nums[i])
            ans = max(nums[j] * small, nums[j] * large, ans)
        return ans