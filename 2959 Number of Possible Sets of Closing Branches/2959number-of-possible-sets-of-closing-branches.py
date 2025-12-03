class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def check(subset, n, maxDistance, roads):
            dist = [[float('inf')] * n for _ in range(n)]
            for i in range(n):
                dist[i][i] = 0
            for u, v, w in roads:
                if u in subset and v in subset:
                    dist[u][v] = min(dist[u][v], w)
                    dist[v][u] = min(dist[v][u], w)
            for k in subset:
                for i in subset:
                    for j in subset:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            for i in subset:
                for j in subset:
                    if dist[i][j] > maxDistance:
                        return False
            return True
        
        ans = 0
        for r in range(n + 1):
            for subset in itertools.combinations(range(n), r):
                if check(subset, n, maxDistance, roads):
                    ans += 1
        return ans