from math import isqrt

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        a = ord('a')
        prefix = [[0]*26 for _ in range(n+1)]
        for i, ch in enumerate(s, 1):
            row = prefix[i-1][:]
            row[ord(ch)-a] += 1
            prefix[i] = row
        ds = []
        for d in range(1, int(math.isqrt(n))+1):
            if n % d == 0:
                ds.append(d)
                if d != n // d:
                    ds.append(n // d)
        ds.sort()
        for m in ds:
            base = [prefix[m][k] for k in range(26)]
            ok = True
            for i in range(m, n, m):
                if any(prefix[i+m][k] - prefix[i][k] != base[k] for k in range(26)):
                    ok = False
                    break
            if ok:
                return m
        return n