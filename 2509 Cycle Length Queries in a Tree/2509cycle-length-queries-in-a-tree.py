class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        

        res = []
        for i,j in queries:
            ii, jj = i,j 
            while ii!=jj:
                while ii > jj:
                    ii//=2
                while jj > ii:
                    jj//=2
            
            res.append(
                floor(log(i,2)) + floor(log(j,2)) - 2*floor(log(ii,2)) + 1
            )
            
        return res
                