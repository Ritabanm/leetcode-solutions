class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 10**9 + 7

        def count(x: int) -> int:
            total = 0
            for v, d in zip(value, decay):
                if v >= x:
                    total += (v - x) // d + 1
            return total

        def cSum(x: int) -> int:
            total = 0
            for v, d in zip(value, decay):
                if v >= x:
                    c = (v - x) // d + 1
                    total += c * (2 * v - (c - 1) * d) // 2
            return total

        pos = count(1)

        if pos <= m:
            return cSum(1) % MOD

        first, last = 1, max(value)

        while first < last:
            mid = (first + last + 1) // 2
            if count(mid) >= m:
                first = mid
            else:
                last = mid - 1

        f = first
        cnt = count(f + 1)
        sm = cSum(f + 1)

        rem = m - cnt
        ans = sm + rem * f

        return ans % MOD