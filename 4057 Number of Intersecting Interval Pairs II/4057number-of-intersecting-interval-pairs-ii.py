class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        begs = [x for x, _ in intervals]
        ans = - n*(n+1)//2
        for _, end in intervals:
            ans+= bisect_right(begs, end)
        return ans