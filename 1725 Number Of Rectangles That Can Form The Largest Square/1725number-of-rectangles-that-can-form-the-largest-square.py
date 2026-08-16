class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        m = []
        for i in rectangles:
            m.append(min(i))
        res = m.count(max(m))
        return res