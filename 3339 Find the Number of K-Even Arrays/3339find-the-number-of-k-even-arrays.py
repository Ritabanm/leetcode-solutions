class Solution:
    def countOfArrays(self, n: int, m: int, k: int) -> int:
        o, e, mod = (m+1)//2, m//2, 10**9+7

        # Precompute powers and factorials
        op, ep, fac = [1], [1], [1]
        for i in range(n):
            op.append(op[-1]*o % mod)
            ep.append(ep[-1]*e % mod)
            fac.append(fac[-1]*(i+1) % mod)

        res = 0
        if k == 0:
            res += op[n]

        for x in range(1, (n+1-k)//2+1):
            res += ep[x+k] * op[n-x-k] \
                * fac[x+k-1] * pow(fac[x-1] * fac[k], mod-2, mod) \
                * fac[n-x-k+1] * pow(fac[x] * fac[n-k+1-2*x], mod-2, mod) \
                % mod
        
        return res % mod