class Solution:
    def countComponents(self, A: List[int], k: int) -> int:
        ds = {}
        def find(u):
            ds.setdefault(u, u)
            if ds[u] != u:
                ds[u] = find(ds[u])
            return ds[u]
        for a in A:
            for b in range(a, k + 1, a):
                ds[find(a)] = find(b)
        return len({*map(find, A)})