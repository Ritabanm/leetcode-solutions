class Solution:
    def minXor(self, A, K):
        N = len(A)
        P = list(accumulate(A, operator.xor, initial=0))

        @cache
        def dp(i, k):
            if k == 1:
                return P[i]
            ans = inf
            for j in range(k - 1, i):
                ans = min(ans, max(dp(j, k - 1), P[i] ^ P[j]))
            return ans

        return dp(N, K)