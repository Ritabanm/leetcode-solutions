class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        cache = {}
        def findways(pos, k):
            if (pos, k) in cache:
                return cache[(pos, k)]
            if k==0:
                return pos == endPos
            
            res = findways(pos+1, k-1)+findways(pos-1, k-1)
            cache[(pos, k)] = res

            return res
        return findways(startPos,k)%(10**9+7)