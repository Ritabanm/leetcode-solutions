class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return 1
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        parent = {}  # For Union-Find
        grid = [[0] * n for _ in range(m)]  # To track land cells
        islands = 0  # Current number of islands
        answer = []
        
        for r, c in positions:
            if grid[r][c] == 1:  # Skip if already land
                answer.append(islands)
                continue
                
            grid[r][c] = 1
            islands += 1
            current = r * n + c
            parent[current] = current  # Initialize disjoint set
            
            # Check all 4 directions and union if adjacent land found
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and 
                    grid[nr][nc] == 1):
                    neighbor = nr * n + nc
                    islands -= union(current, neighbor)
            
            answer.append(islands)
            
        return answer