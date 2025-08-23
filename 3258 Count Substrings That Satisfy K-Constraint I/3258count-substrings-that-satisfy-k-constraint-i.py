class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = one = ii = 0
        for i, ch in enumerate(s):
            if ch == '1': 
                one+=1
            while one>k and i-ii-one+1>k:
                if s[ii] == '1': one-=1
                ii +=1
            ans += i-ii+1
        return ans