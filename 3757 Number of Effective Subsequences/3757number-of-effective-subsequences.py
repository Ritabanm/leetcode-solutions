mod = 10**9 + 7
# Precompute powers of 2
pw = list(accumulate(range(10**5), func=lambda a, _: (a << 1) % mod, initial=1))
# Precompute bit counts (population count)
ppc = list(map(int.bit_count, range(1 << 20)))

class Solution:
    def countEffective(self, l: List[int]) -> int:
        m = reduce(or_, l)      # Calculate Total OR
        bl = m.bit_length()     # Determine bit length
        bit = 1 << bl
        n = len(l)
        
        # Initialize frequency array
        cnt = [0] * bit
        for v in l: cnt[v] += 1
            
        # SOS DP: Propagate counts
        for k in range(bl):
            b = bb = 1 << k
            # Iterate only masks where k-th bit is 1 (Trick 1)
            while b < bit:
                cnt[b] += cnt[b ^ bb]
                b = (b + 1) | bb

        ans = 0
        sub = m
        # PIE: Iterate over submasks (Trick 2)
        while True:
            # If missing bits (ppc[m^sub]) is odd, subtract; else add.
            term = pw[cnt[sub]]
            if ppc[m ^ sub] & 1:
                ans -= term
            else:
                ans += term
                
            if sub == 0: break
            sub = (sub - 1) & m
            
        # Ans now holds the count of subsets with OR == Total OR
        # Result = Total subsets (2^n) - Ineffective subsets
        return (pw[n] - ans) % mod