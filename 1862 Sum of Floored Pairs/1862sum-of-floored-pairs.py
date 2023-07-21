
class Solution:
    def sumOfFlooredPairs(self, n: List[int]) -> int:
        f, m, c = Counter(n), max(n), [0]*(max(n)+1)
        for k in f:
            d, r = f[k], 1
            while r*k <= m: c[r*k] += d; r += 1
        r, j = 0, 0
        for i in range(m+1):
            r += c[i]
            if i in f: j += f[i]*r
        return j%(10**9+7)
		