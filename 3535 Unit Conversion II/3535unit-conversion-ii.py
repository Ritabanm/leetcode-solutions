class Solution:
    def queryConversions(self, conversions: List[List[int]], queries: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(list)
        n = len(conversions)+1
        mod = 10**9+7
        for source, target, cf in conversions:
            dic[source].append((target, cf))
            
        from_root = [1] * n
        def dfs(a):
            for b, cf in dic[a]:
                from_root[b] = (from_root[a] * cf) % mod
                dfs(b)
        dfs(0)
        res = [0] * len(queries)
        for i, (a, b) in enumerate(queries):
            print(from_root[a])
            res[i] = (pow(from_root[a], -1, mod) * from_root[b])%mod
        return res