class Solution:
    def numberOfWays(self, n: int, res = 0) -> int:

        for four, six in product((0, 4, 8), range(0, n+1, 6)):

            pref = four + six
            if pref > n: continue
            res+= (n - pref)//2+1

        return res %1_000_000_007 