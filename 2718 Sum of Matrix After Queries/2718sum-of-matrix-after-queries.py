class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:

        rowcol, ans, Seen = [n,n], 0, [0,0]

        for typ, idx, val in reversed(queries):
     
            if Seen[typ]&(1<<idx): continue
            Seen[typ]|= (1<<idx)
    
            ans+= val * rowcol[typ]
            rowcol[typ^1]-= 1

        return  ans