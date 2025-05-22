cac = {}

class Solution:
    def maxSizedArray(self, s: int) -> int:
        l, r = 1, 1196

        while l < r:
            mid = (l + r + 1) // 2

            if mid not in cac:
                # count set bits
                ct = Counter()
                for j in range(1, mid):
                    while j:
                        vb = j & -j
                        ct[vb] += 1
                        j -= vb
                
                # calcualte how many times bit is set in (n * n) matrix
                cac[mid] = 0
                for vb in ct:
                    cac[mid] += vb * (mid ** 2 - (mid - ct[vb]) ** 2)
                
                # the i loop, sum of indices = 0 + 1 + ... + (mid - 1)
                cac[mid] *= mid * (mid - 1) // 2
                
            if cac[mid] <= s:
                l = mid
            else:
                r = mid - 1
        
        return l