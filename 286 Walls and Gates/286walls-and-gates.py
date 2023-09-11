from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        
        # Step 1: Find all gates
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:  # Gate found
                    queue.append((i, j))
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Step 2: Perform BFS
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # If within bounds and the room is empty (INF)
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                    rooms[nx][ny] = rooms[x][y] + 1  # Update distance
                    queue.append((nx, ny))
