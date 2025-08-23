class Solution:
    def maxSelectedElements(self, nums: List[int], mx = 1) -> int:

        nums.sort(reverse = True)
        dp = [0]*(nums[0] + 3)

        for num in nums:
            dp[num] = 1 + dp[num + 1]
            dp[num + 1] = 1 + dp[num + 2]
            mx = max(mx, dp[num], dp[num + 1])

        return mx