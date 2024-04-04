class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        
        MOD = 10 ** 9 + 7

        def smallest_prime_factors():
            N = max(n for _, n in queries) 
            spf = [0] * (N + 1)

            for i in range(2, N + 1):
                if spf[i] == 0:
                    spf[i] = i
                    for j in range(i * i, N + 1, i):
                        if spf[j] == 0:
                            spf[j] = i

            return spf

        spf = smallest_prime_factors()

        def prime_factorization_powers(n):
            primes_and_powers = defaultdict(int)

            while n > 1:
                primes_and_powers[spf[n]] += 1
                n //= spf[n]

            return primes_and_powers.values()

        answer = []
        for n, k in queries:
            powers = prime_factorization_powers(k)
            answer.append(1)
            for power in powers:
                answer[-1] = (answer[-1] * comb(power + n - 1, n - 1)) % MOD

        return answer

        
            