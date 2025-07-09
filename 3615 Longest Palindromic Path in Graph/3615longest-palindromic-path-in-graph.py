class Solution:
    def maxLen(self, n: int, edges: List[List[int]], s: str) -> int:
        g, edges = [[] for _ in range(n)], [sorted(e) for e in edges]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        # For all-connected graph, we only need to focus on the string
        # Time changes from 33% to 99% with these lines
        if len(edges)==n*(n-1)//2:
            cnt = Counter(s)
            mid = any(x%2 for x in cnt.values())
            return sum((x//2)*2 for x in cnt.values())+mid

        @lru_cache(None)
        def dfs(i, j, mask):
            ans = mask.bit_count()
            s1 = [x for x in g[i] if not mask&(1<<x)]
            s2 = [x for x in g[j] if not mask&(1<<x)]
            for a, b in product(s1, s2):
                u, v = min(a, b), max(a, b)
                if u!=v and s[u]==s[v]:
                    ans = max(ans, dfs(u, v, mask|(1<<u)|(1<<v)))
            return ans
        
        ans1 = max(dfs(i, i, 1<<i) for i in range(n))
        ans2 = max([dfs(i, j, (1<<i)|(1<<j)) for i, j in edges if s[i]==s[j]] or [0])
        return max(ans1, ans2)