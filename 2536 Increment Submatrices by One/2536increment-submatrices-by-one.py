class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        m = [[0]*n for i in range(n)]
        for q in queries:
            sr, sc, er, ec = q
            for i in range(sr, er+1):
                m[i][sc] += 1
                if ec+1 < n:
                    m[i][ec+1] -=1
        
        for i in range(n):
            for j in range(1, n):
                m[i][j] += m[i][j-1]
                
        return m