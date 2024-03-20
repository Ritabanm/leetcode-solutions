class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges: graph[u][v] = graph[v][u] = w
        
        ans = 0
        pq = [(0, 0)] # min-heap 
        
        seen = [False] * n
        used = defaultdict(int)
        
        while pq: 
            x, u = heappop(pq)
            if not seen[u]: 
                ans += 1
                seen[u] = True 
                for v, c in graph[u].items(): 
                    if not used[u, v]: 
                        if used[v, u] < graph[v][u]: 
                            used[u, v] = min(maxMoves - x, graph[v][u] - used[v, u])
                            ans += used[u, v]
                        if x + c + 1 <= maxMoves and not seen[v]: heappush(pq, (x + c + 1, v))
        return ans 