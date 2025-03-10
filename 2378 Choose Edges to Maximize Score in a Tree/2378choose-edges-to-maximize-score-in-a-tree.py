from collections import defaultdict
from functools import cache
class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for w,(v, cost) in enumerate(edges):
            G[v].append((w,cost))
        @cache
        def dfs(v, chosen):
            if not G[v]: return 0
            total = 0
            for w,cost in G[v]:
                total += dfs(w, False)
            if chosen:
                return total
            res = total
            for w,cost in G[v]:
                res = max(res, total - dfs(w,False) + cost + dfs(w,True))
            return res
        return dfs(0, False)
            