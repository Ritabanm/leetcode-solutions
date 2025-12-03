class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n, self.X, self.Y = len(circles), X, Y
        uf = UnionFind(n+2)

        for i in range(n):
            x1, y1, r1 = circles[i]
            if x1**2 + y1**2 <= r1**2 or (x1-X)**2 + (y1-Y)**2 <= r1**2:
                # (0,0) or (X,Y) in the circle
                return False
            if x1 >= X and y1 >= Y or x1 >= X+r1 or y1 >= Y+r1:
                # completely off the rectangle
                continue
            if x1**2 + (y1-Y)**2 <= r1**2 or x1 <= r1 and 0 <= y1 <= Y or abs(y1-Y) <= r1 and 0 <= x1 <= X:
                # union with the top&left edges
                uf.union(i, n)
            if (x1-X)**2 + y1**2 <= r1**2 or y1 <= r1 and 0 <= x1 <= X or abs(x1-X) <= r1 and 0 <= y1 <= Y:
                # union with the bottom&right edges
                uf.union(i, n+1)
            for j in range(i+1, n):
                if self.checkCross(circles[i], circles[j]):
                    # intersect in the rectangle
                    uf.union(i, j)

        return uf.find(n) != uf.find(n+1)

    def checkCross(self, circle1: List[int], circle2: List[int]) -> bool:
        (x1, y1, r1), (x2, y2, r2) = circle1, circle2

        # squared distance betwen the two centres
        r = (x1-x2)**2 + (y1-y2)**2
        if r <= (r1-r2)**2 or r > (r1+r2)**2:
            # not connected or one inside the other
            return False

        rr = (r1**2-r2**2)/(2*r)
        delta = (r1**2+r2**2)/(2*r) - rr**2 - 0.25
        if delta < 1e-9:
            # two circles in touch
            delta = 0
        dr = sqrt(delta)

        # coordinates of the intersection points
        cx1, cy1 = (x1+x2)/2 + rr * (x2-x1) + dr * (y2-y1), (y1+y2)/2 + rr * (y2-y1) + dr * (x1-x2)
        cx2, cy2 = (x1+x2)/2 + rr * (x2-x1) - dr * (y2-y1), (y1+y2)/2 + rr * (y2-y1) - dr * (x1-x2)
        
        # check if any of the intersection points in the rectangle
        return (0 <= cx1 <= self.X) and (0 <= cy1 <= self.Y) or (0 <= cx2 <= self.X) and (0 <= cy2 <= self.Y)


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1: int, node2: int):
        r1, r2 = self.find(node1), self.find(node2)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.parent[r1] = r2
            else:
                self.parent[r2] = r1
                if self.rank[r1] == self.rank[r2]:
                    self.rank[r1] += 1