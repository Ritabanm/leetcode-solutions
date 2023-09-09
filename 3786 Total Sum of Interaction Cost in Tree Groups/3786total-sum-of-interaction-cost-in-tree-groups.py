class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        graph = {i:set([]) for i in range(n)}
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        self.counts = [[0]*21 for i in range(n)]
        def dfs(node,parent):
            self.counts[node][group[node]] += 1
            for child in graph[node]:
                if child == parent:continue
                dfs(child,node)
                for i in range(21):
                    self.counts[node][i] += self.counts[child][i]
        dfs(0,-1)
        res = 0
        for u in range(n):
            for i in range(21):
                res += self.counts[u][i]*(self.counts[0][i]-self.counts[u][i])
        return res

            