class Solution:
    def maxProduct(self, s):
        n = len(s)

        dp, before, after = [0]*n, [0]*n, [0]*n

        c, r = -1, -1

        for i in range(n):
            k = min(dp[2*c-i],r-i) if i<=r else 0
            p, q = i-k, i+k

            while p>=0 and q<n and s[p] == s[q]:
                before[q] = max(before[q],q-p+1)
                after[p] = max(after[p],q-p+1)
                p -= 1
                q += 1

            dp[i] = q-i-1

            if q-1 > r: c, r = i, q-1

        for i in range(1,n):
            before[i] = max(before[i-1],before[i])

        for i in range(n-2,-1,-1):
            after[i] = max(after[i+1],after[i])

        return max([before[i-1]*after[i] for i in range(1,n)])



            











        
        