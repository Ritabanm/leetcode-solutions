class Solution:
    def longestPrefix(self, s: str) -> str:
        b = len(s)
        t = 0
        p = ""
        for i in range(len(s)-1):
            if s[:i+1]==s[b-1-i:]:
                if i+1>t:
                    p = s[:i+1]
                    t= i+1              
        return p


        