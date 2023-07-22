import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        minHeap = []
        
        # Step 1: Add all boundary cells to the minHeap
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    heapq.heappush(minHeap, (heightMap[r][c], r, c))
                    visited[r][c] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        water_trapped = 0

        # Step 2: Process cells in the minHeap
        while minHeap:
            height, x, y = heapq.heappop(minHeap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    visited[nx][ny] = True
                    water_trapped += max(0, height - heightMap[nx][ny])  # Water trapped
                    heapq.heappush(minHeap, (max(height, heightMap[nx][ny]), nx, ny))  # Update height
                    
        return water_trapped
