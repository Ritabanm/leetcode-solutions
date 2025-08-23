class Solution:
    def maximizeXorAndXor(self, nums: list[int]) -> int:
        def best(s, m):
            b = [0] * nbBits
            while s:
                t = s & -s
                i = (t.bit_length() - 1)
                x = nums[i] & m
                while x:
                    k = x.bit_length() - 1
                    if b[k]:
                        x ^= b[k]
                    else:
                        b[k] = x
                        break
                s ^= t
            res = 0
            for k in range(nbBits - 1, -1, -1):
                if b[k] and (res ^ b[k]) > res:
                    res ^= b[k]
            return res 
         
            
        n = len(nums)
        XORtot = 0
        for v in nums:
            XORtot ^= v
        nbBits = max(XORtot, max(nums, default=0)).bit_length() or 1
        bitmask = (1 << nbBits) - 1
        N = 1 << n

        xr, ad = [0] * N, [0] * N
        ad[0] = bitmask
        for m in range(1, N):
            b = m & -m
            i = (b.bit_length() - 1)
            pm = m ^ b
            xr[m] = xr[pm] ^ nums[i]
            ad[m] = ad[pm] & nums[i]

        ans = 0
        for mB in range(N):
            andB = 0 if mB == 0 else ad[mB]
            XORAC = XORtot ^ xr[mB]
            M = bitmask ^ XORAC
            complB = (N - 1) ^ mB
            ans = max(ans, andB + XORAC + 2 * best(complB, M)) 
        return ans