class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
       
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        visited = set()
        

        queue = deque([(rCenter, cCenter)])
        visited.add((rCenter, cCenter))
        
        while queue:
            r, c = queue.popleft()
            res.append([r, c])
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return res




        