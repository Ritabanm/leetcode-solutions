class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        sq = sorted([y, l] for x,y,l in squares)
        def areaUnder(y):
            area = 0
            for s in sq:
                if s[0]+s[1]<=y:
                    area += (s[1]**2)
                elif s[0]<y<(s[0]+s[1]):
                    h = y-s[0]
                    area += (s[1]*h)
                else:
                    break
            return area
        
        half = sum(l**2 for _,l in sq)/2
        l = 0
        r = max(y+l for y, l in sq)
        while r-l>1e-6:
            mid = (l+r)/2
            area_under = areaUnder(mid)
            if area_under<half:
                l = mid
            else:
                r = mid
        return l