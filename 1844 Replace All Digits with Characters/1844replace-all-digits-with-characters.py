class Solution:
    def replaceDigits(self, s: str) -> str:
        m=''
        for x in range(len(s)):
            if x%2!=0:
                m+=chr(ord(s[x-1])+int(s[x]))
            else:
                m+=s[x]
        return m


        
        