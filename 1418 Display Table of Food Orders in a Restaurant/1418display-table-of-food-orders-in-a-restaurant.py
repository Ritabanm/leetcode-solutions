from collections import defaultdict

class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        foods, tables = set(), set()
        counts = defaultdict(lambda: defaultdict(int))
        for _, t, f in orders:
            tables.add(int(t))
            foods.add(f)
            counts[int(t)][f] += 1
        foods = sorted(foods)
        displayTable = [["Table"] + foods]
        for t in sorted(tables):
            row = [str(t)]
            cnt = counts[t]
            for f in foods:
                row.append(str(cnt.get(f, 0)))
            displayTable.append(row)
        return displayTable