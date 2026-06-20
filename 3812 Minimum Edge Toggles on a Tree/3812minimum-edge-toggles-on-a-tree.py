class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        
        graph = [[] for _ in range(n)]
        for edge, (u, v) in enumerate(edges):
            graph[u].append((v, edge))
            graph[v].append((u, edge))
        ans = [False] * (n-1)

        def dfs(node, parent):
            flip = 0
            for neibhor, edge in graph[node]:
                if neibhor != parent and dfs(neibhor, node):
                    ans[edge] = True
                    flip ^= 1    
            return (start[node] != target[node]) ^ flip
          

        return [-1] if dfs(0, -1) else [edge for edge, flip in enumerate(ans) if flip]         