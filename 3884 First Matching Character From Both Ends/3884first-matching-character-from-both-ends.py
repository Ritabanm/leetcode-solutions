class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        m = len(s)
        for i in range(0,m):
            if s[i]==s[m-i-1]:
                return i
            elif m==1:
                return 0
            else:
                i+=1
        return -1