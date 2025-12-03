class Solution:
    def numOfSubsequences(self, s: str) -> int:
        l, c, t = 0, 0, 0
        lc, ct, lt = 0, 0, 0
        t_total = s.count("T")
        lct = 0

        for ch in s:
            if ch == "L":
               l += 1
            elif ch == "C":
                c += 1
                lc += l
            elif ch == "T":
                t += 1
                ct += c
                lct += lc
            
            lt = max(lt, l*(t_total-t))
            
        return lct + max([lc, ct, lt])