class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ones = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i%2)==(j%2):
                    ones.append((i,j))
        matched = {}

        def dfs(node,visted):
            r,c = node
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    if (nr,nc) not in matched or dfs(matched[(nr,nc)],visited):
                        matched[(nr,nc)] = node
                        return True
            return False
        
        res = 0
        for node in ones:
            visited = set([])
            if dfs(node,visited): res += 1
        return res



        