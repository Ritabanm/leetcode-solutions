class Solution:
    def minCostExcludingMax(self, n: int, edges: List[List[int]]) -> int:
        self.conn = [[] for _ in range(n)]
        for a,b,w in edges:
            self.conn[a].append((b,w))
            self.conn[b].append((a,w))

        d0, d1 = self.dijkstra(0), self.dijkstra(n-1)
        return min(min(d0[a]+d1[b], d1[a]+d0[b]) for a,b,_ in edges)

    def dijkstra(self, node: int) -> List[int]:
        # Regular Dijkstra
        dp = [inf] * len(self.conn)
        dp[node] = 0
        heap = [(0, node)]
        while heap:
            dist, node = heappop(heap)
            if dist > dp[node]:
                continue
            for nxt, w in self.conn[node]:
                if dist + w >= dp[nxt]:
                    continue
                dp[nxt] = dist + w
                heappush(heap, (dist + w, nxt))
        return dp       