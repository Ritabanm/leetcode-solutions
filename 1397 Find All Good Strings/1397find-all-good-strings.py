class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        m = len(evil)
        kmp = [0]*m
        j = 0
        for i in range(1,m):
            while j and evil[i]!=evil[j]:
                j = kmp[j-1]
            if evil[i] == evil[j]:
                j += 1
            kmp[i] = j

        @cache
        def dp(i,j,tight1,tight2):
            if j == m:return 0
            if i == n:
                return 1
            a1 = ord('a')
            a2 = ord('z')
            if tight1:
                a1 = ord(s1[i])
            if tight2:
                a2 = ord(s2[i])
            res = 0
            for k in range(a1,a2+1):
                newl = chr(k)
                nevil = 0
                nt1 = False
                nt2 = False
                nj = j
                while nj and evil[nj]!=newl:
                    nj = kmp[nj-1]
                if newl == evil[nj]:
                    nj += 1
                if k == a1:
                    nt1 = True
                if k == a2:
                    nt2 = True
                if j+nevil<m:
                    res += dp(i+1,nj,tight1 and nt1,tight2 and nt2)
            return res % (10**9+7)
        return dp(0,0,True,True) % (10**9+7)
                
        