class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        
        def getdist(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        total = 0
        for nut in nuts:            
            total += getdist(tree, nut) * 2

        ans = float('inf')        
        for nut in nuts:
            squirrel_dist = getdist(nut, squirrel)
            nut_dist = getdist(nut, tree)

            ans = min(ans, total - nut_dist + squirrel_dist)

        return ans