class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        

        rlen = len(matrix)
        clen = len(matrix[0])
        maxpath = float("-inf")

        dt = [[0] * clen for _ in range(rlen)]
        

        def dfs(r,c,prev):
            if r < 0 or c < 0 or r >= rlen or c >= clen or prev >= matrix[r][c]:
                return 0
            if dt[r][c]:
                return dt[r][c]
            
            path = 1
            node = matrix[r][c]

            rp= dfs(r+1, c, node)
            rm= dfs(r-1, c, node)
            cp= dfs(r, c+1, node)
            cm= dfs(r, c-1, node)

            path += max(rp,rm,cp,cm)

            dt[r][c] = path
            return path

        
        for r in range(rlen):
            for c in range(clen):
                if not dt[r][c]:
                    maxpath = max(maxpath, dfs(r,c,float("-inf")))

        return maxpath
