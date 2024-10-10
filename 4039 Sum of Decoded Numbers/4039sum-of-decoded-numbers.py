class Solution:
    def sumDecoded(self, nums: list[int]) -> int:

        MOD, ans = 1_000_000_007, 0

        for num in nums:
            d, width = divmod(num, 10)
            exp = len(str(d)) - width
            x, y = divmod(d, 10 ** exp)
            ans+= pow(x, y, MOD)
       
        return ans % MOD