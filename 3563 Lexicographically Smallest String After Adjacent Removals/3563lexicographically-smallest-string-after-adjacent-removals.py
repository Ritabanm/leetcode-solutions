class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        N = len(s)
        @cache
        def is_removable(i,j):
            if (j - i) % 2 == 0: return False
            if i >= j: return False
            if j-i == 1:
                return abs(ord(s[i])-ord(s[j])) in (1,25)
            else:
                remv = (is_removable(i+1,j-1) and (abs(ord(s[i])-ord(s[j])) in (1,25)))
                if remv: return True
                for k in range(i+1,j,2):
                    remv = remv or ( is_removable(k+1,j) and is_removable(i,k))
                    if remv: return True
                return False
        remvtable = {}
        for i in range(N):
            remvtable[i] = set([])
            for j in range(i,N):
                if is_removable(i,j): remvtable[i].add(j)
        @cache 
        def dp(i):
            if i == N:
                return ""
            res = s[i:]
            for j in range(i+1,N):
                if j in remvtable[i]:
                    res = min(res,dp(j+1))
                res = min(res,s[i:j]+dp(j))
            return res
        return dp(0)





