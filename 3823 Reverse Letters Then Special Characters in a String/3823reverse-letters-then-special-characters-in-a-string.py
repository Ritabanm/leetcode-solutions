class Solution:
    def reverseByType(self, s: str) -> str:
        l,sc="",""
        for i in range(len(s)):
            if s[i].isalpha(): l=s[i]+l
            else: sc=s[i]+sc
        x=y=0
        ans=""
        for i in range(len(s)):
            if s[i].isalpha():
                ans+=l[x]
                x+=1
            else:
                ans+=sc[y]
                y+=1
        return ans