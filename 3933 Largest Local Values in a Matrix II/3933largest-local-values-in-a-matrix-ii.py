class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        K = self.log[self.n] + 1
        self.st = [[0] * K for _ in range(self.n)]
        for i in range(self.n):
            self.st[i][0] = arr[i]
        j = 1
        while (1 << j) <= self.n:
            for i in range(self.n - (1 << j) + 1):
                self.st[i][j] = max(
                    self.st[i][j - 1],
                    self.st[i + (1 << (j - 1))][j - 1]
                )
            j += 1
    def query(self, L, R):
        length = R - L + 1
        j = self.log[length]
        return max(
            self.st[L][j],
            self.st[R - (1 << j) + 1][j]
        )

class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        if n == 1 and m == 1: return 1 if matrix[0][0] != 0 else 0
        mx = []
        for row in matrix: mx.append(SparseTable(row))
        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0: continue 
                R = matrix[i][j]
                u = max(0, i-R)
                d = min(n-1, i+R)
                l = max(0, j-R)
                r = min(m-1, j+R)
                MX = 0 
                for k in range(u, d+1):
                    if k == i-R or k == i+R:
                        nL, nR = l, r 
                        if l == j-R: nL += 1 
                        if r == j+R: nR -= 1 
                        MX = max(MX, mx[k].query(nL, nR))
                    else: 
                        MX = max(MX, mx[k].query(l, r))
                    if MX > R: break 
                if MX <= R: res += 1 
        return res 