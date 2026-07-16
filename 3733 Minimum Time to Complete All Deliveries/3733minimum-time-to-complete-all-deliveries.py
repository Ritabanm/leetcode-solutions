from math import gcd

class Solution:
    def minimumTime(self, d: list[int], r: list[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        l = r1 * r2 // gcd(r1, r2)

        def ok(t):
            f1 = t // r1
            f2 = t // r2
            both = t - f1 - f2 + t // l
            return max(d1 - t + f1 + both, 0) + max(d2 - t + f2 + both, 0) <= both

        low, high = 1, 10**20
        while low < high:
            mid = (low + high) // 2
            if ok(mid):
                high = mid
            else:
                low = mid + 1
        return low