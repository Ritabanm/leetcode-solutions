class Solution:
    def numberOfSubstrings(self,s):
        ctr = Counter(); res = 0
        for c in s:
            ctr[c]+=1
            res+=ctr[c]
        return res