class Solution:
    def interleaveCharacters(self, a: str, b: str, target: str) -> int:
        MOD = 1_000_000_007
        n, n2, m = len(a), len(b), len(target)

        def new_table():
            return [[[[0, 0], [0, 0]] for _ in range(n2 + 1)] for _ in range(n + 1)]

        dp = new_table()
        dp[0][0][0][0] = 1

        for i in range(1, m + 1):
            dpnxt = new_table()
            x = target[i - 1]

            for prevb in range(n2 + 1):
                for t in range(2):
                    pref0 = [0] * (n + 1)
                    pref1 = [0] * (n + 1)
                    pref0[0] = dp[0][prevb][0][t]
                    pref1[0] = dp[0][prevb][1][t]
                    for preva in range(1, n + 1):
                        pref0[preva] = (pref0[preva - 1] + dp[preva][prevb][0][t]) % MOD
                        pref1[preva] = (pref1[preva - 1] + dp[preva][prevb][1][t]) % MOD
                    for preva in range(1, n + 1):
                        if a[preva - 1] != x:
                            continue
                        dpnxt[preva][prevb][1][t] = (
                            dpnxt[preva][prevb][1][t] + pref0[preva - 1] + pref1[preva - 1]) % MOD

            for preva in range(n + 1):
                for k in range(2):
                    pref0 = [0] * (n2 + 1)
                    pref1 = [0] * (n2 + 1)
                    pref0[0] = dp[preva][0][k][0]
                    pref1[0] = dp[preva][0][k][1]
                    for prevb in range(1, n2 + 1):
                        pref0[prevb] = (pref0[prevb - 1] + dp[preva][prevb][k][0]) % MOD
                        pref1[prevb] = (pref1[prevb - 1] + dp[preva][prevb][k][1]) % MOD
                    for prevb in range(1, n2 + 1):
                        if b[prevb - 1] != x:
                            continue
                        dpnxt[preva][prevb][k][1] = (
                            dpnxt[preva][prevb][k][1] + pref0[prevb - 1] + pref1[prevb - 1]) % MOD

            dp = dpnxt

        ans = 0
        for preva in range(n + 1):
            for prevb in range(n2 + 1):
                ans = (ans + dp[preva][prevb][1][1]) % MOD
        return ans