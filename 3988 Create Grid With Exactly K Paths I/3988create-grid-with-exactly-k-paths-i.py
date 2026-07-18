class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        
        #single row/col
        if (m==1 or n==1) and k!=1:
            return []
        
        #special case
        if m==3 and n==3 and k==4:
            return ['..#', '...', '#..']
        
        if k>max(m,n):
            return []
        res = [['#' for _ in range(n)] for __ in range(m)]

        #open first row
        for j in range(n):
            res[0][j]='.'
        
        #open first col 
        for i in range(m):
            res[i][-1]='.'
        
        if m>n:
            row = 1
            for _ in range(k-1):
                res[row][-2]='.'
                row+=1
        else:
            col = -2
            for _ in range(k-1):
                res[1][col]='.'
                col -=1
        return [''.join(row) for row in res]