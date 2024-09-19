class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        
        i=round(math.log(n,3),10)
        return math.ceil(i)-i==0
        