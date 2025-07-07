class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        conn, far, remap = [0] * n, list(range(n)), [0] * n
        nums_with_idx = sorted((v, i) for i, v in enumerate(nums))
        for sorted_pos, (_, orig_idx) in enumerate(nums_with_idx): remap[orig_idx] = sorted_pos
        nums_sorted = [v for v, _ in nums_with_idx]
        curc = 0
        for i in range(1, n):
            if nums_sorted[i] - nums_sorted[i - 1] > maxDiff: curc = i
            conn[i] = curc
        j = 0
        for i in range(n):
            while j < n and nums_sorted[j] - nums_sorted[i] <= maxDiff: j += 1
            far[i] = j - 1
        maxlog = floor(math.log2(n)) if n > 1 else 0
        st = [[0] * (maxlog + 1) for _ in range(n)]
        for i in range(n): st[i][0] = far[i]
        for k in range(1, maxlog + 1):
            for i in range(n): st[i][k] = st[st[i][k - 1]][k - 1]
        @lru_cache(None)
        def min_jumps(u, v):
            if u == v: return 0
            if u > v: u, v = v, u
            if far[u] >= v: return 1
            jumps = 0
            for k in range(maxlog, -1, -1):
                nxt = st[u][k]
                if nxt < v:
                    u = nxt
                    jumps += (1 << k)
            return jumps + 1
        ans = []
        for u, v in queries:
            u, v = remap[u], remap[v]
            ans.append(min_jumps(u, v) if conn[u] == conn[v] else -1)
        return ans