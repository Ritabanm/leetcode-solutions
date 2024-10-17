class Solution:
    def simpleGraphExists(self, deg: List[int]) -> bool:
        if sum(deg) & 1:
            return False
        n = len(deg)
        deg.sort()
        pf = list(accumulate(deg)) + [0]

        for k in range(1, n + 1):
            le = pf[n - 1] - pf[n - k - 1]
            #
            ri = k * (k - 1)
            x = bisect_right(deg, k + 1)
            if not x: # k is smaller than all degs, min(di, k) = k
                ri += k * (n - k)
            elif x >= n - k: # k is greater than smallest n - k degs, min(di, k) = di
                ri += pf[n - k - 1]
            else: # left to x, min(di, k) = di; right to x, min(di, k) = k
                ri += pf[x - 1] + (n - k - x) * k
            # 
            if le > ri:
                return False
        return True