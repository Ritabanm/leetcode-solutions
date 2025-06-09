class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        width = 0
        for i in range(n-1):
            width = max(points[i+1][0]-points[i][0], width)
        return width