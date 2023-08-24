class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        
        # Handle small cases directly
        if primeFactors <= 3:
            return primeFactors
        
        # Calculate the maximum number of nice divisors
        if primeFactors % 3 == 0:
            return pow(3, primeFactors // 3, MOD)
        elif primeFactors % 3 == 1:
            # If remainder is 1, use one less group of 3 and add 4
            return (pow(3, (primeFactors // 3) - 1, MOD) * 4) % MOD
        else:  # primeFactors % 3 == 2
            # If remainder is 2, use one extra factor of 2
            return (pow(3, primeFactors // 3, MOD) * 2) % MOD
