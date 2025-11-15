class NumMatrix:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.m = len(matrix[0]) if self.n else 0
        self.matrix = [row[:] for row in matrix]
        # Fenwick Tree for efficient sum and updates
        self.bit = [[0]*(self.m+1) for _ in range(self.n+1)]
        for i in range(self.n):
            for j in range(self.m):
                self._updateBIT(i+1, j+1, matrix[i][j])

    def _updateBIT(self, x, y, delta):
        i = x
        while i <= self.n:
            j = y
            while j <= self.m:
                self.bit[i][j] += delta
                j += j & -j
            i += i & -i

    def _queryBIT(self, x, y):
        res = 0
        i = x
        while i > 0:
            j = y
            while j > 0:
                res += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return res

    def update(self, row, col, val):
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._updateBIT(row+1, col+1, delta)

    def sumRegion(self, row1, col1, row2, col2):
        def query(r, c):
            return self._queryBIT(r+1, c+1)
        res = (
            query(row2, col2)
            - query(row2, col1-1)
            - query(row1-1, col2)
            + query(row1-1, col1-1)
        )
        return res

# Example test
ops = ["NumMatrix", "sumRegion", "update", "sumRegion"]
params = [
    [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]],
    [2, 1, 4, 3],
    [3, 2, 2],
    [2, 1, 4, 3]
]

obj = NumMatrix(params[0])
results = [None]
results.append(obj.sumRegion(*params[1]))  # 8
obj.update(*params[2])
results.append(None)
results.append(obj.sumRegion(*params[3]))  # 10
print(results)
