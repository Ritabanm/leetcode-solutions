class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        forest.append([0] * len(forest[0]))
        for row in forest: row.append(0)
        def bfs(end, start):
            if end == start: return 0
            visited, queue = set(), {start}
            visited.add(start)
            step = 0
            while queue:
                s = set()
                step += 1
                for p in queue:                    
                    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        r, c = p[0] + dr, p[1] + dc
                        if not forest[r][c] or (r, c) in visited: continue
                        if (r, c) == end: return step
                        visited.add((r, c))
                        s.add((r, c))
                queue = s

        trees = [(height, r, c) for r, row in enumerate(forest) for c, height in enumerate(row) if forest[r][c] > 1]
        # check
        queue = [(0, 0)]
        reached = set()
        reached.add((0, 0))
        while queue:
            r, c = queue.pop()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                row, col = r + dr, c + dc
                if forest[row][col] and (row, col) not in reached:
                    queue.append((row, col))
                    reached.add((row,col))
        if not all([(i, j) in reached for (height, i, j) in trees]): return -1
        trees.sort()
        return sum([bfs((I,J),(i,j)) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees)])