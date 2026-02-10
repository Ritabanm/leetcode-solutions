class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        rods = [[] for _ in range(10)]
        for i in range(0,n,2):
            col, idx = rings[i], int(rings[i + 1])
            if col not in rods[idx]:
                rods[idx].append(col)
                rods[idx].sort()
        return rods.count(['B', 'G', 'R'])