class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        ans = 0

        moves = {
            "rook": [[1, 0], [-1, 0], [0, 1], [0, -1]],
            "queen": [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1],
                [1, 1],
                [1, -1],
                [-1, 1],
                [-1, -1],
            ],
            "bishop": [[1, 1], [1, -1], [-1, 1], [-1, -1]],
        }
        visited = defaultdict(set)

        # all possible destinations
        possible_destinations = defaultdict(list)

        for i in range(len(pieces)):
            for dx, dy in moves[pieces[i]]:
                r, c = positions[i]
                r += dx
                c += dy
                while r > 0 and c > 0 and r < 9 and c < 9:
                    possible_destinations[i].append((r, c))
                    r += dx
                    c += dy
            possible_destinations[i].append(positions[i])

        # print(possible_destinations)

        def simulate(destinations: list[list[int]]):
            cur_positions = positions[:]
            while True:
                new_positions = []
                moved = False
                occupied = set()
                for i, (r, c) in enumerate(cur_positions):
                    dr, dc = destinations[i]
                    if r == dr and c == dc:
                        # already at destination
                        new_positions.append((r, c))
                    else:
                        r += 1 if r < dr else -1 if r > dr else 0
                        c += 1 if c < dc else -1 if c > dc else 0
                        new_positions.append((r, c))
                        moved = True
                    if (r, c) in occupied:
                        return False  # collision
                    occupied.add((r, c))

                if not moved:  # all pieces have reached their respective destinations
                    break
                cur_positions = new_positions

            # no collisions found
            # pieces reached their destinations
            return True

        n = len(pieces)

        def backtrack(i, destinations):
            nonlocal ans
            if i == n:
                # all pieces are assigned destinations
                if simulate(destinations):
                    ans += 1
                return

            for d in possible_destinations[i]:
                destinations.append(d)
                backtrack(i + 1, destinations)
                destinations.pop()

        backtrack(0, [])

        return ans