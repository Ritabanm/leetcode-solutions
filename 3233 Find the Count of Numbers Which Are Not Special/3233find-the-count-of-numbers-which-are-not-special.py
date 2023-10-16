class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def cnt_prime_numbers(s: int, e: int) -> int:
            prime_numbers = 0
            primes = [0 if i % 2 == 0 else 1 for i in range(e + 2)]
            primes[1], primes[2] = 0, 1
            i = 3
            while i * i <= e:
                if primes[i] == 1:
                    j = i * i
                    while j <= e:
                        primes[j] = 0
                        j += 2 * i
                i += 2
            i = s
            for i in range(s, e + 1):
                if primes[i] == 1: prime_numbers += 1
            return prime_numbers
        
        prime_numbers = cnt_prime_numbers(int(math.ceil(math.sqrt(l))), int(math.sqrt(r)))
        return r - l + 1 - prime_numbers
            