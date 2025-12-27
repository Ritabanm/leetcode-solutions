class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        ans = 0
        prev = -inf 
        for x, _ in sorted(points): 
            if prev + w < x: 
                ans += 1
                prev = x 
        return ans 