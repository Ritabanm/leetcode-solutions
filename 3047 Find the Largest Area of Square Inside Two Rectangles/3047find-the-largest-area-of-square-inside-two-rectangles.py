class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                w = max(0, min(topRight[i][0], topRight[j][0]) - max(bottomLeft[i][0], bottomLeft[j][0]))                
                h = max(0, min(topRight[i][1], topRight[j][1]) - max(bottomLeft[i][1], bottomLeft[j][1]))
                res = max(res, min(w, h)**2)
        return res
                    
        
        