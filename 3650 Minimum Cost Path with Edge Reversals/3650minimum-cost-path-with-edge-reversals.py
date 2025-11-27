class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # create adj list
        adj = [[] for _ in range(n)]
        for u, v, wt in edges:
            adj[u].append((v, wt))      # direct edge
            adj[v].append((u, 2 * wt))  # reverse edge

        dist = [float("inf")] * n
        dist[0] = 0

        # (cost, node)
        pq = [(0, 0)] 

        while pq:
            total, u = heapq.heappop(pq)

            if dist[u] > total:
                continue

            if u == n - 1:
                return total

            # push both direct and reverse edges
            for v, wt in adj[u]:
                if dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
                    heapq.heappush(pq, (dist[v], v))

        return -1