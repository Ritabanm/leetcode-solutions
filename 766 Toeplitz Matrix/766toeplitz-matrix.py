class Solution:
    def isToeplitzMatrix(self, matrix:List[List[int]])-> bool:
        diagonal_map = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i-j) not in diagonal_map:
                    diagonal_map[i-j]=matrix[i][j]
                elif diagonal_map[i-j]!=matrix[i][j]:
                    return False
        return True