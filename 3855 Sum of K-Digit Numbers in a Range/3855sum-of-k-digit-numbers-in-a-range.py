class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        MOD = 10**9 + 7
        ed = pow(r - l + 1, k - 1, MOD) * (l + r) * (r - l + 1) // 2
        mlt = (pow(10, k, MOD) - 1) * pow(9, MOD - 2, MOD) % MOD
        return ed * mlt % MOD