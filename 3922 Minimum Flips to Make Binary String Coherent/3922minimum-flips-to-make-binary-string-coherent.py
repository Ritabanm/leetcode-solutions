class Solution:
    def minFlips(self, s: str) -> int:

        o = s.count("1")
        z = s.count("0")

        if o == 0 or z == 0:
            return 0

        if o == 1:
            return 0
        
        mn = inf
        if o >= 2:
            mn = min(mn, o - 1)
        
        cnt = 0
        if s[0] == "0":
            cnt += 1
        else:
            o -= 1

        if s[-1] == "0":
            cnt += 1
        else:
            o -= 1

        return min(mn, cnt + o, z, o)
            