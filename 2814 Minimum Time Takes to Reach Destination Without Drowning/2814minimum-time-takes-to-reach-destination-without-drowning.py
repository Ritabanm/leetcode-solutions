class Solution:
    def minimumSeconds(self, mat: List[List[str]]) -> int:
        q = deque()
        n, m, si, sj = len(mat), len(mat[0]),-1, -1
        visited = [[0] * m for _ in range(n)]        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == "*":
                    q.append([i, j, -1])
                    visited[i][j] = -1
                elif mat[i][j] == "S":
                    si, sj = i, j
        q.append([si, sj, 0])
        visited[si][sj] = 1
        while len(q):
            i, j, l = q.popleft()
            if mat[i][j] == "D" and l != -1:
                return l
            for next in [[-1,0],[0,-1],[0,1],[1,0]]:
                ii, jj = i + next[0], j + next[1]
                if 0 <= ii < n and 0 <= jj < m and visited[ii][jj] >= 0 and mat[ii][jj] != "X":
                    if l >= 0: # run
                        if visited[ii][jj] == 0:
                            visited[ii][jj] = l+1
                            q.append([ii,jj,l+1])
                    else: # flood
                        if mat[ii][jj] != "D":
                            visited[ii][jj] = -1
                            q.append([ii,jj,-1])

        return -1