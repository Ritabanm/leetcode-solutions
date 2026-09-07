class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x>y: 
            (x,y) = (y,x)
            
        def insideCycle(lenCycle):
            frequencies = [0]*n
            for i in range((lenCycle-1)//2): 
                frequencies[i]+=2*lenCycle
                
            if lenC&1==0: 
                frequencies[(lenCycle-1)//2]+=lenCycle

            return frequencies
            
        def insideLR(length):
            frequencies = [0]*(n*2)

            for i in range(length-1):
                frequencies[i]+=(length-1-i) * 2
            return frequencies[:n]
            
        def LRtoCycle(lengthSegment,lengthCycle):
            frequencies = [0]*(n*2)
            for i in range(lengthSegment):
                frequencies[i+1]+=4
                if lengthCycle%2==0: 
                    frequencies[i+(lengthCycle//2)]-=4
                    frequencies[i+(lengthCycle//2)]+=2 
                    frequencies[i+1+(lengthCycle//2)]-=2 
                    
                else:
                    frequencies[i+1+(lengthCycle//2)]-=4

                frequencies[i]+=2
                frequencies[i+1]-=2

            return list(accumulate(frequencies))[:n]


        def LtoR(lengthL,lengthR):
            frequencies = [0]*(n*2)
            for i in range(lengthL):
                if x== y: 
                    frequencies[i+1]+=2
                    frequencies[i+1+lengthR]-=2 

                else: 
                    frequencies[i+2]+=2
                    frequencies[i+2+lengthR]-=2 

            return list(accumulate(frequencies))[:n]
        
        lenC = y-x + 1
        L = x-1
        R = (n-y)
        
        ans = [0]*n
        ans = list(map(add, ans, insideCycle(lenC)))
        ans = list(map(add, ans, insideLR(L)))
        ans = list(map(add, ans, insideLR(R)))
        ans = list(map(add, ans, LRtoCycle(L,lenC)))
        ans = list(map(add, ans, LRtoCycle(R,lenC)))
        ans = list(map(add, ans, LtoR(L,R)))
        return ans
            
            
            