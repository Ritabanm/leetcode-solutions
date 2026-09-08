class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        flat = []
        for i in range(m):
            for j in range(n):
                flat.append(mat[i][j])
        
        newMat = []
        for _ in range(r):
            row = []
            for __ in range(c):
                row.append(flat.pop(0))
            newMat.append(row)
        
        return newMat