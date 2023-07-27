class Solution:
    def findNumber(self, mxBits = 30) -> int:

        ans, pwr2 = 0, 1,
        zeros = commonBits(0)

        while zeros < mxBits:

            if commonBits(0) - commonBits(pwr2)!= 1:
                ans+= pwr2
                zeros+= 1
                
            pwr2*= 2
                    
        return ans 