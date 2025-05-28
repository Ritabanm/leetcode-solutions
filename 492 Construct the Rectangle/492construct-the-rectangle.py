class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        st = {}
        mn = float('Inf')
        for h in range(1, int(area ** 0.5 + 1)) :
            if area % h == 0:
                w = area // h
                st[w - h] = (w, h)
                mn = min(mn, w - h)
        return list(st[mn])