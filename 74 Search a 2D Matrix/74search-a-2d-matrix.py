class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        l,r = 0, m*n-1
        while l<=r:
            pi = (l+r)//2
            pe = matrix[pi//n][pi%n]
            if target==pe:
                return True
            else:
                if target<pe:
                    r = pi-1
                else:
                    l = pi+1
        return False