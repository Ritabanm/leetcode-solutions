class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph, reversed_graph = defaultdict(dict), defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = min(w, graph[u].get(v, inf))
            reversed_graph[v][u] = min(w, reversed_graph[v].get(u, inf))
        
        def dijkstra(g, src):
            dist = {}
            h = [(0, src)]
            while h:
                d, v = heappop(h)
                if v not in dist:
                    dist[v] = d
                    for u in g[v]:
                        if u not in dist:
                            heappush(h, (d+g[v][u], u))
            return dist

        src1_dist = dijkstra(graph, src1)
        src2_dist = dijkstra(graph, src2)
        dest_dist = dijkstra(reversed_graph, dest)
        return min((src1_dist[k] + src2_dist[k] + dest_dist[k] for k in range(n) 
                    if k in src1_dist and k in src2_dist and k in dest_dist), 
                    default=-1)