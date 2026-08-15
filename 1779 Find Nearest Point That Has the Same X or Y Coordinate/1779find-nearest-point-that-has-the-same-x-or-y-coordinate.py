class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = float('inf')
        count = -1
        for i , p in enumerate(points):
            if p[0]==x or p[1]==y:
                man_dist = abs(p[0]-x)+abs(p[1]-y)
                if man_dist < dist:
                    count = i
                    dist = man_dist
        return count