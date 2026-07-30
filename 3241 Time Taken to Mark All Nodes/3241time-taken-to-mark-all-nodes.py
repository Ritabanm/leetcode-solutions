class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = [-1] * n
        longestBranch1, longestBranch2 = [0] * n, [0] * n

        def dfs(node: int, par: int) -> int:
            res = 0
            for adj in graph[node]:
                if adj != par:
                    branch = dfs(adj, node) + (2 - adj % 2)
                    res = max(res, branch)
                    #Record top two longest branch except its parent
                    if branch > longestBranch1[node]:
                        longestBranch2[node] = longestBranch1[node]
                        longestBranch1[node] = branch
                    elif branch > longestBranch2[node]:
                        longestBranch2[node] = branch
            ans[node] = res
            return res

        dfs(0, -1)

        def dfs2(node: int, par: int) -> None:
            #For nodes except 0, calculate the branch length from its parent
            parTime = -1
            if 2 - node % 2 + ans[node] == longestBranch1[par]:
                #this is the longest branch of its parent
                parTime = 2 - par % 2 + longestBranch2[par]
            else:
                #this is not the longest branch of its parent
                parTime = 2 - par % 2 + longestBranch1[par]
            #Update top two longest branch of the current node
            if parTime > longestBranch1[node]:
                longestBranch2[node] = longestBranch1[node]
                longestBranch1[node] = parTime
            elif parTime > longestBranch2[node]:
                longestBranch2[node] = parTime
            #ans[node] has already cauculated in the first DFS, just update it by comparing to the new branch, that is its parent
            ans[node] = max(parTime, ans[node])
            for adj in graph[node]:
                if adj != par:
                    dfs2(adj, node)

        for next in graph[0]:
            dfs2(next, 0)

        return ans