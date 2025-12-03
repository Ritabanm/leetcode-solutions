class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        N = len(vals)
        adj = [[] for _ in range(N)]
        for u in range(1, N):
            adj[par[u]].append(u)

        def dfs(u):
            du = {0: 0}
            s = str(abs(vals[u]))
            if len(s) == len(set(s)):
                m = sum(1 << int(c) for c in s)
                du[m] = vals[u]

            for v in adj[u]:
                dv = dfs(v)
                for mv, sv in dv.items():
                    for mu, su in list(du.items()):
                        if mu & mv == 0:
                            du[mu | mv] = max(du.get(mu | mv, 0), su + sv)

            self.ans += max(du.values())
            return du

        self.ans = 0
        dfs(0)
        return self.ans % (10**9 + 7)