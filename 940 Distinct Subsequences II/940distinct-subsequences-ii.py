class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9+7
        tot = 0
        dp = [0]*26
        for char in s:
            c = ord(char)-ord('a')
            new_subsequences = (tot + 1 - dp[c])%mod
            tot = (tot+new_subsequences)%mod
            dp[c]=(dp[c] + new_subsequences)%mod
        return tot