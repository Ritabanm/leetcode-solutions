from collections import defaultdict, deque

class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: List[List[int]]):
        self.connected_edges = defaultdict(list)
        
        for a, b, distance in edgeList:
            self.connected_edges[a].append((b, distance))
            self.connected_edges[b].append((a, distance))

    def query(self, p: int, q: int, limit: int) -> bool:
        visited = set()
        stack = deque([p])
        while stack:
            node = stack.pop()

            if node == q:
                return True

            if node in visited:
                continue

            visited.add(node)
            for x in self.connected_edges[node]:
                if x[1] < limit:
                    stack.appendleft(x[0])

        return False