class Solution:
    def minEatingSpeed(self, piles,h):
        l = 1
        r = max(piles)

        while l<r:
            m = (l+r)//2
            hs = 0
            for pile in piles:
                hs += math.ceil(pile/m)
            if hs<=h:
                r = m
            else:
                l = m+1
        return r