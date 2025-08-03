class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, visited):
            if visited[node]:
                return 0
            visited[node]=True
            return 1+sum(dfs(neighbor, visited) for neighbor in graph[node])
        
        #Build adjacency graph.
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        #Calculate Sizes of connected components.
        visited = [False]*n
        sizes = [dfs(i, visited) for i in range(n)]
        return sum([sizes[i]* (n-sizes[i]) for i in range(n)])//2