class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp, has_0, mod = [0, 0], 0, 10**9+7
        for char in binary:
            if char == '0':
                has_0 = 1
                new_val = sum(dp)
                dp[0] = new_val
            else:
                new_val = sum(dp) + 1
                dp[1] = new_val
        return (sum(dp) + has_0) % mod     