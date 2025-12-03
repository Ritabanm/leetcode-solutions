dp = [0] * 801
for i in range(2, 801):
    count = 1
    num = i
    while num != 1 and count <= 5:
        num = bin(num).count("1")
        count += 1
    dp[i] = count if count <= 5 else float("inf")
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        N = len(s)
        MOD = 10**9 + 7
        @cache
        def go(i,tight,cnt,leading):
            if i == N:    
                if tight or cnt==0:
                    return 0
                return 1 if (leading and cnt==1) or dp[cnt] <= k else 0
            max_digit = int(s[i]) if tight else 1
            ans = 0
            for j in range(max_digit + 1):
                ans += go(i + 1,tight and (j == max_digit),cnt + (j == 1),leading and (j == 0))
            return ans%MOD
        r =  go(0, True, 0, True)
        go.cache_clear()
        return r