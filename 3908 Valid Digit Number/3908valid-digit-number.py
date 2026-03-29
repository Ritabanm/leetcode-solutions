class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s,x = str(n), str(x)
        if s[0]==x:
            return False
        
        for ch in s:
            if ch==x:
                return True
        return False