class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Collect all candidate k values (divisors > 1)
        ks = set([2])  # always include k = 2
        for x in nums:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    ks.add(d)
                    if x // d > 1:
                        ks.add(x // d)
                d += 1
            if x > 1:
                ks.add(x)

        best_diff = -10**30
        best_k = None

        # Kadane's algorithm for each k
        for k in ks:
            cur = 0
            best = -10**30
            for v in nums:
                val = v if v % k == 0 else -v
                cur = max(val, cur + val)
                best = max(best, cur)

            # Update best score difference
            if best > best_diff or (best == best_diff and (best_k is None or k < best_k)):
                best_diff = best
                best_k = k

        return (best_diff * best_k) % MOD