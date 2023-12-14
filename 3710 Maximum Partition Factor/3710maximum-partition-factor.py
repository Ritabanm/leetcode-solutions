class Solution:
    def maxPartitionFactor(self, A: List[List[int]]) -> int:
        N = len(A)
        B = []
        for i, j in combinations(range(N), 2):
            px, py = A[i]
            qx, qy = A[j]
            d = abs(px - qx) + abs(py - qy)
            B.append([d, i, j])

        B.sort()
        dsu = DSUParity(N)
        for d, i, j in B:
            if not dsu.link(i, j):
                return d
        return 0

class DSUParity:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N
        self.x = [0] * N

    def find(self, a):
        if self.par[a] != a:
            r = self.find(self.par[a])
            self.x[a] ^= self.x[self.par[a]]
            self.par[a] = r
        return self.par[a]

    def link(self, a, b, w=1):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return (self.x[a] ^ self.x[b]) == w
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
            a, b = b, a
        self.par[rb] = ra
        self.x[rb] = self.x[a] ^ self.x[b] ^ w
        self.sz[ra] += self.sz[rb]
        return True