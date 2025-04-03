class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * min(k + 1, 51) for _ in range(n)]

        max_length = 1
        
        for i in range(1, n):
            for j in range(min(k, 50) + 1):
                for m in range(i):
                    if nums[m] == nums[i]:
                        dp[i][j] = max(dp[i][j], dp[m][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[m][j - 1] + 1)
                
                max_length = max(max_length, dp[i][j])
        
        return max_length