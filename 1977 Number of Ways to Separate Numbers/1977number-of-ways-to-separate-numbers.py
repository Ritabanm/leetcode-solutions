class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        dp = [[0 for i in range(n)] for j in range(n)]
        for s in range(n - 1, -1, -1):
            for i in range(s + 1, n):
                dp[s][i] = dp[s][i - 1]
                pLen = i - s
                if(num[i] == '0' or i + pLen > n):           
                    continue
                if(num[s : i] <= num[i : i + pLen]):   
                    dp[s][i] += 1 if i + pLen == n else dp[i][i + pLen] - dp[i][i + pLen - 1]
                if(i + pLen < n):
                    dp[s][i] += 1
                    dp[s][i] += dp[i][n - 1] -  dp[i][i + pLen]
        return (dp[0][-1] + 1) % (10 ** 9 + 7) if num[0] != '0' else 0
                

                