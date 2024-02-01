# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> None:
#        
#
#    def isTarget(self) -> bool:
#        
#

from collections import deque

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        reverse_directions = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        visited = set()
        grid = {}
        target = None

        # Step 1: DFS to map the grid and find the target
        def dfs(x, y):
            nonlocal target
            if (x, y) in visited:
                return
            visited.add((x, y))
            if master.isTarget():
                target = (x, y)
            grid[(x, y)] = True  # Mark cell as reachable
            
            for direction in directions:
                new_x, new_y = x + directions[direction][0], y + directions[direction][1]
                if (new_x, new_y) not in visited and master.canMove(direction):
                    master.move(direction)
                    dfs(new_x, new_y)
                    master.move(reverse_directions[direction])  # Backtrack

        dfs(0, 0)

        # If the target is not found during DFS, return -1
        if target is None:
            return -1

        # Step 2: BFS to find the shortest path to the target
        queue = deque([(0, 0, 0)])  # (x, y, steps)
        visited = set()
        visited.add((0, 0))

        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == target:
                return steps

            for direction in directions:
                new_x, new_y = x + directions[direction][0], y + directions[direction][1]
                if (new_x, new_y) in grid and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, steps + 1))

        return -1
