class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2
            
        def cnt_full(l):
            # number of pal-nums with length l
            if l == 1:
                return 2
            hf_n = 1 << (l//2 - 1)
            if l % 2 == 1:
                return hf_n * 2
            return hf_n
            
        def cnt_sm(hf):
            # number of pal-nums whose left half is strictly smaller than `hf`
            if len(hf) == 1:
                return 0
            return int(hf[1:], 2)
        def check_eq(hf, bn, mid):
            # check if hf + mid + hf[::-1] is valid
            full = hf + mid + hf[::-1]
            return int(full, 2) <= n
        bn = bin(n)[2:]
        bnl = len(bn)
        res = 0
        for l in range(1, bnl):
            res += cnt_full(l)

        bn_hf = bn[:(bnl//2)]
        if bnl % 2 == 0:
            res += cnt_sm(bn_hf) + check_eq(bn_hf, bn, '')
        if bnl % 2 == 1:
            res += cnt_sm(bn_hf)*2 + check_eq(bn_hf, bn, '0') + check_eq(bn_hf, bn, '1')
        return res
            