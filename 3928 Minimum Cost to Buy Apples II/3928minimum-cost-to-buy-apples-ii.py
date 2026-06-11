class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        graph = {i:set([]) for i in range(n)}
        if n == 1:
            return prices
        for u,v,c,t in roads:
            graph[u].add((v,c,c*t))
            graph[v].add((u,c,c*t))
        
        def dijk1(source):
            dist = [float('inf')] * n
            dist[source] = 0
            dq = deque([source])
            
            while dq:
                u = dq.popleft()
                for v, w1,w2 in graph[u]:
                    if dist[u] + w1 < dist[v]:
                        dist[v] = dist[u] + w1
                        dq.append(v)
            return dist
        
        def dijk2(source):
            dist = [float('inf')] * n
            dist[source] = 0
            dq = deque([source])
            
            while dq:
                u = dq.popleft()
                for v, w1,w2 in graph[u]:
                    if dist[u] + w2 < dist[v]:
                        dist[v] = dist[u] + w2
                        dq.append(v)
            return dist
        dists1 = []
        dists2 = []
        for i in range(n):
            dists1.append(dijk1(i))
            dists2.append(dijk2(i))
        res = []
        for i in range(n):
            res1 = prices[i]
            res2 = min(prices[j]+dists1[i][j] + dists2[j][i] for j in range(n) if j!=i)
            res.append(min(res1,res2))
        return res


        