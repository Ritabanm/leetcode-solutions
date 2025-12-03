class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        graph = {i:set() for i in range(n)}
        prevs = [0 for i in range(n)]
        for u,v in edges:
            graph[v].add(u)
            prevs[v] |= (1<<u)
        @cache
        def dp(mask):
            T = bin(mask).count('1')
            res = 0
            for i in range(n):
                if (1<<i) & mask == 0:
                    if mask & prevs[i] ==  prevs[i]:
                        res = max(res,(T+1)*score[i]+dp(mask | ((1<<i))))
            return res
        return dp(0)
                    