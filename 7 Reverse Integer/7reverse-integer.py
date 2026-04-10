class Solution:
    def reverse(self, x: int) -> int:
        min = -2**31
        max = 2**31
        sign = -1 if x<0 else 1
        x = abs(x)
        revN = 0
        while x!=0:
            digit = x%10
            revN = revN*10 + digit
            x//=10
        revN *=sign
        if revN<min or revN>max:
            return 0
        return revN