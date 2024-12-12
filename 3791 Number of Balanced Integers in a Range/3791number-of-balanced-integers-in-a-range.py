class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        high = str(high)
        n = len(high)
        low = str(low).zfill(n)
        # print(low, high)
        @cache
        def recursive(i, lf, hf, sm):
            if i >= n: return 1 if sm == 0 else 0
            res = 0
            lw = 0 if not lf else int(low[i])
            hi = 9 if not hf else int(high[i])
            for j in range(lw, hi+1):
                res += recursive(i+1, lf and j==lw, hf and j==hi, sm + (j if i%2 == 1 else -j))
            return res
        return recursive(0, 1, 1, 0)