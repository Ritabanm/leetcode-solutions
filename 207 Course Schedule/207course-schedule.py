class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[u].append(v)
        visit = {}
        def dfs(node):
            if node in visit: return visit[node]==1
            visit[node]=0
            for nei in graph[node]:
                if not dfs(nei): return False
            visit[node]=1
            return True
        return all(dfs(i) for i in range(numCourses))