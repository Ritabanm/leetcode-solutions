class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        m = n - 2
        #Precompute small binomial table mod5
        C5 = [[0]*5 for _ in range(5)]
        for a in range(5):
            C5[a][0] = 1
            for b in range(1, a+1):
                #Pascal mod5
                C5[a][b] = (C5[a-1][b-1] + C5[a-1][b]) % 5
    
        #Compute C(m, k) mod2 using bitwise test
        def nCkmod2(m: int, k: int) -> int:
            # odd iff (k & (m-k)) == 0
            return 1 if (k & (m - k)) == 0 else 0
    
        #Compute C(m, k) mod5 with Lucas's theorem
        def nCkmod5(m: int, k: int) -> int:
            res = 1
            while m > 0 or k > 0:
                mdigit = m % 5
                kdigit = k % 5
                if kdigit > mdigit:
                    return 0
                res = (res * C5[mdigit][kdigit]) % 5
                m //= 5
                k //= 5
            return res
    
        #Acc mod2 & mod5
        acc2 = 0
        acc5 = 0
    
        #Digits as ints
        digits = [ord(ch) - 48 for ch in s]
    
        for i in range(m + 1):
            #Differences mod2 and mod5
            d2 = (digits[i] - digits[i+1]) & 1
            d5 = (digits[i] - digits[i+1]) % 5
    
            #mod2 contribution
            if nCkmod2(m, i):
                acc2 ^= d2
    
            #mod5 contribution
            c5 = nCkmod5(m, i)
            acc5 = (acc5 + c5 * d5) % 5
    
        #Both must be zero
        return acc2 == 0 and acc5 == 0