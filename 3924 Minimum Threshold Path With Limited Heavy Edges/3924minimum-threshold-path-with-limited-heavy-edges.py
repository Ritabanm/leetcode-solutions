class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        nexts = defaultdict(list)
        weights = set([0])
        for u, v, w in edges:
            nexts[u].append((v, w))
            nexts[v].append((u, w))
            weights.add(w)
        weights = sorted(list(weights))

        def valid(t):
            q = deque([(source, 0)])
            dist = {}
            while q:
                u, d = q.popleft()
                if u == target:
                    return d <= k
                if u in dist:
                    continue
                dist[u] = d
                for v, w in nexts[u]:
                    if w > t:
                        q.append((v, d + 1))
                    else:
                        q.appendleft((v, d))
            return False
        
        l, r = 0, len(weights) - 1
        while l < r:
            m = (l + r) // 2
            if valid(weights[m]):
                r = m
            else:
                l = m + 1
        return weights[l] if valid(weights[l]) else -1
                