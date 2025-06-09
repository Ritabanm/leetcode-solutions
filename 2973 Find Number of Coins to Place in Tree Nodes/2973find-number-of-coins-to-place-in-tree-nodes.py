from sortedcontainers import SortedList

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(edges) + 1
        tree = [[] for _ in range(n)]
        for u, v in edges: 
            tree[u].append(v)
            tree[v].append(u)
        ans = [1]*n 
        vals = [SortedList() for _ in range(n)]
        
        def fn(u, p): 
            """Return """
            vals[u].add(cost[u])
            for v in tree[u]: 
                if v != p:
                    fn(v, u)
                    for x in vals[v]: vals[u].add(x)
            while len(vals[u]) > 5: vals[u].pop(2)
            if len(vals[u]) < 3: ans[u] = 1
            else: 
                m = max(vals[u][0]*vals[u][1], vals[u][-3]*vals[u][-2]) * vals[u][-1]
                ans[u] = max(0, m)
        
        fn(0, -1)
        return ans 