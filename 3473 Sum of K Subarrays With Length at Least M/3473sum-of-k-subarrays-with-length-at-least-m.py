inf = float('inf')
class Solution:
    def maxSum(self, nums: List[int], K: int, m: int) -> int:
        n = len(nums)
        psum = [0] * n
        for i in range(n):
            if i == 0:
                psum[i] = nums[i]
            else:
                psum[i] = psum[i-1] + nums[i]
        
        dp = [[-inf] * (K+1) for _ in range(n+1)]
        sub_best = [-inf] * (n+1)
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(n-1, -1, -1):
            sub_best[i] = max(sub_best[i+1], psum[i])
            
        
        for k in range(1, K+1):
            for i in range(n-1, -1, -1):
                if i+m-1 < n:
                    dp[i][k] = max(dp[i+1][k], sub_best[i+m-1] - (psum[i-1] if i > 0 else 0))
            sub_best = [-inf] * (n+1)
            for i in range(n-1, -1, -1):
                sub_best[i] = max(sub_best[i+1], psum[i] + dp[i+1][k])
        return max(dp[i][K] for i in range(n))

                
        
        