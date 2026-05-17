class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        isEven = True
        minNum = min(A)
        
        while minNum != 0:
            if (minNum % 10) % 2 == 1:
                isEven = not isEven
            minNum = minNum // 10
            
        return int(isEven)