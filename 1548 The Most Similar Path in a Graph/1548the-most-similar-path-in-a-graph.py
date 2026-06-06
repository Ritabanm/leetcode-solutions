class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        def createGraph():
            for edge in roads:
                edges[edge[0]].append(edge[1])
                edges[edge[1]].append(edge[0])
            
        
        m = len(targetPath)
        dp = [[float('inf')]*m for _ in range(n)]
        paths = [[[] for _ in range(m)] for _ in range(n)]
        edges = [[] for _ in range(n)]
        createGraph()
        for i in range(n):
            dp[i][m-1] = (names[i] != targetPath[-1])
            paths[i][m-1].append(i)
        for j in range(m-2, -1, -1):
            for i in range(n):
                paths[i][j].append(i)
                min_idx = -1
                for e in edges[i]:
                    if dp[e][j+1] < dp[i][j]:
                        min_idx = e
                        dp[i][j] = dp[e][j+1]
                paths[i][j].extend(paths[min_idx][j+1])
                dp[i][j] += names[i] != targetPath[j]
        ans = None
        min_dist = float('inf')
        for i in range(n):
            if dp[i][0] < min_dist:
                ans = paths[i][0]
                min_dist = dp[i][0]
        return ans