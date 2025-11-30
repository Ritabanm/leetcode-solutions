# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        m = 2**30-1

        limit = commonSetBits(m)

        l, r = 0, m

        while l < r:
            mid = l + (r-l)//2
            midC = commonSetBits(mid)
            if midC < limit:
                l = mid+1
            else:
                r = mid

        return l