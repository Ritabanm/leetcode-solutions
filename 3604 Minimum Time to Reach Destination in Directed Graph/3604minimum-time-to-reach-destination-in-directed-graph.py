class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]
        seen, heap = [False] * n, [(0, 0)]

        for u, v, beg, end in edges:
            graph[u].append((v, beg, end))

        if graph[0] == []: 
            return (n == 1) - 1

        while heap:

            time, parent = heappop(heap)
            if seen[parent]: 
                continue
            if parent == n - 1: 
                return time
            seen[parent] = True

            for child, beg, end in graph[parent]:
                if seen[child] or time > end:
                    continue
                if beg >= time:
                    heappush(heap, (beg  + 1, child))
                else:
                    heappush(heap, (time + 1, child))

        return -1