class Solution:
    def xorAfterQueries(self, A: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        N = len(A)
        MAGIC = isqrt(N) + 1
        events = defaultdict(lambda: [1] * N)

        for l, r, k, v in queries:
            if k <= MAGIC:
                events[k][l] = events[k][l] * v % MOD
                r2 = r + ((l - r) % k or k)
                if r2 < N:
                    events[k][r2] = events[k][r2] * pow(v, MOD - 2, MOD) % MOD
            else:
                for i in range(l, r + 1, k):
                    A[i] = A[i] * v % MOD

        for k, row in events.items():
            for i in range(k):
                cur = 1
                for j in range(i, N, k):
                    cur = cur * row[j] % MOD
                    A[j] = A[j] * cur % MOD

        ans = 0
        for x in A:
            ans ^= x
        return ans