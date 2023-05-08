from typing import List
from collections import deque
import heapq

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        # Build Aho–Corasick over all words (every trie node is a valid prefix)
        nxt = [dict()]
        fail = [0]
        depth = [0]

        def add(w: str):
            s = 0
            for ch in w:
                if ch not in nxt[s]:
                    nxt[s][ch] = len(nxt)
                    nxt.append({})
                    fail.append(0)
                    depth.append(depth[s] + 1)
                s = nxt[s][ch]

        for w in words:
            add(w)

        # Build failure links
        q = deque()
        for ch, v in nxt[0].items():
            q.append(v)
        while q:
            v = q.popleft()
            for ch, u in nxt[v].items():
                q.append(u)
                f = fail[v]
                while f and ch not in nxt[f]:
                    f = fail[f]
                fail[u] = nxt[f][ch] if ch in nxt[f] else 0

        n = len(target)
        if n == 0:
            return 0

        # For each end position r, Lmax[r] = longest prefix length ending at r
        add_at = [[] for _ in range(n)]
        s = 0
        for r, ch in enumerate(target):
            while s and ch not in nxt[s]:
                s = fail[s]
            if ch in nxt[s]:
                s = nxt[s][ch]
            else:
                s = 0
            L = depth[s]
            if L:
                start = r - L + 1
                add_at[start].append(r)

        # Compute reach[i] with a sweep over start positions using a max-heap of ends
        reach = [0] * n
        heap = []  # store -r to simulate max-heap
        for i in range(n):
            for r in add_at[i]:
                heapq.heappush(heap, -r)
            while heap and -heap[0] < i:
                heapq.heappop(heap)
            reach[i] = (-heap[0] + 1) if heap else i

        # Jump Game II over reach
        steps = 0
        i = 0
        cur_end = 0
        next_end = 0
        while cur_end < n:
            if i > cur_end:
                return -1
            steps += 1
            while i <= cur_end:
                next_end = max(next_end, reach[i])
                i += 1
            if next_end == cur_end:
                return -1
            cur_end = next_end
        return steps