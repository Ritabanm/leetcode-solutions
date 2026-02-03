class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-inf]*(k+1) for _ in range(m+1)]
        for j in range(m+1): dp[j][0] = 0

        
        for i in range(n-1, -1, -1):
            tmp = [[-inf]*(k+1) for _ in range(m+1)]
            for j in range(m, -1, -1):
                for K in range(k+1):
                    res = dp[j][K]
                    if j < m: res = max(res, tmp[j+1][K])
                    if K and i < n and j < m: res = max(res, dp[j+1][K-1] + nums1[i]*nums2[j])
                    tmp[j][K] = res
            # print(dp)
            dp = tmp
        # print(dp)
        return dp[0][k]

        
        # @cache
        # def fn(i, j, K):
        #     nonlocal n, m
        #     if i >= n and j >= m: return 0 if K == 0 else -inf
        #     res = -inf
        #     if i < n: res = max(res, fn(i+1, j, K))
        #     if j < m: res = max(res, fn(i, j+1, K))
        #     if K and i < n and j < m: res = max(res, fn(i+1, j+1, K-1) + nums1[i]*nums2[j])
        #     return res
        # fn.cache_clear()
        # return fn(0, 0, k)