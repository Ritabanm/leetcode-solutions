class Solution:
    def countPathsWithXorValue(self, A: List[List[int]], k: int) -> int:
        @cache
        def dp(i, j):
            if i < 0 or j < 0:
                return Counter()
            if (i, j) == (0, 0):
                return Counter({A[0][0]: 1})
            pre = dp(i - 1, j) + dp(i, j - 1)
            return Counter({v ^ A[i][j]: pre[v] % mod for v in pre})

        mod = 10 ** 9 + 7
        res = dp(len(A) - 1, len(A[0]) - 1)
        return res[k] % mod