class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = {}

        for i in range(n):
            graph[i] = []
        
        for (u,v) in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        if len(connections) < n - 1:
            return -1

        def dfs(graph, node, visited):
            visited.add(node)
            summ = 0

            for child in graph[node]:
                if child not in visited:
                    dfs(graph,child,visited)

        ans = []; summ=0
        visited = set()
        for i in range(n):
            if i not in visited:
                summ += 1
                dfs(graph,i,visited)

        return summ-1