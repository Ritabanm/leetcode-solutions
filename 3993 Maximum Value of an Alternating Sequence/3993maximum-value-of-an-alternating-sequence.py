class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n==1:
            return s
        
        numInc = n//2
        numdec = numInc-1
        return s+numInc*m-numdec
        