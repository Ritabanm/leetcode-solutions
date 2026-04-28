class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = 0
        p1, p2 = -1, -1
        for s, e in intervals:
            if s > p2:
                res += 2
                p1, p2 = e - 1, e
            elif s > p1:
                res += 1
                p1, p2 = p2, e
        return res