class Solution:
    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:
        @cache
        def dp(eqr, eqc, rem):
            if rem > 1:                
                rem -= 1
                if eqr:
                    move_r = (n - 1) * dp(False, eqc, rem) % MOD
                else:
                    move_r = (dp(True, eqc, rem) + (n - 2) * dp(False, eqc, rem)) % MOD
                if eqc:
                    move_c = (m - 1) * dp(eqr, False, rem) % MOD
                else:
                    move_c = (dp(eqr, True, rem) + (m - 2) * dp(eqr, False, rem)) % MOD
                return (move_r + move_c) % MOD
            else:
                return 1 if (eqr and not eqc) or (not eqr and eqc) else 0

        MOD = 1_000_000_007
        return dp(source[0] == dest[0], source[1] == dest[1], k)