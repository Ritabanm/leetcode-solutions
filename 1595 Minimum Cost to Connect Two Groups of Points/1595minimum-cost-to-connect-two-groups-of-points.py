class Solution:
    def connectTwoGroups(self, cost):
        m, n = len(cost), len(cost[0])

        ans = [min(i) for i in zip(*cost)]

        @lru_cache(None)
        def dfs(i,mask):
            if i == m: return sum(ans[j] for j in range(n) if not (mask & (1<<j)))
            return min(cost[i][j] + dfs(i+1,mask|(1<<j)) for j in range(n))

        return dfs(0,0)





        