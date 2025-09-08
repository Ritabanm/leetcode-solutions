class Solution:
    def getNoZeroIntegers(self, n):
        for A in range(1,n):
            B = n-A
            if "0" not in str(A) + str(B):
                return [A, B]
        return []
        