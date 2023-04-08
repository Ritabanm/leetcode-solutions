from collections import defaultdict
from typing import List

class Excel:
    def __init__(self, height: int, width: str):
        self.H = height
        self.W = ord(width) - ord('A') + 1
        self.values = [[0] * self.W for _ in range(self.H)]
        self.formulas = [[None] * self.W for _ in range(self.H)]

    def set(self, row: int, column: str, val: int) -> None:
        r, c = row - 1, ord(column) - ord('A')
        self.formulas[r][c] = None
        self.values[r][c] = val

    def get(self, row: int, column: str) -> int:
        r, c = row - 1, ord(column) - ord('A')
        return self._get_value(r, c, {})

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r, c = row - 1, ord(column) - ord('A')
        formula = defaultdict(int)
        for item in numbers:
            if ':' in item:
                start, end = item.split(':')
                sr, sc = int(start[1:]) - 1, ord(start[0]) - ord('A')
                er, ec = int(end[1:]) - 1, ord(end[0]) - ord('A')
                for i in range(sr, er + 1):
                    for j in range(sc, ec + 1):
                        formula[(i, j)] += 1
            else:
                i, j = int(item[1:]) - 1, ord(item[0]) - ord('A')
                formula[(i, j)] += 1
        self.formulas[r][c] = formula
        return self._get_value(r, c, {})

    def _get_value(self, r: int, c: int, cache: dict) -> int:
        if (r, c) in cache:
            return cache[(r, c)]
        if not self.formulas[r][c]:
            return self.values[r][c]

        total = 0
        for (i, j), count in self.formulas[r][c].items():
            total += count * self._get_value(i, j, cache)
        cache[(r, c)] = total
        return total
