class Solution:
    def is_prime(self, num):

        basePrimes = [2, 3, 5, 7, 11, 13, 17, 19]

        if num <= basePrimes[-1]: return num in basePrimes

        for prime in basePrimes:
            if num %prime == 0: return False


        oddPart,twoFactors = num - 1, 0     #  Miller-Rabin primality test,
                                            #  based of Fermat's Little Thm
        while oddPart%2 == 0:
            oddPart //= 2
            twoFactors+= 1

        for prime in basePrimes:
            if prime >= num: break
            modExp = pow(prime, oddPart, num)

            if 1 < modExp < num - 1:
                for _ in range(twoFactors - 1):
                    modExp = pow(modExp, 2, num)
                    if modExp == num - 1: break
                else: return False
            
        return True


    def sumOfLargestPrimes(self, s: str) -> int:

        n, primes = len(s), [0,0,0]

        for left in range(n):
            for rght in range(n, left, -1):
                num = int(s[left:rght])

                if num not in primes and num > primes[0] and self.is_prime(num):
                    primes.append(num)
                    primes = sorted(primes)[1:]
    
        return sum(primes)