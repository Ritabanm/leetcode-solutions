import math

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        e = [(x & -x).bit_length() - 1 for x in nums]
        a = [nums[i] >> e[i] for i in range(n)]
        b0 = 0
        b1 = 0
        for i in range(n):
            g = 0
            em = 10**9
            cm = 0
            for j in range(i, n):
                g = math.gcd(g, a[j])
                ej = e[j]
                if ej < em:
                    em = ej
                    cm = 1
                elif ej == em:
                    cm += 1
                L = j - i + 1
                s = L * g * (1 << em)
                if s > b0:
                    b0 = s
                if cm <= k and s > b1:
                    b1 = s
        return max(b0, 2 * b1)