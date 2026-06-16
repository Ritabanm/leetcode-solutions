class Solution:
    def searchMatrix(self, Matrix:List[List[int]], target: int)-> bool:
        
        for row in Matrix:
            if target in row:
                return True
        return False
