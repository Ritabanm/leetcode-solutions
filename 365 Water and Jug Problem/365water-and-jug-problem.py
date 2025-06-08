from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x+y:
            return False
        visited = set()
        queue = deque()
        queue.append((0,0))
        visited.add((0,0))
        while queue:
            current = queue.popleft()
            a,b = current
            if a== target or b == target or a+b==target:
                return True
            next_states = [(0,b), (a,0), (x,b), (a,y),
                            (min(a+b, x), max(0, b-(x-a))),(max(0, a-(y-b)), min(a+b, y))]
            for state in next_states:
                if state not in visited:
                    queue.append(state)
                    visited.add(state)
        return False