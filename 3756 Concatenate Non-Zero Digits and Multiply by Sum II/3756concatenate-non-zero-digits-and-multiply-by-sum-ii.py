class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefix arrays
        pref_sum = [0] * (n + 1)   # sum of non-zero digits
        pref_cnt = [0] * (n + 1)   # count of non-zero digits
        pref_hash = [0] * (n + 1)  # x value modulo MOD
        pow10 = [1] * (n + 1)      # powers of 10

        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')

            pref_sum[i + 1] = pref_sum[i]
            pref_cnt[i + 1] = pref_cnt[i]
            pref_hash[i + 1] = pref_hash[i]

            if d != 0:
                pref_sum[i + 1] += d
                pref_cnt[i + 1] += 1
                pref_hash[i + 1] = (pref_hash[i] * 10 + d) % MOD

        # simple helper function (same style as yours)
        def calc(L, R):
            cnt = pref_cnt[R + 1] - pref_cnt[L]
            if cnt == 0:
                return 0

            sm = pref_sum[R + 1] - pref_sum[L]

            left = pref_hash[L]
            total = pref_hash[R + 1]

            x = (total - left * pow10[cnt] % MOD + MOD) % MOD
            return (x * sm) % MOD

        output = []
        for L, R in queries:
            output.append(calc(L, R))

        return output