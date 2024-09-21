from collections import deque

class Solution:
    def findMedian(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        neighNodes = [[] for _ in range(n)]
        for u, v, w in edges:
            neighNodes[u].append((v,w))
            neighNodes[v].append((u,w))
        
        length = (n-1).bit_length()
        parents = [[-1]*n for _ in range(length)]
        sumW = [[0]*n for _ in range(length)]
        depth, dist = [0]*n, [0]*n
        dq = deque([0])
        visited = [True] + [False]*(n-1)

        while dq:
            u = dq.popleft()
            for v, w in neighNodes[u]:
                if not visited[v]:
                    visited[v] = True
                    parents[0][v] = u
                    sumW[0][v] = w
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    dq.append(v)
        
        for j in range(1, length):
            for i in range(n):
                p = parents[j-1][i]
                if p != -1:
                    parents[j][i] = parents[j-1][p]
                    sumW[j][i] = sumW[j-1][i] + sumW[j-1][p]

        def lowestCommonAncestor(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            d = depth[u] - depth[v]
            idx = 0
            while d:
                if d & 1:
                    u = parents[idx][u]
                d >>= 1
                idx += 1
            if u == v:
                return u
            for j in range(length-1, -1, -1):
                if parents[j][u] != parents[j][v]:
                    u = parents[j][u]
                    v = parents[j][v]
            return parents[0][u]
        
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(u)
                continue
            w = lowestCommonAncestor(u, v)
            distUW = dist[u] - dist[w]
            distVW = dist[v] - dist[w]
            delt = (distUW + distVW + 1) // 2
            
            if distUW >= delt:
                rem = delt
                curr = u
                for j in range(length-1, -1, -1):
                    if parents[j][curr] != -1 and sumW[j][curr] < rem:
                        rem -= sumW[j][curr]
                        curr = parents[j][curr]
                ans.append(curr if rem == 0 else parents[0][curr])
            else:
                rem = distVW - (delt - distUW)
                curr = v
                for j in range(length-1, -1, -1):
                    if parents[j][curr] != -1 and sumW[j][curr] <= rem:
                        rem -= sumW[j][curr]
                        curr = parents[j][curr]
                ans.append(curr)
        return ans