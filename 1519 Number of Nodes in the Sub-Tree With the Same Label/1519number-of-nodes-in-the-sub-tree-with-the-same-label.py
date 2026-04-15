class Solution:
    def countSubTrees(self, n, edges, labels):
        def dfs(node):
            count= Counter(labels[node])
            for child in graph[node]:
                graph[child].discard(node)
                count+=dfs(child)
            ret[node] =count[labels[node]]
            return count
        graph = collections.defaultdict(set)
        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)
        ret = [0]*n
        dfs(0)
        return ret