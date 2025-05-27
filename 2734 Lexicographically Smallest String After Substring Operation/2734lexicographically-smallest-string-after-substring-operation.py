class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        i = 0
        while s[i]=='a' and i<n:
            i+=1
            if i==n:
                return s[:len(s)-1]+'z'
        start = i
        while i<n:
            if s[i]!='a':
                i+=1
            else:
                break
        end = i
        xx = [*str(s)]
        for i in range(start, end):
            xx[i]= chr(ord(xx[i])-1)
        return "".join(xx)