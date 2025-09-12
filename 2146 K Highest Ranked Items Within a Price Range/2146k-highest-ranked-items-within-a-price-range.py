from typing import List
from collections import deque

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        low, high = pricing
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(start[0], start[1], 0)])
        visited = set()
        visited.add((start[0], start[1]))
        items = []

        while queue:
            x, y, dist = queue.popleft()
            if low <= grid[x][y] <= high:
                items.append((dist, grid[x][y], x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != 0:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

        items.sort(key=lambda item: (item[0], item[1], item[2], item[3]))
        return [[item[2], item[3]] for item in items[:k]]

# Example test cases
solution = Solution()
print(solution.highestRankedKItems([[1,2,0,1],[1,3,0,1],[0,2,5,1]], [2,5], [0,0], 3))  # Output: [[0,1],[1,1],[2,1]]
print(solution.highestRankedKItems([[1,2,0,1],[1,3,3,1],[0,2,5,1]], [2,3], [2,3], 2))  # Output: [[2,1],[1,2]]
print(solution.highestRankedKItems([[1,1,1],[0,0,1],[2,3,4]], [2,3], [0,0], 3))  # Output: [[2,1],[2,0]]