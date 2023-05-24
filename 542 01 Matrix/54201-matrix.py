from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # Step 1: Initialize distances and queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))  # Start BFS from all 0s
                else:
                    mat[r][c] = float('inf')  # Mark 1s as unvisited (inf)

        # Step 2: BFS to update distances
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))

        return mat
