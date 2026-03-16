class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        # bounds for binary search
        l = 0
        r = -inf

        # build graph for bfs 
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            r = max(r, w)

        def bfs(money): 
            seen = {0}
            queue = deque([(0, 0)])

            while queue:
                node, distance = queue.popleft()

                if node == n - 1:
                    return True

                if distance < k:
                    for adjacent, cost in graph[node]:
                        if adjacent in seen or cost > money: continue 
                        seen.add(adjacent)
                        queue.append((adjacent, distance + 1))
            
            return False

        # bisect left
        while l < r:
            m = l + (r - l) // 2
            if bfs(m):
                r = m
            else:
                l = m + 1

        return l if bfs(l) else -1

                     

        
        