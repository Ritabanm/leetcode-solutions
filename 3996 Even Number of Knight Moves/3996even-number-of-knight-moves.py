from collections import deque

class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        # All possible knight moves
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (-1, 2), (1, -2), (-1, -2)
        ]

        # (row, col, moves)
        q = deque([(start[0], start[1], 0)])

        visited = {(start[0], start[1])}

        while q:
            r, c, moves = q.popleft()

            # Target reached
            if r == target[0] and c == target[1]:
                return moves % 2 == 0

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < 8 and 0 <= nc < 8:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc, moves + 1))

        return False