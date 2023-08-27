class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        graph = {i:set([]) for i in range(n)}
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        self.upres = [-1 for i in range(n)]
        good = [a if a == 1 else -1 for a in good]
        @cache
        def dfs(node,parent):
            res = good[node]
            for child in graph[node]:
                if child == parent:continue
                sub = dfs(child,node)
                if sub > 0:
                    res += sub
            self.upres[node] = res
            return res
        dfs(0,-1)
        self.downres = [0 for i in range(n)]

        def dfs2(node,parent,sub_parent):
            self.downres[node] = self.upres[node]+max(0,sub_parent)
            for child in graph[node]:
                if child == parent:
                    continue
                subv = self.downres[node] - max(0,self.upres[child])
                dfs2(child,node,subv)
        dfs2(0,-1,0)
        return self.downres
        