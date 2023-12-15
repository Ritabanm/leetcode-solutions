class Solution:
    def nthSmallest(self, n: int, k: int) -> int:

        ans = 0
        m = bisect_left(range(n + k), True, 
                               key = lambda x: comb(x, k) > n)
        while m >= 0 and k > 0:
            mCk = comb(m, k)
            m-= 1
            if n - mCk <= 0: continue
            ans+= 1 << (m + 1)
            n -= mCk
            k -= 1
    
        return ans