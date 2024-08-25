class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        pre_s = [1]*n
        pre_t = [1]*m
        t = t[::-1]
        res = 1

        def precompal(st):
            ln = len(st)
            comp = [1]*ln
            dp = [[False for _ in range(ln+1)] for _ in range(ln+1)]
            for i in range(ln):
                dp[i][i] = True
            for i in range(ln-1):
                if st[i]==st[i+1]:
                    comp[i]=2
                    dp[i][i+1] = True
            for k in range(3,ln+1):
                for i in range(ln-k+1):
                    j = i+k-1
                    if st[i]==st[j] and dp[i+1][j-1] == True:
                        dp[i][j] = True
                        comp[i] = max(comp[i],j-i+1)

            return comp
        pre_s = precompal(s)
        pre_t = precompal(t)
        res = max(max(pre_s),max(pre_t))

        dp = [[0 for _ in range(m+1)] for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i-1][j-1])
                    e_s,e_t = '',''
                    p_s,p_t = 0,0
                    if i<n:
                        p_s = pre_s[i]
                        e_s = s[i:i+p_s]
                    if j<m:
                        p_t = pre_t[j]
                        e_t = t[j:j+p_t]
                    if p_s == p_t and p_s>0 and p_t>0:
                        if e_s==e_t:
                          res = max(res, 2*dp[i][j]+p_s+p_t)
                        else:
                          res = max(res, 2*dp[i][j]+max(p_s,p_t))
                    else:
                        res = max(res,2*dp[i][j]+max(p_s,p_t))
        return res




    
        

        


        
          



        




        