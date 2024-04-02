class Solution:
    def getSmallestString(self, s: str) -> str:

        s = list(s)
 
        for i, j in pairwise(range(len(s))):

            if s[i] > s[j] and (ord(s[i])-ord(s[j]))%2 == 0 :
                s[i], s[j] = s[j], s[i]
 
                break

        return ''.join(s)