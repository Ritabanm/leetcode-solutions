class Solution:
    def maximumScore(self, A: List[int], K: int) -> int:
        N = len(A)

        def solve(A):
            dp = list(accumulate(A, max))
            for i, lo in enumerate(accumulate(A, min)):
                dp[i] -= lo
            ans = dp[N - 1]

            for layer in range(K - 1):
                ndp = [-inf] * N
                X = Y = -inf
                for j in range(1, N):
                    X = max(X, dp[j - 1] - A[j])
                    Y = max(Y, dp[j - 1] + A[j])
                    ndp[j] = max(ndp[j - 1], X + A[j], Y - A[j])
                dp = ndp
                ans = max(ans, dp[N - 1])

            return ans

        i = A.index(min(A))
        A = A[i:] + A[:i]
        B = A[1:] + A[:1]
        return max(solve(A), solve(B))