class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:

        
        def F(m):
            count = 0 
            
            for i in range(1,80):
                bit = (i*x)-1
                S = 1<<bit
                B = m//(S)
                
                count+=(S)*(B//2)
                if B&1: 
                    count+= m%(S)
                
            return count
        
            
        l = 0
        r = 10**20
        
        while l+1<r:
            m = (l+r)>>1
            
            if F(m+1)<=k: l = m 
            else: r = m
                
        return l