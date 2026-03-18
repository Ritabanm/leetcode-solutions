class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        o = t.count('1')
        z = t.count('0')
        ans = ""
        for i in s:
            if i=='0':
                if o>0:
                    ans+='1'
                    o-=1
                else:
                    ans+='0'
                    z-=1
            if i=='1':
                if z>0:
                    ans+='1'
                    z-=1
                else:
                    ans+='0'
                    o-=1
        return ans