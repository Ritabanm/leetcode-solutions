class Matrix3D:

    def __init__(self, n: int):
        self.matrix = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        self.dimension_sizes = [[0, i] for i in range(n)]
        self.curr_max = n - 1
        self.prev_max = max(0, n - 2)

    def setCell(self, x: int, y: int, z: int) -> None:
        compare = self.compare
        dimension_sizes = self.dimension_sizes
        
        old_val = self.matrix[x][y][z]
        if old_val == 1:
            return
        self.matrix[x][y][z] = 1
        dimension_sizes[x][0] += 1

        if x == self.prev_max \
                and compare(dimension_sizes[x], dimension_sizes[self.curr_max]) > 0:
            self.prev_max, self.curr_max = self.curr_max, self.prev_max
        elif x != self.curr_max:
            if compare(dimension_sizes[x], dimension_sizes[self.curr_max]) > 0:
                self.prev_max = self.curr_max
                self.curr_max = x
            elif compare(dimension_sizes[x], dimension_sizes[self.prev_max]) > 0:
                self.prev_max = x


    def unsetCell(self, x: int, y: int, z: int) -> None:
        compare = self.compare
        dimension_sizes = self.dimension_sizes

        old_val = self.matrix[x][y][z]
        if old_val == 0:
            return
        self.matrix[x][y][z] = 0
        dimension_sizes[x][0] -= 1

        if self.curr_max == x \
                and compare(dimension_sizes[x], dimension_sizes[self.prev_max]) < 0:
            self.prev_max, self.curr_max = self.curr_max, self.prev_max


    def compare(self, a, b):
        if a[0] == b[0]:
            return a[1] - b[1]
        return a[0] - b[0]

    def largestMatrix(self) -> int:
        return self.curr_max

# Your Matrix3D object will be instantiated and called as such:
# obj = Matrix3D(n)
# obj.setCell(x,y,z)
# obj.unsetCell(x,y,z)
# param_3 = obj.largestMatrix()