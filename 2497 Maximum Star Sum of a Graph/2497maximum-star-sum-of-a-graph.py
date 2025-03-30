class Solution:
    def maxStarSum(self, v: List[int], edges: List[List[int]], k: int) -> int:
        
        g = defaultdict(set)
        for i,j in edges:
            if v[i] > 0 : g[j].add(i)
            if v[j] > 0 : g[i].add(j)
                
        return max(w + sum(sorted([v[j] for j in g[i]], reverse=True)[0:k])
                   for i,w in enumerate(v))