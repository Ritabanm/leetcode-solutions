class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        mp = defaultdict(list)
        for u,v in edges:
            mp[u].append(v)
        def dfs(node):
            if len(mp[node])==0:
                return baseTime[node]
            mini =inf
            maxi = -inf
            for child in mp[node]:
                val = dfs(child)
                mini = min(mini, val)
                maxi = max(maxi, val)
            return 2*maxi-mini + baseTime[node]
        return dfs(0)