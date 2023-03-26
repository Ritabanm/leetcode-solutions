from collections import defaultdict

class Solution:
    def sumOfAncestors(self, n: int, edges: list[list[int]], nums: list[int]) -> int:
        def squareFree(x):
            r = 1
            while x > 1:
                p, c = spf[x], 0
                while x%p == 0:
                    x //= p
                    c ^= 1
                if c:
                    r *= p
            return r

        m = max(nums)
        spf = list(range(m+1))
        for i in range(2,int(m**0.5)+1):
            if spf[i] == i:
                step = i
                for j in range(i**2, m+1, i):
                    if spf[j] == j:
                        spf[j] = i
        v = [squareFree(x) for x in nums]
        g = [[] for _ in range(n)]
        for u, w in edges:
            g[u].append(w)
            g[w].append(u)
        f = defaultdict(int)
        ans = 0
        st = [(0,-1,0)]
        while st:
            u, p, t = st.pop()
            if t == 0:
                ans += f[v[u]]
                f[v[u]] += 1
                st.append((u,p,1))
                for w in g[u]:
                    if w != p:
                        st.append((w,u,0))
            else:
                f[v[u]] -= 1
        return ans