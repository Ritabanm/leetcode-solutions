class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        res = [ranges[0]]
        
        for s1, e1 in ranges[1 : ]:
            s2, e2 = res[-1]
            
            if max(s1, s2) <= min(e1, e2):
                res[-1] = [min(s1, s2), max(e1, e2)]
            else:
                res.append([s1, e1])
        
        return pow(2, len(res), pow(10, 9) + 7)