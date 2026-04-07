# Sieve of Eratosthenes

class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        if n == 1:
            return -1
        if m == 1 and n % 2 == 1:
            return -1
        
        def sieve(max_value):
            is_primes = [True] * (max_value + 1)
            is_primes[0] = is_primes[1] = False

            for p in range(4, max_value + 1, 2):
                is_primes[p] = False
            yield 2

            for p in range(3, max_value + 1, 2):
                if is_primes[p]:
                    yield p
                    for other in range(p ** 2, max_value + 1, 2 * p):
                        is_primes[other] = False
        
        prime_numbers = []
        for i, prime in enumerate(sieve(n), 1):
            prime_numbers.append(prime)
            if i == m:
                break
        unique_prime_numbers = set(prime_numbers)

        @cache
        def dp(value):
            if value in unique_prime_numbers:
                return 1
            result = float('inf')
            for prime in prime_numbers:
                if 2 * prime > value:
                    break
                result = min(result, 1 + dp(value - prime))
                if result == 2:
                    return 2
            return result
        
        result = dp(n)
        if result == float('inf'):
            return -1
        return result