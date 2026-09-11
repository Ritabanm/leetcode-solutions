class Solution:
    def minOperations(self, nums):
        MAX_XOR = 2048
        n = len(nums)

      
        total = 0
        
        for x in nums:
            total ^= x

        if total == 0:
            return 0


        if len(set(nums)) == 1:
            return -1

       
        values = set(nums)

        INF = n + 1
        dp = [INF] * MAX_XOR
        dp[0] = 0

        for x in values:
            new_dp = dp[:]

            for v in range(MAX_XOR):
                if dp[v] != INF:
                    nv = v ^ x
                    new_dp[nv] = min(new_dp[nv], dp[v] + 1)

            dp = new_dp

        k = dp[total]


        if k >= n:
            return -1

        return k