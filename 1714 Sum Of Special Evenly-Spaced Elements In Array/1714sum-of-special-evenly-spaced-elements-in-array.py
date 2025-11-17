class Solution:
    def solve(self, nums, queries):
        n = len(nums)

        m, mod = int(n**0.5), 10**9+7

        ans = [nums[:] for _ in range(m)]

        for i in range(1,m):
            for j in range(n-1,-1,-1):
                if i+j < n:
                    ans[i][j] = (ans[i][j] + ans[i][i+j])%mod

        return [ans[k][b] if k < m else sum(nums[b::k])%mod for b,k in queries]

        

        
        