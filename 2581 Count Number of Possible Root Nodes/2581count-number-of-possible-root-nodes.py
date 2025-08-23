class Solution:
    def rootCount(self, E, G, k):
        n = len(E)
        G = set(map(tuple, G))
        graph = [[] for _ in range(n + 1)]
        for a, b  in E:
            graph[a].append(b)
            graph[b].append(a)
        def count(node, parent):
            val = 0
            for i in graph[node]:
                if i == parent: continue
                if (node, i) in G: val += 1
                val += count(i, node)
            return val
        def dfs(node, parent, val):
            ans = 0
            if val >= k: ans += 1
            for i in graph[node]:
                if i == parent: continue
                cur = val - (1 if (node, i) in G else 0) + (1 if (i, node) in G else 0)
                ans += dfs(i, node, cur)
            return ans
        return dfs(0, -1, count(0, -1))