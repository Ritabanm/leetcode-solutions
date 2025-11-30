class Solution:
    def stringCount(self, n):
        mod = 10**9+7 

        if n < 4:
            return 0 

        total = pow(26,n,mod)

        res = (pow(25,n,mod))%mod 

        res += (pow(25,n,mod) + n*pow(25,n-1,mod))%mod 

        res += (pow(25,n,mod))%mod 

        res -= (pow(24,n,mod))%mod 

        res -= (pow(24,n,mod) + n*pow(24,n-1,mod))%mod

        res -= (pow(24,n,mod) + n*pow(24,n-1,mod))%mod

        res += (pow(23,n,mod) + n*pow(23,n-1,mod))%mod

        return (total-res)%mod 