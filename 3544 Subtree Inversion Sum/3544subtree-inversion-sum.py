class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[[-inf] * (k + 1) for _ in range(2)] for _ in range(n)]
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, parent):
            for v in adj[u]:
                if v == parent:
                    continue
                dfs(v, u)
            for p in (0, 1):
                for d in range(k + 1):
                    p1, d1 = p, min(d + 1, k)
                    val1 = ((1 if p1 == 0 else -1) * nums[u] + sum(dp[v][p1][d1] for v in adj[u] if v != parent))
                    if d == k:
                        p2, d2 = 1 - p, 1
                        val2 = ((1 if p2 == 0 else -1) * nums[u] + sum(dp[v][p2][d2] for v in adj[u] if v != parent))
                    else:
                        val2 = -inf
                    dp[u][p][d] = max(val1, val2)
        
        dfs(0, -1)
        return dp[0][0][k]