class Solution:
    def isEscapePossible(
        self,
        blocked: list[list[int]],
        source: list[int],
        target: list[int]
    ) -> bool:
        def walk(source: list[int], target: list[int]) -> bool:
            currCells = [source]
            visited = {tuple(source)}
            for r, c in currCells:
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < MAX_POSITION and 0 <= nc < MAX_POSITION and \
                            (nr, nc) not in visited and (nr, nc) not in blocks:
                        if [nr, nc] == target:
                            return True

                        currCells.append([nr, nc])
                        visited.add((nr, nc))

                if len(currCells) > MAX_BLOCKED_AREA:
                    return True

            return False

        if not blocked:  # No blocks.
            return True

        B = len(blocked)
        MAX_POSITION = 10 ** 6
        MAX_BLOCKED_AREA = (B * (B - 1)) >> 1
        blocks = {tuple(cell) for cell in blocked}
        return walk(source, target) and walk(target, source)