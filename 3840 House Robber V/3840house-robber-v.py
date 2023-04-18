class Solution:
    def rob(self, nums, colors):
        n = len(nums)
        if n==1:
            return nums[0]
        
        dp = [0]*(n+2)
        for i in range(n-1,-1,-1):
            if i+1<n and colors[i]!=colors[i+1]:
                take = nums[i]+dp[i+1]
            else:
                take = nums[i]+dp[i+2]
            skip = dp[i+1]
            dp[i]=max(skip, take)
        return dp[0]