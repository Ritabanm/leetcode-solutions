class Solution:
    def countCoprime(self, A: List[List[int]]) -> int:
        MOD = 10**9 + 7

        dp = Counter([0])
        for row in A:
            ndp = Counter()
            for g, ways in dp.items():
                for x in row:
                    ndp[gcd(g, x)] += ways
                    ndp[gcd(g, x)] %= MOD
            dp = ndp

        return dp[1]