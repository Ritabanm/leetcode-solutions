class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u].append((v, 1))  # 1 indicates a directed edge in the original graph
            graph[v].append((u, 0))  # 0 indicates an undirected edge in the original graph
            
        ans = [0] * n
        
        # DFS to calculate initial answer
        def dfs(u, p=-1):
            for v, d in graph[u]:
                if v == p: 
                    continue 
                ans[0] += 1 if d == 0 else 0  
                dfs(v, u)
                
        dfs(0)
        
        # DFS to calculate answer for other nodes
        def dfs2(u, p=-1):
            for v, d in graph[u]: 
                if v == p: 
                    continue
                if d: 
                    ans[v] = ans[u] + 1
                else:
                    ans[v] = ans[u] - 1
                dfs2(v, u)
                    
        dfs2(0)        
        return ans